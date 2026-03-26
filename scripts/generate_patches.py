#!/usr/bin/env python3
"""
Generate patch-package files for SimCam iOS simulator runtime camera fixes.
Upstream references:
- expo-camera: https://github.com/expo/expo/pull/44159
- react-native-webrtc: https://github.com/react-native-webrtc/react-native-webrtc/pull/1801
- react-native-vision-camera: https://github.com/mrousavy/react-native-vision-camera/pull/3724
- @fishjam-cloud/react-native-webrtc: same approach as upstream WebRTC (compile-time simulator skip)
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATCHES = ROOT / "patches"

SIM_CHECK = """#if TARGET_IPHONE_SIMULATOR
    AVCaptureDevice *cameraDevice = [AVCaptureDevice defaultDeviceWithMediaType:AVMediaTypeVideo];
    if (cameraDevice == nil) {
        return videoTrack;
    }
#endif

"""


def patch_webrtc_media_stream_m(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "AVFoundation/AVFoundation.h" not in text:
        if "#if TARGET_OS_IOS" in text and "#import <React/RCTLog.h>" in text:
            text = text.replace(
                "#if TARGET_OS_IOS\n\n#import <React/RCTLog.h>",
                "#if TARGET_OS_IOS\n\n#import <AVFoundation/AVFoundation.h>\n#import <React/RCTLog.h>",
                1,
            )
        elif "#if TARGET_OS_IOS" in text:
            text = text.replace(
                "#if TARGET_OS_IOS\n",
                "#if TARGET_OS_IOS\n#import <AVFoundation/AVFoundation.h>\n",
                1,
            )
        else:
            text = text.replace(
                "#import <objc/runtime.h>\n",
                "#import <objc/runtime.h>\n\n#import <AVFoundation/AVFoundation.h>\n",
                1,
            )

    marker = "#if !TARGET_IPHONE_SIMULATOR\n"
    if marker not in text:
        raise RuntimeError(f"Missing simulator guard in {path}")
    if "defaultDeviceWithMediaType:AVMediaTypeVideo" in text:
        return

    m = re.search(
        r"#if !TARGET_IPHONE_SIMULATOR\n(?P<body>(?:    .*\n)+?)#endif\n",
        text,
    )
    if not m:
        raise RuntimeError(f"Could not parse capturer block in {path}")
    body = m.group("body")
    text = text.replace(m.group(0), SIM_CHECK + body, 1)
    path.write_text(text, encoding="utf-8")


def run_patch_package(work: Path, pkg_name: str, npm_spec: str) -> Path:
    env = os.environ.copy()
    env["npm_config_audit"] = "false"
    env["npm_config_fund"] = "false"
    subprocess.run(
        ["npm", "init", "-y"],
        cwd=work,
        check=True,
        env=env,
        capture_output=True,
    )
    pkg_json = work / "package.json"
    data = pkg_json.read_text(encoding="utf-8")
    if '"patch-package"' not in data:
        subprocess.run(
            ["npm", "install", "--save-dev", "patch-package"],
            cwd=work,
            check=True,
            env=env,
        )
    subprocess.run(
        ["npm", "install", npm_spec],
        cwd=work,
        check=True,
        env=env,
    )

    if pkg_name == "react-native-webrtc":
        rel = Path("node_modules/react-native-webrtc/ios/RCTWebRTC/WebRTCModule+RTCMediaStream.m")
    elif pkg_name == "@fishjam-cloud/react-native-webrtc":
        rel = Path(
            "node_modules/@fishjam-cloud/react-native-webrtc/ios/RCTWebRTC/WebRTCModule+RTCMediaStream.m"
        )
    else:
        raise ValueError(pkg_name)

    patch_webrtc_media_stream_m(work / rel)
    subprocess.run(
        ["npx", "patch-package", pkg_name],
        cwd=work,
        check=True,
        env=env,
    )
    patches_dir = work / "patches"
    found = list(patches_dir.glob("*.patch"))
    if len(found) != 1:
        raise RuntimeError(f"Expected one patch in {patches_dir}, got {found}")
    return found[0]


def main() -> None:
    rnw_versions = [
        "106.0.7",
        "111.0.6",
        "118.0.7",
        "124.0.0",
        "124.0.4",
        "124.0.7",
    ]
    fishjam_versions = ["0.25.0", "0.25.2", "0.25.3", "0.25.4", "0.25.5", "0.25.6"]

    for ver in rnw_versions:
        with tempfile.TemporaryDirectory(prefix="simcam-rnw-") as td:
            work = Path(td)
            patch_file = run_patch_package(work, "react-native-webrtc", f"react-native-webrtc@{ver}")
            dest = PATCHES / "react-native-webrtc" / patch_file.name
            shutil.copy2(patch_file, dest)
            print(f"Wrote {dest.relative_to(ROOT)}")

    for ver in fishjam_versions:
        with tempfile.TemporaryDirectory(prefix="simcam-fj-") as td:
            work = Path(td)
            patch_file = run_patch_package(
                work,
                "@fishjam-cloud/react-native-webrtc",
                f"@fishjam-cloud/react-native-webrtc@{ver}",
            )
            dest = PATCHES / "fishjam-react-native-webrtc" / patch_file.name
            shutil.copy2(patch_file, dest)
            print(f"Wrote {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
