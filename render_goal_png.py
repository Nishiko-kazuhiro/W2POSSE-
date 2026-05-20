#!/usr/bin/env python3
"""Render drill goal.html to goal.png using Chrome headless (macOS)."""
import subprocess
import sys
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT = Path(__file__).resolve().parent


def render_one(d: Path) -> None:
    html = d / "goal.html"
    png = d / "goal.png"
    if not html.is_file():
        print("skip (no goal.html):", html)
        return
    url = html.as_uri()
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            f"--screenshot={png}",
            "--window-size=800,900",
            "--no-sandbox",
            url,
        ],
        check=True,
        timeout=60,
    )
    print("wrote", png)


def render_images_html(html_path: Path, png_path: Path) -> None:
    if not html_path.is_file():
        print("skip:", html_path)
        return
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            f"--screenshot={png_path}",
            "--window-size=900,800",
            "--no-sandbox",
            html_path.as_uri(),
        ],
        check=True,
        timeout=60,
    )
    print("wrote", png_path)


def main() -> None:
    if not Path(CHROME).is_file():
        print("Chrome not found at", CHROME, file=sys.stderr)
        sys.exit(1)

    targets = sys.argv[1:] if len(sys.argv) > 1 else None

    if targets:
        for name in targets:
            render_one(ROOT / name)
    else:
        for d in sorted(ROOT.iterdir()):
            if d.is_dir() and d.name.startswith("week") and (d / "goal.html").is_file():
                render_one(d)

    images = ROOT.parent / "images"
    for html_name, png_name in [
        ("minidrill-week01-goal.html", "minidrill-week01-goal.png"),
        ("minidrill-week01-artist.html", "minidrill-week01-artist.png"),
        ("minidrill-week01-event.html", "minidrill-week01-event.png"),
        ("minidrill-week03-goal.html", "minidrill-week03-goal.png"),
        ("minidrill-week03-pricing-goal.html", "minidrill-week03-pricing-goal.png"),
    ]:
        render_images_html(images / html_name, images / png_name)


if __name__ == "__main__":
    main()
