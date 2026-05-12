# PH1 ミニドリル（Week06〜08 追加分）

教材リポジトリ（`curriculum-refactor`）と同じ内容を、別リポジトリ `drill-ph1` で配布する場合は、このフォルダを **`curriculum-modules/drill-ph1/` に rsync する**のが簡単です。

```bash
rsync -a /Users/jun/projects/posse/curriculum-refactor/new/PH1/drill-ph1/ \
  /Users/jun/projects/posse/curriculum-modules/drill-ph1/
```

手元のパスに読み替えてください。

## goal.png について

- 各 `week**-* /goal.png` は、**実機の Chrome で `goal.html` を headless キャプチャ**すると教材画像と一致しやすいです。
- 自動生成スクリプト: `render_goal_png.py`（macOS + Google Chrome 想定）。
- プレースホルダの単色 PNG だけを置いた場合は、ローカルで上記を実行して差し替えてください。

## フォルダ一覧（Week06〜08）

| フォルダ | 内容 |
|---|---|
| `week06-1` | 割り勘（切り上げ） |
| `week06-2` | バグ診断（文字列連結） |
| `week06-3` | 復習（Flex + 小計計算） |
| `week07-1` | 在庫付きカウンター |
| `week07-2` | バグ診断（querySelector） |
| `week07-3` | 復習ダッシュボード |
| `week08-1` | 備品テーブル + forEach |
| `week08-2` | バグ診断（map の return） |
| `week08-3` | 名前ソート + カード再描画 |
