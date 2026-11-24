import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import soundfile as sf

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "analyze_music.py"


class MusicAnalysisTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.sr = 22050

    def tearDown(self):
        self.tmp.cleanup()

    def run_script(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                              capture_output=True, text=True, timeout=120)

    def make_wav(self, name, data):
        path = self.root / name
        sf.write(path, data, self.sr)
        return path

    def test_click_track_reports_timing_and_source_identity(self):
        audio = np.zeros(self.sr * 8, dtype=np.float32)
        for seconds in np.arange(0, 8, 0.5):
            i = int(seconds * self.sr)
            audio[i:i+100] = np.hanning(100) * 0.8
        track = self.make_wav("clicks.wav", np.column_stack((audio, audio * 0.7)))
        original = hashlib.sha256(track.read_bytes()).hexdigest()
        result = self.run_script(track, "--output-dir", self.root / "out")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads((self.root / "out" / "clicks.analysis.json").read_text())
        self.assertAlmostEqual(report["duration_seconds"], 8.0, places=2)
        self.assertEqual(report["source_sha256"], original)
        self.assertEqual(hashlib.sha256(track.read_bytes()).hexdigest(), original)
        self.assertGreater(report["tempo_estimate_bpm"], 0)
        self.assertGreater(len(report["beat_times_seconds"]), 3)
        self.assertGreater(len(report["onset_times_seconds"]), 3)
        self.assertEqual(len(report["energy_windows"]), 4)
        self.assertIn("Limitations:", (self.root / "out" / "clicks.analysis.txt").read_text())

    def test_silence_has_no_fabricated_tempo(self):
        track = self.make_wav("silence.wav", np.zeros(self.sr * 2))
        result = self.run_script(track, "--output-dir", self.root / "out")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads((self.root / "out" / "silence.analysis.json").read_text())
        self.assertIsNone(report["tempo_estimate_bpm"])
        self.assertEqual(report["beat_times_seconds"], [])
        self.assertTrue(any("silent" in note for note in report["notes"]))

    def test_energy_change_candidates_are_window_based(self):
        quiet = np.zeros(self.sr * 2, dtype=np.float32)
        t = np.arange(self.sr * 2) / self.sr
        loud = (0.4 * np.sin(2 * np.pi * 440 * t)).astype(np.float32)
        track = self.make_wav("change.wav", np.concatenate((quiet, loud)))
        result = self.run_script(track, "--output-dir", self.root / "out")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads((self.root / "out" / "change.analysis.json").read_text())
        self.assertEqual(report["energy_change_candidates"][0]["time_seconds"], 2.0)
        self.assertGreater(report["energy_change_candidates"][0]["delta_rms_db"], 3)
        self.assertIn("Energy-change candidates", (self.root / "out" / "change.analysis.txt").read_text())

    def test_existing_reports_are_not_replaced_without_flag(self):
        track = self.make_wav("silence.wav", np.zeros(self.sr))
        output = self.root / "out"
        output.mkdir()
        report = output / "silence.analysis.txt"
        report.write_text("keep me", encoding="utf-8")
        result = self.run_script(track, "--output-dir", output)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(report.read_text(), "keep me")
        self.assertFalse((output / "silence.analysis.json").exists())

    def test_missing_and_overlong_inputs_fail(self):
        result = self.run_script(self.root / "missing.wav")
        self.assertNotEqual(result.returncode, 0)
        track = self.make_wav("long.wav", np.zeros(self.sr * 2))
        result = self.run_script(track, "--max-seconds", "1", "--output-dir", self.root / "out")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("limit", result.stderr)


if __name__ == "__main__":
    unittest.main()
