# 問題1：お問い合わせフォーム（20分）

このフォルダ（`week09-1`）で作業してください。

お名前（テキスト）とお問い合わせ内容（テキストエリア）を入力して送信ボタンを押すと、未入力ならエラー、両方入っていれば受付メッセージを表示するフォームを完成させます。

**完成したら同じフォルダ内の `goal.png` を開いて見比べてください。同じになっていれば OK です。**

作業前に、「取得する要素（`.value` か `.checked` か）・どのイベントか・どんな条件で弾くか」を表に書いてから進めてください。

#### 仕様

| 項目 | Tailwindクラス / 内容 |
|---|---|
| ページ背景 | `bg-slate-50`（`flex` で中央寄せ） |
| カード | `max-w-md bg-white rounded-xl border border-slate-200 shadow-sm p-8` |
| 入力欄 | `w-full border border-slate-300 rounded px-3 py-2`（`focus:ring-2`） |
| メッセージ | `id="result"`。失敗時は `text-red-500`、成功時は `text-green-600` |
| ボタン | `w-full bg-blue-600 text-white font-bold py-2 rounded` |

#### 掲載する内容

- お名前（`type="text"`）／お問い合わせ内容（`<textarea rows="4">`）／送信ボタン

#### Step 1：`form` に `submit` イベントを登録し、コールバックの最初で `event.preventDefault()` を呼ぶ

#### Step 2：`name` が空なら「お名前を入力してください」、`message` が空なら「お問い合わせ内容を入力してください」、両方OKなら「〇〇さんのお問い合わせを受け付けました」を表示する。失敗は赤・成功は緑にクラスを切り替える

#### Step 3：空のまま送信／正常入力の両方を試し、`goal.png` とレイアウトを照合する
