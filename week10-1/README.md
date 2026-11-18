# 問題1：投稿タイトル一覧（fetch × forEach）（20分）

このフォルダ（`week10-1`）で作業してください。

APIから投稿データを取得し、最初の5件のタイトルを一覧表示するコードを完成させます。

**完成したら同じフォルダ内の `goal.png` を開いて見比べてください。同じになっていれば OK です。**

作業前に、「どのAPIから取得するか・いつ取得するか（読み込み時か入力時か）・`console.log` で何の形（配列かオブジェクトか）を確認するか・失敗時に何を出すか」を表に整理してから進めてください。

#### 仕様

| 項目 | Tailwindクラス / 内容 |
|---|---|
| ページ背景 | `bg-slate-50`（`p-8`） |
| コンテナ | `mx-auto max-w-2xl` |
| 各投稿 | `<li>`：`rounded-xl border border-slate-200 bg-white px-4 py-3 shadow-sm` |
| ステータス | `id="status"`。失敗時は `text-red-500` |

#### 掲載する内容

- 取得元URL：`https://jsonplaceholder.typicode.com/posts`
- 最初の5件だけ表示する（`slice(0, 5)` を使う）／各投稿の `title` を `<li>` として `<ul id="postList">` に追加する

#### Step 1：`async` 関数の中で `await fetch(...)` → `response.ok` 確認 → `await response.json()` の順で取得し、`console.log` で配列の形を確認する

#### Step 2：`slice(0, 5)` で5件にし、`forEach` で `<li>` を作って `postList` に追加する。取得できたら `status` を空にする

#### Step 3：`try/catch` で失敗時に「取得に失敗しました」を表示する。`goal.png` とレイアウトを照合する
