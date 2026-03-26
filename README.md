# simcam.app patches

[patch-package](https://github.com/ds300/patch-package) patches so **iOS Simulator** can use a **runtime** video device (for example SimCam’s injected virtual camera) instead of libraries that skip camera capture at compile time.

Upstream fixes this pattern in:

| Library | Reference |
| --- | --- |
| `expo-camera` | [expo/expo#44159](https://github.com/expo/expo/pull/44159) |
| `react-native-webrtc` | [react-native-webrtc#1801](https://github.com/react-native-webrtc/react-native-webrtc/pull/1801) |
| `react-native-vision-camera` | [react-native-vision-camera#3724](https://github.com/mrousavy/react-native-vision-camera/pull/3724) |
| `@fishjam-cloud/react-native-webrtc` | Same idea as `react-native-webrtc` (forked WebRTC module) |

Until those land in the versions you depend on, copy the matching patch into your app’s `patches/` directory.

## Layout

```
patches/
  expo-camera/                      # npm package: expo-camera
  react-native-webrtc/
  react-native-vision-camera/
  fishjam-react-native-webrtc/      # npm: @fishjam-cloud/react-native-webrtc
```

Filenames follow patch-package: `package+version.patch` (scoped packages use `@scope+package+version.patch`).

## Usage

1. Install patch-package in your app: `npm install -D patch-package` (or Yarn / pnpm equivalent).
2. Add a postinstall script, for example: `"postinstall": "patch-package"`.
3. Copy **one** patch file that matches your locked dependency version from this repo into your project’s `patches/` folder (same path patch-package expects: project root `patches/`).
4. Run `npx patch-package` (or reinstall `node_modules`).

## Covered versions (generated Mar 2026)

| Package | Versions with a patch in this repo |
| --- | --- |
| `expo-camera` | `17.0.8`, `17.0.9`, `17.0.10`, `55.0.8`, `55.0.9`, `55.0.10` |
| `expo-camera` (no patch) | `55.0.11` and newer on the 55 line include the upstream runtime-camera behavior; prefer upgrading instead of patching. |
| `react-native-webrtc` | `106.0.7`, `111.0.6`, `118.0.7`, `124.0.0`, `124.0.4`, `124.0.7` |
| `react-native-vision-camera` | `4.5.0`, `4.5.3`, `4.6.0`, `4.6.4`, `4.7.0`, `4.7.3` (same iOS change; 4.x `CameraSession+Configuration.swift` matches across these) |
| `@fishjam-cloud/react-native-webrtc` | `0.25.0`, `0.25.2`, `0.25.3`, `0.25.4`, `0.25.5`, `0.25.6` |

## Regenerating patches

From this repo root:

```bash
python3 scripts/generate_patches.py
```

That script installs each listed version, edits `WebRTCModule+RTCMediaStream.m`, and runs `patch-package`. `expo-camera` and `react-native-vision-camera` patches are copied from validated SimCam example patches in the network-limiter worktree when refreshing by hand.
