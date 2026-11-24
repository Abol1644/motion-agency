#!/usr/bin/env python3
"""Analyze an audio file locally; produce timing cues, not musical interpretation."""

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

try:
    import librosa
    import numpy as np
    import soundfile as sf
except ImportError as exc:
    sys.exit(f"Missing dependency: {exc}. Install requirements-music.txt first.")

SAMPLE_RATE = 22050
HOP_LENGTH = 512


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def analyze(path, window_seconds, max_seconds):
    try:
        info = sf.info(str(path))
    except (RuntimeError, ValueError) as exc:
        raise ValueError(
            "Could not read the audio. Try a WAV or FLAC file; for unsupported "
            "formats convert locally with FFmpeg (see the README)."
        ) from exc
    if info.frames <= 0 or info.samplerate <= 0:
        raise ValueError("The audio file is empty or has an invalid sample rate.")
    duration = info.frames / info.samplerate
    if duration > max_seconds:
        raise ValueError(f"Audio is {duration:.1f} seconds; the limit is {max_seconds:.1f}. "
                         "Use --max-seconds to raise it deliberately.")
    try:
        with sf.SoundFile(str(path)) as source:
            samples = source.read(dtype="float32", always_2d=True)
        audio = samples.mean(axis=1, dtype=np.float32)
        if info.samplerate != SAMPLE_RATE:
            audio = librosa.resample(audio, orig_sr=info.samplerate, target_sr=SAMPLE_RATE)
        sr = SAMPLE_RATE
    except Exception as exc:
        raise ValueError(f"Could not decode the audio: {exc}") from exc
    if audio.size == 0 or not np.isfinite(audio).all():
        raise ValueError("The decoded audio is empty or contains invalid samples.")
    # Use decoded length so all analysis times refer to the audio actually analyzed.
    duration = len(audio) / sr
    overall_rms = float(np.sqrt(np.mean(np.square(audio, dtype=np.float64))))
    is_silent = overall_rms < 1e-5
    beats, onsets, tempo = [], [], None
    if not is_silent and duration >= 1.0:
        onset_strength = librosa.onset.onset_strength(y=audio, sr=sr, hop_length=HOP_LENGTH)
        onset_frames = librosa.onset.onset_detect(onset_envelope=onset_strength, sr=sr,
                                                  hop_length=HOP_LENGTH, backtrack=False)
        onsets = [round(float(t), 3) for t in librosa.frames_to_time(
            onset_frames, sr=sr, hop_length=HOP_LENGTH) if t < duration]
        # Do not publish a tempo when there is insufficient detected activity.
        if len(onsets) >= 3:
            bpm, beat_frames = librosa.beat.beat_track(
                onset_envelope=onset_strength, sr=sr, hop_length=HOP_LENGTH,
                trim=False, units="frames")
            raw_bpm = float(np.asarray(bpm).reshape(-1)[0])
            if math.isfinite(raw_bpm) and raw_bpm > 0:
                tempo = round(raw_bpm, 1)
                beats = [round(float(t), 3) for t in librosa.frames_to_time(
                    beat_frames, sr=sr, hop_length=HOP_LENGTH) if t < duration]
    window_samples = max(1, round(window_seconds * sr))
    energy = []
    for start in range(0, len(audio), window_samples):
        end = min(start + window_samples, len(audio))
        rms = float(np.sqrt(np.mean(np.square(audio[start:end], dtype=np.float64))))
        energy.append({"start_seconds": round(start / sr, 3),
                       "end_seconds": round(end / sr, 3),
                       "rms_dbfs": round(20 * math.log10(max(rms, 1e-6)), 1)})
    energy_changes = []
    for previous, current in zip(energy, energy[1:]):
        delta = round(current["rms_dbfs"] - previous["rms_dbfs"], 1)
        if abs(delta) >= 3.0:
            energy_changes.append({"time_seconds": current["start_seconds"],
                                   "delta_rms_db": delta})
    notes = [
        "Tempo, beat and onset positions are estimates; half/double-tempo errors are possible.",
        "Onsets are detected sound changes, not necessarily musical beats or scene cuts.",
        "Energy is windowed RMS dBFS, not LUFS, perceived loudness or named song sections.",
        "Energy-change candidates compare adjacent windows at their boundary; exact transition time is unknown.",
        "No vocals, lyrics, instruments, mood, downbeats or rights are identified.",
        "Listen to the selected track and verify any cue before synchronizing animation."
    ]
    if is_silent:
        notes.insert(0, "The track is effectively silent; tempo and beat analysis were skipped.")
    elif duration < 1.0:
        notes.insert(0, "The track is too short for a meaningful tempo estimate.")
    elif tempo is None:
        notes.insert(0, "Insufficient rhythmic activity for a useful tempo estimate.")
    return {"format_version": "1.0", "source_file": path.name,
            "source_sha256": digest(path), "duration_seconds": round(duration, 3),
            "analysis_sample_rate_hz": sr, "mono_mix_for_analysis": True,
            "tempo_estimate_bpm": tempo, "beat_times_seconds": beats,
            "onset_times_seconds": onsets, "energy_window_seconds": window_seconds,
            "energy_windows": energy, "energy_change_candidates": energy_changes, "notes": notes}


def render_report(data):
    def times(values):
        return ", ".join(f"{v:.3f}" for v in values) if values else "None detected"
    bpm = data["tempo_estimate_bpm"]
    lines = ["MUSIC ANALYSIS REPORT", "", f"File: {data['source_file']}",
             f"SHA-256: {data['source_sha256']}",
             f"Duration: {data['duration_seconds']:.3f} seconds",
             f"Estimated tempo: {f'{bpm:.1f} BPM' if bpm is not None else 'Not available'}",
             "", "Estimated beats (seconds):", times(data["beat_times_seconds"]),
             "", "Detected onsets (seconds):", times(data["onset_times_seconds"]),
             "", "Energy windows (start-end seconds: RMS dBFS):"]
    lines += [f"{v['start_seconds']:.3f}-{v['end_seconds']:.3f}: {v['rms_dbfs']:.1f}"
              for v in data["energy_windows"]]
    lines += ["", "Energy-change candidates (window boundary seconds: RMS change dB):"]
    changes = data["energy_change_candidates"]
    lines += ([f"{v['time_seconds']:.3f}: {v['delta_rms_db']:+.1f}" for v in changes]
              if changes else ["None detected"])
    return "\n".join(lines + ["", "Limitations:"] + [f"- {n}" for n in data["notes"]] + [""])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio", type=Path, help="Audio file to analyze (WAV/FLAC recommended)")
    parser.add_argument("--output-dir", type=Path, default=Path("."), help="Output directory")
    parser.add_argument("--window", type=float, default=2.0, help="Energy window in seconds (default: 2)")
    parser.add_argument("--max-seconds", type=float, default=600.0,
                        help="Maximum input duration in seconds (default: 600)")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing reports")
    args = parser.parse_args(argv)
    if not math.isfinite(args.window) or args.window < 0.1:
        parser.error("--window must be a finite number of at least 0.1 seconds")
    if not math.isfinite(args.max_seconds) or args.max_seconds <= 0:
        parser.error("--max-seconds must be a positive finite number")
    if not args.audio.is_file():
        parser.error(f"Audio file not found: {args.audio}")
    json_path = args.output_dir / f"{args.audio.stem}.analysis.json"
    text_path = args.output_dir / f"{args.audio.stem}.analysis.txt"
    try:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        if not args.overwrite and (json_path.exists() or text_path.exists()):
            raise FileExistsError("A report already exists; choose another output directory or use --overwrite.")
        result = analyze(args.audio, args.window, args.max_seconds)
        # JSON and text are separate outputs; never change the source audio.
        json_path.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        text_path.write_text(render_report(result), encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(f"Analysis failed: {exc}", file=sys.stderr)
        return 1
    print(f"Text report: {text_path}\nJSON report: {json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
