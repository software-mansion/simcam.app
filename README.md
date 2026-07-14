# [SimCam](https://simcam.swmansion.com)

<p align="center">
  <img src="./assets/simcam-logo.png" alt="SimCam logo" width="180" />
</p>

SimCam lets your iOS simulator use your Mac's camera.

Go to our website for product details and download links: [simcam.swmansion.com](https://simcam.swmansion.com)

## Quick start

SimCam does not require any changes to your code to work, and we have tested it against popular iOS frameworks, camera libraries, and streaming libraries:

1. Head to our website to [download and install SimCam](https://simcam.swmansion.com)
2. Start the SimCam app on your computer
3. Launch your app and navigate to screens where your app uses camera to verify SimCam can stream camera image
4. If everything works correctly, purchase and activate your license to unlock all SimCam features, including Mac camera, image, and custom QR sources
5. See the [troubleshooting](#troubleshooting) section in case of any issues

## Using the Menubar App

SimCam is a macOS menubar app for local simulator development and testing.
Start SimCam before launching the simulator app that should use the camera.
If your simulator app is already running, restart it after SimCam starts so the app can see the simulated camera environment.

Use the menubar app to choose the camera source you want to test with, such as your Mac camera, an image, a video, or a generated QR source.
The settings window also includes diagnostics that can inspect a running simulator app and point out common setup issues.

## Local coding agent use

This setup is intended for coding agents running locally on your Mac. For coding agents running in cloud environments, follow the [SimCam in CI and Cloud Agents](CI.md) guide instead.

Local coding agents should control SimCam with `simcamctl`.
To allow local agent use, open SimCam settings and enable `Install simcamctl in PATH`.
Agents can use `simcamctl` to switch the active camera source, configure generated sources such as QR codes, check license status, and run diagnostics for simulator apps.

After installing `simcamctl`, add instructions for your agent to call:

```bash
simcamctl help
```

The help command is the source of truth for current command line usage.
Agents should use it to discover available commands and options.

## CI or Cloud Agents use

The standard SimCam license is for one desktop seat. This licensing model is not ideal for CI/Automation/Cloud Agent environments where many machines need to be provisioned at any time. For using SimCam in such environments we introduced a special CI/Agent License that allows SimCam to be easily installed and activated in a headless cloud environment and used on as many machines as you require (with the limitation that one license instance is restricted to a single application ID it can be used with).

Go to our [SimCam in CI and Cloud Agents](CI.md) guide for more details, for setup instructions, and example use with GitHub Actions and cloud agent environments.

## Support

Use this repository's [Issues for support and bug reports](https://github.com/software-mansion/simcam.app/issues/new) related to SimCam usage.

SimCam works well for the majority of popular iOS camera frameworks including SwiftUI, UIKit, React Native and Flutter.
We have tested it against a broad set of camera and streaming libraries, including Google's WebRTC, Agora, and popular React Native camera libraries.

### Frameworks / libraries that may require patching

SimCam does not require any changes to your application code to work.
However, some popular libraries make compile-time assertions for simulator environments, assume the camera is not available, and disable camera functionality entirely.
While we work with library authors to remove those checks in future versions of their libraries, older versions may still require local patches.

Below is a list of known libraries with versions that may require patching.
Follow the links for package-specific instructions:

| Library                              | Versions that require patching | Instructions                                                                          |
| ------------------------------------ | ------------------------------ | ------------------------------------------------------------------------------------- |
| `expo-camera`                        | `<55.0.11`                     | [patches/expo-camera](/patches/expo-camera/README.md)                                 |
| `react-native-vision-camera`         | `<5.0`                         | [patches/react-native-vision-camera](/patches/react-native-vision-camera/README.md)   |
| `react-native-webrtc`                | `*`                            | [patches/react-native-webrtc](/patches/react-native-webrtc/README.md)                 |
| `@fishjam-cloud/react-native-webrtc` | `*`                            | [patches/fishjam-react-native-webrtc](/patches/fishjam-react-native-webrtc/README.md) |

We welcome reports about other libraries not listed here that disable camera APIs on simulators. We will prioritize documenting them here together with patching instructions.

## Known limitations

We are actively working on addressing the following limitations:

1. Some video conferencing software based on Google's WebRTC or Agora does not dispatch remote video streams on the simulator when using the hardware H.264 encoder. The current workaround is to force a different codec by default, such as the software H.264 encoder or VP8.
2. Some apps use Apple's Vision framework, which has limited simulator support. In those cases, the camera stream itself will work normally, but app features that depend on Vision may not.

## Troubleshooting

If you have trouble getting SimCam to work in your project, it is usually either a local setup problem or a compatibility issue with SimCam itself.
Before opening an issue, make sure you have done all of the following:

1. Make sure the SimCam app is running before you start your application. Restart your app if needed.
2. Make sure your application code does not perform simulator environment checks that disable camera functionality.
3. Use the `Run Diagnostics` button in the SimCam settings window and follow the guidance if any issues are detected. Make sure your app is running in the simulator when you run diagnostics.
4. Some popular camera libraries require patching. This should typically be detected during diagnostics, but check the section above for the list of known libraries where patches may be necessary.

## Authors

SimCam is created by Software Mansion.

Since 2012 [Software Mansion](https://swmansion.com/) is a software agency with experience in building web and mobile apps as well as complex multimedia solutions. We are Core React Native Contributors and experts in live streaming and broadcasting technologies. We can help you build your next dream product - [Hire us](https://swmansion.com/contact/projects).

Copyright 2026, [Software Mansion](https://swmansion.com/)

[![Software Mansion](https://logo.swmansion.com/logo?color=white&variant=desktop&width=200&tag=simcam-github)](https://swmansion.com/)
