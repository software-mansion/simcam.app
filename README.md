# [SimCam](https://simcam.swmansion.com)

SimCam lets your iOS simulator use your Mac's camera.

Go to our website for product details and download links: [simcam.swmansion.com](https://simcam.swmansion.com)

## Quick start

SimCam does not require any changes to your code to work, and we have tested it against popular iOS frameworks, camera libraries, and streaming libraries:

1. Head to our website to [download and install SimCam](https://simcam.swmansion.com)
2. Start the SimCam app on your computer
3. Launch your app and navigate to screens where your app uses camera to verify SimCam can stream camera image
4. If everything works correctly, purchase and activate your license to unlock all SimCam features, including Mac camera, image, and custom QR sources
5. See the [troubleshooting](#troubleshooting) section in case of any issues

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
