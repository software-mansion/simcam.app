# react-native-vision-camera patches

`react-native-vision-camera` does not require patches starting from version `5.0`.

This folder contains `patch-package` patches for selected `react-native-vision-camera` `4.x` versions that disable camera behavior on simulator builds.

The patch files in this folder are not an exhaustive list of all versions that may require patching.
They only cover some recent versions that we prepared patches for.
Older versions may also require patching.
If your exact version is not listed here, you can usually adapt one of the existing patches to your version.
These patches are simple because they mainly remove simulator target checks so the library can use the runtime camera device provided by SimCam.

## How to apply

1. Install `patch-package` in your app:
   `npm install -D patch-package`
2. Add `"postinstall": "patch-package"` to your `package.json`.
3. Copy the patch file matching your exact `react-native-vision-camera` version into your app's root `patches/` directory.
4. Reinstall dependencies or run:
   `npx patch-package`

## Available patches

This repository currently includes patch files for:

- `4.5.0`
- `4.5.3`
- `4.6.0`
- `4.6.4`
- `4.7.0`
- `4.7.3`

## Important version note

Versions earlier than `5.0` may still require patching, even if this folder does not include a patch file for that exact version.
VisionCamera `5.0` and newer do not require patches from this folder.

Upstream reference: [react-native-vision-camera#3724](https://github.com/mrousavy/react-native-vision-camera/pull/3724)
