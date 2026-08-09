# 問題2：バグ診断（追加ボタンを押しても画面が変わらない）（15分）

**このフォルダに作業ファイルはありません。** 手を動かして確かめたい場合は、自分の Vite + React プロジェクトで再現してください。

次のコードは、タスクを追加しようとしています。追加ボタンを押しても、リストには何も増えません（入力欄の文字もそのまま残ります）。何が問題か説明し、修正してください。

```jsx
import { useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [input, setInput] = useState("");

  const addTask = () => {
    tasks.push({ id: Date.now(), text: input, done: false });
  };

  return (
    <div className="p-4">
      <input value={input} onChange={(event) => setInput(event.target.value)} />
      <button onClick={addTask}>追加</button>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>{task.text}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

解答は、カリキュラムの Week15 → ミニドリル → 問題2 にあります。
