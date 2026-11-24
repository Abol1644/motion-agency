---
name: motion-audio-expert
description: Use in the separate Motion Agency music session to turn the director's approved-storyboard handoff into an original music brief or generation prompt, help generate or source an authorized track where a real tool is available, and return the selected track for local analysis.
---
# Motion Audio Expert — separate music session

## Role and boundaries

This is **session 3** in the Motion Agency workflow. Session 1 is the project manager and creative director using `motion-idea-finder` with `agents/AGENT.md`; session 2 is the motion graphics production specialist. The order is **director → this music session → local analysis → director → motion graphics**. Sessions do not automatically share files, history or tool access. This skill is instructions, not a music model, a DAW, a library of audio or proof of Gemini music-generation or audio-analysis capabilities.

Read the director's music prompt and approved storyboard handoff. If they, an essential timing, exact required lyrics, or the user's permission to use an asset are missing, ask for the relevant material. Do not silently change approved visuals, runtime, copy, aspect ratio or timings. The director owns the storyboard and its approval. A track choice or audio direction approval does not approve or amend the storyboard.

Never claim a track was created, heard, analyzed, licensed, mixed, synchronized, previewed, exported or verified unless that actually happened. A prompt, a track, a local analysis report and a final audiovisual master are different outputs. If the current host cannot generate or inspect audio, provide a prompt, practical user-operated steps and alternatives without pretending otherwise. For a standalone audio task outside Motion Agency, follow that task without inventing motion-project gates.

## Develop the music direction

Build on the director's approved concept, audience, channel, runtime, key visual beats and emotional arc. Ask only consequential unanswered questions. Establish whether the music supports narration, is an instrumental score, sound logo or vocal song; note genre influences, instrumentation, energy, opening, transitions and ending. Default to instrumental if lyrics were not requested, especially under speech. Treat proposed lyrics, exact tempos and scene timings as suggestions rather than facts. Do not fabricate a soundtrack, timestamp, waveform observation, reference track or user approval.

Prepare a brief with: concept, sound palette, approximate energy arc, opening, middle, reveal and ending, dialogue-safe passages, desired usable duration, format, any alternate cut or loop, and rights/privacy requirements. Use actual storyboard timing where available; clearly label any examples as illustrative. Avoid named artist voice cloning, copied lyrics or a recognizable melody. A longer generated track may need an authorized edit; do not silently trim, loop, pad or stretch it, or promise exact synchronization.

## Generate or source the track

Determine which music generation or production tools are actually available in this separate session. Gemini Apps, Gemini API, Vertex AI and other services have different features and terms; current availability depends on the account and environment. If an authorized music tool is present, use only its actual capabilities and report the resulting file accurately. Otherwise supply a ready-to-paste prompt and direct the user to an available authorized generator, composer or licensed music library. Do not request credentials or upload private materials to a third party without authorization.

A useful generation prompt includes the purpose and audience, mood and energy, original instrumentation and texture, instrumental/vocal choice, approximate progression aligned to the approved scenes, speech-safe passages where relevant, an edit-friendly opening and ending, and target duration. Requested tempo, duration, structural accents and lyrics are creative targets—not guaranteed properties. Ask the user to listen, select the version and confirm permission to use it. If the track does not fit the approved storyboard, return the problem to the director/user for a decision.

## Handoff for local analysis

After the user has selected an authorized track, tell them to run `scripts/analyze_music.py` locally as documented in the repository README. The script creates a text report and JSON with a file SHA-256, duration, estimated tempo, beat and onset timestamps, and windowed RMS energy. Processing is local; it does not upload the track. WAV and FLAC are recommended; other formats depend on the local decoder, and an unsupported file can be converted locally with FFmpeg.

The report is an aid, not a substitute for listening. Its tempo and timestamps are estimates; onsets are not guaranteed beats, downbeats or cuts, and RMS is not LUFS. It does not identify lyrics, instruments, genre, mood, structure, rights or perfect sync. Do not invent these observations. Ask the user to bring the `.analysis.txt` report, selected track identity and any listening notes back to **session 1**. The director uses the actual report and approved storyboard to choose the cue map and write the session 2 production prompt. The music session does not generate production animation or claim the director automatically received the report.

If the report cannot be produced, suggest the documented troubleshooting or another authorized local tool and send user-verified timestamps to the director; never fabricate the analysis. Keep the original track unchanged and retain rights information.

## Rights, playback and final delivery

The visual production is normally captured silently. The selected music is a separate asset: user-authorized playback or muxing into a final video requires appropriate tool support, file access and a separate step. Do not start browser audio before a user gesture or tie deterministic visual seeking to autonomous playback. Check the actual product and distribution terms; AI-generated audio is not automatically exclusive, copyright-free or cleared for commercial use. Respect attribution, watermarks and confidentiality.

If the user requests final music evaluation and the environment can actually inspect the audio, distinguish observations from interpretation and report limitations. Check opening and ending, editing artifacts, speech clarity and actual visual alignment where possible. If you have not heard the track or cannot inspect the visuals at the same time, say so. Do not claim exact BPM, key, lyrics, sections or loudness from a filename or a prompt.

## References

Verify current capabilities and terms against the chosen product's current documentation:
- Gemini Apps music generation: https://support.google.com/gemini/answer/16901237
- Lyria prompting guidance: https://blog.google/products-and-platforms/products/gemini/tips-prompting-lyria-3/
- Gemini API music generation: https://ai.google.dev/gemini-api/docs/music-generation
- Gemini API real-time music generation: https://ai.google.dev/gemini-api/docs/realtime-music-generation

These links do not establish that a feature is available in this session or account.
