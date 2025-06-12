# Week02 ミニドリル 2問目 - Flexboxヘッダー練習

## 問題

Week02で学習したFlexbox（`display: flex`）を使って、ヘッダーのレイアウトを横並びに修正してください。

### 現在の状態

- ロゴとナビゲーションが縦に並んでいる
- ナビゲーションメニューの項目も縦に並んでいる

### 目標

以下のようなヘッダーレイアウトを作成してください：

1. **ロゴとナビゲーションを横並び**にする
2. **ロゴを左端、ナビゲーションを右端**に配置する
3. **ナビゲーションメニューの項目を横並び**にする
4. **ロゴとナビゲーションを垂直方向で中央揃え**にする

### 修正箇所

`css/style.css` の以下の箇所を修正してください：

1. `.header-container` クラス（29行目付近）
2. `.nav-list` クラス（47行目付近）

### 修正方法

#### ステップ1: ヘッダーコンテナをFlexboxにする

`.header-container` のコメントアウトされた部分を有効にしてください：

```css
.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

#### ステップ2: ナビゲーションリストをFlexboxにする

`.nav-list` のコメントアウトされた部分を有効にしてください：

```css
.nav-list {
  list-style: none;
  display: flex;
  gap: 30px;
}
```

#### ステップ3: ナビゲーションの上マージンを調整

`.nav` クラスの `margin-top` を `0` に変更してください：

```css
.nav {
  margin-top: 0;
}
```

### 終了条件

- ロゴとナビゲーションが横並びで表示されている
- ロゴが左端、ナビゲーションが右端に配置されている
- ナビゲーションメニューの項目（About, Service, Contact）が横並びで表示されている
- ロゴとナビゲーションが垂直方向で中央揃えされている

### 学習ポイント

この問題では以下のFlexboxプロパティを練習できます：

- **display: flex**: 要素を横並びにする基本プロパティ
- **justify-content: space-between**: 要素を両端に配置し、間隔を均等にする
- **align-items: center**: 要素を垂直方向で中央揃えにする
- **gap**: Flexアイテム間の間隔を指定する

これらはモダンなWebレイアウトで必須のテクニックです。

### 参考

完成形のCSSは `style.css` の最下部にコメントとして記載されています。