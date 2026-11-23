# GSAP production reference

## Purpose and selection
Use GSAP for complex choreography, timelines, coordinated DOM/SVG/Canvas/Three.js properties, easing, staggering, runtime playback controls and precision sequencing. Choose it as a primary timeline engine when its strengths fit the storyboard; use Anime.js instead if specified or more suitable. Three.js may render a 3D scene while GSAP animates its properties. Do not use multiple animation engines to control the same property.

This is an independent project reference. GSAP's creators publish an official collection of AI skills; linking to that collection does not install or activate it.

## Dependencies and licensing
- Pin the GSAP release and any plugins to compatible versions. For example, `gsap@3.13.0` is an identifiable release; verify the exact URLs and API before generation. Import only the required modules, register plugins when needed, and avoid silently including unrelated plugins.
- A CDN import needs internet access and may be blocked by a host's CSP. If needed, use an approved local dependency bundle and serve the project locally. Do not describe CDN-backed HTML as offline self-contained.
- GSAP's library has its own **No Charge** standard license, distinct from any license on the official GSAP skill documents. The official license permits many commercial uses but contains restrictions concerning certain competing visual animation builders. Review the current terms for the actual use case and distribution; do not claim that GSAP is MIT-licensed or that all uses are unrestricted.

## Timeline design
- Create a master timeline with an explicit initial paused state. Place animations by scene time, labels or relative positions, rather than chaining long sets of independent `delay`s. Use named sections for clarity.
- Use `fromTo` when exact start/end states matter, and avoid conflicting writes to the same target/property. Recheck immediate-render behavior when multiple `from`/`fromTo` tweens affect the same property.
- Use deliberate `ease`, `duration` and `stagger`; make text readable and allow end holds. Prefer transforms and opacity over layout-changing properties where feasible, and implement meaningful reduced motion for interactive preview.
- Plugins such as SplitText, MorphSVG, DrawSVG or MotionPath can serve specific tasks; use only when needed and register/import them according to the chosen version. Confirm font readiness, path compatibility, brand rights and actual access to each plugin.

## Absolute-time integration
GSAP's numeric timeline positions are in **seconds**. `seek(t, true)` suppresses callbacks; therefore do not rely on timeline callbacks to build required visual state during export. `seek` alone does not pause an advancing timeline: call `pause()` first. For repeat/yoyo, reason about total time and test the actual configured timeline.

Conceptual adapter, assuming an existing DOM/SVG/Three.js scene and timeline:

```js
const timeline = gsap.timeline({ paused: true });
timeline.to(title, { x: 80, opacity: 1, duration: 1, ease: 'power2.out' }, 0);
timeline.to(object.position, { x: 1.5, duration: 1.2, ease: 'power2.inOut' }, 0.4);

function pause() { timeline.pause(); }
function seek(seconds) {
  const t = Math.max(0, Math.min(duration, seconds));
  timeline.pause().seek(t, true);
  renderer.render(scene, camera); // omit for DOM-only animation
}
```

This is a pattern, not a complete animation: define targets, `duration`, renderer and scene where applicable, expose `window.__motion`, await resources, implement controls and fit the approved board. For DOM-only work, remove the renderer call. Animate distinct scene properties so seeking works regardless of call order. If a render was tied to `onUpdate`, explicitly invoke it after a callback-suppressed seek.

## Choreography techniques
- **Kinetic type:** stagger words or lines inside a clipped region; keep a single accessible text equivalent and hold the final phrase.
- **Shape-led transition:** timeline position aligns the exit and entrance around a shared shape, while spatial continuity guides attention.
- **3D product reveal:** animate Three.js object/camera properties on the same paused timeline; after seek render the Three.js scene.
- **Layered editorial sequence:** overlap subtle crop, type and index-line animations; use labels and a meaningful hold instead of constant movement.
- **SVG path motion:** use registered plugins or supported SVG properties where appropriate; verify path geometry and tests at intended size.

## Review
Check first, middle, each transition boundary and final frames, with forward, backward and repeat seeks. Inspect the console and dependency failures. Verify DOM/SVG and WebGL layers stay synchronized, and retain an accessible reduced-motion option. Separate tested observations from assumptions.

## Sources and specialist skills
- Official GSAP skill repository: https://github.com/greensock/gsap-skills
- Official timeline skill: https://github.com/greensock/gsap-skills/blob/main/skills/gsap-timeline/SKILL.md
- Official core skill: https://github.com/greensock/gsap-skills/blob/main/skills/gsap-core/SKILL.md
- GSAP timelines: https://gsap.com/docs/v3/GSAP/Timeline/
- GSAP seek: https://gsap.com/docs/v3/GSAP/Timeline/seek()/
- GSAP standard license: https://gsap.com/community/standard-license/

Optional: a compatible agent environment may allow the official GSAP skills to be installed separately after source and licensing review. A link or reference does not mean they are present in the user's Gemini account.
