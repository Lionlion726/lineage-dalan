$dir = 'C:\Users\zoo29\Desktop\大藍蕉天堂網站'

$nav = '<nav class="topnav"><div class="topnav-logo">⚔ 大藍蕉天堂</div><div class="topnav-sep"></div><div class="topnav-links" id="navLinks"><a class="topnav-link" href="index.html">首頁</a><div class="topnav-dropdown"><a class="topnav-link">活動公告 ▾</a><div class="dropdown-menu"><a href="events.html">開局紅變+紅娃</a><a href="event-line.html">預約LINE禮包</a><a href="event-bonfire.html">烽火慶典禮包</a></div></div><div class="topnav-dropdown"><a class="topnav-link">遊戲特色 ▾</a><div class="dropdown-menu"><a href="features.html">特色總覽</a><a href="feature-01.html">法師召喚物系統</a><a href="feature-02.html">職業特色技能</a><a href="feature-03.html">職業之力介紹</a><a href="feature-04.html">戰馬雕像能力</a><a href="feature-05.html">寵物系統介紹</a><a href="feature-06.html">主線任務勳章</a><a href="feature-07.html">威望系統</a><a href="feature-08.html">高寵介紹</a><a href="feature-09.html">在線禮包</a><a href="feature-10.html">赫卡特介紹</a><a href="feature-11.html">傲慢的掛飾</a><a href="feature-12.html">換金道具</a></div></div><div class="topnav-dropdown"><a class="topnav-link">道具裝備 ▾</a><div class="dropdown-menu"><a href="items.html">道具介紹</a><a href="weapons.html">武器介紹</a><a href="armor.html">防具介紹</a></div></div><div class="topnav-dropdown"><a class="topnav-link">遊戲資料 ▾</a><div class="dropdown-menu"><a href="transform.html">變身介紹</a><a href="dolls.html">娃娃介紹</a><a href="boss.html">BOSS介紹</a><a href="maps.html">地圖介紹</a></div></div><a class="topnav-link" href="download.html">檔案下載</a><a class="topnav-link" href="sponsor.html">贊助系統</a><a class="topnav-link" href="rates.html">版本倍率</a><div class="topnav-dropdown"><a class="topnav-link">規章說明 ▾</a><div class="dropdown-menu"><a href="disclaimer.html">免責聲明</a><a href="rules.html">遊戲規章</a><a href="sponsor-info.html">贊助須知</a></div></div></div><div class="topnav-right"><a class="topnav-line-btn" href="#" onclick="document.getElementById(''modal-line'').classList.add(''open'');return false;">LINE 客服</a></div><div class="hamburger" onclick="document.getElementById(''navLinks'').classList.toggle(''open'')"><span></span><span></span><span></span></div></nav>'

$modals = '<div class="float-sidebar"><button class="float-btn sponsor" data-modal="modal-sponsor">💰 贊助方案</button><button class="float-btn" data-modal="modal-gift">🎁 申請禮包</button><button class="float-btn" data-modal="modal-line">💬 LINE</button></div><div class="float-modal" id="modal-sponsor"><div class="float-modal-box"><span class="modal-close">✕</span><div class="modal-title">💰 贊助方案</div><div class="modal-body"><p>▸ 贊助詳情請加入 LINE 社群詢問</p></div><a class="modal-btn" href="sponsor.html">查看贊助頁面</a></div></div><div class="float-modal" id="modal-gift"><div class="float-modal-box"><span class="modal-close">✕</span><div class="modal-title">🎁 新手禮包</div><div class="modal-body"><p>加入 LINE 官方社群後私訊管理員即可領取。</p></div><a class="modal-btn" href="#">前往 LINE 領取</a></div></div><div class="float-modal" id="modal-line"><div class="float-modal-box"><span class="modal-close">✕</span><div class="modal-title">💬 LINE 聯絡方式</div><div class="modal-body" style="text-align:center"><div style="width:150px;height:150px;background:var(--bg4);border:1px solid var(--border);margin:0 auto 12px;display:flex;align-items:center;justify-content:center;color:var(--text-muted);font-size:11px;">LINE QR Code</div></div><a class="modal-btn" href="#">加入 LINE 官方社群</a></div></div>'

$footer = '<footer><div class="footer-inner"><div><div class="footer-col-title">大藍蕉天堂</div><ul class="footer-links"><li><a href="index.html">首頁</a></li><li><a href="download.html">檔案下載</a></li><li><a href="sponsor.html">贊助系統</a></li></ul></div><div><div class="footer-col-title">遊戲資訊</div><ul class="footer-links"><li><a href="features.html">遊戲特色</a></li><li><a href="transform.html">變身介紹</a></li><li><a href="dolls.html">娃娃介紹</a></li><li><a href="boss.html">BOSS介紹</a></li><li><a href="maps.html">地圖介紹</a></li></ul></div><div><div class="footer-col-title">規章說明</div><ul class="footer-links"><li><a href="disclaimer.html">免責聲明</a></li><li><a href="rules.html">遊戲規章</a></li><li><a href="sponsor-info.html">贊助須知</a></li></ul></div><div><div class="footer-col-title">聯絡我們</div><ul class="footer-links"><li><a href="#" onclick="document.getElementById(''modal-line'').classList.add(''open'');return false;">LINE 客服</a></li></ul></div></div><div class="footer-copy">© 2026 大藍蕉天堂</div></footer><script src="main.js"></script>'

$pages = @(
  @{ file='disclaimer.html'; title='免責聲明'; badge='DISCLAIMER'; h1='免責聲明'; sub='請詳細閱讀以下內容'; body='<div class="feature-detail-content" style="max-width:800px;margin:0 auto"><h3>免責聲明</h3><p>本站為私人架設之天堂遊戲伺服器，與 NC Soft 官方及任何官方授權單位無任何關聯。</p><p>本站所使用之遊戲圖片、名稱、系統等資源，版權均屬 NC Soft 所有，本站僅供玩家懷舊娛樂使用。</p><ul><li>本伺服器為免費私人架設，管理團隊不對任何遊戲損失負責</li><li>贊助行為屬自願性質，不保證永久營運，亦不提供退款</li><li>伺服器可能因維護、技術問題或不可抗力因素暫停或關閉</li><li>玩家資料有遺失風險，請勿投入超出個人承受範圍的金錢</li><li>本站保留隨時修改、暫停或終止服務之權利，恕不另行通知</li></ul></div>' },
  @{ file='rules.html'; title='遊戲規章'; badge='GAME RULES'; h1='遊戲規章'; sub='違規將依情節輕重處置'; body='<div class="feature-detail-content" style="max-width:800px;margin:0 auto"><h3>基本行為規範</h3><ul><li>禁止使用第三方外掛程式（本服提供官方內掛）</li><li>禁止惡意騷擾、辱罵其他玩家</li><li>禁止散布不實謠言、惡意中傷本伺服器</li><li>禁止利用遊戲 BUG 獲取不當利益</li><li>禁止帳號買賣或轉讓</li></ul><h3>處罰規定</h3><ul><li>輕度違規：口頭警告</li><li>中度違規：停權 3～7 天</li><li>重度違規：永久封號，贊助款項不予退還</li></ul><h3>申訴方式</h3><ul><li>申訴請加入 LINE 官方社群聯繫管理員</li><li>管理員將於 24 小時內回覆</li><li>最終解釋權歸管理團隊所有</li></ul></div>' },
  @{ file='sponsor-info.html'; title='贊助須知'; badge='SPONSOR INFO'; h1='贊助須知'; sub='贊助前請詳細閱讀'; body='<div class="feature-detail-content" style="max-width:800px;margin:0 auto"><h3>贊助說明</h3><ul><li>贊助屬自願性質，贊助金額用於維持伺服器日常開銷</li><li>贊助後請勿要求退款，一經確認概不退還</li><li>贊助回饋為遊戲內道具，不含任何現金價值</li><li>贊助回饋將於確認付款後 24 小時內發送至角色</li></ul><h3>注意事項</h3><ul><li>請確認角色名稱正確後再進行贊助</li><li>名稱填寫錯誤導致發送失敗，管理員不負責補發</li><li>管理員不會主動要求玩家提供帳號密碼，請小心詐騙</li></ul></div>' },
  @{ file='events.html'; title='活動公告'; badge='EVENT'; h1='開局活動公告'; sub='開局限時好禮，先搶先贏'; body='<div style="max-width:900px;margin:0 auto"><div class="section-header"><div class="section-eyebrow">LIMITED EVENT</div><h2 class="section-title">開局紅變＋紅娃活動</h2><div class="section-line"></div></div><div class="feature-detail-content"><h3>活動說明</h3><p>開服慶典限時活動！加入大藍蕉天堂即可獲得開局專屬大禮包，包含稀有紅色變身及紅色娃娃！</p><ul><li>活動期間：開服起至另行公告</li><li>活動對象：所有新加入玩家</li><li>領取方式：加入 LINE 官方社群私訊管理員</li></ul><h3>活動獎勵</h3><ul><li>🔴 開局紅色變身 × 1</li><li>🎀 開局紅色娃娃 × 1</li><li>新手加速符 × 7（7日有效）</li><li>生命藥水（大）× 200</li></ul></div></div>' },
  @{ file='event-line.html'; title='預約LINE禮包'; badge='LINE EVENT'; h1='預約LINE禮包'; sub='加入社群即可領取'; body='<div class="feature-detail-content" style="max-width:800px;margin:0 auto"><h3>預約禮包說明</h3><p>加入大藍蕉天堂官方 LINE 社群，完成預約即可領取限定禮包！</p><h3>禮包內容</h3><ul><li>預約紀念道具 × 1</li><li>生命藥水（大）× 100</li><li>魔力藥水（大）× 100</li><li>新手加速符 × 3</li></ul><h3>領取方式</h3><ul><li>加入官方 LINE 社群</li><li>私訊管理員提供角色名稱</li><li>確認後 24 小時內發送</li></ul></div>' },
  @{ file='event-bonfire.html'; title='烽火慶典禮包'; badge='BONFIRE EVENT'; h1='烽火慶典禮包'; sub='限時慶典活動'; body='<div class="feature-detail-content" style="max-width:800px;margin:0 auto"><h3>烽火慶典說明</h3><p>大藍蕉天堂烽火慶典正式開跑！參與活動可獲得豐厚獎勵！</p><h3>活動獎勵</h3><ul><li>烽火紀念道具 × 1</li><li>強化石 × 10</li><li>祝福捲軸 × 5</li><li>生命藥水（大）× 200</li><li>烽火慶典稱號 × 1</li></ul><h3>參與方式</h3><ul><li>活動期間登入遊戲即可參與</li><li>詳細規則請加入 LINE 社群查詢</li></ul></div>' },
  @{ file='transform.html'; title='變身介紹'; badge='TRANSFORMATION'; h1='變身介紹'; sub='強化你的戰鬥能力'; body='<div style="max-width:1100px;margin:0 auto"><div class="section-image"><div class="img-placeholder">[ 變身介紹主圖 ]</div></div><div class="feature-detail-content" style="margin-top:32px"><h3>變身系統說明</h3><p>變身道具可強化角色能力，不同變身提供不同屬性加成。稀有度越高，加成效果越強。</p><ul><li>變身分為普通、稀有、史詩、傳說四個等級</li><li>紅色變身為最高等級，提供最強屬性加成</li><li>部分變身為活動限定，錯過即無法取得</li></ul></div><div class="section-image" style="margin-top:32px"><div class="img-placeholder">[ 變身列表圖 ]</div></div></div>' },
  @{ file='dolls.html'; title='娃娃介紹'; badge='DOLL SYSTEM'; h1='娃娃介紹'; sub='可愛的戰鬥夥伴'; body='<div style="max-width:1100px;margin:0 auto"><div class="section-image"><div class="img-placeholder">[ 娃娃介紹主圖 ]</div></div><div class="feature-detail-content" style="margin-top:32px"><h3>娃娃系統說明</h3><p>娃娃是跟隨玩家的輔助角色，可提供各種被動加成效果，讓你在冒險中更加強大。</p><ul><li>娃娃分為普通、稀有、史詩、傳說四個等級</li><li>紅色娃娃為活動限定，擁有獨特外觀與強力加成</li><li>同時只能攜帶一隻娃娃</li></ul></div><div class="section-image" style="margin-top:32px"><div class="img-placeholder">[ 娃娃列表圖 ]</div></div></div>' },
  @{ file='weapons.html'; title='武器介紹'; badge='WEAPONS'; h1='武器介紹'; sub='強力武器一覽'; body='<div style="max-width:1100px;margin:0 auto"><div class="section-image"><div class="img-placeholder">[ 武器介紹主圖 ]</div></div><div class="feature-detail-content" style="margin-top:32px"><h3>武器說明</h3><p>本服提供多種強力武器，各職業有專屬武器，強化上限依版本設定。</p><ul><li>祝福強化不破壞武器</li><li>特殊武器僅能透過特定途徑取得</li></ul></div><div class="section-image" style="margin-top:24px"><div class="img-placeholder">[ 武器列表圖 ]</div></div></div>' },
  @{ file='armor.html'; title='防具介紹'; badge='ARMOR'; h1='防具介紹'; sub='強力防具一覽'; body='<div style="max-width:1100px;margin:0 auto"><div class="section-image"><div class="img-placeholder">[ 防具介紹主圖 ]</div></div><div class="feature-detail-content" style="margin-top:32px"><h3>防具說明</h3><p>本服提供多種強力防具套裝，完整套裝可獲得額外套裝加成。</p><ul><li>防具可強化提升防禦力</li><li>祝福強化不破壞防具</li><li>套裝效果穿齊觸發</li></ul></div><div class="section-image" style="margin-top:24px"><div class="img-placeholder">[ 防具列表圖 ]</div></div></div>' },
  @{ file='maps.html'; title='地圖介紹'; badge='MAP GUIDE'; h1='地圖介紹'; sub='各地圖掉落與建議等級'; body='<div style="max-width:1100px;margin:0 auto"><div class="section-image"><div class="img-placeholder">[ 地圖主圖 ]</div></div><div class="feature-detail-content" style="margin-top:32px"><h3>地圖說明</h3><p>本服開放多張地圖，各地圖有不同的建議等級與掉落道具，選擇適合的地圖能讓你事半功倍。</p></div><div class="section-image" style="margin-top:24px"><div class="img-placeholder">[ 地圖掉落表 ]</div></div><div class="section-image"><div class="img-placeholder">[ 特殊地圖圖 ]</div></div></div>' }
)

foreach ($p in $pages) {
  $html = @"
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>大藍蕉天堂 - $($p.title)</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
$nav
$modals
<div class="hero" style="height:240px">
  <div class="hero-bg" style="background:linear-gradient(135deg,#1a0a08,#0a0818);"></div>
  <div class="hero-content">
    <div class="hero-badge">$($p.badge)</div>
    <h1 class="hero-title"><span style="font-size:2rem">$($p.h1)</span></h1>
    <p class="hero-tagline">$($p.sub)</p>
  </div>
</div>
<div class="container" style="padding-top:56px;padding-bottom:80px">
$($p.body)
</div>
$footer
</body>
</html>
"@
  [System.IO.File]::WriteAllText("$dir\$($p.file)", $html, [System.Text.Encoding]::UTF8)
  Write-Host "Created $($p.file)"
}
Write-Host "Done!"
