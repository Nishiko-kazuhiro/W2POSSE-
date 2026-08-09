# drill-ph1（PH1 ミニドリル）

PH1 のミニドリル用リポジトリです。カリキュラムに `week02-2` と書いてあるときは、**このリポジトリの `week02-2/` フォルダ**で作業します。

## 初回

```bash
git clone git@github.com:posse-ap/drill-ph1.git
cd drill-ph1/week02-2   # その週・問題のフォルダ名（2桁: week02 など）
```

各フォルダの **README.md** に、その問題の仕様と手順が書いてあります。

## フォルダ名

- **使う:** `week06-1` のように週が2桁
- **使わない:** `week6-1` など1桁（旧形式）

## 作業の流れ

1. カリキュラムのミニドリルで「分解」の表を埋める
2. このリポジトリの `index.html` を編集する
3. 同じフォルダの **`goal.png`** と見比べて確認する

## Week13 以降のフォルダについて

Week13 で `pnpm create vite` を使い、自分の開発環境を持ちます。そこから先のミニドリルは、**自分で作った Vite プロジェクトの中で** 進めてください。

そのため `week13-1` 以降のフォルダには **README.md（と必要なら `goal.png`）しか入っていません**。編集する `index.html` は配っていません。ここで Vite 雛形を配ってしまうと、Week13 で学んだ「自分で環境を作る」を先回りして奪ってしまうためです。

| 週 | 作業する場所 |
|---|---|
| Week13 | `pnpm create vite my-counter-app --template vanilla` で作った自分のプロジェクト |
| Week14〜15 | `pnpm create vite ... --template react` で作った自分のプロジェクト |
| Week16 | コードを読むだけ（書き換え不要） |
