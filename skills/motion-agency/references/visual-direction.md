# Visual direction, storyboard and composition

## Contents
1. Read the brief as a communication problem
2. Decode references and define a design system
3. Compose frames with hierarchy
4. Type, color, imagery and depth
5. Build the narrative and storyboard
6. Direct transitions and sound
7. Worked example and review
8. Sources

## 1. Read the brief as a communication problem
Before decorating anything, name the audience, action they should take or insight they should remember, context of viewing, mandatory information and constraints. A good piece carries one main message per beat. Prioritize user-supplied factual and brand data; label creative or numerical assumptions. Do not invent a customer's results, citations, testimonials or product functions.

Create a compact creative brief: `purpose / audience / core message / desired feeling / duration / format / required content / forbidden content / resources / chosen look / constraints`. Mark each line confirmed, proposed or unknown. Ask only the highest-impact missing questions. If someone delegates creative choices, propose defaults and invite changes.

## 2. Decode references and define a design system
For each viewable reference, observe framing, subject size, geometry, contrast, light, palette, rhythm, transitions and texture. Label observation vs hypothesis; a still cannot reveal timing. Ask: “What should I take from this—the color, type, pacing, framing, or overall feeling?” Note what must not be copied. Build an original look from principles rather than reproducing a specific protected work.

Define a small, coherent system:
- **Palette:** dominant neutral or brand color, foreground, accent and optional secondary. Confirm supplied brand values. Check legibility in context.
- **Type:** one headline system and one supporting system; define scale, line length, case, weight and safe fallbacks. Specify user-supplied copy exactly.
- **Geometry:** shape families, corner treatment, stroke weight, visual grid and allowed texture.
- **Image:** photography, illustration, procedural geometry, UI or typographic-only. Require permission and access to use specific images or fonts.
- **Motion:** three action verbs and a pacing profile; define how objects enter, relate, transition and settle.
- **Composition:** focal subject, margins, spatial rhythm, where the audience's gaze should go.

## 3. Compose frames with hierarchy
A frame needs a focal point, a supporting element and visual breathing room. Establish contrast through scale, weight, position or value, not just hue. Use alignment and proximity to group related items. Create a reading path from primary message to secondary detail. Apply a consistent grid but do not use a grid as an excuse for static sameness; contrast wide and tight views intentionally.

Useful strategies:
- **Hero + annotation:** one large subject and a restrained label, good for a product feature.
- **Headline + proof:** main claim paired with a real supplied number or illustration, good for an announcement.
- **Split screen:** two complementary ideas or before/after; do not imply an unverified outcome.
- **Sequence / progression:** repeat an anchor across changing scenes to show a process.
- **Reveal / conceal:** hide a portion with a simple mask, then expose it to focus attention.
- **Full-bleed type:** use bold scale while protecting safe edges and sufficient reading time.

For delivery sizes, choose actual dimensions and aspect ratio to suit the channel; examples are 1920×1080 landscape, 1080×1920 portrait, and 1080×1080 square. These are starting points, not platform requirements. Use even dimensions for standard H.264 output. Check legibility at the smallest intended display size. Place important information within a generous safe region and check the actual platform's overlays rather than pretending there is one universal safe-area percentage.

## 4. Type, color, imagery and depth
**Typography:** Preserve exact text and language. Distinguish display type from explanatory copy. Avoid overlong lines, tiny footnotes, unstable fallback metrics, excessive text along paths and word breaks that change meaning. Plan a hold after the complete phrase appears. System fonts are a safe default; embedded fonts must be licensed and actually accessible. Generated image text may be inaccurate; production text should be code-rendered when accuracy matters.

**Color:** Choose values that support readable contrast and a coherent mood. Use the user's exact brand colors if provided. Do not infer colors from a low-quality compressed screenshot without confirming critical values. Use accent color to indicate hierarchy or meaning, not as a substitute for one. Verify contrast against the actual background after overlays and gradients.

**Imagery:** Distinguish essential owned assets from inspiration. Use authorized logos as supplied. Explain any unavoidable simplification. Be honest about limitations of procedurally drawing a real product, human or place. Give alternative visual directions rather than fabricating a faithful reproduction.

**Depth and light:** Decide on flatness, layered parallax, simulated perspective or actual 3D before animating. Keep the focal plane clear. Specify light direction, shadow softness and layer order consistently. Too much depth, blur or camera movement can make both reading and rendering worse.

## 5. Build the narrative and storyboard
A common structure is **hook → context → transformation → evidence or feature → resolution → end hold**. This is a tool, not a mandatory template. For an educational story, causality may matter more than a dramatic hook; for an ambient loop, continuity matters more than a call to action. Each scene should answer: what changes, why it changes and what the viewer should notice.

Plan rough timing by information load rather than fixed speed. Allow longer holds for unfamiliar text. Storyboard in a table with: scene, in/out time, framing, visible elements and exact/proposed text, action and easing, transition, narrative purpose, asset/dependency. Time ranges should sum to the proposed duration without gaps or accidental overlaps. Include aspect, dimensions, fps, end frame/loop seam, safety and optional sound. Do not fabricate dialogue, precise time sync or data.

A strong storyboard specifies visual states at the opening, change and landing. Use still-frame sketches or contact sheets as conceptual aids; AI-generated images are illustrative and can differ from code-rendered results. Offer the user revision and obtain clear approval before coding.

## 6. Direct transitions and sound
Choose transitions for continuity: match shape/position across a cut, animate an existing object into the next scene, slide a mask across a meaningful boundary, or simply cut to change subject. Plan the outgoing and incoming visual states and protect text readability during overlap. Avoid using every transition style in one piece.

Choose a restrained audio approach only if requested. No autoplay; seek rights to supplied music/voice. Browser playback and video export are separate operations. If no audio is supplied or approved, plan a silent animation and say so. If audio is used, plan markers only from real supplied timestamps or user-approved timing, not invented beat positions.

## 7. Worked example — illustrative, not factual
Brief: introduce an imaginary scheduling concept to a general audience in 12 seconds, landscape, with no supplied brand assets. Until the user approves, proposed words and visual choices are not final.

- **Direction:** editorial geometry with a calm, useful tone. Dark neutral, light foreground and one proposed accent; large headline and a simple time-block motif.
- **0–2 s:** A blank block opens like a calendar page; proposed text “Make room” appears and settles. Purpose: introduce the theme.
- **2–5 s:** Overlapping blocks separate and align in a simple row; proposed text “See the day clearly.” Purpose: show order.
- **5–9 s:** One block becomes a focused frame around a short message; supplied product name would replace a temporary generic label only after confirmation. Purpose: connect idea to product.
- **9–12 s:** Everything resolves to the chosen end card and holds. Purpose: aid recall. Transition: a shared block shape carries between scenes. Silent by default.

Ask: “Do you approve this storyboard, or what would you like to change?”

## 8. Review
- Can the message be understood from selected still frames? Is the next action clear when one is requested?
- Does each move serve hierarchy, continuity, character, or meaning?
- Are key text, details, margins, contrast and chosen language appropriate for actual delivery size?
- Are claims, images and brand assets supplied or clearly proposed?
- Do durations make room for reading and a final hold?
- Are meaningful changes faithfully represented in the user's approved board?

## Sources
- Motion planning and choreography: https://www.designsystems.com/5-steps-for-including-motion-design-in-your-system/
- Accessibility considerations for web motion: https://web.dev/learn/accessibility/motion
- Google image understanding guidance, API-specific: https://ai.google.dev/gemini-api/docs/image-understanding
