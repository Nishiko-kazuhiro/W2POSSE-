#!/usr/bin/env python3
"""Render drill goal.html to goal.png using Chrome headless (macOS)."""
import subprocess
import sys
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT = Path(__file__).resolve().parent


def main() -> None:
    if not Path(CHROME).is_file():
        print("Chrome not found at", CHROME, file=sys.stderr)
        sys.exit(1)
    for name in [
        "week06-1",
        "week06-2",
        "week06-3",
        "week07-1",
        "week07-2",
        "week07-3",
        "week08-1",
        "week08-2",
        "week08-3",
    ]:
        d = ROOT / name
        html = d / "goal.html"
        png = d / "goal.png"
        if not html.is_file():
            print("skip (no goal.html):", html)
            continue
        url = html.as_uri()
        subprocess.run(
            [
                CHROME,
                "--headless=new",
                f"--screenshot={png}",
                "--window-size=800,600",
                "--no-sandbox",
                url,
            ],
            check=True,
            timeout=60,
        )
        print("wrote", png)


if __name__ == "__main__":
    main()
