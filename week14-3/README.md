# 問題3：Week08 の一覧描画を、React の map で書き直す（25分）

**このフォルダに作業ファイルはありません。** 自分の Vite + React プロジェクトの `App.jsx` に書いてください。

Week08 では、配列を `forEach` で回し、`document.createElement` で要素を作って `appendChild` で画面に足す、という書き方でリストを表示しました。次はその「素の JavaScript 版」です。

```html
<ul id="fruitList"></ul>
```

```js
const fruits = [
  { id: 1, name: "りんご", price: 120 },
  { id: 2, name: "みかん", price: 80 },
  { id: 3, name: "ぶどう", price: 300 },
];

const list = document.getElementById("fruitList");
fruits.forEach((fruit) => {
  const li = document.createElement("li");
  li.textContent = `${fruit.name} - ${fruit.price}円`;
  list.appendChild(li);
});
```

これと**同じデータ・同じ見た目**を、React の `map` で書き直してください。書き直せたら、**2つの方式のどこが違うかを、自分の言葉で1行だけ**書いてください。

**完成状態の確認方法:** ブラウザに「りんご - 120円」「みかん - 80円」「ぶどう - 300円」の3行が並べば OK です。コンソールに `key` の警告が出ていないことも確認してください。

ヒントと解答は、カリキュラムの Week14 → ミニドリル → 問題3 にあります。
