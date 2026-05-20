# PH1 ミニドリル統一仕様（v4）

> **目的:** Version 2.0 の「分解 → 実装 → 確認 → 理由」が毎週同じ型で回るようにする。  
> **AI:** ミニドリル全体で禁止（POSSE課題のみ可）。

## 受講生の作業場所（確定）

- ミニドリルは **[`posse-ap/drill-ph1`](https://github.com/posse-ap/drill-ph1)** に **単一管理**
- 受講生は `git clone` し、**`drill-ph1/weekNN-N/`** で作業する
- **stub** 週は README のみ同梱 → カリキュラム仕様どおり同フォルダ内で `index.html` を作成
- **ready** 週は `index.html` / `goal.html` / `goal.png` あり
- 一覧: [STATUS.md](./STATUS.md) ／ 週ファイル: [minidrill-workspace.md](../v4/minidrill-workspace.md)
- 開発用コピー: `curriculum-refactor/new/PH1/drill-ph1/` → GitHub へ rsync / push

## 命名規則（確定）

```
drill-ph1/weekNN-N/
```

| ルール | 例 |
|--------|-----|
| 週番号は **2桁ゼロ埋め** | `week06-1` ✅ / `week6-1` ❌ |
| 問題番号は **1〜3** | `week07-2` |
| 各フォルダに最低限 | `index.html`（TODO付き骨格）・`goal.html`（完成例）・`goal.png`（比較用） |

教材側の表記も `week06-1` に揃える（`week6-1` は使わない）。

## 1週の共通構造（Markdown）

各 `v4/weekNN.md` のミニドリルは次の順で書く。

```markdown
## ミニドリル（AI禁止・○分）

### 着手前：○○を分解する（5分）
- 今週の分解の型（1〜2文）
- 分解の見本画像（あれば）
- **着手前表**（空表を置き、受講生が埋める）

---

### 問題1：○○（○分）
- clone した `drill-ph1/weekNN-1/` で作業（README で stub / ready を確認）
- 仕様表（Tailwindクラス / DOM / 入出力）
- Step 1 分解を見ながら着手順を決める
- Step 2 1単位ずつ実装して確認
- Step 3 `goal.png` と見比べる

### 問題2：バグ診断（○分）
- 壊れた `index.html` を直す、またはコード読解のみ
- 原因を **2点以上** 自分の言葉で書く → 修正
- `goal.html` と同じ結果になること

### 問題3：復習 or 別UI（○分）
- 過去週の技術を組み合わせる、または別パターンの実装
- `drill-ph1` の `weekNN-3/`（あれば）
```

### 着手前表の型（週タイプ別）

| 週タイプ | 表の列 |
|----------|--------|
| **UI（HTML/Tailwind）** | ブロック名 / 役割 / 使うタグ or クラス / 確認方法 |
| **レイアウト（Flex/Grid/レスポンシブ）** | 完成状態 / 親要素 / 方向 or 列数 / `md:` の切り替え / 確認方法 |
| **JavaScript** | 完成状態 / 入力 / 処理 / 出力 / 境界値 / 確認方法 |
| **DOM** | 取得する要素 / イベント / 変える表示 / 確認方法 |
| **データ（配列・Fetch）** | データ形 / ループ or await / DOM の差し込み先 / 確認方法 |

Week04以降で「Week03の着手前を参照」と書く場合は、**その週用の列1行サマリ**も併記し、他週ファイルを開かなくても始められるようにする（順次改善）。

## 問題の3パターン（意図）

| # | 種類 | 育てる力 |
|---|------|----------|
| 1 | **実装** | 指示力（分解どおりに作る）・理解力 |
| 2 | **バグ診断** | 理解力・評価力（何が壊れているか言語化） |
| 3 | **復習・統合** | 指示力・過去週の定着 |

Week01〜03 は問題2を「HTMLスニペットのバグ診断」（drill なし）でよい。Week04以降は可能なら `weekNN-2` を drill 実体にする。

## `drill-ph1` フォルダの中身

### 必須ファイル

| ファイル | 役割 |
|----------|------|
| `index.html` | 受講生が編集する。**HTMLコメントでゴール条件**を書く |
| `goal.html` | 完成例（見比べ・バグ診断の正解側） |
| `goal.png` | `goal.html` のスクショ（Chrome headless 推奨） |
| `images/` | 問題で使う素材（必要な週のみ） |

### `index.html` の書き方（Week06-1 を標準）

- Tailwind CDN を `<head>` に入れる
- 骨格だけ置き、中身は `<!-- TODO: ... -->` と `<script>` 内 TODO
- ゴール条件をファイル先頭コメントに列挙

バグ診断問題（問題2）では、**意図的にバグった `index.html`** を置き、`goal.html` が修正後の見た目になる。

## 実装状況（2026-05-21）

| Week | 教材で drill 参照 | `drill-ph1` 実体 | 備考 |
|------|-------------------|------------------|------|
| 01 | week01-1〜3 | ✅ ready | 教材ゴールPNGは `new/PH1/images/minidrill-week01-*.png` |
| 02 | week02-1〜2 | ✅ ready | 教材ゴールPNGは `minidrill-week02-goal.png` |
| 03 | week03-2 のみ | ✅ ready | 問題1・2は教材内。問題3は `week03-2`（`week02-2` ではない） |
| 04 | week04-1〜3 | ✅ ready | |
| 05 | week05-1〜3 | ✅ ready | |
| 06 | week06-1〜3 | ✅ | **テンプレ週** |
| 07 | week07-1〜3 | ✅ | |
| 08 | week08-1〜3 | ✅ | |
| 09〜10 | なし（教材内のみ） | ❌ | Week06型への移行候補 |
| 11 | AI週（別設計） | — | v3 `week08` から評価系ミニドリルを移植予定 |
| 12〜16 | 教材内のみ | ❌ | React 週は後続で drill 要否を判断 |

## 作業の優先順位

1. **Week01〜05** の `weekNN-N` フォルダを Week06-1 をコピー元に生成（仕様は各 `v4/weekNN.md` から）
2. **Week09〜10** を Week06 と同型（着手前表 + drill 3問）に教材を揃える
3. **Week04〜05** の「Week03参照のみ」を各週の着手前表に自足化
4. **Week11** に v3 アーカイブの AI 評価ミニドリルを追加（POSSE課題はAI可のまま）

## 配布

別リポジトリ `curriculum-modules/drill-ph1` へ rsync する場合は `drill-ph1/README.md` の手順に従う。
