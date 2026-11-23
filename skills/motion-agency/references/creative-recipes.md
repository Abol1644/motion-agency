# Creative recipes, prompts and review

## Contents
1. How to use recipes
2. Eight adaptable creative recipes
3. Reference analysis and question patterns
4. Storyboard prompt and coding handoff
5. Art direction critique
6. Troubleshooting

## 1. How to use recipes
These are original starting patterns, not ready-made final designs. Select a pattern based on the approved purpose and audience, modify it to fit the user's inputs, and preserve the resource, DONE and storyboard approval gates. Timings are illustrative rather than universal; adjust for text length and viewing context. Never claim these examples were tested in the current environment.

Each recipe contains: concept, visual construction, motion, feasibility and one quality risk. Avoid defaulting every project to the same palette, grid, arc or loop.

## 2. Eight adaptable creative recipes

### A. Editorial statement
- **Concept:** Make a short idea feel authoritative through type and rhythm.
- **Visual:** An oversized headline, compact subtitle, asymmetrical margin and a restrained supporting line.
- **Motion:** Reveal a phrase through an aligned mask; let one important word change scale; settle into a final frame.
- **Technique:** DOM or SVG text, clip paths and absolute-time transforms. Use user-approved copy, verify fallback fonts.
- **Risk:** Animation ends before the complete sentence can be read.

### B. Product, assembled from parts
- **Concept:** Show how a product's form or modules come together.
- **Visual:** A single hero silhouette with a few labeled parts and a quiet background.
- **Motion:** Separate shapes enter along a coherent path, join, then highlight one approved feature. Hold final product and name.
- **Technique:** SVG paths, Canvas geometry, match transforms. Obtain authentic geometry or clearly label a procedural approximation.
- **Risk:** Inventing physical details or functionality.

### C. The insight becomes the graphic
- **Concept:** Show one real metric or idea becoming understandable.
- **Visual:** Label, value, proportional chart and concise takeaway, all sourced from provided data.
- **Motion:** Establish axis and units, introduce data from a neutral baseline, emphasize one relevant comparison.
- **Technique:** Canvas/SVG scales and pure interpolation; design readable end state.
- **Risk:** Unsupported numbers, cropped scales or motion that implies causation.

### D. Paper journey
- **Concept:** Use layered cut-paper forms to explain a process.
- **Visual:** Two or three textured layers, simple icons, readable short labels.
- **Motion:** Each layer slides to reveal the next; a persistent shape links scenes. Use small parallax and clear breaks.
- **Technique:** Inline vector silhouettes and stable grain; manage occlusion.
- **Risk:** Texture competing with contrast or becoming expensive at export resolution.

### E. Interface action → outcome
- **Concept:** Make a demonstrated workflow easy to follow.
- **Visual:** One realistic interface panel with a single primary action, not a full unreadable dashboard.
- **Motion:** Pointer focuses a control, action happens, result appears. Brief pause between steps.
- **Technique:** DOM or SVG mock interface with deterministic cursor path and state changes.
- **Risk:** Showing or claiming features the product does not possess. If unknown, mark the interface as illustrative.

### F. Kinetic phrase system
- **Concept:** Let a short message carry the narrative.
- **Visual:** A few carefully chosen words, a consistent type system and one geometric anchor.
- **Motion:** A word transforms position or scale on each beat; a stable anchor guides the eye between changes.
- **Technique:** Animate complete words with a reusable ease; maintain semantic accessibility.
- **Risk:** Line wraps change across environments or text moves before it can be read.

### G. Abstract dimensional identity
- **Concept:** Express a brand idea through form rather than literal illustration.
- **Visual:** A small family of layered or projected shapes with a clear light direction.
- **Motion:** Rotate, unfold or align around a simple focal center; an occasional graphic accent marks a beat.
- **Technique:** Three.js for dimensional scenes, optionally driven by GSAP or Anime.js. Document compatible library versions and maintain deterministic time.
- **Risk:** Decorative movement disconnects from the actual message or becomes too expensive.

### H. Seamless ambient loop
- **Concept:** Create an unobtrusive recurring visual state.
- **Visual:** Small set of recognizable forms and a restrained palette.
- **Motion:** Periodic motion with matched start/end state; prevent sudden changes in direction or phase.
- **Technique:** Pure periodic functions derived from absolute time; match the loop length to whole cycles.
- **Risk:** Visible seam, distracting perpetual motion, or no accessible pause.

## 3. Reference analysis and question patterns
When a user says “make it cinematic,” turn the label into decisions: “Do you mean slow, atmospheric camera movement, high-contrast dramatic framing, or a polished product reveal?” When they say “modern,” ask if they want precise minimalism, energetic typography or tactile graphics. Ask about only the top two to four unanswered questions. Send an explicit invitation for resource batches and DONE.

After seeing a reference, describe only observable aspects: “The sample uses large type, a dark field and a central object. Is its restrained pacing or its color contrast the part you want to carry over?” If timing cannot be observed, say so.

## 4. Storyboard and coding handoff templates

**Creative direction**
- Goal and intended audience:
- Message and required exact copy:
- Proposed visual style, palette, typography and shape language:
- Motion verbs, tempo, transitions and ending:
- Resource register, permission/access notes and missing assets:
- Duration, aspect ratio, approximate dimensions, fps, audio and accessibility:
- Explicit assumptions needing approval:

**Storyboard**
`Scene | time in–out | composition and visible text | movement and transition | audience takeaway | assets/notes`

Ensure the time intervals, final end frame and total duration are coherent. End: “Do you approve this storyboard, or what would you like to change?” Do not treat DONE, a partial reply, or image request as approval.

**Production handoff after approval**
1. Freeze the approved board and exact text; document changes if the user revises it.
2. Identify capture dimensions, fps and duration and choose Canvas/SVG/DOM approach.
3. Define compositional assets, scene geometry and a single absolute-time function.
4. Implement `window.__motion` with duration, fps, width, height, seek and pause; make resources ready before capture.
5. Produce complete runnable HTML and explicitly declared library dependencies, test if the environment permits, and state limits.
6. Provide local rendering steps and explain that image-sequence output is silent.

## 5. Art direction critique
Evaluate the actual result if you can see it. Otherwise clearly present this as a proposed checklist, not a passed test. Ask:
- **Message:** What should a viewer remember after three seconds? Is every scene helping?
- **Hierarchy:** Is the focal point obvious at thumbnail size? Can secondary information be read without competing movement?
- **Composition:** Are objects purposefully aligned, weighted and spaced, with safe margins?
- **Motion:** Do elements move for a reason, with appropriate easing, overlap and rest? Is the path meaningful?
- **Continuity:** Do transitions preserve identity or intentionally shift context? Are there accidental jumps?
- **Authenticity:** Are supplied assets, exact copy and data correct? Are all claims supported?
- **Craft:** Are line weights, font sizes, material, colors, shadows and visual tempo consistent?
- **Access:** Can users pause/replay and use a reduced-motion variant? Are there flashing or readability hazards?
- **Technical:** Does seeking reproduce frames, are dependencies available, and was the specified output really tested?

Prioritize the top three problems and say how to fix each. Do not hide uncertainty behind a numeric score. Avoid empty praise like “stunning” when the frame has not been inspected.

## 6. Troubleshooting
- **Looks generic:** identify the central metaphor, remove unrelated motifs, choose a specific visual system and one purposeful signature transition.
- **Too busy:** reduce simultaneous changes, increase visual holds, remove secondary effects, and make one subject dominant.
- **Feels flat:** clarify foreground/midground/background or hierarchy; add purposeful contrast or restrained layering, not automatic 3D.
- **Feels robotic:** inspect spacing, anticipation and settling; vary holds and consider arcs without adding needless bounce.
- **Feels sluggish:** shorten transitions rather than reading holds; stage dependent motions in parallel only where clarity survives.
- **Not readable on mobile:** reduce copy, simplify hierarchy, increase type size, test the actual final view size.
- **Reference not accessible:** request a frame or textual description. Do not guess its content or timing.
- **Export differs from preview:** check fonts, image readiness, dimensions, `pause()`, seek behavior, frame rate, CSS animations, and stale frames before offering a correction.
- **Seek differs on repeat:** eliminate per-frame random calls, time accumulation, asynchronous updates and unmanaged animations.
- **User dislikes result:** ask which frame or transition and what feels wrong, revise the storyboard if the conceptual direction changes, and only then revise code.
