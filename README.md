# Motion Agency

A creative direction and motion graphics workflow for Gemini. Motion Agency guides a project from an initial brief through reference collection, storyboard approval, and a code-based browser animation.

The project combines a reusable skill with a per-project agent brief. Its reference library covers visual styles, storyboarding, animation techniques, creative recipes, and Gemini-specific workflows.

## Contents

- [How it works](#how-it-works)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Start a project](#start-a-project)
- [Output and video rendering](#output-and-video-rendering)
- [Using Motion Agency without an installed skill](#using-motion-agency-without-an-installed-skill)
- [Compatibility and limitations](#compatibility-and-limitations)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Resources](#resources)

## How it works

Motion Agency uses two complementary roles:

- **Motion director:** clarifies the brief, develops a visual direction, and presents a storyboard.
- **Motion graphics designer:** translates the approved storyboard into a browser animation using code.

A typical project follows four stages:

1. **Discovery.** Gemini asks a small number of focused questions about the goal, audience, format, and desired visual style.
2. **Resource collection.** The user provides assets and references in one or more batches. Gemini waits for **DONE** before finalizing a storyboard. Use **DONE — no assets** if there are no materials to provide.
3. **Direction and approval.** Gemini proposes a time-coded storyboard. The user can request revisions or, where image generation is available, an illustrative storyboard image. Production begins only after explicit storyboard approval, unless the user waives that step.
4. **Production.** Gemini creates a browser animation and provides instructions for rendering it to video. The default approach is a self-contained HTML file using plain HTML, CSS, SVG, Canvas, and JavaScript.

These stages are instructions to the model, not technical guarantees. Review the storyboard, generated code, and final output before use.

## Project structure

```text
motion-agency/
├── agents/
│   └── AGENT.md
├── skills/
│   └── motion-agency/
│       ├── references/
│       │   ├── creative-recipes.md
│       │   ├── gemini-workflow.md
│       │   ├── motion-styles.md
│       │   ├── motion-techniques.md
│       │   └── visual-direction.md
│       └── SKILL.md
└── README.md
```

| Path | Purpose |
| --- | --- |
| [`agents/AGENT.md`](agents/AGENT.md) | Per-project launcher defining the roles and workflow. |
| [`skills/motion-agency/SKILL.md`](skills/motion-agency/SKILL.md) | Skill instructions, workflow gates, production requirements, and a rendering tutorial. |
| [`creative-recipes.md`](skills/motion-agency/references/creative-recipes.md) | Adaptable concepts, handoff templates, critique, and troubleshooting. |
| [`gemini-workflow.md`](skills/motion-agency/references/gemini-workflow.md) | Gemini setup considerations, resource handling, and capability limitations. |
| [`motion-styles.md`](skills/motion-agency/references/motion-styles.md) | A reference library of visual and motion styles. |
| [`motion-techniques.md`](skills/motion-agency/references/motion-techniques.md) | Animation principles, browser techniques, accessibility, and capture guidance. |
| [`visual-direction.md`](skills/motion-agency/references/visual-direction.md) | Composition, typography, visual research, and storyboarding. |

> **Naming:** The repository and skill directory are named `motion-agency`. The current `name` in `SKILL.md` and the name referenced by `AGENT.md` are `motion-director`. Select `motion-director` in Gemini if that is the name displayed. If a host requires a skill directory to match its metadata name, upload a copy of the skill directory named `motion-director` or use the ZIP method below. Do not change only one name without updating the corresponding references.

## Requirements

- A signed-in Gemini account with access to the relevant features. Skills availability may vary by account type, administrator settings, region, and rollout.
- The files in this repository. An installed skill should include both `SKILL.md` and its `references/` directory.
- A modern browser for opening the generated animation locally, if the active Gemini environment does not provide a suitable preview.
- Optional local tools for frame-by-frame video rendering: Python, Playwright, a Playwright-compatible Chromium installation, and FFmpeg. Installation may require administrator approval.

The skill and launcher are text instructions. They do not install software, guarantee access to Gemini tools, or automatically create a video file.

## Installation

### Option 1: Upload the skill folder

If Skills is available in your Gemini web app:

1. Open [Gemini](https://gemini.google.com/).
2. Go to **Customize → Skills → Create → Upload**.
3. Select the `skills/motion-agency/` folder, or a copy named `motion-director` if the upload flow requires the folder name to match the skill metadata.
4. Review the imported skill and confirm that the reference files are included.
5. Create or activate the skill.

To update an existing installation, open the skill and use **More → Replace skill**. Upload the complete skill folder or archive so that the references are included with the updated instructions.

### Option 2: Create and upload a ZIP archive

The archive should contain `SKILL.md` at its root, alongside the `references/` directory. From the repository root, run:

```bash
cd skills/motion-agency
python3 -m zipfile -c ../../motion-agency-skill.zip SKILL.md references
```

Then select `motion-agency-skill.zip` in the Gemini skill-upload flow described above. On systems where the Python command is named `python`, use that command instead of `python3`.

Uploading `SKILL.md` alone installs only the instructions; it does not include the expanded reference library. See Google's [skill creation and upload guide](https://support.google.com/gemini/answer/17094296?hl=en&co=GENIE.Platform%3DDesktop) for current requirements.

## Start a project

1. Start a new Gemini chat and select the installed `motion-director` skill using the available `/` or `@` selector. An active skill may also be selected automatically, but automatic selection is not guaranteed.
2. Attach [`agents/AGENT.md`](agents/AGENT.md) to your opening message.
3. Describe the animation you want to make. Include any details you already know, such as the audience, duration, placement, message, and desired style.
4. Answer Gemini's questions and provide references or assets in batches.
5. When all resources have been sent, write **DONE**. If you have no resources, write **DONE — no assets**.
6. Review the proposed storyboard, request any revisions, and approve it explicitly before production.

Example opening prompt:

```text
Use the motion-director skill and the attached AGENT.md.

I need a 20-second motion graphic introducing a productivity tool. It will
appear on our website. Ask me about the visual direction and wait for my
assets before creating the storyboard.
```

Gemini may ask for logos, brand guidelines, copy, images, fonts, or examples. Google documents up to 10 supported file attachments per prompt, subject to availability; an attached `AGENT.md` counts toward the limit for that message. File-size, file-type, and context limits also apply. See [Google's file-upload guidance](https://support.google.com/gemini/answer/14903178?hl=en&co=GENIE.Platform%3DDesktop).

Only upload materials you are authorized to use. Identify references that are for inspiration rather than direct reproduction.

## Output and video rendering

After storyboard approval, the default deliverable is a self-contained browser animation. The skill instructs Gemini to use a deterministic timeline so that individual frames can be captured for video rendering.

The skill also provides a local frame-by-frame rendering tutorial using Python, Playwright, Chromium, and FFmpeg. The baseline image-sequence workflow produces a **silent MP4**; adding authorized audio is a separate step. A local screen recorder can be a simpler alternative, but may be less frame-accurate.

Generated code and rendering instructions should be reviewed and tested in the intended environment. A browser preview, generated HTML file, and rendered video are distinct outputs; do not assume one has been created merely because another exists.

## Using Motion Agency without an installed skill

If your account does not have access to Skills, you can use the files as chat attachments instead:

1. Attach `agents/AGENT.md` and `skills/motion-agency/SKILL.md` to a Gemini chat.
2. Attach the relevant files from `skills/motion-agency/references/` as needed.
3. Ask Gemini to follow the attached instructions, then provide your project brief.
4. Send project assets in additional batches and finish with **DONE**.

This approach uses the files as conversational context; it does not install or activate a skill. Attachment limits and context limits still apply.

If you need to move the work into a separate session, carry over the approved storyboard, requirements, and relevant instructions. Reattach the assets and references needed for production, and confirm the new session can access them. A new session may not retain the original conversation or files.

## Compatibility and limitations

- **Gemini features vary.** Skill installation, image generation, previews, file downloads, and other features depend on the account and environment.
- **Canvas compatibility is limited.** Google currently documents that Gemini app Skills do not yet work with Canvas. If necessary, complete direction in one session and transfer the approved brief and relevant materials to a compatible session. Check Google's current [Skills feature guidance](https://support.google.com/gemini/answer/18560919?hl=en).
- **Storyboard images are optional.** An illustrative image requires an available image-generation capability. If unavailable, use the written storyboard or a prompt for an available image tool.
- **Plain code is the default.** The workflow does not assume external libraries, fonts, images, or network access. A library such as Three.js is an additional dependency and should be used only when appropriate and available.
- **References are guidance, not a guarantee.** The model may miss instructions, misunderstand assets, or produce code that requires revision. Verify visual quality, accessibility, factual claims, and export behavior.
- **Confidentiality and rights remain your responsibility.** Follow your organization's policies and obtain permission for assets, music, fonts, and other materials before use.

## Troubleshooting

| Problem | Suggested action |
| --- | --- |
| Skills is not available | Check account or administrator settings, or use the files as chat attachments. |
| Gemini does not use the skill | Select `motion-director` explicitly if the selector is available, or attach the relevant instructions. |
| A reference file is not available to Gemini | Reattach it or upload the complete skill with its reference directory. |
| Gemini starts production before approval | Restate the workflow gate and ask it to return to the storyboard. |
| A storyboard image cannot be generated | Use the written storyboard or request a prompt for an available image tool. |
| The animation does not preview in Gemini | Save the complete HTML locally and open it in a compatible browser. |
| A video export differs from the preview | Check dimensions, frame rate, fonts, asset loading, playback pause, and deterministic frame seeking. |
| The new session does not know the project | Transfer the approved brief and storyboard, and reattach the necessary assets and instructions. |

For a first test, use a short brief and a small set of assets. Check that Gemini waits for **DONE**, asks for explicit storyboard approval, and only then creates the animation.

## Contributing

Improvements to the skill, reference library, and documentation are welcome. When proposing a change:

1. Explain the problem and intended improvement.
2. Keep the **DONE** and storyboard-approval gates intact unless the change explicitly addresses them.
3. Update the relevant references and keep the instructions consistent with the agent launcher.
4. Check any external links and platform-specific claims against current documentation.
5. Describe what you tested and any limitations.

Avoid including private project assets, credentials, or material you do not have permission to share.

## License

No license file was included in the project structure provided for this README. Add a license to the repository and consult its terms before redistributing or reusing the project.

## Resources

- [Create and manage skills for Gemini Apps](https://support.google.com/gemini/answer/17094296?hl=en&co=GENIE.Platform%3DDesktop)
- [Write effective skills for Gemini Apps](https://support.google.com/gemini/answer/17102773?hl=en)
- [About the transition from Gems to skills](https://support.google.com/gemini/answer/18560919?hl=en)
- [Upload and analyze files in Gemini Apps](https://support.google.com/gemini/answer/14903178?hl=en&co=GENIE.Platform%3DDesktop)
