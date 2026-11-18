# 問題2：バグ診断（import のファイル名）（15分）

**このフォルダに作業ファイルはありません。** 手を動かして確かめたい場合は、自分の Vite プロジェクト（`my-counter-app`）で再現してください。

次のコードは、ある Vite プロジェクトの `src/main.js` です。`pnpm run dev` で起動すると、画面が真っ赤なエラー表示になり、スタイルも当たりません。何が問題か説明し、修正してください。

```js
// src/main.js
import './styles.css';

document.querySelector('#app').innerHTML = '<h1>こんにちは</h1>';
```

このとき、ブラウザの Console とターミナルには、次のエラーが出ています。

```
[vite] Internal server error: Failed to resolve import "./styles.css" from "src/main.js". Does the file exist?
  Plugin: vite:import-analysis
  File: /.../src/main.js:1:8
  1  |  import './styles.css';
     |          ^
```

解答は、カリキュラムの Week13 → ミニドリル → 問題2 にあります。
