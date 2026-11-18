# 問題3：タスク1件を `TaskItem` コンポーネントに切り出す（25分）

**このフォルダに作業ファイルはありません。** 自分の Vite + React プロジェクトの中で作業してください。

先週（Week14）は、部品（コンポーネント）に props を渡して見た目を作りました。今週はそこに state を組み合わせます。完成サンプルの「タスク1件分の `<li>`」を、`TaskItem` という別コンポーネントに切り出してください。

state（`tasks`）は `App` に置いたまま、`TaskItem` には「表示するタスク」と「押されたときに呼ぶ関数」を props で渡すのがポイントです。

**要件:**

- `src/components/TaskItem.jsx` に `TaskItem` を作り、`export default` する
- `TaskItem` は `task`（タスク1件）・`onToggle`・`onDelete` の3つの props を受け取る
- タスクの文字をクリックしたら `onToggle` を、削除ボタンを押したら `onDelete` を、それぞれ `task.id` を渡して呼ぶ
- `App` 側は `map` の中で `<TaskItem ... />` を使い、`onToggle={toggleTask}` `onDelete={deleteTask}` を渡す

**完成状態の確認方法:** 見た目と動きは、切り出す前とまったく同じ（追加・完了切り替え・削除が動く）なら OK です。コンポーネントに分けても機能が変わらないことを確認してください。

ヒントと解答は、カリキュラムの Week15 → ミニドリル → 問題3 にあります。
