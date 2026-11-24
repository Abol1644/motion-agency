# Motion techniques and production engineering

## Scope and workflow

This reference supports the separate motion graphics production session. In Motion Agency, the director first approves the storyboard with the user, writes a prompt for the separate music session, and receives the selected track's local analysis report. The director then supplies the production session with the approved storyboard, track identity, report and a cue map. Do not start production with invented approvals, audio observations or missing timing; request the necessary handoff. A silent project or bypass of the music step needs explicit user direction. The frame-capture master is silent even when an authorized soundtrack is planned.

## Core animation principles

Choose principles that serve the piece, not an obligatory checklist. **Staging** makes the subject clear; **anticipation** prepares a major action; **timing and spacing** convey weight; **slow-in/slow-out** can soften acceleration and stops; **arcs** often make movement coherent; **follow-through and overlapping action** prevent elements from arriving as a single rigid block; **secondary action** supports the main action without stealing attention; **exaggeration** strengthens meaning while remaining legible; **appeal** comes from well-designed poses, visual rhythm and clarity. Squash and stretch can imply flexibility; preserve plausible volume and never distort required logos without permission. Linear motion is valid for constant-rate processes and intentionally mechanical direction.

## Time, easing and choreography

Use seconds as the master time domain. Define each scene's start/end and use normalized progress `p = clamp((t - start) / duration, 0, 1)`. Compute all positions from `t`, not the frame count or an accumulated delta, so seeking to any time gives the same state. Hold the final pose; a transition is not a reading hold. Use consistent timing families but vary pacing intentionally.

Useful pure functions in vanilla JS:

```js
const clamp01 = (x) => Math.max(0, Math.min(1, x));
const progress = (t, start, duration) => clamp01((t - start) / Math.max(duration, 0.00001));
const lerp = (a, b, p) => a + (b - a) * p;
const easeIn = (p) => p * p;
const easeOut = (p) => 1 - (1 - p) * (1 - p);
const easeInOut = (p) => p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
const smooth = (p) => p * p * (3 - 2 * p);
const stagger = (t, index, first, gap, span) => progress(t, first + index * gap, span);
```

Pass clamped `p` to easing. Use stagger to introduce layers in a meaningful order, not to delay every item. An overshoot may be computed from an explicitly bounded easing function; avoid overshoot for precision interfaces or logos unless approved. For heavier objects, alter acceleration, travel and settling purposefully rather than assuming slow is always heavy. Do not present generic timing ranges as universal rules; compare at the target output size and pace.

Use the director's scene-to-music cue map and the actual local analysis report. Tempo, onset and beat times are estimates; onset detections are not guaranteed musical beats or scene cuts. Do not fabricate song structure, downbeats or perceived qualities. Resolve conflicts between the chosen track and approved board with the user rather than silently retiming either.

## Deterministic browser architecture

A browser project may use an HTML entry point with pinned Three.js, GSAP or Anime.js dependencies. Select a primary timeline engine, include only necessary libraries, and use an approved CDN or a properly licensed local bundle. An HTML file loading a CDN is not offline self-contained. Explain required network access, CSP, version and local-server setup. For Canvas, SVG and 3D render layers, use an absolute-time rendering architecture with explicit stage dimensions and capture control. Keep random or noise functions seeded or time-derived. Consult the corresponding library reference.

Expose `window.__motion = {duration, fps, width, height, seek, pause, ready}`. `seek(seconds)` clamps seconds, synchronously sets all scene state and draws without animation-frame playback interfering. `pause()` cancels the scheduled animation frame and prevents subsequent automatic updates; call it during capture. `ready` may be a resolved promise when no resources are asynchronous, but await actual fonts and assets when needed. Use one stage element `#motion-stage` at the declared resolution in capture mode; playback controls and focus UI must remain outside it. CSS or DOM transitions and native animated media are not deterministic unless their state is explicitly synchronized.

A conceptual playback loop, to adapt to the actual scene:

```js
let playing = false, raf = 0, origin = 0, current = 0;
function seek(seconds) { current = Math.max(0, Math.min(duration, seconds)); render(current); }
function pause() { playing = false; cancelAnimationFrame(raf); }
function tick(now) {
  if (!playing) return;
  seek((now - origin) / 1000);
  if (current < duration) raf = requestAnimationFrame(tick);
  else pause();
}
function play() {
  if (playing) return;
  if (current >= duration) seek(0);
  playing = true; origin = performance.now() - current * 1000;
  raf = requestAnimationFrame(tick);
}
```

This is a pattern, not a complete deliverable; define `duration` and `render`, attach accessible controls, expose the full API and handle initialization. `seek` alone does not stop a previously running loop: capture must call `pause()` first.

## Drawing and motion techniques

- **Typography reveal:** Set complete text in a real accessible element; reveal using a mask or clip without splitting semantic words unnecessarily. Hold the unmasked final state.
- **Path drawing:** Set SVG path dash length and offset from progress, or trace an interpolated path on Canvas. Precompute lengths when possible, and handle missing or invalid geometry.
- **Mask wipe:** Move a deterministic rectangle, circle or path through a layer; use it to reveal a relevant underlying state. Add room for a readability hold.
- **Shape morph:** Interpolate corresponding points with compatible topology. If shapes do not share vertices, use a designed cut, crossfade or mask instead of generating self-intersecting paths.
- **Transform and match cut:** Match origin, scale, shape or screen position between adjacent scenes. Compute both scenes at the transition boundary; prevent gaps or visible double images.
- **Parallax:** Offset a few depth layers by small amounts, preserving subject readability. Avoid large camera-like movement where it risks motion sensitivity.
- **Procedural particles:** Generate from a seeded list, calculate position directly from time, restrict count and opacity. Do not use `Math.random()` inside each rendered frame.
- **Stroke and grid:** Draw crisp lines at device-appropriate widths; avoid excessive subpixel shimmer. Keep grids subordinate to the main subject.
- **Simulated depth:** Use size, layered occlusion, shadows and projected points. Be honest that simulated 2D depth is not a full 3D engine. Use Three.js when actual 3D serves the brief; disclose version-pinned dependencies and environment needs.
- **Texture:** Use stable procedural texture or an authorized embedded asset, not freshly randomized noise. Keep it subtle, fast and contrast-safe.
- **Counting and charts:** Interpolate quantities only from user-supplied values; label units and source, preserve proportional encodings, avoid implying facts that do not exist.

## Transitions and scene structures

- **Hard cut:** instant switch at a boundary; useful to change topic and can be more elegant than a decorative effect.
- **Cross dissolve:** opacity blend of designed scene layers; maintain contrast and avoid double-legible text during overlap.
- **Match movement:** a visual object exits as its counterpart enters in a coherent direction; preserve scale and visual identity.
- **Transform:** reuse a visual anchor as it changes role or form; explicitly define start, middle and end poses.
- **Reveal through mask:** the action directs attention to new information; align the reveal with the narrative.
- **Camera-like move:** translate/scale a layered composition around a defined focal point. Use sparingly; supply a reduced-motion alternative if appropriate.
- **Seamless loop:** match last-to-first state and, when necessary, velocity. Do not assume the loop works merely because frame 0 resembles the last scene.

## Performance, accessibility and audio

Favor a small number of composited layers and precomputed geometry. Avoid repeated layout reads/writes, full-screen high-cost blur, thousands of unbounded objects and huge bitmap resources. Verify in the target browser when possible. Keep visual fidelity separate from playback performance; capture exact times rather than assuming a screen recording maintained frame rate.

Use keyboard-accessible play, pause and replay controls with descriptive names. Honor `prefers-reduced-motion` for interactive playback where feasible; make the important message available without motion. Avoid flash/strobe effects and avoid implying untested WCAG compliance. Use actual WCAG guidance for required conformance, including thresholds and circumstances. Verify text contrast and visibility with real foreground/background colors.

The selected audio is separate from the text report. Confirm rights and file access, and decide whether it accompanies local playback, export or both. Do not autoplay audio. Browser audio cannot be assumed to appear in an image-sequence export: frame capture is silent, and authorized music must be muxed separately. Verify actual sync instead of claiming it from code or a cue map alone.

## Capture and render

The production skill's main instructions contain a Python/Playwright screenshot script and FFmpeg command. Important invariants: `pause()` first; wait for fonts and assets; validate dimensions; set viewport to declared width and height; call `seek(i / fps)`; capture only the stage; use a fresh frame directory rather than overwriting old captures; encode at the same fps; use even H.264 dimensions or pad; make silence explicit; review the resulting MP4. Variable browser/device settings, unsupported fonts or non-deterministic CSS animation can change the output, so never claim pixel-perfect portability without actual comparison.

Screen recording is simpler but may drop frames and includes the real-time browser environment. Use a local-only workflow and approved tools; don't ask for credentials or upload private materials to a website.

## Quality checklist and further reading

- Storyboard fidelity and exact copy confirmed; timing and assets match.
- Selected track and real report identified; uncertain cues distinguished from user-confirmed timing.
- First frame, transition boundaries, representative intermediate frames and final hold reviewed when possible.
- `seek` is deterministic, pause prevents animation drift and capture dimensions are valid.
- Keyboard, reduced motion, legibility, no hazardous flashing; any untested area is disclosed.
- Output, prerequisites and whether the file/video was actually rendered are stated accurately.

References:
- MDN Canvas animation: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_animations
- MDN requestAnimationFrame: https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame
- MDN reduced motion: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
- Accessibility and motion: https://web.dev/learn/accessibility/motion
- W3C flashes or below threshold: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
- FFmpeg image sequence documentation: https://ffmpeg.org/ffmpeg-formats.html#image2
