# Using SimCam in CI and Cloud Agents

SimCam can be installed and controlled from command line on macOS CI runners and cloud-agent environments. The automation setup has three steps:

1. Generate a CI/Agent license token using the purchased license key at [simcam-license.swmansion.com](https://simcam-license.swmansion.com).
2. Store that token in your CI or cloud-agent secret store.
3. Add install and activation steps to your CI workflow or Cloud Agent environment file

## Install SimCam

For CI or Cloud Agent environments, we recommend installing SimCam via Homebrew:

```bash
brew install --cask --appdir="$HOME/Applications" software-mansion/tap/simcam
```

The cask installs the SimCam app and links `simcamctl`, which allows further control via the CLI interface.
The above command installs the latest version of SimCam. If needed, you can install a specific SimCam version by appending it to the end of the cask name (e.g. `software-mansion/tap/simcam@1.12`).

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

## Notes

In your CI / agent workflows, use static images or videos as camera sources.
Typically, cloud environments either lack a Mac camera entirely (e.g. GitHub-hosted runners) or can't grant it a system permission non-interactively, so the Mac camera source generally isn't usable in automation.

If you run on self-hosted / your own Mac fleet and still want to use the Mac camera, you need to log into a GUI session on that machine once (e.g. via Screen Sharing/VNC) and approve the camera permission for SimCam in System Settings. There is no CLI or non-interactive way to grant this permission.
