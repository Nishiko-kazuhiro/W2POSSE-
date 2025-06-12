# Week04 ミニドリル 1問目 - Grid Layout基本練習

## 問題

以下の要件に従って、Grid Layoutを使用したレイアウトを作成してください。

### 要件

1. **基本的な2列レイアウト**
   - `.grid-container`クラスに`display: grid`を適用
   - `grid-template-columns`を使用して2列のレイアウトを作成
   - 各列の幅は`1fr 1fr`で等幅に設定

2. **カードレイアウトの実装**
   - 6つのカード要素（`.card`）を配置
   - カードは2列×3行で表示される
   - 各カードには画像、タイトル、説明文を含む

3. **fr単位の理解**
   - `1fr 2fr`のパターンも試してみる（コメントアウトで用意済み）
   - `repeat()`関数の使用も学習する

### 学習目標

- `display: grid`の基本的な使い方を理解する
- `grid-template-columns`プロパティの使い方を覚える
- `fr`単位の概念を理解し、実際に使えるようになる
- Grid LayoutとFlexboxの違いを体感する

### 完成イメージ

```
[カード1] [カード2]
[カード3] [カード4]
[カード5] [カード6]
```

各カードは等幅で、きれいに格子状に配置される。

### 参考

- [MDN - CSS Grid Layout](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_Grid_Layout)
- [MDN - grid-template-columns](https://developer.mozilla.org/ja/docs/Web/CSS/grid-template-columns)

### 終了条件

- ブラウザで表示した際に、6つのカードが2列×3行で整然と配置されている
- 各カードの幅が等しく、見た目が整っている
- CSSでGrid Layoutが正しく実装されている
