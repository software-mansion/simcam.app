# SimCam public repository

This repository is the public home for SimCam:

- basic information about the product
- issue tracker for support
- compatibility patches for selected camera libraries

SimCam itself is a paid, closed-source product.  
Website and downloads: [simcam.swmansion.com](https://simcam.swmansion.com)

## What is SimCam?

SimCam lets you stream your computer camera into the iOS Simulator as a camera image.

The goal is 0-config usage. In practice, some camera libraries (especially in React Native projects) still make compile-time simulator checks and disable camera APIs before runtime camera devices can be used. This repository hosts patch-package patches for these cases.

## Support

Use this repository's Issues for support and bug reports related to SimCam usage and library patching.

## Patches in this repository

```
patches/
  expo-camera/                      # npm package: expo-camera
  react-native-webrtc/
  react-native-vision-camera/
  fishjam-react-native-webrtc/      # npm: @fishjam-cloud/react-native-webrtc
```

Each folder includes a local `README.md` with package-specific notes.

## Patching instructions

SimCam patches are distributed in `patch-package` format.

1. Install `patch-package` in your app:
   `npm install -D patch-package`
2. Add postinstall to your `package.json`:
   `"postinstall": "patch-package"`
3. Copy the patch file matching your exact dependency version from this repo into your app's root `patches/` folder.
4. Reinstall dependencies or run:
   `npx patch-package`

Patch file naming follows `patch-package` conventions:

- `package+version.patch`
- `@scope+package+version.patch` for scoped packages

## Version notes

| Package | Notes |
| --- | --- |
| `expo-camera` | Patches exist here for `17.0.8`, `17.0.9`, `17.0.10`, `55.0.8`, `55.0.9`, `55.0.10`. Upstream patch is included from `55.0.11`, so no patch is needed on `55.0.11+`. |
| `react-native-vision-camera` | Patches in this repo target `4.x` (`4.5.0`, `4.5.3`, `4.6.0`, `4.6.4`, `4.7.0`, `4.7.3`). VisionCamera `5.x` does not require these patches. |
| `react-native-webrtc` | Patches exist for `106.0.7`, `111.0.6`, `118.0.7`, `124.0.0`, `124.0.4`, `124.0.7`. |
| `@fishjam-cloud/react-native-webrtc` | Patches exist for `0.25.0`, `0.25.2`, `0.25.3`, `0.25.4`, `0.25.5`, `0.25.6`. |

Upstream references:

- `expo-camera`: [expo/expo#44159](https://github.com/expo/expo/pull/44159)
- `react-native-webrtc`: [react-native-webrtc#1801](https://github.com/react-native-webrtc/react-native-webrtc/pull/1801)
- `react-native-vision-camera`: [react-native-vision-camera#3724](https://github.com/mrousavy/react-native-vision-camera/pull/3724)

## Regenerating patches

From repository root:

```bash
python3 scripts/generate_patches.py
```

## Authors

SimCam is created by Software Mansion.

Since 2012 [Software Mansion](https://swmansion.com/) is a software agency with experience in building web and mobile apps as well as complex multimedia solutions. We are Core React Native Contributors and experts in live streaming and broadcasting technologies. We can help you build your next dream product - [Hire us](https://swmansion.com/contact/projects).

Copyright 2026, [Software Mansion](https://swmansion.com/) [![Software Mansion](https://logo.swmansion.com/logo?color=white&variant=desktop&width=200&tag=simcam-github)](https://swmansion.com/)
