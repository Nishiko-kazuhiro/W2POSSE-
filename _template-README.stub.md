# {{FOLDER}}

| 項目 | 内容 |
|------|------|
| ステータス | **stub**（README のみ。スターター未配布） |
| カリキュラム | Week{{WEEK}} ミニドリル 問題{{PROBLEM}} |

## 受講生

ミニドリルは **[`posse-ap/drill-ph1`](https://github.com/posse-ap/drill-ph1)** で一元管理しています。課題用リポジトリに自分で `minidrill/` を作る必要はありません。

```bash
git clone git@github.com:posse-ap/drill-ph1.git
cd drill-ph1/{{FOLDER}}
```

このフォルダに `index.html` がまだ無い場合は、カリキュラムの仕様表どおり **このディレクトリ内** で新規作成してください。

- 見本画像はカリキュラム週ファイル内のゴールUIを参照
- 旧1桁フォルダ（`week{{WEEK_SHORT}}-{{PROBLEM}}` など）は **v4 では使いません**

## スタッフ

- 仕様元: `new/PH1/v4/week{{WEEK_PADDED}}.md`
- 実装後: `index.html` / `goal.html` / `goal.png` / `images/` をこのフォルダに追加し、ステータスを README で **ready** に更新
