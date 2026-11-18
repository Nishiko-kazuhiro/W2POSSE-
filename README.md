# W2POSSE-<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CAFÉ LUMEN - Menu</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-stone-100 text-stone-800 font-sans min-h-screen">

  <!-- ヘッダー -->
  <header class="bg-stone-900 text-stone-100 py-10 shadow-md">
    <div class="max-w-5xl mx-auto px-4 text-center">
      <h1 class="text-3xl md:text-4xl font-serif tracking-wider font-bold">CAFÉ LUMEN</h1>
    </div>
  </header>

  <main class="max-w-5xl mx-auto px-4 py-12">
    
    <!-- ドリンク セクション -->
    <section class="mb-14">
      <div class="flex items-center gap-3 mb-6 border-b-2 border-amber-800 pb-2">
        <span class="text-2xl">☕</span>
        <h2 class="text-2xl font-bold text-stone-900">Drink Menu</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- ドリンク 1 -->
        <div class="bg-white rounded-lg shadow-md p-6 border border-stone-200 hover:-translate-y-1 hover:bg-border-400 flex flex-col justify-between">
          <div>
            <div class="flex justify-between items-start mb-2">
              <h3 class="text-xl font-bold text-stone-800">ハンドドリップブレンド</h3>
            </div>
            <p class="text-sm text-stone-600 leading-relaxed">
              深煎り豆を中心にブレンド。深みのあるコクとすっきりとした後味が特徴の定番ブレンドです。
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-100 flex justify-between items-center">
            <span class="text-lg font-bold text-amber-800">¥550</span>
          </div>
        </div>

        <!-- ドリンク 2 -->
        <div class="bg-white rounded-lg shadow-md p-6 border border-stone-200 hover:-translate-y-1 hover:bg-border-400 flex flex-col justify-between">
          <div>
            <h3 class="text-xl font-bold text-stone-800 mb-2">カフェラテ</h3>
            <p class="text-sm text-stone-600 leading-relaxed">
              濃厚なエスプレッソとまろやかな北海道産スチームミルクの豊かなバランス。
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-100 flex justify-between items-center">
            <span class="text-lg font-bold text-amber-800">¥600</span>
          </div>
        </div>
      </div>
      </section>

            <!-- スイーツ セクション -->
    <section class="mb-14">
      <div class="flex items-center gap-3 mb-6 border-b-2 border-amber-800 pb-2">
        <span class="text-2xl">🍰</span>
        <h2 class="text-2xl font-bold text-stone-900">Sweets & Dessert</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- スイーツ 1 -->
        <div class="bg-white rounded-lg shadow-md p-6 border border-stone-200 hover:-translate-y-1 hover:bg-border-400 flex flex-col justify-between">
          <div>
            <div class="flex justify-between items-start mb-2">
              <h3 class="text-xl font-bold text-stone-800">濃厚ベイクドチーズケーキ</h3>
            </div>
            <p class="text-sm text-stone-600 leading-relaxed">
              2種類のクリームチーズを贅沢に使用。しっとりとなめらかな口当たりでコーヒーとの相性抜群です。
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-100 flex justify-between items-center">
            <span class="text-lg font-bold text-amber-800">¥680</span>
          </div>
        </div>

        <!-- スイーツ 2 -->
        <div class="bg-white rounded-lg shadow-md p-6 border border-stone-200 hover:-translate-y-1 hover:bg-border-400 flex flex-col justify-between">
          <div>
            <h3 class="text-xl font-bold text-stone-800 mb-2">自家製珈琲ゼリーパフェ</h3>
            <p class="text-sm text-stone-600 leading-relaxed">
              当店抽出のエスプレッソで作ったほろ苦いゼリーに、バニラアイスとほのかなキャラメルソースをプラス。
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-100 flex justify-between items-center">
            <span class="text-lg font-bold text-amber-800">¥620</span>
          </div>
        </div>
      </div>
    </section>

      </main>

  <!-- フッター -->
  <footer class="bg-stone-800 text-stone-400 py-6 text-center text-xs">
    <p>© 2026 CAFÉ LUMEN. All Rights Reserved.</p>
  </footer>

</body>
</html>