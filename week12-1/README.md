# 問題1：ホバーアニメーション（transition × transform）（20分）

このフォルダ（`week12-1`）で作業してください。

3枚のスキルカードに、ホバーすると少し浮き上がり・影が強くなるアニメーションを追加します。

**完成したら同じフォルダ内の `goal.png` を開いて見比べてください。カードの見た目（普段の状態）が同じになっていれば OK です。ホバーの動きはマウスを乗せて確認します。**

作業前に、「普段とホバー時で何がどう変わるか・どのクラス（`transition-all` / `duration-xxx` / `hover:...`）を使うか」を表に整理してから進めてください。

#### 仕様

| 項目 | Tailwindクラス / 内容 |
|---|---|
| ページ背景 | `bg-slate-50`（`p-8`） |
| カード | `rounded-xl border border-slate-200 bg-white p-6 shadow-sm` |
| アニメーション | `transition-all duration-300` |
| ホバー（浮く） | `hover:-translate-y-1` |
| ホバー（影） | `hover:shadow-lg` |

#### 掲載する内容

- 3枚のカード（HTML / Tailwind CSS / JavaScript）。すべて同じホバー演出を付ける

#### Step 1：各カードの `class` に `transition-all duration-300` を足して、アニメーションを有効にする

#### Step 2：`hover:-translate-y-1`（浮き上がり）と `hover:shadow-lg`（影を強く）を足す

#### Step 3：ブラウザでマウスを乗せ、3枚とも滑らかに浮き上がることを確認する。`goal.png` と普段の見た目を照合する
