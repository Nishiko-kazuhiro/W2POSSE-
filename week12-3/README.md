# 問題3：作品カードのホバー演出（group-hover の復習）（25分）

このフォルダ（`week12-3`）で作業してください。

普段はサムネイルだけ表示され、ホバーすると半透明のオーバーレイと「詳細を見る」が浮かび上がる作品カードを作ります。Week12のtransition・transformと、`group` / `group-hover` / `opacity` を組み合わせた復習問題です。

- 普段：オーバーレイは透明（`opacity-0`）で見えない
- ホバー時：オーバーレイが表示され（`group-hover:opacity-100`）、カードが少し持ち上がる

**完成したら `goal.png` を開いて見比べてください。普段の見た目（サムネイルだけ）が同じになっていれば OK です。ホバーの動きはマウスを乗せて確認します。**

#### Step 1：各カードの外側 `<div>` に `group` を足し、`transition-all duration-300 hover:-translate-y-1 hover:shadow-lg` でカードを浮かせる

#### Step 2：オーバーレイ（`bg-black/50` の `<div>`）に `opacity-0 group-hover:opacity-100 transition-opacity duration-300` を足し、普段は隠れて親へのホバーで表示されるようにする

#### Step 3：3枚ともマウスを乗せたときだけオーバーレイが出ること・普段はサムネイルだけ見えることを確認する。`goal.png` と普段の見た目を照合する
