# 問題2：バグ診断（preventDefault）（15分）

このフォルダ（`week09-2`）で作業してください。`index.html` を開いてください。

「ログイン」ボタンを押すと、メッセージが**一瞬表示されてすぐ消えてしまいます**。正しく修正できると、ボタンを押してもメッセージが消えずに表示され続けます。何が問題か説明し、修正してください。

`index.html` には次のようなコードがあります。

```js
form.addEventListener("submit", () => {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username === "" || password === "") {
    result.textContent = "すべて入力してください";
    return;
  }

  result.textContent = "ログイン成功！";
});
```

**ヒント:** フォームの送信ボタンを押したときの、ブラウザのデフォルト動作を思い出してみましょう。

<details>
<summary>解答の要点</summary>

`event.preventDefault()` が呼ばれていないため、ボタンを押すとブラウザがフォームを送信してページを**リロード**しています。メッセージは表示された直後にリロードで消えてしまいます。`addEventListener("submit", (event) => { ... })` のように引数で `event` を受け取り、最初の行で `event.preventDefault()` を呼べば直ります。

</details>

修正後、ボタンを押してもメッセージが消えないことを確認してください。**`goal.png`** も参考にしてください。
