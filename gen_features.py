# -*- coding: utf-8 -*-
import os
os.chdir(r"C:\Users\zoo29\Desktop\大藍蕉天堂網站")

# ─── Nav dropdown HTML ────────────────────────────────────────────────────────
_DD_FEAT_ACTIVE = '''    <div class="topnav-dropdown">
      <a class="topnav-link active">遊戲特色 ▾</a>
      <div class="dropdown-menu">
        <a href="feature-01.html">法師召喚物系統</a><a href="feature-02.html">職業特色技能</a>
        <a href="feature-03.html">職業之力介紹</a><a href="feature-05.html">寵物系統介紹</a>
        <a href="feature-07.html">威望系統</a><a href="feature-08.html">高寵介紹</a>
        <a href="feature-09.html">在線禮包</a><a href="feature-12.html">換金道具</a>
      </div>
    </div>'''

_DD_FEAT_PLAIN = '''    <div class="topnav-dropdown">
      <a class="topnav-link">遊戲特色 ▾</a>
      <div class="dropdown-menu">
        <a href="feature-01.html">法師召喚物系統</a><a href="feature-02.html">職業特色技能</a>
        <a href="feature-03.html">職業之力介紹</a><a href="feature-05.html">寵物系統介紹</a>
        <a href="feature-07.html">威望系統</a><a href="feature-08.html">高寵介紹</a>
        <a href="feature-09.html">在線禮包</a><a href="feature-12.html">換金道具</a>
      </div>
    </div>'''

_DD_ITEM_ACTIVE = '''    <div class="topnav-dropdown">
      <a class="topnav-link active">道具裝備 ▾</a>
      <div class="dropdown-menu">
        <a href="items.html">道具介紹</a><a href="hexagram.html">六芒星徽章</a>
        <a href="feature-04.html">戰馬雕像能力</a><a href="feature-06.html">主線任務勳章</a>
        <a href="feature-10.html">赫卡特介紹</a><a href="feature-11.html">傲慢的掛飾</a>
      </div>
    </div>'''

_DD_ITEM_PLAIN = '''    <div class="topnav-dropdown">
      <a class="topnav-link">道具裝備 ▾</a>
      <div class="dropdown-menu">
        <a href="items.html">道具介紹</a><a href="hexagram.html">六芒星徽章</a>
        <a href="feature-04.html">戰馬雕像能力</a><a href="feature-06.html">主線任務勳章</a>
        <a href="feature-10.html">赫卡特介紹</a><a href="feature-11.html">傲慢的掛飾</a>
      </div>
    </div>'''

_NAV_CORE = '''<nav class="topnav">
  <div class="topnav-logo">⚔ 大藍蕉天堂</div><div class="topnav-sep"></div>
  <div class="topnav-links" id="navLinks">
    <a class="topnav-link" href="index.html">首頁</a>
    <a class="topnav-link" href="sponsor.html">贊助系統</a>
    <a class="topnav-link" href="events.html">活動介紹</a>
{DD_FEAT}
{DD_ITEM}
    <a class="topnav-link" href="boss.html">BOSS介紹</a>
    <a class="topnav-link" href="download.html">檔案下載</a>
    <a class="topnav-link" href="maps.html">特殊地圖掉落</a>
    <a class="topnav-link" href="rates.html">版本倍率</a>
    <a class="topnav-link" href="referral.html">推文系統</a>
  </div>
  <div class="topnav-right"><a class="topnav-line-btn" href="#" onclick="document.getElementById(\'modal-line\').classList.add(\'open\');return false;">LINE 客服</a></div>
  <div class="hamburger" onclick="document.getElementById(\'navLinks\').classList.toggle(\'open\')"><span></span><span></span><span></span></div>
</nav>'''

NAV_FEAT = _NAV_CORE.replace('{DD_FEAT}', _DD_FEAT_ACTIVE).replace('{DD_ITEM}', _DD_ITEM_PLAIN)
NAV_ITEM = _NAV_CORE.replace('{DD_FEAT}', _DD_FEAT_PLAIN).replace('{DD_ITEM}', _DD_ITEM_ACTIVE)

SIDEBAR = '''<div class="float-sidebar">
  <button class="float-btn sponsor" data-modal="modal-sponsor">💰 贊助方案</button>
  <button class="float-btn" data-modal="modal-gift">🎁 申請禮包</button>
  <button class="float-btn" data-modal="modal-line">💬 LINE</button>
</div>
<div class="float-modal" id="modal-sponsor"><div class="float-modal-box"><span class="modal-close">✕</span><div class="modal-title">💰 贊助方案</div><div class="modal-body"><p>▸ 贊助詳情請加入 LINE 社群詢問</p></div><a class="modal-btn" href="sponsor.html">查看贊助頁面</a></div></div>
<div class="float-modal" id="modal-gift"><div class="float-modal-box"><span class="modal-close">✕</span><div class="modal-title">🎁 新手禮包</div><div class="modal-body"><p>加入 LINE 官方社群後私訊管理員即可領取。</p></div><a class="modal-btn" href="#">前往 LINE 領取</a></div></div>
<div class="float-modal" id="modal-line"><div class="float-modal-box"><span class="modal-close">✕</span><div class="modal-title">💬 LINE 聯絡方式</div><div class="modal-body" style="text-align:center"><div style="width:150px;height:150px;background:var(--bg4);border:1px solid var(--border);margin:0 auto;"></div></div><a class="modal-btn" href="#">加入 LINE 官方社群</a></div></div>'''

def page(num, title, heading, img_url, body, prev_n, next_n, nav_html=None, category='遊戲特色'):
    nav = nav_html if nav_html else NAV_FEAT
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>大藍蕉天堂 - {title}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
{nav}
{SIDEBAR}
<div style="margin-top:56px"></div>
<div class="feature-detail">
  <div style="margin-bottom:20px"><a href="features.html" style="color:var(--text-muted);font-size:.78rem;letter-spacing:1px;">← 返回遊戲特色</a></div>
  <div class="section-header" style="text-align:left;margin-bottom:32px">
    <div class="section-eyebrow">{category}</div>
    <h2 class="section-title" style="text-align:left">{heading}</h2>
  </div>
  <div class="feature-detail-img"><img src="{img_url}" alt="{heading}"></div>
  <div class="feature-detail-content">
{body}
  </div>
  <div class="feature-nav-btns">
    <a href="feature-{prev_n:02d}.html" class="btn-outline">← 上一項</a>
    <a href="feature-{next_n:02d}.html" class="btn-outline">下一項 →</a>
  </div>
</div>
<footer><div class="footer-copy">© 2026 大藍蕉天堂</div></footer>
<script src="main.js"></script>
</body>
</html>'''

# ─── style helpers ────────────────────────────────────────────────────────────
def block(hdr_icon, hdr_text, hdr_rgb, content, border_rgb=None):
    r,g,b = hdr_rgb
    br,bg_c,bb = border_rgb if border_rgb else hdr_rgb
    return f'''<div style="background:linear-gradient(135deg,#131010,#0d0b0b);border:1px solid rgba({br},{bg_c},{bb},.28);border-radius:10px;overflow:hidden;margin-bottom:24px">
  <div style="background:linear-gradient(90deg,rgba({r},{g},{b},.18),transparent);padding:14px 20px;border-bottom:1px solid rgba({r},{g},{b},.2);display:flex;align-items:center;gap:10px">
    <span style="font-size:1.25em">{hdr_icon}</span>
    <h3 style="margin:0;color:rgb({r},{g},{b});font-size:1.05em;letter-spacing:1px;font-weight:700">{hdr_text}</h3>
  </div>
  <div style="padding:18px 20px">{content}</div>
</div>'''

def dtable(headers, col_widths, rows, hr, max_label='MAX'):
    r,g,b = hr
    ths = ''.join(f'<th style="padding:10px 6px;text-align:center;border:1px solid rgba({r},{g},{b},.3);font-size:.82em;letter-spacing:.5px;width:{w}">{h}</th>' for h,w in zip(headers,col_widths))
    thead = f'<thead><tr style="background:rgba({r},{g},{b},.22);color:#fff">{ths}</tr></thead>'
    trs = []
    for i,row in enumerate(rows):
        is_max = str(row[0]).upper() == max_label.upper()
        bg = 'rgba(201,169,110,.07)' if is_max else ('#1c1818' if i%2==0 else '#131010')
        top_border = f'border-top:1px solid rgba(201,169,110,.35);' if is_max else ''
        tds = ''.join(f'<td style="padding:8px 5px;text-align:center;border:1px solid #2e2828;color:{"#c9a96e" if is_max else "#e8e2d8"};font-size:.83em;{"font-weight:700;" if is_max else ""}">{c}</td>' for c in row)
        trs.append(f'<tr style="background:{bg};{top_border}">{tds}</tr>')
    tbody = f'<tbody>{"".join(trs)}</tbody>'
    return f'<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse">{thead}{tbody}</table></div>'

def info_row(label, value, color='#c9a96e'):
    return f'<div style="display:flex;gap:8px;align-items:baseline;margin-bottom:8px"><span style="color:#9a8f85;font-size:.85em;min-width:90px">{label}</span><span style="color:{color};font-weight:600;font-size:.9em">{value}</span></div>'

def warn_box(icon, title, body_html, color='#ff6b6b'):
    r,g,b = (255,107,107) if color=='#ff6b6b' else (255,180,50)
    if color not in ('#ff6b6b','#ff6b6b'):
        # parse from color string if possible, else default
        pass
    if color == '#c9a96e':
        r,g,b = 201,169,110
    return f'<div style="background:rgba({r},{g},{b},.07);border-left:4px solid {color};border-radius:0 8px 8px 0;padding:14px 16px;margin-bottom:20px"><strong style="color:{color};font-size:.95em">{icon} {title}</strong><div style="color:#c8bdb5;font-size:.88em;margin-top:8px;line-height:1.7">{body_html}</div></div>'

# ─── FEATURE-03: 職業之力介紹 ─────────────────────────────────────────────────
IMG_NPC_HO = 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAICxmnDqCzjpOo8frX0sB8a_j2-ZNbbAAKsDmsbWOchVqWfhoQ1mTwpAQADAgADeQADOgQ.jpg'

job_tables = [
    ('👑','王族：殷海薩之力',(74,158,255),
     ['等級','遭受傷害機率治癒','PVP 減傷','近距傷害'],['12%','42%','23%','23%'],
     [('初始','4% 機率治癒 50~100','+1','+1'),
      ('LV.1','5% 機率治癒 100~150','+1','+1'),
      ('LV.2','6% 機率治癒 150~200','+2','+2'),
      ('LV.3','7% 機率治癒 200~250','+2','+2'),
      ('LV.4','8% 機率治癒 250~300','+3','+3'),
      ('LV.5','9% 機率治癒 300~350','+3','+3'),
      ('MAX','10% 機率治癒 350~400','+5','+5')]),
    ('🛡️','騎士：屠龍者之力',(220,80,80),
     ['等級','衝擊之暈命中率','新增抗魔','HP 加成','傷害減免'],['10%','22%','18%','27%','23%'],
     [('初始','提高 1%','+2','+100','+1'),
      ('LV.1','提高 2%','+4','+200','+2'),
      ('LV.2','提高 3%','+6','+300','+3'),
      ('LV.3','提高 5%','+8','+400','+4'),
      ('LV.4','提高 7%','+10','+500','+5'),
      ('LV.5','提高 9%','+12','+800','+6'),
      ('MAX','提高 12%','+15','+1000','+8')]),
    ('🏹','妖精：席琳之力',(60,200,100),
     ['等級','三重矢傷害','降低迴避','近距攻擊'],['12%','42%','23%','23%'],
     [('初始','+5','+1','+1'),('LV.1','+8','+2','+2'),('LV.2','+10','+3','+2'),
      ('LV.3','+12','+4','+2'),('LV.4','+14','+5','+10'),('LV.5','+16','+6','+10'),
      ('MAX','+20','+7','+15')]),
    ('🪄','法師：艾歐丁之力',(180,80,255),
     ['等級','魅力加成','烈炎術傷害','魔力回復'],['12%','38%','30%','20%'],
     [('初始','+9','+8','+2'),('LV.1','+12','+15','+2'),('LV.2','+12','+30','+4'),
      ('LV.3','+18','+45','+4'),('LV.4','+21','+60','+6'),('LV.5','+25','+75','+6'),
      ('MAX','+36','+100','+10')]),
    ('🗡️','黑暗妖精：格蘭肯之力',(130,130,160),
     ['等級','近戰爆擊率','爆擊倍率','攻擊命中'],['12%','38%','30%','20%'],
     [('初始','+1%','1.02 倍','+1'),('LV.1','+2%','1.04 倍','+1'),('LV.2','+3%','1.06 倍','+2'),
      ('LV.3','+4%','1.08 倍','+2'),('LV.4','+5%','1.10 倍','+3'),('LV.5','+6%','1.12 倍','+3'),
      ('MAX','+8%','1.15 倍','+5')]),
]

body_03 = block('🔨','製作方式',(201,169,110),
    f'<p style="color:#9a8f85;margin:0 0 14px 0">請前往主城尋找 NPC <strong style="color:#ff6b6b;font-size:1.05em">"霍"</strong> 進行升級。</p>'
    f'<div style="text-align:center"><img src="{IMG_NPC_HO}" style="max-width:100%;border-radius:8px;border:1px solid #2e2828;box-shadow:0 4px 20px rgba(0,0,0,.5)"></div>')

for icon, title, rgb, headers, widths, rows in job_tables:
    body_03 += block(icon, title, rgb, dtable(headers, widths, rows, rgb))

# ─── FEATURE-04: 戰馬雕像能力 ─────────────────────────────────────────────────
horses = [
    ('🔥','烈焰戰馬雕像 (近戰)',(220,80,80),
     ['+0','+1','+2','+3','+4','+5','+6','+7','+8','+9'],
     ['防+1, 體+10','防+1, 體+20','防+2, 體+30','防+2, 體+50','防+2, 體+70','防+3, 體+90','防+3, 體+100','防+3, 體+120','防+4, 體+150','防+5, 體+200'],
     ['近距離傷害+1','近距離傷害+1','近距離傷害+1',
      '近距離傷害+2, PVP近距離傷害+1','近距離傷害+2, PVP近距離傷害+1',
      '近距離傷害+2, PVP近距離傷害+2','近距離傷害+3, PVP近距離傷害+2',
      '近距離傷害+3, PVP近距離傷害+3, 力量+1','近距離傷害+3, PVP近距離傷害+3, 力量+2',
      '近距離傷害+5, PVP近距離傷害+5, 力量+3']),
    ('🌿','疾風戰馬雕像 (遠程)',(60,180,80),
     ['+0','+1','+2','+3','+4','+5','+6','+7','+8','+9'],
     ['防+1, 體+10','防+1, 體+20','防+2, 體+30','防+2, 體+50','防+2, 體+70','防+3, 體+90','防+3, 體+100','防+3, 體+120','防+4, 體+150','防+5, 體+200'],
     ['遠距離傷害+1','遠距離傷害+1','遠距離傷害+1',
      '遠距離傷害+2, PVP遠距離傷害+1','遠距離傷害+2, PVP遠距離傷害+1',
      '遠距離傷害+2, PVP遠距離傷害+2','遠距離傷害+3, PVP遠距離傷害+2',
      '遠距離傷害+3, PVP遠距離傷害+3, 敏捷+1','遠距離傷害+3, PVP遠距離傷害+3, 敏捷+2',
      '遠距離傷害+5, PVP遠距離傷害+5, 敏捷+3']),
    ('❄️','寒冰戰馬雕像 (魔法)',(60,160,220),
     ['+0','+1','+2','+3','+4','+5','+6','+7','+8','+9'],
     ['防+1, 體+10','防+1, 體+20','防+2, 體+30','防+2, 體+50','防+2, 體+70','防+3, 體+90','防+3, 體+100','防+3, 體+120','防+4, 體+150','防+5, 體+200'],
     ['魔防+1, 魔攻+1','魔防+1, 魔攻+1','魔防+1, 魔攻+1',
      '魔防+2, 魔攻+2','魔防+2, 魔攻+2','魔防+2, 魔攻+2','魔防+3, 魔攻+3',
      '魔防+3, 魔攻+3, 智力+1','魔防+3, 魔攻+3, 智力+2','魔防+5, 魔攻+5, 智力+3']),
    ('🏆','黃金戰馬雕像 (防禦)',(201,169,110),
     ['+0','+1','+2','+3','+4','+5','+6','+7','+8','+9'],
     ['防+1, 體+10','防+1, 體+20','防+2, 體+30','防+2, 體+50','防+2, 體+70','防+3, 體+90','防+3, 體+100','防+3, 體+120','防+4, 體+150','防+5, 體+200'],
     ['傷害減傷+1, PVP減傷+1','傷害減傷+1, PVP減傷+1','傷害減傷+1, PVP減傷+1',
      '傷害減傷+2, PVP減傷+2','傷害減傷+2, PVP減傷+2','傷害減傷+2, PVP減傷+2',
      '傷害減傷+3, PVP減傷+3','傷害減傷+3, PVP減傷+3, 力敏+1',
      '傷害減傷+3, PVP減傷+3, 力敏智+1','傷害減傷+5, PVP減傷+5, 力敏智精+2']),
]

prob_grid = ''.join(f'<div style="background:#1c1818;border:1px solid #2e2828;padding:5px;text-align:center;border-radius:4px;font-size:.8em;color:#e8e2d8">{s}</div>' for s in ['0→1: 20%','1→2: 10%','2→3: 9%','3→4: 8%','4→5: 7%','5→6: 6%','6→7: 5%','7→8: 4%','8→9: 3%'])

body_04 = f'''<div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:24px">
  <div style="flex:1;min-width:260px;background:#131010;border:1px solid #2e2828;border-radius:10px;padding:18px">
    <h3 style="color:#c9a96e;margin:0 0 14px 0;border-left:3px solid #c9a96e;padding-left:10px;font-size:1em">🛠️ 強化說明</h3>
    {info_row("強化道具","雕像升級石（精靈墓穴）")}
    {info_row("強化費用","每次 10,000 天幣")}
    {info_row("失敗機制","")}
    <span style="background:rgba(0,200,100,.12);color:#00c864;padding:3px 10px;border-radius:20px;font-size:.82em;font-weight:700">✔ 失敗不退階</span>
  </div>
  <div style="flex:1;min-width:240px;background:#131010;border:1px solid #2e2828;border-radius:10px;padding:18px">
    <h3 style="color:#c9a96e;margin:0 0 14px 0;border-left:3px solid #c9a96e;padding-left:10px;font-size:1em">📈 強化成功機率</h3>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px">{prob_grid}</div>
  </div>
</div>'''

for icon, title, rgb, levels, base_stats, special in horses:
    r,g,b = rgb
    rows = list(zip(levels, base_stats, special))
    body_04 += block(icon, title, rgb, dtable(['等級','基礎能力','特殊能力加成'],['10%','30%','60%'], rows, rgb))

# ─── FEATURE-05: 寵物系統介紹 (Card Grid per family) ────────────────────────
feed_items = [('🐇 暴走兔','胡蘿蔔'),('🐯 虎男','虎男飼料'),('🐼 貓熊','貓熊的食物'),('🥊 袋鼠','袋鼠的食物')]
feed_html = ''.join(f'<div style="background:#1c1818;border:1px solid #2e2828;padding:6px 10px;border-radius:6px;font-size:.83em;color:#e8e2d8"><strong style="color:#ff9944">{n}</strong>：{f}</div>' for n,f in feed_items)

body_05 = f'''<div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:24px">
  <div style="flex:1;min-width:260px;background:#131010;border:1px solid #2e2828;border-radius:10px;padding:18px">
    <h3 style="color:#c9a96e;margin:0 0 14px 0;border-left:3px solid #c9a96e;padding-left:10px;font-size:1em">💡 捕捉與進化</h3>
    <p style="color:#9a8f85;font-size:.88em;margin:0 0 8px 0">捕捉地點：<strong style="color:#ff6b6b">【寵物之島】</strong>，魅力需求 <strong style="color:#c9a96e">6</strong></p>
    <p style="color:#9a8f85;font-size:.88em;margin:0">進化需求：等級達 <strong style="color:#c9a96e">Lv.30</strong></p>
    <ul style="color:#9a8f85;font-size:.83em;margin:8px 0 0 0;padding-left:16px">
      <li>二階（高等）：使用 <strong style="color:#e8e2d8">進化果實</strong></li>
      <li>三階（進擊）：使用 <strong style="color:#e8e2d8">勝利果實</strong></li>
    </ul>
  </div>
  <div style="flex:1;min-width:260px;background:#131010;border:1px solid rgba(255,153,68,.25);border-radius:10px;padding:18px">
    <h3 style="color:#ff9944;margin:0 0 12px 0;border-left:3px solid #ff9944;padding-left:10px;font-size:1em">🥕 餵食指南</h3>
    <p style="color:#9a8f85;font-size:.85em;margin:0 0 10px 0">🛒 購買地點：主城 <strong style="color:#ff6b6b">「道具商」</strong> NPC</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">{feed_html}</div>
  </div>
</div>'''

# Pet families: (icon, family, stats_atk_hp_spd, base_name, base_skill, mid_name, mid_skill, top_name, top_skill)
pet_families = [
    ('🐻','熊族','極高攻／極高血／極慢速',
     '熊','-', '高等熊','-', '進擊的熊','爪痕暴擊（水屬性）'),
    ('🐺','狼族','稍低攻／中血／快速',
     '狼','-', '高等狼','兩格攻擊', '進擊的狼','兩格攻擊・爪痕暴擊（風屬性）'),
    ('🐕','柯利族','中攻／高血／慢速',
     '柯利','兩格攻擊', '高等柯利','兩格攻擊', '進擊的柯利','兩格攻擊・爪痕暴擊（火屬性）'),
    ('🐩','牧羊犬族','中攻／中血／中速',
     '牧羊犬','-', '高等牧羊犬','-', '進擊的牧羊犬','爪痕暴擊（火屬性）'),
    ('🦮','杜賓狗族','高攻／少血／快速',
     '杜賓狗','-', '高等杜賓狗','-', '進擊的杜賓狗','爪痕暴擊（地屬性）'),
    ('🐶','哈士奇族','中攻／高血／中速',
     '哈士奇','-', '高等哈士奇','-', '進擊的哈士奇','爪痕暴擊（水屬性）'),
    ('🐾','高麗犬族','高攻／中血／中速',
     '高麗幼犬','-', '高麗犬','瘋狂咬擊', '進擊的高麗犬','瘋狂咬擊・爪痕暴擊（風屬性）'),
    ('🥊','袋鼠族','高攻／高血／中速',
     '袋鼠','-', '高等袋鼠','爆裂拳', '進擊的袋鼠','弱化術・爪痕暴擊（風屬性）'),
    ('🐯','虎男族','高攻／高血／中速',
     '虎男','-', '真・虎男','爆裂勾爪', '進擊的虎男','爆裂勾爪・爪痕暴擊（地屬性）'),
    ('🐱','貓族','極高攻／少血／中速',
     '貓','寒冷戰慄', '高等貓','寒冷戰慄', '進擊的貓','寒冷戰慄・爪痕暴擊（風屬性）'),
    ('🐇','暴走兔族','高攻／中血／快速',
     '暴走兔','冰錐', '高等暴走兔','冰錐', '進擊的暴走兔','冰錐・爪痕暴擊（水屬性）'),
    ('🦝','浣熊族','中攻／高血／慢速',
     '浣熊','緩速術', '高等浣熊','緩速・疾病・弱化', '進擊的浣熊','緩速/疾病/弱化・爪痕暴擊（火屬性）'),
    ('🐶','小獵犬族','偏低攻／高血／中速',
     '小獵犬','地獄之牙', '高等小獵犬','地獄之牙', '進擊的小獵犬','地獄之牙・爪痕暴擊（地屬性）'),
    ('🐕','聖伯納犬族','偏低攻／高血／中速',
     '聖伯納犬','風刃', '高等聖伯納犬','風刃', '進擊的聖伯納犬','風刃・爪痕暴擊（水屬性）'),
    ('🦊','狐狸族','偏低攻／中血／中速',
     '狐狸','火箭術', '高等狐狸','火箭術', '進擊的狐狸','火箭術・爪痕暴擊（火屬性）'),
    ('🐼','熊貓族','高攻／高血／慢速',
     '熊貓','兩格攻擊', '高等熊貓','兩格攻擊・熊貓爆擊', '進擊的熊貓','兩格/緩速/爆擊・爪痕暴擊（地屬性）'),
    ('🐒','猴子族','高攻／高血／慢速',
     '猴子','-', '高等猴子','衝擊波', None, None),
]

def pet_card(icon, family, stats, base_n, base_s, mid_n, mid_s, top_n, top_s):
    tier_rows = [
        ('基礎', base_n, base_s, '#9a8f85'),
        ('高等', mid_n,  mid_s,  '#00e5ff'),
    ]
    if top_n:
        tier_rows.append(('進擊', top_n, top_s, '#ff6b6b'))
    tiers_html = ''
    for tier_label, name, skill, color in tier_rows:
        skill_str = f'<span style="color:#666;font-size:.78em"> — {skill}</span>' if skill and skill != '-' else ''
        tiers_html += f'<div style="display:flex;align-items:baseline;gap:6px;padding:5px 0;border-bottom:1px solid #2e2828"><span style="min-width:30px;text-align:center;font-size:.72em;background:rgba(255,255,255,.05);border-radius:3px;padding:1px 4px;color:{color};font-weight:700">{tier_label}</span><span style="color:{color};font-size:.84em;font-weight:600">{name}</span>{skill_str}</div>'
    return f'''<div style="background:linear-gradient(135deg,#131010,#0d0b0b);border:1px solid #2e2828;border-radius:10px;padding:14px 16px">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;border-bottom:1px solid rgba(201,169,110,.2);padding-bottom:8px">
    <span style="font-size:1.4em">{icon}</span>
    <div>
      <div style="color:#c9a96e;font-weight:700;font-size:.92em">{family}</div>
      <div style="color:#666;font-size:.75em;margin-top:1px">{stats}</div>
    </div>
  </div>
  {tiers_html}
</div>'''

pet_cards_html = '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;margin-bottom:8px">'
for fam in pet_families:
    pet_cards_html += pet_card(*fam)
pet_cards_html += '</div>'

body_05 += block('🐾','寵物族群一覽',(74,158,255), pet_cards_html)

# ─── FEATURE-06: 主線任務勳章 (六芒星 removed — see hexagram.html) ──────────
IMG_MAIN_NPC = 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAICxWnDpzCaKTe8Q1Gr89aR3R3t12YMAAKmDmsbWOchVi2wXBX1q0B1AQADAgADeQADOgQ.jpg'

main_rows = [
    ('Lv.0','創角獲得','HP+5 MP+3','-','-'),
    ('Lv.1','騎士洞窟','HP+10 MP+5','-','30張 / 5萬'),
    ('Lv.2','奇岩地監','HP+30 MP+10','-','30張 / 5萬'),
    ('Lv.3','海音地監','HP+50 MP+20','-','30張 / 5萬'),
    ('Lv.4','古魯丁地監','HP+70 MP+30','經驗+1%','150張 / 50萬'),
    ('Lv.5','象牙塔','HP+100 MP+40','經驗+1%, 回血+2','150張 / 50萬'),
    ('Lv.6','水晶洞窟','HP+130 MP+50','經驗+1%, 回血+2, 回魔+2, 抗魔+1','150張 / 50萬'),
    ('Lv.7','拉斯塔巴德','HP+160 MP+60','經驗+2%, 回血+2, 回魔+2, 抗魔+1','300張 / 100萬'),
    ('Lv.8','海賊島地監','HP+200 MP+70','經驗+3%, 回血+2, 回魔+2, 抗魔+1','300張 / 100萬'),
    ('Lv.9','龍谷地監','HP+250 MP+80','經驗+4%, 回血+2, 回魔+2, 抗魔+1','300張 / 100萬'),
    ('Lv.10','地底湖','HP+300 MP+90','經驗+5%, 回血+2, 回魔+2, 抗魔+1','500張 / 300萬'),
    ('Lv.11','精靈墓穴','HP+350 MP+100','經驗+6%, 回血+2, 回魔+2, 防禦-1, 抗魔+2','500張 / 300萬'),
    ('Lv.12','遺忘之島','HP+400 MP+110','經驗+6%, 回血+2, 回魔+2, 防禦-1, 抗魔+2, 藥水回復+2','500張 / 300萬'),
    ('Lv.13','夢幻之島','HP+450 MP+120','經驗+6%, 回血+2, 回魔+2, 防禦-1, 抗魔+2, 藥水回復+2','500張 / 300萬'),
    ('Lv.14','傲慢之塔 1F','HP+500 MP+130','經驗+7%, 回血+2, 回魔+2, 防禦-2, 抗魔+4, 藥水回復+2','500張 / 500萬'),
    ('Lv.15','傲慢之塔 2F','HP+550 MP+140','經驗+7%, 回血+2, 回魔+2, 防禦-2, 抗魔+4, 藥水回復+4','500張 / 500萬'),
    ('Lv.16','傲慢之塔 3F','HP+600 MP+150','經驗+7%, 回血+4, 回魔+4, 防禦-2, 抗魔+4, 藥水回復+4','500張 / 500萬'),
    ('Lv.17','傲慢之塔 4F','HP+650 MP+160','經驗+8%, 回血+4, 回魔+4, 防禦-2, 抗魔+5, 藥水回復+4','500張 / 500萬'),
    ('Lv.18','傲慢之塔 5F','HP+700 MP+170','經驗+8%, 回血+4, 回魔+4, 防禦-2, 抗魔+5, 藥水回復+6, 所有傷害+2','500張 / 500萬'),
    ('Lv.19','傲慢之塔 6F','HP+750 MP+180','經驗+8%, 回血+4, 回魔+4, 防禦-2, 抗魔+5, 藥水回復+6, 所有傷害+2, 所有命中+1','500張 / 500萬'),
    ('Lv.20','傲慢之塔 7F','HP+800 MP+190','經驗+9%, 回血+4, 回魔+4, 防禦-2, 抗魔+6, 藥水回復+6, 所有傷害+2, 所有命中+1','500張 / 500萬'),
    ('Lv.21','傲慢之塔 8F','HP+850 MP+200','經驗+9%, 回血+5, 回魔+5, 防禦-3, 抗魔+6, 藥水回復+8, 所有傷害+3, 所有命中+2','500張 / 500萬'),
    ('Lv.22','傲慢之塔 9F','HP+900 MP+210','經驗+9%, 回血+5, 回魔+5, 防禦-3, 抗魔+6, 藥水回復+8, 所有傷害+3, 所有命中+2','500張 / 500萬'),
    ('Lv.23','傲慢之塔 10F','HP+950 MP+220','經驗+10%, 回血+5, 回魔+5, 防禦-3, 抗魔+8, 藥水回復+10, 所有傷害+3, 所有命中+3','500張 / 500萬'),
    ('Lv.24','古代遺忘之島','HP+1000 MP+230','經驗+10%, 回血+5, 回魔+5, 防禦-3, 抗魔+8, 藥水回復+10, 所有傷害+5, 所有命中+3','500張 / 500萬'),
    ('Lv.25','古代高崙','HP+1050 MP+250','經驗+12%, 回血+6, 回魔+6, 防禦-3, 抗魔+10, 藥水回復+15, 所有傷害+5, 所有命中+5','500張 / 500萬'),
]

body_06 = f'''<div style="text-align:center;margin-bottom:24px">
  <img src="{IMG_MAIN_NPC}" style="max-width:100%;border-radius:10px;border:1px solid #2e2828;box-shadow:0 4px 20px rgba(0,0,0,.5)">
  <p style="color:#9a8f85;font-size:.82em;margin-top:8px">📍 村莊主線任務 NPC</p>
</div>'''
body_06 += warn_box('⚠️','重要注意事項','勳章進行升階製作時，請務必先「脫下裝備」再執行製作，以確保流程正常。','#ff6b6b')
body_06 += block('🛠️','製作與取得方式',(201,169,110),
    f'{info_row("製作地點","村莊主線任務 NPC")}'
    f'{info_row("證明獲取","相關地圖獲取對應道具")}'
    f'<div style="background:rgba(0,229,255,.07);border:1px solid rgba(0,229,255,.2);border-radius:6px;padding:10px;font-size:.85em;color:#9a8f85;margin-top:8px">'
    f'💡 主線勳章 <span style="color:#00e5ff">Lv.0</span> 於創角時即可獲得。若有遺失，請至奇物商城購買。</div>')
body_06 += block('📈','主線任務勳章等級一覽',(74,158,255),
    dtable(['等級','證明地點','核心能力 (HP/MP)','其他能力加成','消耗（證明/天幣）'],
           ['8%','18%','18%','38%','18%'], main_rows, (74,158,255)))

# ─── FEATURE-07: 威望系統 ─────────────────────────────────────────────────────
IMG_PRESTIGE_NPC = 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAICx2nDq7dn0MCLgZfkfw_3AzEF3ZuTAAK3DmsbWOchVub6-6S1-itwAQADAgADeAADOgQ.jpg'

score_map_rows = [
    ('騎士洞窟 1~4樓','1','地底湖','2'),
    ('奇岩地監 1~4樓','1','精靈墓穴','2'),
    ('海音地監 1~4樓','1','夢幻之島','2'),
    ('象牙塔 4~8樓','1','傲慢之塔 1F~9F','2'),
    ('古魯丁地監 1~7樓','1','傲慢之塔 10F','3'),
    ('水晶洞窟 1~3樓','1','新遺忘之島','3'),
    ('龍谷地監 1~7樓','1','-','-'),
    ('海賊島地監 1~3樓','1','-','-'),
    ('拉斯塔巴德 1~3樓','1','-','-'),
]

prestige_rows = [
    ('初入龍域','100','0','0','+10 / +5','-'),
    ('見習獵手','500','0','0','+20 / +10','-'),
    ('鋒芒初露','1,500','0','0','+30 / +15','-'),
    ('披荊斬棘','4,000','0','0','+50 / +25','回血魔+3'),
    ('浴血屠龍','10,000','500','300','+70 / +35','回血魔+5, 狩獵經驗+5%'),
    ('龍血玄黃','20,000','1,000','600','+100 / +50','回血魔+7, 經驗+5%, 魔防+5'),
    ('手刃逆鱗','30,000','1,500','900','+100 / +50','回血魔+7, 經驗+5%, 魔防+5, 魔命+1, 物命+2'),
    ('腳踏龍首','60,000','3,000','1,800','+100 / +50','回血魔+7, 經驗+5%, 魔防+5, 魔命+1, 物命+2, 全傷+1'),
    ('威震龍穴','120,000','6,000','3,600','+100 / +50','回血魔+7, 經驗+5%, 魔防+5, 魔命+1, 物命+2, 全傷+1, 力敏智+1'),
    ('橫掃龍族','200,000','10,000','6,000','+100 / +50','回血魔+7, 經驗+5%, 魔防+5, 魔命+1, 物命+2, 全傷+1, 全能力+1'),
    ('龍騎統領','300,000','15,000','9,000','+110 / +55','回血魔+9, 經驗+6%, 魔防+6, 魔命+1, 物命+2, 全傷+1, 全能力+1'),
    ('屠龍宗師','450,000','22,500','13,500','+120 / +60','回血魔+10, 經驗+6%, 魔防+7, 魔命+1, 物命+2, 全傷+1, 全能力+1'),
    ('龍影尊主','650,000','32,500','19,500','+130 / +65','回血魔+11, 經驗+7%, 魔防+7, 魔命+1, 物命+2, 全傷+1, 全能力+1'),
    ('龍魂主宰','950,000','47,500','28,500','+140 / +70','回血魔+11, 經驗+7%, 魔防+8, 魔命+1, 物命+2, 全傷+1, 全能力+1'),
    ('傲世龍王','1,350,000','67,500','40,500','+150 / +75','回血魔+11, 經驗+7%, 魔防+8, 魔命+2, 物命+3, 全傷+2, 全能力+2'),
    ('滅世龍皇','1,800,000','90,000','54,000','+170 / +85','回血魔+12, 經驗+8%, 魔防+9, 魔命+2, 物命+3, 全傷+2, 全能力+2'),
    ('天龍剋星','2,400,000','120,000','72,000','+200 / +100','回血魔+12, 經驗+8%, 魔防+10, 魔命+2, 物命+3, 全傷+2, 全能力+2'),
    ('神話締造','3,100,000','155,000','93,000','+230 / +115','回血魔+13, 經驗+8%, 魔防+12, 魔命+2, 物命+3, 全傷+2, 全能力+2'),
    ('龍界傳說','3,900,000','195,000','117,000','+260 / +130','回血魔+14, 經驗+9%, 魔防+14, 魔命+3, 物命+3, 全傷+2, 全能力+3'),
    ('屠龍至尊','5,000,000','250,000','150,000','+300 / +100','回血魔+15, 經驗+10%, 魔防+16, 魔命+3, 物命+3, 全傷+2, 全能力+3'),
]

body_07 = f'''<div style="background:#131010;border:1px solid rgba(255,215,0,.25);border-radius:10px;padding:20px;margin-bottom:24px;display:flex;gap:20px;flex-wrap:wrap;align-items:center">
  <img src="{IMG_PRESTIGE_NPC}" style="width:140px;border-radius:8px;border:2px solid rgba(201,169,110,.4);flex-shrink:0">
  <div>
    <strong style="color:#c9a96e;font-size:1.1em;display:block;margin-bottom:10px">📢 玩家必看重要備註</strong>
    <p style="color:#9a8f85;font-size:.9em;margin:0 0 8px 0">1. 玩家自己看不到自己頭銜是 <strong style="color:#ff6b6b;font-size:1.1em">「正常」</strong> 現象。</p>
    <p style="color:#9a8f85;font-size:.9em;margin:0">2. 若要查詢階級，請在對話框輸入 <span style="background:rgba(0,229,255,.1);color:#00e5ff;padding:2px 10px;border-radius:4px;font-weight:700">/who</span></p>
  </div>
</div>'''
body_07 += block('📍','積分獲取地圖與分數',(74,158,255),
    dtable(['地圖名稱','積分','地圖名稱','積分'],['38%','12%','38%','12%'], score_map_rows, (74,158,255)))
body_07 += warn_box('⛔','積分損失機制',
    '<strong style="color:#e8e2d8">擊殺掠奪：</strong>擊殺 10,000 威望以上玩家，可獲得對方死亡損失的 <strong style="color:#ff6b6b">60%</strong> 威望。<br>'
    '<strong style="color:#e8e2d8">死亡損失：</strong>角色死亡時，依威望階級扣除約 <strong style="color:#ff6b6b">5% 威望值</strong>。','#ff6b6b')
body_07 += block('🎖️','威望階級與能力表',(201,169,110),
    dtable(['威望名稱','晉升積分','死亡扣除','擊殺奪取','HP / MP','能力加成'],
           ['16%','13%','13%','13%','13%','32%'], prestige_rows, (201,169,110)))

# ─── FEATURE-08: 高寵介紹 (removed bottom gold text) ─────────────────────────
steps = [('步驟一','雙方先點選 <strong style="background:rgba(201,169,110,.15);color:#c9a96e;padding:1px 8px;border-radius:4px">"允許跟隨"</strong>'),
         ('步驟二','雙方面對面（<span style="color:#00c864;font-weight:700">優化過無須組隊也可以</span>）'),
         ('步驟三','選擇高寵設定 <span style="color:#00e5ff">（成為高寵）</span>'),
         ('步驟四','補師打開高寵系統'),
         ('步驟五','進行補師補血設定及輔助魔法設定')]
steps_html = ''.join(f'<div style="display:flex;gap:14px;align-items:baseline;padding:10px 14px;background:#1c1818;border-radius:8px;margin-bottom:8px"><span style="color:#c9a96e;font-weight:700;font-size:1em;min-width:54px">【{s}】</span><span style="color:#e8e2d8;font-size:.9em">{t}</span></div>' for s,t in steps)

rules = [
    ('01','高寵需<strong style="color:#ff6b6b">主人及高寵皆擁有</strong>才可使用'),
    ('02','使用高寵補血 / BUFF 需要組隊'),
    ('03','高寵可跟隨主人瞬間移動<span style="color:#00c864">（限同張地圖）</span>'),
    ('04','主人與高寵不同地圖、死亡或登出，將自動切斷'),
    ('05','補血範圍限制 <strong style="color:#c9a96e">8格內</strong>，且強制延遲 <strong style="color:#c9a96e">1秒</strong>'),
    ('06','進入攻城範圍自動切斷；每位主人限設一名高寵'),
    ('07','無法使用未學習法術；若卡畫面需手動調整'),
    ('08','主人死亡後會<strong style="color:#ff6b6b">強制解除</strong>高寵系統'),
    ('09','<span style="color:#c9a96e;font-weight:700">【絕對禁忌】</span>主人或高寵任一方隱身，皆無法使用'),
]
rules_trs = ''.join(f'<tr style="background:{"rgba(255,215,0,.05);border:1px solid rgba(201,169,110,.3)" if r[0]=="09" else ("#131010" if int(r[0])%2==1 else "#1c1818")}"><td style="padding:10px 8px;border:1px solid #2e2828;text-align:center;color:#c9a96e;font-weight:700;width:50px">{r[0]}</td><td style="padding:10px 10px;border:1px solid #2e2828;color:#e8e2d8;font-size:.88em">{r[1]}</td></tr>' for r in rules)

body_08 = block('⚔️','高寵設定使用教學',(201,169,110), steps_html)
body_08 += block('⚠️','使用前請詳讀規範',(220,80,80),
    f'<table style="width:100%;border-collapse:collapse"><thead><tr style="background:rgba(220,80,80,.22);color:#fff"><th style="padding:10px;border:1px solid rgba(220,80,80,.3);width:50px;font-size:.85em">編號</th><th style="padding:10px;border:1px solid rgba(220,80,80,.3);text-align:left;font-size:.85em">規範內容</th></tr></thead><tbody>{rules_trs}</tbody></table>')

# ─── FEATURE-09: 在線禮包 ─────────────────────────────────────────────────────
IMG_ONLINE_BANNER = 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDh2oEHce-y1HfTATDxQuSryZS13I4AALcD2sbG-kgVKiu2r7oeYq5AQADAgADeQADOwQ.jpg'

gift_rows = [
    ('💰 金幣','1,000 ~ 10,000','15%'),
    ('💙 藍鑽','1 ~ 10','5%'),
    ('⭐ 六芒星升階石','1','5%'),
    ('🐴 戰馬雕像升級石','1','5%'),
    ('🌿 聖物成長藥劑','1','5%'),
    ('🍶 終極治癒藥水','10 ~ 50','10%'),
    ('🍶 濃縮終極體力恢復劑','10 ~ 50','10%'),
    ('🍶 古代終極體力恢復劑','10 ~ 50','10%'),
    ('⚡ 150% 經驗藥水（刻印）','1 ~ 5','10%'),
    ('⚡ (2階) 150% 經驗藥水（刻印）','1 ~ 5','10%'),
    ('🎴 一般變身卡寶箱','1 ~ 2','7.5%'),
    ('🎴 一般娃娃卡寶箱','1 ~ 2','7.5%'),
]

body_09 = f'<div style="text-align:center;margin-bottom:20px"><img src="{IMG_ONLINE_BANNER}" style="max-width:100%;border-radius:10px;border:1px solid rgba(212,175,55,.3);box-shadow:0 4px 20px rgba(0,0,0,.6)"></div>'
body_09 += f'''<div style="background:linear-gradient(135deg,#131010,#0d0b0b);border:1px solid rgba(212,175,55,.2);border-radius:10px;padding:18px;margin-bottom:20px">
  <p style="color:#9a8f85;font-size:.9em;line-height:1.8;margin:0">
    親愛的勇者，我們深知<strong style="color:#c9a96e">手動練功的辛勞</strong>，每一滴汗水都是榮耀的印記。<br>
    為了體恤大家的付出並增加伺服器的熱血活躍度，特別準備了「在線福袋」，讓您在冒險奮戰之餘，物資補給永遠充足！
  </p>
</div>'''
body_09 += warn_box('📍','活動規則',
    '參與資格：角色等級達 <strong style="color:#c9a96e">LV 50</strong> 以上<br>'
    '獲取方式：每持續在線滿 <strong style="color:#c9a96e">45 分鐘</strong><br>'
    '獎勵發送：系統將自動發送「在線福袋」至您的背包','#c9a96e')
body_09 += block('🏆','在線禮包獎勵一覽',(201,169,110),
    dtable(['獎勵物品名稱','獲得數量範圍','機率'],['55%','30%','15%'], gift_rows, (201,169,110)))

# ─── FEATURE-10: 赫卡特介紹 ───────────────────────────────────────────────────
IMG_HEC_ATK = 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAICrGmroQ-y1USvlS8cw5tFph7DhhHtAAKODGsbk0xhVR_qZrqrFkFdAQADAgADbQADOgQ.png'
IMG_HEC_DEF = 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAICq2mroMvw8hWO126PLTqO56L77d86AAKKDGsbk0xhVfaDCLd6LHbQAQADAgADbQADOgQ.png'
IMG_MOON    = 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAICrWmroar4TPQWLdUyx_WMwI6xILHNAAKQDGsbk0xhVfoNBggSL4RjAQADAgADbQADOgQ.png'

hec_atk_rows = [(f'+{i}',v) for i,v in enumerate([
    '體力+50、魔力+10','體力+100、魔力+20','體力+150、魔力+30','體力+200、魔力+40','體力+250、魔力+50',
    '體力+300、魔力+60','體力+350、魔力+70','體力+400、魔力+80、近距攻擊+1、遠近距攻擊+1',
    '體力+450、魔力+90、近距攻擊+3、遠近距攻擊+3、魔攻+1',
    '體力+500、魔力+100、近距攻擊+5、遠近距攻擊+5、魔攻+2、力量+1、敏捷+1、智力+1'])]
hec_def_rows = [(f'+{i}',v) for i,v in enumerate([
    '體力+50、魔力+10','體力+100、魔力+20','體力+150、魔力+30','體力+200、魔力+40','體力+250、魔力+50',
    '體力+300、魔力+60','體力+350、魔力+70','體力+400、魔力+80、火/水/風/地屬防禦+5、體魔回復+1',
    '體力+450、魔力+90、火/水/風/地屬防禦+15、體魔回復+3、傷害減免+1',
    '體力+500、魔力+100、火/水/風/地屬防禦+30、體魔回復+5、傷害減免+3'])]
moon_mats = '● 鑽石×5, 品質鑽石×3, 紅寶石×10, 品質紅寶石×5, 藍寶石×10, 品質藍寶石×5, 綠寶石×10, 品質綠寶石×5'
moon_prob_items = [('0→1','60%'),('1→2','50%'),('2→3','40%'),('3→4','30%'),('4→5','20%'),('5→6','10%'),('6→7','5%'),('7→8','5%'),('8→9','5%')]

body_10 = f'''<div style="background:#131010;border:1px solid rgba(201,169,110,.25);border-radius:10px;padding:18px;margin-bottom:24px;display:flex;gap:18px;flex-wrap:wrap;align-items:flex-start">
  <img src="{IMG_NPC_HO}" style="width:160px;border-radius:8px;border:1px solid rgba(201,169,110,.3);flex-shrink:0">
  <div>
    <div style="color:#c9a96e;font-weight:700;margin-bottom:8px;font-size:1em">🔨 製作與升級地點</div>
    <p style="color:#9a8f85;font-size:.88em;margin:0 0 6px 0">請前往主城尋找 NPC <strong style="color:#ff6b6b">"霍"</strong> 進行神話裝備的製作與強化。</p>
    <p style="color:#666;font-size:.82em;margin:0">※ 強化時請確認材料數量是否充足。</p>
  </div>
</div>
<div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:24px">'''

for img, title, rgb, rows, mats in [
    (IMG_HEC_ATK,'⚔️ 赫卡特的攻擊',(220,80,80),hec_atk_rows,'💰 金幣×3,000,000  📜 高級製作秘笈×5  📜 稀有製作秘笈×3  💎 高品質鑽石×20  💎 高品質紅寶石×20'),
    (IMG_HEC_DEF,'🛡️ 赫卡特的防禦',(68,138,255),hec_def_rows,'💰 金幣×3,000,000  📜 高級製作秘笈×5  📜 稀有製作秘笈×3  💎 高品質鑽石/紅/藍/綠寶石各×20'),
]:
    r,g,b = rgb
    body_10 += f'''<div style="flex:1;min-width:300px;background:#131010;border:1px solid rgba({r},{g},{b},.25);border-radius:10px;padding:16px;display:flex;flex-direction:column">
    <div style="text-align:center;margin-bottom:12px"><img src="{img}" style="width:70px;filter:drop-shadow(0 0 5px rgba({r},{g},{b},.5))"></div>
    <h3 style="color:rgb({r},{g},{b});margin:0 0 8px 0;text-align:center;font-size:1em">{title}</h3>
    <div style="background:rgb({r},{g},{b});color:#fff;text-align:center;padding:3px;border-radius:4px;font-size:.8em;font-weight:700;margin-bottom:12px">製作機率 100%</div>
    <div style="color:#c9a96e;font-size:.82em;border-bottom:1px solid #2e2828;padding-bottom:6px;margin-bottom:8px;font-weight:700">📍 製作材料</div>
    <p style="color:#9a8f85;font-size:.8em;line-height:1.7;margin:0 0 12px 0">{mats}</p>
    <div style="color:#c9a96e;font-size:.82em;border-bottom:1px solid #2e2828;padding-bottom:6px;margin-bottom:8px;font-weight:700">📊 強化能力屬性</div>
    {dtable(["等級","詳細能力內容"],["15%","85%"], rows, rgb)}
  </div>'''

body_10 += '</div>'
body_10 += warn_box('⚠️','注意','【赫卡特的攻擊】與【赫卡特的防禦】僅限配戴一個，無法同時裝備。','#c9a96e')

moon_probs = ''.join(f'<div style="background:#1c1818;border:1px solid #2e2828;padding:5px;text-align:center;border-radius:4px;font-size:.78em;color:#c9a96e;font-weight:700">{a}<br><span style="color:#9a8f85">{b}</span></div>' for a,b in moon_prob_items)
body_10 += f'''<div style="background:linear-gradient(135deg,rgba(106,27,154,.12),rgba(0,0,0,.4));border:1px solid rgba(179,157,219,.25);border-radius:10px;padding:20px;margin-top:8px">
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:16px;flex-wrap:wrap">
    <img src="{IMG_MOON}" style="width:60px;filter:drop-shadow(0 0 6px rgba(179,157,219,.5))">
    <div><h3 style="color:#b39ddb;margin:0;font-size:1.1em">🌙 夜月之力</h3><p style="color:#b39ddb;font-size:.85em;margin:4px 0 0 0">用於強化赫卡特裝備之重要資材</p></div>
  </div>
  <div style="display:flex;gap:16px;flex-wrap:wrap">
    <div style="flex:1;min-width:240px">
      <div style="color:#c9a96e;font-size:.85em;font-weight:700;margin-bottom:8px">🛠️ 製作材料</div>
      <p style="color:#9a8f85;font-size:.82em;line-height:1.8;margin:0">{moon_mats}</p>
    </div>
    <div style="flex:1;min-width:240px">
      <div style="color:#c9a96e;font-size:.85em;font-weight:700;margin-bottom:8px">📈 強化機率表</div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:5px">{moon_probs}</div>
    </div>
  </div>
</div>'''

# ─── FEATURE-11: 傲慢的掛飾 (bright purple colors) ────────────────────────────
IMG_PENDANT = 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAICrmmrpLgWoW3UFsFgqyAots4RLuVwAAKcDGsbk0xhVZVe_3THKuaUAQADAgADbQADOgQ.png'

pendants = [
    ('潔尼斯','近遠成功+1、額外近遠+1、血+50、魔+30、防禦+1、傷害減免+1、魔法防禦+2',
     '擊殺 【BOSS】潔尼斯女王 獲得（掉落機率 10%）',
     '魂魄（潔尼斯）x1、金幣×100萬、鑽石×15、紅/藍/綠寶石各×30、品質鑽石×15、品質紅/藍/綠各×15、高品質鑽石×10、高品質紅/藍/綠各×10',None),
    ('幻象眼魔','近遠成功+1、額外近遠+1、血+70、魔+50、防禦+1、傷害減免+1、魔法防禦+2',
     '擊殺 【BOSS】幻象眼魔 獲得（掉落機率 9%）',
     '魂魄（幻象眼魔）x1、掛飾(潔尼斯)×1、金幣×200萬、高級製作秘笈×3、稀有製作秘笈×2、紅寶石×50、品質紅×30、高品質紅×20','潔尼斯'),
    ('吸血鬼','近遠成功+2、額外近遠+2、血+90、魔+70、防禦+2、傷害減免+1、魔法防禦+2',
     '擊殺 【BOSS】吸血鬼 獲得（掉落機率 8%）',
     '魂魄（吸血鬼）x1、掛飾(幻象眼魔)×1、金幣×300萬、高級×4、稀有×3、藍寶石×50、品質藍×30、高品質藍×20','幻象眼魔'),
    ('殭屍王','近遠成功+2、額外近遠+2、血+110、魔+90、防禦+2、傷害減免+2、魔法防禦+4',
     '擊殺 【BOSS】殭屍王 獲得（掉落機率 7%）',
     '魂魄（殭屍王）x1、掛飾(吸血鬼)×1、金幣×400萬、高級×6、稀有×5、綠寶石×50、品質綠×30、高品質綠×20','吸血鬼'),
    ('黑豹','近遠成功+3、額外近遠+3、血+150、魔+110、防禦+3、傷害減免+2、魔法防禦+4',
     '擊殺 【BOSS】黑豹 獲得（掉落機率 6%）',
     '魂魄（黑豹）x1、掛飾(殭屍王)×1、金幣×500萬、高級×8、稀有×7、鑽石×50、品質鑽石×30、高品質鑽石×20','殭屍王'),
    ('木乃伊','近遠成功+3、額外近遠+3、血+200、魔+130、防禦+3、傷害減免+2、魔法防禦+4',
     '擊殺 【BOSS】木乃伊王 獲得（掉落機率 5%）',
     '魂魄（木乃伊）x1、掛飾(黑豹)×1、金幣×600萬、高級×10、稀有×8、英雄×1、鑽石×50、紅/藍/綠各×100','黑豹'),
    ('艾莉絲','近遠成功+4、額外近遠+4、血+250、魔+150、防禦+4、傷害減免+3、魔法防禦+6',
     '擊殺 【BOSS】艾莉絲 獲得（掉落機率 4%）',
     '魂魄（艾莉絲）x1、掛飾(木乃伊)×1、金幣×700萬、高級×12、稀有×10、英雄×2、品質鑽石×30、品質紅/藍/綠各×60','木乃伊'),
    ('騎士范德','近遠成功+4、額外近遠+4、血+300、魔+200、防禦+4、傷害減免+3、魔法防禦+6',
     '擊殺 【BOSS】騎士范德 獲得（掉落機率 3%）',
     '魂魄（騎士范德）x1、掛飾(艾莉絲)×1、金幣×800萬、高級×14、稀有×12、英雄×3、高品質鑽石×30、高品質紅/藍/綠各×80','艾莉絲'),
    ('巫妖','近遠成功+5、額外近遠+5、血+350、魔+250、防禦+5、傷害減免+3、魔法防禦+6',
     '擊殺 【BOSS】巫妖 獲得（掉落機率 2%）',
     '魂魄（巫妖）x1、掛飾(騎士范德)×1、金幣×900萬、高級×16、稀有×14、英雄×4、鑽石×50、紅/藍/綠各×100、品質鑽石×30、品質紅/藍/綠各×50、高品質鑽石×20、高品質紅/藍/綠各×30','騎士范德'),
    ('鐮刀死神','近遠成功+5、額外近遠+5、血+500、魔+300、防禦+5、傷害減免+4、魔法防禦+8',
     '擊殺 【BOSS】鐮刀死神 獲得（掉落機率 1%）',
     '魂魄（鐮刀死神）x1、掛飾(巫妖)×1、金幣×1000萬、高級×18、稀有×16、英雄×5、鑽石×50、紅/藍/綠各×100、品質鑽石×30、品質紅/藍/綠各×50、高品質鑽石×20、高品質紅/藍/綠各×30','巫妖'),
]

body_11 = f'''<div style="background:#131010;border:1px solid rgba(180,74,255,.35);border-radius:10px;padding:18px;margin-bottom:24px;display:flex;gap:18px;flex-wrap:wrap;align-items:center">
  <img src="{IMG_NPC_HO}" style="width:160px;border-radius:8px;border:1px solid rgba(180,74,255,.4);flex-shrink:0">
  <div style="flex:1;min-width:220px;text-align:center">
    <div style="color:#d4a8ff;font-weight:700;margin-bottom:8px">🏰 製作地點</div>
    <p style="color:#9a8f85;font-size:.88em;margin:0">請前往主城找道具製作 NPC <strong style="color:#ff6b6b;font-size:1.1em">「霍」</strong> 進行珍品製作與終極進化</p>
  </div>
</div>
<div style="text-align:center;margin-bottom:20px">
  <img src="{IMG_PENDANT}" style="width:90px;filter:drop-shadow(0 0 8px rgba(180,74,255,.6))">
  <p style="color:#d4a8ff;font-weight:700;font-size:.85em;margin-top:8px">⚠️ 本系列製作機率均為 100% 成功</p>
</div>'''

for i,(name,ability,drop,mats,prev) in enumerate(pendants):
    is_last = (name == '鐮刀死神')
    # Use bright purple throughout, crimson only for the final tier
    r,g,b = (220,50,50) if is_last else (180,74,255)
    txt_color = '#ff8080' if is_last else '#d4a8ff'
    border_color = f'rgba({r},{g},{b},.4)'
    hdr_bg = f'rgba({r},{g},{b},.18)'
    body_11 += f'''<div style="background:#131010;border:1px solid {border_color};border-radius:10px;overflow:hidden;margin-bottom:18px">
  <div style="background:linear-gradient(90deg,{hdr_bg},transparent);padding:12px 18px;border-bottom:1px solid {border_color}">
    <h3 style="margin:0;color:{txt_color};font-size:.95em">📿 傲慢宿主的掛飾（{name}）</h3>
  </div>
  <div style="padding:14px 18px">
    <div style="background:rgba({r},{g},{b},.1);border:1px dashed rgba({r},{g},{b},.4);border-radius:6px;padding:10px 14px;margin-bottom:10px;color:{txt_color};font-size:.83em;font-weight:700">✨ {ability}</div>
    <div style="background:rgba(255,153,68,.05);border:1px solid rgba(255,153,68,.2);border-radius:6px;padding:8px 12px;margin-bottom:10px;color:#ff9944;font-size:.82em;font-weight:700">👾 {drop}</div>
    <div style="color:#ff6b6b;font-size:.82em;font-weight:700;margin-bottom:6px">📍 製作材料</div>
    <p style="color:#9a8f85;font-size:.81em;line-height:1.7;margin:0">{mats}</p>
  </div>
</div>'''

# ─── FEATURE-12: 換金道具 (larger image) ──────────────────────────────────────
IMG_EXCHG = 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAICtmm_lazHrRZsNzE-gWQ1VHVaLsF7AAL8DWsbSrIAAVYZxdDWJFLDPgEAAwIAA20AAzoE.png'

features_list = [
    ('✔','全地圖覆蓋','主線、大陸地圖所有怪物機率掉落，練功打寶兩不誤。'),
    ('✔','BOSS 必爭','全 Boss 掉落機率大幅提升，讓 BOSS 更具挑戰價值。'),
    ('✔','商店回收','獲得後直接販售給 NPC，即刻換取高額金幣，升級無煩惱。'),
]
feat_html = ''.join(f'<div style="display:flex;align-items:flex-start;gap:12px;padding:10px 14px;background:#1c1818;border-radius:8px;margin-bottom:8px"><span style="color:#00c864;font-size:1.1em;flex-shrink:0;font-weight:900">{icon}</span><div><strong style="color:#c9a96e;font-size:.88em">【{label}】</strong><span style="color:#9a8f85;font-size:.85em"> {desc}</span></div></div>' for icon,label,desc in features_list)

body_12 = f'''<div style="background:linear-gradient(135deg,rgba(120,0,0,.2),rgba(0,0,0,.5));border:2px solid rgba(201,169,110,.3);border-radius:12px;padding:24px;margin-bottom:24px;text-align:center">
  <h2 style="color:#c9a96e;margin:0 0 10px 0;font-size:1.5em;letter-spacing:3px;text-shadow:0 0 12px rgba(201,169,110,.4)">💰 全民發財：終結貧窮危機 💰</h2>
  <p style="color:#9a8f85;font-size:.9em;margin:0">聽見玩家的心聲！我們決定讓「金幣自由」不再是夢想。</p>
</div>'''

body_12 += f'''<div style="text-align:center;margin-bottom:24px;position:relative">
  <img src="{IMG_EXCHG}" style="width:100%;max-width:800px;border:2px solid rgba(201,169,110,.4);border-radius:12px;box-shadow:0 0 24px rgba(201,169,110,.25)">
  <div style="margin-top:14px;display:inline-block;background:linear-gradient(135deg,rgba(140,0,0,.6),rgba(80,0,0,.8));color:#fff;padding:10px 28px;border-radius:50px;border:2px solid #fff;font-weight:900;font-size:.9em;letter-spacing:1px;box-shadow:0 4px 12px rgba(0,0,0,.5)">💎 積少成多，穩定掉落 💎</div>
</div>'''

body_12 += f'''<div style="text-align:center;margin-bottom:20px">
  <h3 style="color:#c9a96e;font-size:1.1em;letter-spacing:2px;margin:0 0 6px 0">🛡️ 失傳祕寶：少了刀刃的武器</h3>
  <p style="color:#9a8f85;font-size:.88em;max-width:700px;margin:0 auto;line-height:1.8">
    還在為了升級技能、裝備強化的天幣不足而煩惱嗎？從今日起，大陸各處將出現失傳已久的軍資殘骸。賣給各地 NPC 商人即可獲得天幣，終結您的貧窮體感！
  </p>
</div>'''

body_12 += block('✔','掉落特點說明',(201,169,110), feat_html)

# ─── Image URLs ───────────────────────────────────────────────────────────────
IMGS = {
    3:  'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDgmoDV2tILLSGbFNqKngTHiNpP0BlAAIvDmsbb2ohVFKgsBoarPkwAQADAgADeQADOwQ.jpg',
    4:  'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDg2oDV3Y19i2kpzJDlL2uYGI7_qglAAIwDmsbb2ohVCAWLuQicDlAAQADAgADeQADOwQ.jpg',
    5:  'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDfmoDVyS9O3xry2dk3SI2Lkx-vpvMAAIrDmsbb2ohVP4AAaXGRKUq2gEAAwIAA3kAAzsE.jpg',
    6:  'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDfGoDVw9AZ_nYWUKAXC9AjHKCD9uzAAIpDmsbb2ohVDA6zq_6Y9rNAQADAgADeQADOwQ.jpg',
    7:  'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDhWoDV4V5UEjCyNnsZcHOetYNgaySAAIyDmsbb2ohVKimx6xDjX06AQADAgADeQADOwQ.jpg',
    8:  'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDe2oDVwABdWp7nAQC6iWw8-KuoPJgqAACKA5rG29qIVTDxFbiZr6oqAEAAwIAA3kAAzsE.jpg',
    9:  'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDemoDVvQyowTsRGc7ZDlV572SS6KJAAInDmsbb2ohVIswFPRAm6ILAQADAgADeQADOwQ.jpg',
    10: 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDgWoDV2PHE6IMuE7VdQxDDZqtGOP5AAIuDmsbb2ohVJKxCe4c66yuAQADAgADeQADOwQ.jpg',
    11: 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDgGoDV1sklC5ejNk-9i7wtWUdH205AAItDmsbb2ohVNf1R3HvZRkFAQADAgADeQADOwQ.jpg',
    12: 'https://telegraph-image-1n0.pages.dev/file/AgACAgUAAyEGAAS3SV8sAAIDfWoDVxvoiYathFFp060wA1jBUrrtAAIqDmsbb2ohVFTjFMKa7UAUAQADAgADeQADOwQ.jpg',
}

# Pages: (num, title, heading, body, prev, next, nav)
PAGES = [
    (3,  '職業之力介紹', '職業之力介紹',  body_03, 2,  4,  NAV_FEAT, '遊戲特色'),
    (4,  '戰馬雕像能力', '戰馬雕像能力',  body_04, 3,  5,  NAV_ITEM, '道具裝備'),
    (5,  '寵物系統介紹', '寵物系統介紹',  body_05, 4,  6,  NAV_FEAT, '遊戲特色'),
    (6,  '主線任務勳章', '主線任務勳章',  body_06, 5,  7,  NAV_ITEM, '道具裝備'),
    (7,  '威望系統',    '威望系統',      body_07, 6,  8,  NAV_FEAT, '遊戲特色'),
    (8,  '高寵介紹',    '高寵介紹',      body_08, 7,  9,  NAV_FEAT, '遊戲特色'),
    (9,  '在線禮包',    '在線禮包',      body_09, 8,  10, NAV_FEAT, '遊戲特色'),
    (10, '赫卡特介紹',  '赫卡特介紹',    body_10, 9,  11, NAV_ITEM, '道具裝備'),
    (11, '傲慢的掛飾',  '傲慢的掛飾',    body_11, 10, 12, NAV_ITEM, '道具裝備'),
    (12, '換金道具',    '換金道具',      body_12, 11, 1,  NAV_FEAT, '遊戲特色'),
]

for num, title, heading, body, prev_n, next_n, nav, cat in PAGES:
    html = page(num, title, heading, IMGS[num], body, prev_n, next_n, nav_html=nav, category=cat)
    fname = f'feature-{num:02d}.html'
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'OK {fname}')

print('Done!')
