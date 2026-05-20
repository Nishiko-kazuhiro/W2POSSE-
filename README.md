# drill-ph1（PH1 ミニドリル単一リポジトリ）

PH1 のミニドリルは **このリポジトリだけ** を正とします。カリキュラムに `week02-2` と書いてあるときは、**このリポジトリ内の `week02-2/` フォルダ** を指します。

| 向け | ドキュメント |
|------|----------------|
| 受講生 | 各 `weekNN-N/README.md` ／ [ミニドリルの作業場所](../v4/minidrill-workspace.md) |
| スタッフ | [MINIDRILL-SPEC.md](./MINIDRILL-SPEC.md) ／ [STATUS.md](./STATUS.md) |

## 受講生：初回セットアップ

```bash
git clone git@github.com:posse-ap/drill-ph1.git
cd drill-ph1
ls week02-2   # フォルダと README があることを確認
cd week02-2
```

- **`stub`:** README のみ。カリキュラムの仕様表どおり、このフォルダ内で `index.html` を新規作成する
- **`ready`:** `index.html`（骨組み）と `goal.html` / `goal.png` あり。TODO を埋めて `goal` と見比べる

課題用リポジトリ（`my-profile` 等）にまとめたい場合は、作業後に `week02-2` フォルダごとコピーして PR してもよい。

## フォルダ名（v4 確定）

```
weekNN-N/
```

- 週は **2桁**（`week02`）。`week2-2` など **1桁は旧形式で使わない**

## 開発・配布（スタッフ）

このディレクトリは `curriculum-refactor` 内の同期元です。更新後に GitHub へ反映します。

```bash
rsync -a new/PH1/drill-ph1/ /path/to/curriculum-modules/drill-ph1/
# または posse-ap/drill-ph1 リポジトリへ push
```

`goal.png` 生成: `python3 render_goal_png.py week06-1`

### ミニドリル用の写真素材（`images/*.jpg`）

- **placehold.co は使わない**（返ってくるのは SVG で、拡張子が `.jpg` でも中身が JPEG ではない）
- 単色プレースホルダが必要なときは `scripts/make-jpeg-placeholder.sh`（Chrome スクショ → macOS `sips` で **本物の JPEG** に変換）
- イラストは `team.svg` のように **SVG を同梱**する

## 旧フォルダについて

リポジトリに `week2-1` など **1桁** のフォルダが残っている場合、v4 カリキュラムとは無関係です。削除または [LEGACY.md](./LEGACY.md) を参照。
