# 問題2：バグ診断（await 忘れ）（15分）

このフォルダ（`week10-2`）で作業してください。`index.html` を開いてください。

`index.html` を開くと、ユーザー名が**表示されず**、Consoleにエラーが出ています。正しく修正できると、名前とメールが正しく表示されます。何が問題か説明し、修正してください。

`index.html` には次のようなコードがあります。

```js
async function loadUser() {
  // ここにバグがあります（Console のエラーを読みながら直してください）
  const response = fetch("https://jsonplaceholder.typicode.com/users/1");
  const data = await response.json();

  document.getElementById("userName").textContent = data.name;
  document.getElementById("userEmail").textContent = data.email;
}

loadUser();
```

**ヒント:** `fetch()` はすぐに結果を返さず、Promiseを返します。その前に必要なキーワードが1つ抜けています。Consoleのエラー文を読んでみましょう。

<details>
<summary>解答の要点</summary>

`const response = fetch(...)` に `await` が付いていません。`await` なしの `fetch()` はPromiseオブジェクトを返すため、そのまま `.json()` を呼ぶとエラーになります（`response.json is not a function` のようなエラーが出ます）。`const response = await fetch(...)` のように `await` を付けると、レスポンスが返ってくるまで待ってから次の行へ進むので直ります。非同期処理では `await` が必要な箇所を意識的に確認しましょう。

</details>

修正後、名前とメールが正しく表示されることを確認してください。**`goal.png`** も参考にしてください。
