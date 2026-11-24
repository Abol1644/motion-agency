# Creative recipes, prompts and review

## How to use recipes

These are adaptable starting patterns, not ready-made final designs. Select a pattern based on the approved purpose and audience, modify it to fit the user's inputs, and preserve the resource, DONE and storyboard approval gates. Timings are illustrative, not universal; adjust for text length and viewing context. Never claim these examples were tested in the current environment. Avoid defaulting every project to the same palette, grid, arc or loop.

In Motion Agency the idea skill and `AGENT.md` direct the project in session 1. After storyboard approval, the director creates a music prompt for session 3, receives the selected track's local analysis report, and only then creates the motion production prompt for session 2. Transfer materials manually; do not assume shared session context. A silent project or bypass of the music step needs explicit user direction.

## Eight adaptable creative recipes

### A. Editorial statement
- **Concept:** Make a short idea feel authoritative through type and rhythm.
- **Visual:** Oversized headline, compact subtitle, asymmetrical margin and restrained supporting line.
- **Motion:** Reveal a phrase through an aligned mask; let one important word change scale; settle into a final frame.
- **Technique:** DOM or SVG text, clip paths and absolute-time transforms. Use user-approved copy, verify fallback fonts.
- **Risk:** Animation ends before the complete sentence can be read.

### B. Product assembled from parts
- **Concept:** Show how a product's form or modules come together.
- **Visual:** A single hero silhouette with a few labeled parts and a quiet background.
- **Motion:** Separate shapes enter along a coherent path, join, then highlight one approved feature. Hold final product and name.
- **Technique:** SVG paths, Canvas geometry and matching transforms. Obtain authentic geometry or clearly label a procedural approximation.
- **Risk:** Inventing physical details or functionality.

### C. The insight becomes the graphic
- **Concept:** Show one real metric or idea becoming understandable.
- **Visual:** Label, value, proportional chart and concise takeaway, sourced from provided data.
- **Motion:** Establish axis and units, introduce data from a neutral baseline and emphasize one relevant comparison.
- **Technique:** Canvas/SVG scales and pure interpolation; design a readable end state.
- **Risk:** Unsupported numbers, cropped scales or motion that implies causation.

### D. Paper journey
- **Concept:** Use layered cut-paper forms to explain a process.
- **Visual:** Two or three textured layers, simple icons and readable short labels.
- **Motion:** Each layer slides to reveal the next; a persistent shape links scenes. Use small parallax and clear breaks.
- **Technique:** Inline vector silhouettes and stable grain; manage occlusion.
- **Risk:** Texture competing with contrast or becoming expensive at export resolution.

### E. Interface action → outcome
- **Concept:** Make a demonstrated workflow easy to follow.
- **Visual:** One realistic interface panel with a single primary action, not an unreadable dashboard.
- **Motion:** Pointer focuses a control, action happens, result appears. Brief pause between steps.
- **Technique:** DOM or SVG mock interface with deterministic cursor path and state changes.
- **Risk:** Showing or claiming features the product does not possess. If unknown, mark the interface as illustrative.

### F. Kinetic phrase system
- **Concept:** Let a short message carry the narrative.
- **Visual:** A few carefully chosen words, a consistent type system and one geometric anchor.
- **Motion:** A word transforms position or scale on each beat; a stable anchor guides the eye between changes.
- **Technique:** Animate complete words with reusable easing; maintain semantic accessibility.
- **Risk:** Line wraps change across environments or text moves before it can be read.

### G. Abstract dimensional identity
- **Concept:** Express a brand idea through form rather than literal illustration.
- **Visual:** A small family of layered or projected shapes with a clear light direction.
- **Motion:** Rotate, unfold or align around a simple focal center; an occasional graphic accent marks a beat.
- **Technique:** Three.js for dimensional scenes, optionally driven by GSAP or Anime.js. Document compatible library versions and maintain deterministic time.
- **Risk:** Decorative movement disconnects from the actual message or becomes too expensive.

### H. Seamless ambient loop
- **Concept:** Create an unobtrusive recurring visual state.
- **Visual:** A small set of recognizable forms and a restrained palette.
- **Motion:** Periodic motion with matched start/end state; prevent sudden changes in direction or phase.
- **Technique:** Pure periodic functions derived from absolute time; match the loop length to whole cycles.
- **Risk:** Visible seam, distracting perpetual motion or no accessible pause.

## Reference analysis and question patterns

When a user says “make it cinematic,” turn the label into decisions: “Do you mean slow, atmospheric camera movement, high-contrast dramatic framing, or a polished product reveal?” When they say “modern,” ask if they want precise minimalism, energetic typography or tactile graphics. Ask only the highest-impact unanswered questions. Invite resource batches and DONE.

After seeing a reference, describe only observable aspects. Ask which aspects should carry over; if timing cannot be observed, say so. Use references for inspiration without copying protected assets or implying permissions.

## Storyboard and handoff templates

**Creative direction**
- Goal, audience, intended channel and message.
- Exact supplied copy and approved facts versus proposed wording.
- Visual style, palette, typography, geometry and composition.
- Motion verbs, tempo, transitions, ending and accessibility.
- Resource register, rights, access, duration, aspect, dimensions and fps.

**Storyboard**
`Scene | time in–out | composition and visible text | movement and transition | audience takeaway | assets/notes`

Ensure the time intervals, final end frame and total duration are coherent. Ask: “Do you approve this storyboard, or what would you like to change?” Do not treat DONE, a partial reply, a concept choice or image request as approval.

**Music-session handoff after approval**
1. Preserve the approved board and exact text. Write a self-contained prompt with concept, audience, duration, visual beats, emotional arc, sound palette, opening, ending and narration/vocal constraints. Mark suggestions and approximate timings as such.
2. Ask the user to carry the prompt to the separate audio session, generate or source an authorized track, listen and select a version. Do not claim a track was produced or heard when it was not.
3. The user analyzes the selected version locally with `scripts/analyze_music.py` and returns the text report and listening notes to the director. Verify track identity and duration. BPM, beats and onsets are estimates; RMS windows are not named song sections. Do not invent musical interpretation or missing cue times.

**Motion-session handoff after music analysis**
1. The director uses the approved board and actual report to propose a scene-to-music cue map; distinguish reported times, user-confirmed accents and proposed choices. Resolve material duration conflicts with the user.
2. Provide the complete board, exact copy, authorized assets, selected track identity/hash and duration, cue map and analysis limitations, dimensions, fps, ending, style, library/runtime constraints and accessibility.
3. Require a single deterministic source of time and `window.__motion = {duration, fps, width, height, seek, pause, ready}` with `#motion-stage`, stage-sized capture and controls outside it.
4. Ask the user to carry the handoff and assets to a new motion graphics session using the historical `motion-director` production skill. A report is not the music file; provide the authorized audio separately when playback or muxing is needed.
5. Produce complete runnable animation only after the receiving session confirms required material. Frame-sequence video is silent; audio integration is a separate authorized step. State what was actually tested.

## Art direction critique

Evaluate the actual result if you can see it. Otherwise clearly present this as a proposed checklist, not a passed test. Ask:
- **Message and hierarchy:** What should a viewer remember? Is the focal point obvious and readable at the intended size?
- **Composition:** Are objects purposefully aligned, weighted and spaced, with safe margins?
- **Motion and continuity:** Does each move serve a reason, with appropriate easing and rest? Are there accidental jumps?
- **Authenticity and craft:** Are supplied assets, exact copy and data correct? Are visual details consistent?
- **Access:** Can users pause/replay and use a reduced-motion option? Are there flashing or readability hazards?
- **Technical:** Does seeking reproduce frames, are dependencies available, and was the specified output really tested?

Prioritize the top problems and concrete corrections. Avoid empty praise or scores when the result has not been inspected.

## Troubleshooting

- **Looks generic:** identify the central metaphor, remove unrelated motifs and choose a purposeful signature transition.
- **Too busy:** reduce simultaneous changes, increase holds and make one subject dominant.
- **Feels flat or robotic:** clarify hierarchy and layering, inspect timing and settling; add movement only when meaningful.
- **Not readable on mobile:** reduce copy, simplify hierarchy, increase type size and test the actual final view size.
- **Reference not accessible:** request a frame or textual description. Do not guess its content or timing.
- **Music report unavailable or unreliable:** obtain a valid local report or user-verified timestamps; do not fabricate musical cues.
- **Export differs from preview:** check fonts, image readiness, dimensions, `pause()`, seek behavior, frame rate and CSS animations.
- **Seek differs on repeat:** eliminate per-frame random calls, time accumulation, asynchronous updates and unmanaged animations.
- **User dislikes result:** ask which frame or transition and what feels wrong; revise the storyboard if the conceptual direction changes.
