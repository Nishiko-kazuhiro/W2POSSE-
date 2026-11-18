# 問題3：投稿検索（fetch × filter・input の復習）（25分）

このフォルダ（`week10-3`）で作業してください。

APIから取得した投稿一覧を、入力欄のキーワードで絞り込むアプリを作ります。Week10のfetchと、Week08の配列・`filter`・`forEach`、Week09の入力値取得（`.value`）を組み合わせた復習問題です。

- ページ読み込み時にfetchで投稿を取得し、`allPosts`（10件）に貯めて一覧を描く
- 入力欄に文字を打つたびに、タイトルにその文字を含む投稿だけに絞り込んで描き直す

**完成したら `goal.png` を開いて見比べてください。同じになっていれば OK です。**

#### Step 1：`render(posts)` 関数を作る。`postList.innerHTML = ""` → `posts.forEach` で `<li>` を作って `appendChild`（Week08の復習）

#### Step 2：`async` 関数でfetch → `response.ok` 確認 → `json()` → `slice(0, 10)` を `allPosts` に代入 → `render(allPosts)`。`try/catch` で失敗時の表示も書く

#### Step 3：`keyword` の `input` イベントで `allPosts.filter(post => post.title.includes(keyword))` を `render()` に渡す。キーワードを消すと全件に戻ることを確認する
