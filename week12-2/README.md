# 問題2：バグ診断（Splideのクラス名）（15分）

このフォルダ（`week12-2`）で作業してください。`index.html` を開いてください。

`index.html` を開くと、スライダーが**表示されず**、矢印ボタンも出ません（スライドが縦に並んだままです）。正しく修正できると、スライダーとして動きます。何が問題か説明し、修正してください。

`index.html` には次のようなHTMLがあります。

```html
<section class="splide" aria-label="作品スライダー">
  <div class="splide__track">
    <ul class="splide-list">
      <li class="splide__slide"> ...作品1... </li>
      <li class="splide__slide"> ...作品2... </li>
      <li class="splide__slide"> ...作品3... </li>
    </ul>
  </div>
</section>
```

**ヒント:** Splideは特定のクラス名を見つけることで動きます。各要素のクラス名を、インプット「5. Splide.js の導入」のHTML構造と1つずつ見比べてみましょう。区切り文字に注目してください。

<details>
<summary>解答の要点</summary>

`<ul>` のクラス名が `splide-list`（ハイフン）になっており、正しくは `splide__list`（アンダースコア2つ）です。Splideはクラス名 `splide__list` を内部で探しているため、ハイフンだとリストを認識できず、スライダーとして機能しません。`splide__track` や `splide__slide` も同じく `__`（アンダースコア2つ）が正しい書き方です。

</details>

修正後、スライダーとして動き、矢印ボタンが出ることを確認してください。**`goal.png`** も参考にしてください。
