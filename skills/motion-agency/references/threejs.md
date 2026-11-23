# Three.js production reference

## Purpose and selection
Use Three.js for actual 3D geometry, materials, lights, cameras, object hierarchies, shaders, particle fields, or imported models. For an animated film combine Three.js with one timeline engine—GSAP or Anime.js—when useful. Three.js draws the scene; a timeline library can set scene properties. Honor the user's chosen tool. Do not invent 3D brand assets or pretend a 2D mockup is a real 3D model.

This is an independently authored guide, not the upstream Three.js skill. Consult current official documentation and version-matched examples. The linked community skills are optional external material and are not installed automatically.

## Dependency and compatibility
- Use a single pinned Three.js release. If using addons, match their version to core. For example, `three@0.180.0` publishes ESM at `build/three.module.js` and addon modules under `examples/jsm/`. Confirm the paths and browser support for the chosen version; versions shown are examples, not claims of latest.
- If using browser ESM, configure an import map before the module script; three.js addons can import the bare specifier `three`. Do not mix multiple versions or multiple copies of Three.js.
- A CDN-backed HTML file requires an allowed network connection and compatible CSP. For offline use, provide legally obtained local modules and matching dependencies, and serve them from a local HTTP server. No runtime should silently download code or assets without disclosing it.
- Detect missing WebGL and module/asset loading failures, show a clear message, and describe a local-browser alternative. Do not claim that a host preview supports WebGL or remote imports without testing it.

Example import map for a version-pinned browser project:

```html
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.180.0/examples/jsm/"
  }
}
</script>
<script type="module">
import * as THREE from 'three';
// Add the scene and animation code here.
</script>
```

This snippet demonstrates dependency wiring only. It is not a complete animation. If the CDN or host is unavailable, do not claim it will run.

## Composition and rendering
1. Define the stage resolution, aspect and output-safe area. Use a Three.js renderer, a scene and a camera; choose a perspective camera for camera depth or orthographic projection for a controlled graphic/isometric treatment.
2. Create purposeful geometry and scene hierarchy. For a premium reveal, build or load a subject, key/fill/rim lighting, a background with sufficient separation, and an intentional camera path. Respect provided brand geometry; label approximations.
3. Choose appropriate material/light pairs. Lit materials need lighting. Avoid automatically using transparent materials or many expensive shadow maps without a reason. Keep a consistent color management and tone-mapping approach for the pinned Three.js version.
4. Layer readable DOM/SVG type over the canvas when appropriate. Keep all layers inside `#motion-stage`, with controls outside. Respect contrast, type rights and safe margins.
5. Set renderer size and pixel ratio intentionally. Responsive preview may scale the stage; export should use the exact declared width and height at device scale factor 1. Update camera projection if its aspect changes. Dispose renderer, geometries, materials and textures where lifecycle demands it.

## Absolute-time motion and frame capture
The public contract is `window.__motion = {duration, fps, width, height, seek, pause, ready}`. Use one master clock in seconds. A `seek(t)` must calculate every visible property from absolute time, update timeline targets, sample mixers where applicable, update shader time uniforms and render once. Stop autonomous loops and clocks in `pause()`. For a compatible Three.js `AnimationMixer`, `setTime(t)` may provide absolute sampling; check action loop, timeScale and other clip state for the chosen version. Complex stateful simulations need a deterministic reset/replay strategy or a documented limitation.

A minimal conceptual pattern, assuming scene, camera, mesh, renderer and `timeline` exist:

```js
function applyTime(t) {
  timeline.pause();
  timeline.seek(t, true);       // GSAP: seconds; callbacks suppressed
  mesh.rotation.y = t * 0.4;  // or compute from a storyboard-specific curve
  renderer.render(scene, camera);
}
function pause() {
  timeline.pause();
  renderer.setAnimationLoop(null);
}
function seek(seconds) {
  const t = Math.max(0, Math.min(duration, seconds));
  applyTime(t);
}
```

This is pseudocode, not a complete project. Do not let GSAP and the direct assignment write the same property. If using Anime.js instead, convert seconds to the engine's configured unit and avoid unsynchronized animation engines. Derive procedural randomness from a fixed seed, not `Math.random()` each frame. Keep the final pose stable.

For screenshot export, render the requested time before capture. Some Chromium/WebGL configurations may need `preserveDrawingBuffer: true` or a different capture strategy; choose based on actual tests rather than promising universal behavior. Capture the full stage, including DOM/SVG overlays. Inspect repeated seeks, out-of-order seeks, transitions, first and last frames, and the resulting MP4. Report whether WebGL was actually available.

## Motion design recipes
- **Dimensional logo reveal:** a permitted logo as geometry or a texture; choreograph lighting, camera and the final lockup without modifying protected brand marks without permission.
- **Product hero:** a stylized or approved real model, measured camera orbit, precise material and light design; coordinate feature labels on a 2D layer.
- **Procedural sculpture:** stable geometry, seeded particle placement and camera movement mapped directly to the storyboard's time.
- **Exploded assembly:** parent logical groups, control separation and alignment along intentional paths, then return to the product silhouette.
- **2D/3D match cut:** transform a geometric anchor across the 3D canvas and overlay, avoiding mismatched frame rate or perspective.

## Sources and optional specialist skills
- Three.js documentation: https://threejs.org/docs/
- Three.js AnimationMixer: https://threejs.org/docs/pages/AnimationMixer.html
- Three.js WebGLRenderer: https://threejs.org/docs/pages/WebGLRenderer.html
- Community Three.js skill collection: https://github.com/CloudAI-X/threejs-skills
- Community Three.js animation skill: https://github.com/CloudAI-X/threejs-skills/blob/main/skills/threejs-animation/SKILL.md

The linked skills are community-maintained, not official Three.js skills. Review version compatibility and licensing before installing. Nothing here installs them in Gemini or enables external integrations.
