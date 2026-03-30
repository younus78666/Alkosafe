"""Inject off-canvas mobile menu into all HTML pages."""
import os

OC_CSS = """/* Off-Canvas Menu */
.mob-toggle{display:none;background:none;border:none;cursor:pointer;padding:8px}
.mob-toggle .ico{width:24px;height:24px;stroke:var(--g8)}
.oc-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:199;opacity:0;visibility:hidden;transition:all .3s}
.oc-overlay.open{opacity:1;visibility:visible}
.oc-panel{position:fixed;top:0;right:0;width:300px;height:100%;background:var(--w);z-index:200;transform:translateX(100%);transition:transform .3s ease;box-shadow:-4px 0 24px rgba(0,0,0,.1);display:flex;flex-direction:column;overflow-y:auto}
.oc-panel.open{transform:translateX(0)}
.oc-header{display:flex;align-items:center;justify-content:space-between;padding:20px 24px;border-bottom:1px solid var(--g2)}
.oc-logo{display:flex;align-items:center;gap:10px}
.oc-logo img{height:28px}
.oc-logo span{font-family:var(--fd);font-size:15px;font-weight:700;color:var(--b8)}
.oc-logo span em{font-style:normal;color:var(--gd)}
.oc-close{background:none;border:none;cursor:pointer;padding:8px}
.oc-close .ico{width:24px;height:24px;stroke:var(--g8)}
.oc-nav{display:flex;flex-direction:column;padding:16px 0}
.oc-nav a{display:block;padding:14px 24px;font-family:var(--fd);font-size:14px;font-weight:500;color:var(--g8);text-decoration:none;border-bottom:1px solid var(--g1);transition:background .2s;letter-spacing:.02em}
.oc-nav a:hover{background:var(--g0);color:var(--b6)}
.oc-footer{padding:20px 24px;margin-top:auto;border-top:1px solid var(--g2)}
.oc-lang{display:flex;gap:2px;margin-bottom:16px;font-size:13px;font-weight:600;border:1px solid var(--g2);border-radius:6px;overflow:hidden}
.oc-lang a{flex:1;text-align:center;padding:8px;text-decoration:none;color:var(--g6);transition:all .2s}
.oc-lang a.active{background:var(--b7);color:var(--w)}
.oc-cta{display:block;width:100%;padding:14px;background:var(--gd);color:var(--b9);font-family:var(--fd);font-size:15px;font-weight:700;text-align:center;text-decoration:none;border-radius:8px;letter-spacing:.02em;transition:background .2s}
.oc-cta:hover{background:var(--gl)}
body.oc-open{overflow:hidden}"""

EN_OC_HTML = """<!-- Off-Canvas Menu -->
<div class="oc-overlay" id="oc-overlay" onclick="closeMenu()"></div>
<div class="oc-panel" id="oc-panel">
  <div class="oc-header">
    <div class="oc-logo"><img src="/images/logo.png" alt="CROM TEST"><span>Alko<em>Safe</em></span></div>
    <button class="oc-close" onclick="closeMenu()"><svg class="ico" viewBox="0 0 24 24" stroke="currentColor" fill="none" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
  </div>
  <nav class="oc-nav">
    <a href="/en/how-it-works/">How It Works</a>
    <a href="/en/compliance/">Certifications</a>
    <a href="/en/about/">About</a>
    <a href="/en/contact/">Contact</a>
  </nav>
  <div class="oc-footer">
    <div class="oc-lang"><a href="/en/" class="active">EN</a><a href="/tr/">TR</a></div>
    <a href="/en/shop" class="oc-cta">Buy Now</a>
  </div>
</div>"""

TR_OC_HTML = """<!-- Off-Canvas Menu -->
<div class="oc-overlay" id="oc-overlay" onclick="closeMenu()"></div>
<div class="oc-panel" id="oc-panel">
  <div class="oc-header">
    <div class="oc-logo"><img src="/images/logo.png" alt="CROM TEST"><span>Alko<em>Safe</em></span></div>
    <button class="oc-close" onclick="closeMenu()"><svg class="ico" viewBox="0 0 24 24" stroke="currentColor" fill="none" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
  </div>
  <nav class="oc-nav">
    <a href="/tr/nasil-calisir/">Nasil Calisir</a>
    <a href="/tr/sertifikalar/">Sertifikalar</a>
    <a href="/tr/hakkimizda/">Hakkimizda</a>
    <a href="/tr/iletisim/">Iletisim</a>
  </nav>
  <div class="oc-footer">
    <div class="oc-lang"><a href="/en/">EN</a><a href="/tr/" class="active">TR</a></div>
    <a href="/en/shop" class="oc-cta">Hemen Al</a>
  </div>
</div>"""

HAMBURGER = '<button class="mob-toggle" onclick="openMenu()" aria-label="Open menu"><svg class="ico" viewBox="0 0 24 24" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round"><path d="M3 12h18M3 6h18M3 18h18"/></svg></button>'

OC_JS = """function openMenu(){document.getElementById('oc-overlay').classList.add('open');document.getElementById('oc-panel').classList.add('open');document.body.classList.add('oc-open')}
function closeMenu(){document.getElementById('oc-overlay').classList.remove('open');document.getElementById('oc-panel').classList.remove('open');document.body.classList.remove('oc-open')}"""

EN_FILES = [
    'en/about.html', 'en/compliance.html', 'en/contact.html',
    'en/cookie-policy.html', 'en/disclaimer.html', 'en/how-it-works.html',
    'en/privacy-policy.html', 'en/product/alkosafe-saliva-alcohol-test.html',
    'en/refund-policy.html', 'en/shipping-policy.html', 'en/terms-and-conditions.html'
]

TR_FILES = [
    'tr/index.html', 'tr/hakkimizda.html', 'tr/iletisim.html',
    'tr/nasil-calisir.html', 'tr/sertifikalar.html', 'tr/urun/alkosafe-tukuruk-alkol-testi.html'
]


def inject(filepath, oc_html):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'oc-overlay' in content:
        print(f'  SKIP (already done): {filepath}')
        return

    # 1. Inject CSS before first @media or </style>
    idx = content.find('@media')
    if idx != -1:
        content = content[:idx] + OC_CSS + '\n' + content[idx:]
    else:
        content = content.replace('</style>', OC_CSS + '\n</style>')

    # 2. Add .mob-toggle{display:block} in 1024px media query
    if '.mob-toggle{display:block}' not in content:
        content = content.replace('.nav{display:none}', '.nav{display:none}\n  .mob-toggle{display:block}')

    # 3. Add hamburger button after </nav> in header
    # Find the first </nav> and insert after it
    nav_end = content.find('</nav>')
    if nav_end != -1:
        insert_pos = nav_end + len('</nav>')
        content = content[:insert_pos] + '\n  ' + HAMBURGER + content[insert_pos:]

    # 4. Add off-canvas HTML before </body>
    content = content.replace('</body>', oc_html + '\n</body>')

    # 5. Add JS
    if 'openMenu' not in content:
        last_script = content.rfind('</script>')
        if last_script != -1:
            content = content[:last_script] + '\n' + OC_JS + '\n' + content[last_script:]
        else:
            content = content.replace('</body>', '<script>\n' + OC_JS + '\n</script>\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  DONE: {filepath}')


print('EN pages:')
for f in EN_FILES:
    inject(f, EN_OC_HTML)

print('\nTR pages:')
for f in TR_FILES:
    inject(f, TR_OC_HTML)

print('\nAll pages updated!')
