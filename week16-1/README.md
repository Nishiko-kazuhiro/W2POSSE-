# AIが生成したコードのレビュー問題（30分）

**このフォルダに作業ファイルはありません。** コードは読むだけで、書き換えて動かす必要はありません。

今週は、AIが生成したコードを**自分の目で**レビューします。AIには頼らず、自分の手と頭だけで答えてください。ここは、AIを使わずに「AIのおかしな出力を見抜けるか」を確認する場です。

以下は、「Reactでタスク管理アプリを作って」と頼んだときに返ってきそうな、一見ちゃんと動きそうなコードです。実際、これらは AI が生成するコードによく混じる書き方ばかりです。問題点・改善すべき箇所を見つけて、理由とともに説明してください（複数あります。見つけられるだけ挙げてください）。

```jsx
import { useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [input, setInput] = useState("");

  const addTask = () => {
    tasks.push({ text: input, done: false });
    setTasks(tasks);
    setInput("");
  };

  const deleteTask = (index) => {
    tasks.splice(index, 1);
    setTasks(tasks);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1 style={{ color: "red" }}>タスク管理</h1>
      <input
        style={{ border: "1px solid black" }}
        onChange={(e) => setInput(e.target.value)}
      />
      <button style={{ color: "white", background: "blue" }} onClick={addTask}>
        追加
      </button>
      <ul>
        {tasks.map((task, index) => (
          <li>
            {task.text}
            <button onClick={() => deleteTask(index)}>削除</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

解答例は、カリキュラムの Week16 → ミニドリル にあります。
