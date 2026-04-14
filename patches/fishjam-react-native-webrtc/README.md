# @fishjam-cloud/react-native-webrtc patches

This folder contains `patch-package` patches for selected versions of the Fishjam fork of `react-native-webrtc`.

These patches follow the same simulator-camera compatibility idea used in `react-native-webrtc`.

The patch files in this folder are not an exhaustive list of all versions that may require patching.
They only cover some recent versions that we prepared patches for.
Older versions may also require patching.
If your exact version is not listed here, you can usually adapt one of the existing patches to your version.
These patches are simple because they mainly remove simulator target checks so the library can use the runtime camera device provided by SimCam.

## How to apply

1. Install `patch-package` in your app:
   `npm install -D patch-package`
2. Add `"postinstall": "patch-package"` to your `package.json`.
3. Copy the patch file matching your exact `@fishjam-cloud/react-native-webrtc` version into your app's root `patches/` directory.
4. Reinstall dependencies or run:
   `npx patch-package`

## Available patches

This repository currently includes patch files for:

- `0.25.0`
- `0.25.2`
- `0.25.3`
- `0.25.4`
- `0.25.5`
- `0.25.6`

No upstream fix is known yet.
Older versions likely require patching, even if this folder does not include a patch file for that exact version.
