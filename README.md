# [SimCam](https://simcam.swmansion.com)

SimCam lets your iOS simulator use your Mac's camera.

Go to our website for product details and download links: [simcam.swmansion.com](https://simcam.swmansion.com)

## Quick start

SimCam does not require any changes to your code to work and we've tested it agains all popular iOS frameworks, camera and streaming libraries:

1. Head to our website to [download and install SimCam](https://simcam.swmansion.com)
2. Start SimCam app on your computer
3. Launch your app and navigate to screens where your app uses camera to verify SimCam can stream camera image
4. If everything works correctly purchase and activate your license to enjoy all features of SimCam including Mac's camera, image, and custom QR sources
5. See the [troubleshooting](#troubleshooting) section in case of any issues

## Support

Use this repository's [Issues for support and bug reports](/issues/new) related to SimCam usage.

SimCam works well for the majority of popular iOS camera frameworks including SwiftUI, UIKit, React Native and Flutter.
We've tested it agains a multitude of camera or streaming focused libraries like Google's webrtc, Agora, or popular camera-focused libraries in React Native ecosystem.

### Frameworks / libraries that may require patching

SimCam does not require any changes to your application code to work.
However, some popular libraries make compile-level assertions for simulator environments assuming camera is not availabile and disabling camera functionaliy entirely.
While we work with library authors to remove those checks in future versions of their libraries (which we already did for some libraries), the older versions may require local patches.

Below we present a list of known libraries with corresponding versions that require patching.
Follow the provided links for direct patching instructions and resources:

[GENRATE A TABLE WITH LIB NAME, VERSION RANGE THAT REQUIRE PATCH, LINK TO PATCHES FOLDER]

We welcome any feedback about other libraries not listed here that disable camera APIs use on simulators and would prioritize to get them listed here along with patching instructions.

## Troubleshooting

If you have troubles getting SimCam to work for your project, it is either a problem with your local setup or a compatiblity issue with SimCam itself.
Before opening an issue make sure that you did all of the following:

1. Make sure that SimCam app is running _before_ you start your application. Restart your app if that's not the case.
2. Make sure that your application code doesn't perform any simulator environment checks that disables camera functionality.
3. Use "Run Diagnostics" button from SimCam settings windows and follow the guidance in case any issues are detected. Make sure your app is launched on the simulator when you perform diagnostics.
4. Some popular camera libraries require patching. This should typically be detected in the diagnostics step, but check the above section for the list of known libraries where patches may be necessary.
5. Make sure that your application code doesn't perform any simulator environment checks that disables camera functionality.

## Authors

SimCam is created by Software Mansion.

Since 2012 [Software Mansion](https://swmansion.com/) is a software agency with experience in building web and mobile apps as well as complex multimedia solutions. We are Core React Native Contributors and experts in live streaming and broadcasting technologies. We can help you build your next dream product - [Hire us](https://swmansion.com/contact/projects).

Copyright 2026, [Software Mansion](https://swmansion.com/)

[![Software Mansion](https://logo.swmansion.com/logo?color=white&variant=desktop&width=200&tag=simcam-github)](https://swmansion.com/)
