# Motion styles and visual languages

## Contents
- How to choose a style
- Editorial and typography-led directions
- Graphic and illustration-led directions
- Product, interface and informational directions
- Textural, cinematic and dimensional directions
- Style mixing, selection and quality checks

## How to choose a style
Translate adjectives into observable decisions. Ask what the user wants the audience to feel, notice, understand and do. Offer two or three distinct directions that differ in composition, material and motion, not merely palette. For each: one-sentence idea, visual ingredients, motion grammar, best use and one risk. The recipes below are adaptable directions, not fixed rules or permissions to imitate a particular artist.

## Editorial and typography-led directions

### Kinetic typography
- **Visual:** Type drives the composition; changes in size, weight, alignment and density communicate emphasis.
- **Motion:** Words reveal through masks, tracking, word swaps, transitions by shared letterform or motion along a baseline. Hold the full message before removal.
- **Use:** Slogans, announcements, lyric-free quote pieces, punchy brand stories.
- **Build:** DOM or SVG text with absolute-time transforms, clipping and opacity. Check language, line breaks, font fallback and screen reader access. Avoid rotating so rapidly that the meaning cannot be read.

### Editorial magazine
- **Visual:** Generous margins, deliberate grid, oversized headlines, small captions, panels and imagery with a clear typographic hierarchy.
- **Motion:** Index lines extend, columns slide into alignment and image crops reveal like editorial spreads. Settle the composition before the next page.
- **Use:** Cultural narratives, interviews, research summaries, luxury information.
- **Avoid:** Tiny footnotes, decorative movement competing with the headline, fake citations.

### Swiss / international typographic
- **Visual:** Restrained grid, asymmetrical balance, geometric shapes, a limited palette and precise typography.
- **Motion:** Alignments, masks and measured shifts communicate structural changes; use an accent sparingly.
- **Use:** Modern informational pieces and identity systems. **Avoid:** assuming red-black-white alone makes a composition Swiss.

### Expressive variable typography
- **Visual:** Flexible type width, weight and rhythm as an expressive material.
- **Motion:** Typography breathes, compresses or expands in response to semantic beats. **Build:** Only use locally available or embedded, licensed fonts; include fallback for missing variation axes. Ensure the text remains readable and do not assume custom fonts are present.

### Title sequence / credits
- **Visual:** Controlled spatial reveals and a strong title hierarchy; artwork and typography establish a mood.
- **Motion:** Use measured beats, recurring motifs and transitions that hint at narrative. Long enough title holds matter more than constant motion.
- **Use:** Openers, event films and short-form campaigns. Never fabricate names or attribution.

## Graphic and illustration-led directions

### Geometric modernism
- **Visual:** Circles, grids, bars and simple constructive shapes carry meaning; limited colors and clean negative space.
- **Motion:** Shape transformation, spatial alignment, periodic rhythms and match cuts. Favor deliberate constraints over a stream of unrelated shapes.
- **Build:** Canvas or SVG; maintain consistent stroke weights and absolute-time state.

### Bold pop / energetic brand
- **Visual:** Punchy scale, strong contrast, playful art and simple graphic symbols.
- **Motion:** Brief anticipation, elastic accent, snappy arrivals and lively holds; let an energetic accent punctuate rather than cover the entire timeline.
- **Use:** Social announcements, youth-oriented campaigns when appropriate. **Avoid:** confusing high energy with flashing or constant movement.

### Flat vector explainer
- **Visual:** Simplified characters, props and icons with consistent geometry, strokes and palette.
- **Motion:** Cause and effect: an object changes, the consequence becomes visible, then the scene resolves. Use staged reveals and clear action arcs.
- **Use:** Education, process explanations, product benefits. **Avoid:** packing too many ideas into one scene.

### Paper cut-out / collage
- **Visual:** Layered paper shapes, cut edges, modest shadows, overlapping images with permitted sources.
- **Motion:** A small parallax offset, sliding layers, hand-placed rearrangement and reveal by tearing/masking illusion.
- **Build:** Use vector silhouettes or allowed embedded images. Make texture stable across frames rather than random noise.

### Hand-drawn / doodle
- **Visual:** Imperfect contours, variable line quality and charming annotations, with consistent art direction.
- **Motion:** Draw-on lines, wobbles of limited amplitude, handwriting-like reveals and subtle secondary movement.
- **Use:** Personal storytelling, approachable education. **Avoid:** implying a handwritten font exists when it does not, or using constant jitter.

### Stop-motion inspired
- **Visual:** Cut-paper, clay-like or arranged-object appearance; small intentional positional changes.
- **Motion:** Hold poses for discrete frames and introduce controlled discontinuities. Use a fixed frame-step or quantized time for deterministic capture.
- **Use:** Handmade, playful stories. **Avoid:** uncontrolled flicker and unintended jumps.

### Line art / technical drawing
- **Visual:** Fine paths, construction lines and callouts. Clear foreground/background separation and readable line weights.
- **Motion:** Stroke reveals, measured tracing and assembly. **Build:** SVG path drawing or Canvas strokes; avoid excessive detail at small sizes.

### Isometric illustration
- **Visual:** Consistent projected axes, simple solids, layered shadows and limited depth.
- **Motion:** Components lift, slide or assemble along the same projected axes. **Build:** Explicit transforms or Canvas projections; do not imply perspective-correct 3D without actual 3D.

## Product, interface and informational directions

### Premium product reveal
- **Visual:** A clear hero object, strong silhouette, limited material cues, deliberate negative space and a restrained palette.
- **Motion:** Details are introduced in stages: silhouette, feature, benefit, final packshot. Use stable highlights and measured camera-like movement.
- **Build:** A stylized procedural object can communicate the idea; obtain real assets for accurate product geometry. Avoid fabricated capabilities or marketing claims.

### Interface / SaaS walkthrough
- **Visual:** Familiar interface controls, content hierarchy, legible labels and believable layout.
- **Motion:** A visible action leads to an observable result; progressively focus attention rather than animate every control. Show important states long enough to read.
- **Use:** Feature demonstration, onboarding. **Avoid:** asserting product behaviors that the user did not confirm.

### Data journalism / charts
- **Visual:** Axes, labels, units, sources and encodings take priority over ornament. Match forms to the type of comparison.
- **Motion:** Reveal a baseline, add data in meaningful order, highlight one insight and preserve relative scale. Show dates, units and caveats where needed.
- **Use:** Reports and explainers. **Avoid:** invented numbers, misleading cropped axes, animation that implies false trends.

### Corporate clarity
- **Visual:** Clean typography, a few brand shapes, credible imagery, consistent component alignment.
- **Motion:** Small directional cues, purposeful reveals and clear pauses. **Use:** internal communication, business updates. **Avoid:** generic stock icons and empty claims.

### Documentary / information-led
- **Visual:** Real supplied images, maps or quotes with attribution and restrained labels. **Motion:** simple image movements, sequential evidence and controlled transitions. **Avoid:** claiming authenticity for invented media; seek rights and protect personal information.

## Textural, cinematic and dimensional directions

### Luxury / elegant
- **Visual:** Space, confident type, a controlled palette and selective detail. **Motion:** restrained starts, considered transitions, quiet holds and one focal gesture. **Avoid:** relying on gold, thin type or slowness alone.

### Cinematic / atmospheric
- **Visual:** Strong framing, depth, tonal contrast and a coherent subject. **Motion:** slow push, reveal through occlusion, lighting-like changes and careful scene cuts. **Build:** procedural depth cues; do not claim photorealistic video without real footage.

### Retro broadcast / analog
- **Visual:** Use a specific period's typography, geometry and color logic; optionally add restrained grain or scan-lines. **Motion:** graphic wipes, stepped changes and title reveals. **Avoid:** rapid flashing, excessive illegibility or anachronistic styles.

### Digital neon / cyber
- **Visual:** Dark field, a limited bright accent, structured grids, crisp vectors and controlled glow. **Motion:** signal sweeps, contour traces and directional pulses. **Avoid:** defaulting to generic neon gradients, flicker, or excessive blur.

### Brutalist / experimental
- **Visual:** Deliberate asymmetry, strong contrast, large type, structural tension and exposed visual mechanics. **Motion:** abrupt cuts or mismatched scales can support meaning. **Avoid:** confusing deliberate disruption with inaccessible chaos.

### Tactile / material-rich
- **Visual:** Material cues such as paper, glass or metal serve a specific idea. **Motion:** layers, light and shadow shift consistently with object movement. **Build:** use vector gradients or lightweight procedural highlights only when approved by the brief; control contrast and rendering cost.

### 3D / dimensional abstract
- **Visual:** Form, perspective, occlusion and light establish depth. **Motion:** orbit, assemble, extrude or rotate with a defined camera and subject.
- **Build:** Use Three.js for actual 3D when it serves the concept, with a compatible GSAP or Anime.js timeline when helpful. Declare pinned dependencies and environment requirements. Preserve deterministic frame seeking.

### Ambient / meditative
- **Visual:** Minimal, repeated shapes and restrained color. **Motion:** slow oscillation, breathing or gradual transformation, designed for seamless looping when required. Provide pause and reduced-motion behavior.

### Dreamlike / surreal
- **Visual:** Unexpected but coherent scale relationships and symbolic object combinations. **Motion:** metamorphosis, impossible transitions, reveal of concealed meaning. **Avoid:** surreal elements that obscure the actual message.

### Organic / nature-inspired
- **Visual:** Curves, growth patterns and restrained natural palettes. **Motion:** branching, unfurling or flow that suggests a process without excessive simulation. Seed any procedural variation to preserve deterministic export.

## Style mixing and selection
Use one dominant system and one supporting accent. Examples: editorial structure + kinetic typography; vector explainer + paper texture; premium product reveal + graphic data overlays. Maintain coherent type hierarchy, line weights, materials, movement character and color roles. Avoid treating unrelated effects as a style.

When recommending a direction, say:
1. Concept and why it fits the audience.
2. Palette/type and composition choices, grounded in provided brand data or proposed as options.
3. Three motion verbs, such as reveal, align, resolve.
4. A risk or tradeoff.
5. A short question seeking the user's preference.

## Further reading
- Motion principles and choreography, Sprout Social Seeds: https://seeds.sproutsocial.com/visual/motion/
- Motion system building blocks: https://www.designsystems.com/5-steps-for-including-motion-design-in-your-system/
- Material Design motion guidance: https://m3.material.io/styles/motion/easing-and-duration
