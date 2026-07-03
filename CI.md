# Using SimCam in CI and Cloud Agents

SimCam can be installed and controlled from command line on macOS CI runners and cloud-agent environments. The automation setup has three steps:

1. Install `SimCam.app` and the bundled `simcamctl` CLI.
2. Generate a CI/Agent license token from your SimCam CI/Agent license key.
3. Store that token in your CI or cloud-agent secret store and install it before launching the simulator app.

## Install SimCam

Install SimCam with Homebrew:

```bash
brew install --cask --appdir="$HOME/Applications" software-mansion/tap/simcam
```

The cask installs `SimCam.app` and links `simcamctl` into Homebrew's `bin` directory.

## Activate SimCam for Automation

Generate a CI/Agent license token at [simcam-license.swmansion.com](https://simcam-license.swmansion.com). This requires a SimCam CI/Agent license, which is separate from a desktop single-seat license. The panel converts your CI/Agent license key into a signed token that can be used offline by CI runners and cloud agents.

When generating the token, enter the bundle ID of the simulator app that will use SimCam. The generated token only works for the bundle IDs registered before token generation. To use one token with multiple simulator apps, add each app's bundle ID in the license panel before generating the token. Additional CI/Agent licenses purchased with the same email address let the same account register more bundle IDs. If you add or change bundle IDs later, generate a new token and update the secret in your CI or agent environment.

Keep the generated token in your CI or cloud-agent secret store. Do not commit it to the repository or print it in logs. The token starts with `simcam.` and can be stored under any secret name you prefer.

Install the token before launching the simulator app:

```bash
simcamctl license install-token "<license-token-from-your-secret-store>"
```

Installing the token also starts SimCam if it is not already running.

## GitHub Actions Example

Store the generated token as a GitHub Actions secret, for example `SIMCAM_LICENSE_TOKEN`, then install SimCam and the token before your simulator app or test step:

```yaml
jobs:
  ios-tests:
    runs-on: macos-15
    steps:
      - uses: actions/checkout@v4

      - name: Install SimCam
        run: brew install --cask --appdir="$HOME/Applications" software-mansion/tap/simcam

      - name: Activate SimCam
        env:
          SIMCAM_LICENSE_TOKEN: ${{ secrets.SIMCAM_LICENSE_TOKEN }}
        run: simcamctl license install-token "$SIMCAM_LICENSE_TOKEN"

      - name: Run simulator tests
        run: |
          # Launch or test the simulator app only after SimCam is active.
          xcodebuild test \
            -scheme YourApp \
            -destination 'platform=iOS Simulator,name=iPhone 16'
```

## Cloud Agent Setup

For cloud-agent environments, add the generated token to the agent platform's secret store and expose it to the agent bootstrap as `SIMCAM_LICENSE_TOKEN`. Run the same install and activation commands before the agent launches the simulator app:

```bash
brew install --cask --appdir="$HOME/Applications" software-mansion/tap/simcam
simcamctl license install-token "$SIMCAM_LICENSE_TOKEN"
```
