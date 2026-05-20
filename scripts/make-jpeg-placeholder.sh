#!/usr/bin/env bash
# 単色のプレースホルダ画像を「本物の JPEG」として出力する（placehold.co は使わない）
# 用法: make-jpeg-placeholder.sh <幅> <高さ> <出力.jpg> [ラベル]
set -euo pipefail
W="${1:?width}"
H="${2:?height}"
OUT="${3:?output path}"
LABEL="${4:-}"
DIR="$(dirname "$OUT")"
mkdir -p "$DIR"
TMP_HTML="$(mktemp /tmp/drill-img-XXXXXX.html)"
TMP_PNG="${OUT%.jpg}.png"
trap 'rm -f "$TMP_HTML" "$TMP_PNG"' EXIT

cat > "$TMP_HTML" <<EOF
<!DOCTYPE html><html><body style="margin:0;background:#334155;display:flex;align-items:center;justify-content:center;width:${W}px;height:${H}px;font:600 24px system-ui,sans-serif;color:#e2e8f0;">${LABEL}</body></html>
EOF

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --screenshot="$TMP_PNG" \
  --window-size="${W},${H}" --virtual-time-budget=3000 --no-sandbox \
  "file://$TMP_HTML" 2>/dev/null &
pid=$!
for _ in 1 2 3 4 5; do kill -0 $pid 2>/dev/null || break; sleep 1; done
kill -0 $pid 2>/dev/null && kill $pid 2>/dev/null; wait $pid 2>/dev/null || true

sips -s format jpeg "$TMP_PNG" --out "$OUT" >/dev/null
file "$OUT"
