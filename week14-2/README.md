# 問題2：バグ診断（key 忘れ）（15分）

**このフォルダに作業ファイルはありません。** 手を動かして確かめたい場合は、自分の Vite + React プロジェクトで再現してください。

次のコードは `map` で書籍リストを表示しようとしています。画面には3件のタイトルが出ますが、ブラウザのコンソール（DevTools の Console タブ）に警告が出ています。何が問題か説明し、修正してください。

```jsx
const books = [
  { id: 1, title: "JavaScript入門" },
  { id: 2, title: "Reactの教科書" },
  { id: 3, title: "CSS設計完全ガイド" },
];

function App() {
  return (
    <ul>
      {books.map((book) => (
        <li>{book.title}</li>
      ))}
    </ul>
  );
}

export default App;
```

解答は、カリキュラムの Week14 → ミニドリル → 問題2 にあります。
