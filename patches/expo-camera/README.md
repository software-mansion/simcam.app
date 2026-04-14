# expo-camera patches

`expo-camera` does not require patches starting from version `55.0.11`.

This folder contains `patch-package` patches for selected `expo-camera` versions that still block simulator camera usage at compile time.

The patch files in this folder are not an exhaustive list of all versions that may require patching.
They only cover some recent versions that we prepared patches for.
Older versions may also require patching.
If your exact version is not listed here, you can usually adapt one of the existing patches to your version.
These patches are simple because they mainly remove simulator target checks so the library can use the runtime camera device provided by SimCam.

## How to apply

1. Install `patch-package` in your app:
   `npm install -D patch-package`
2. Add `"postinstall": "patch-package"` to your `package.json`.
3. Copy the patch file matching your exact `expo-camera` version into your app's root `patches/` directory.
4. Reinstall dependencies or run:
   `npx patch-package`

## Available patches

This repository currently includes patch files for:

- `17.0.8`
- `17.0.9`
- `17.0.10`
- `55.0.8`
- `55.0.9`
- `55.0.10`

## Important version note

`expo-camera` has the upstream fix as of `55.0.11` (PR: [expo/expo#44159](https://github.com/expo/expo/pull/44159)).

Versions earlier than `55.0.11` may still require patching, even if this folder does not include a patch file for that exact version.
For `55.0.11` and newer, no patch from this folder is required.
