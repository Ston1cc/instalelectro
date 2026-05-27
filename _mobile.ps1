# InstalElectro — Mobile-first patch
$base = "w:\website_projects\instalelectro"
$enc  = [System.Text.UTF8Encoding]::new($false)

# ══════════════════════════════════════════════════════════════════════════════
# SHARED SNIPPETS
# ══════════════════════════════════════════════════════════════════════════════

$mobileCss = @'

    /* ── Mobile / Global ── */
    html { scroll-behavior: smooth; }
    body { overflow-x: hidden; }
    a, button { -webkit-tap-highlight-color: transparent; }
    img { max-width: 100%; }
    @media (max-width: 1023px) {
      body { padding-bottom: 68px; }   /* room for floating CTA */
    }
'@

$mobileMenu = @'

  <!-- ░░ MOBILE MENU ░░ -->
  <div id="mobile-menu" class="lg:hidden overflow-hidden" style="max-height:0;transition:max-height .35s cubic-bezier(.4,0,.2,1);">
    <div style="background:#0e1c2e;border-top:1px solid rgba(255,255,255,.08);" class="px-5 pt-3 pb-5">
      <div class="space-y-0.5 mb-4" id="mobile-links">
        <a href="index.html"          class="mob-link">Acasă</a>
        <a href="despre.html"         class="mob-link">Despre</a>
        <a href="servicii.html"       class="mob-link">Servicii</a>
        <a href="servicii.html#preturi" class="mob-link">Prețuri</a>
        <a href="blog.html"           class="mob-link">Blog</a>
        <a href="contact.html"        class="mob-link">Contact</a>
      </div>
      <div class="grid grid-cols-2 gap-3 pt-4" style="border-top:1px solid rgba(255,255,255,.08);">
        <a href="contact.html" class="flex items-center justify-center gap-2 text-white text-xs font-semibold py-3.5 rounded-sm" style="border:1px solid rgba(255,255,255,.25);">
          <i class="fas fa-envelope text-xs"></i> Solicită ofertă
        </a>
        <a href="tel:+37368557199" class="flex items-center justify-center gap-2 bg-red-600 text-white text-xs font-bold py-3.5 rounded-sm hover:bg-red-700">
          <i class="fas fa-phone text-xs"></i> Sună acum
        </a>
      </div>
    </div>
  </div>
  <style>
    .mob-link { display:flex; align-items:center; padding:.75rem .75rem; color:#d1d5db; font-size:.875rem; font-weight:500; border-radius:2px; transition:background .15s,color .15s; }
    .mob-link:hover, .mob-link.active { color:#fff; background:rgba(255,255,255,.07); }
  </style>
  <script>
  // Mobile menu toggle
  function toggleMobileMenu() {
    var m=document.getElementById('mobile-menu');
    var i=document.getElementById('burger-icon');
    var open = m.style.maxHeight && m.style.maxHeight !== '0px';
    m.style.maxHeight = open ? '0px' : '520px';
    if(i){ i.className = open ? 'fas fa-bars text-xl' : 'fas fa-times text-xl'; }
  }
  // Close on outside click
  document.addEventListener('click',function(e){
    var m=document.getElementById('mobile-menu');
    var b=document.getElementById('burger');
    if(m && b && !b.contains(e.target) && !m.contains(e.target) && m.style.maxHeight!=='0px'){
      m.style.maxHeight='0px';
      var i=document.getElementById('burger-icon');
      if(i) i.className='fas fa-bars text-xl';
    }
  });
  // Highlight active link
  (function(){
    var p=location.pathname.split('/').pop()||'index.html';
    document.querySelectorAll('.mob-link').forEach(function(a){
      if(a.getAttribute('href')===p || (p==='' && a.getAttribute('href')==='index.html')) a.classList.add('active');
    });
  })();
  </script>
'@

$floatingCta = @'

  <!-- ░░ MOBILE FLOATING CTA ░░ -->
  <div class="lg:hidden fixed bottom-0 inset-x-0 z-40 flex" style="box-shadow:0 -4px 24px rgba(0,0,0,.35);">
    <a href="tel:+37368557199"
       class="flex-1 flex items-center justify-center gap-2.5 bg-red-600 text-white font-bold py-4 text-sm active:bg-red-700"
       style="letter-spacing:.04em;">
      <svg width="17" height="17" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
      Sună acum
    </a>
    <a href="contact.html"
       class="flex-1 flex items-center justify-center gap-2.5 text-white font-semibold py-4 text-sm active:opacity-80"
       style="background:#1a2535;border-left:1px solid rgba(255,255,255,.12);">
      <svg width="17" height="17" fill="currentColor" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
      Solicită ofertă
    </a>
  </div>
'@

# ══════════════════════════════════════════════════════════════════════════════
# APPLY TO ALL FILES
# ══════════════════════════════════════════════════════════════════════════════

foreach ($f in (Get-ChildItem "$base\*.html")) {
    $c = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)

    # 1. Add mobile CSS (before </style>)
    if ($c -notmatch 'overflow-x: hidden') {
        $c = $c -replace '</style>', ($mobileCss + "`n  </style>")
    }

    # 2. Hide top bar on mobile
    $c = $c.Replace(
        '<div class="bg-navy-950 text-gray-400 text-xs py-2 border-b border-white/5">',
        '<div class="hidden sm:block bg-navy-950 text-gray-400 text-xs py-2 border-b border-white/5">')

    # 3. Update burger button with id + onclick
    $c = $c.Replace(
        '<button class="lg:hidden text-white p-2 -mr-2">
          <i class="fas fa-bars text-xl"></i>',
        '<button id="burger" onclick="toggleMobileMenu()" class="lg:hidden text-white p-2 -mr-2" aria-label="Meniu">
          <i id="burger-icon" class="fas fa-bars text-xl"></i>')

    # Also handle index.html variant (has extra comment inside)
    $c = $c.Replace(
        '<button class="lg:hidden text-white p-2 -mr-2">
          <i class="fas fa-bars text-xl"></i>
        </button>',
        '<button id="burger" onclick="toggleMobileMenu()" class="lg:hidden text-white p-2 -mr-2" aria-label="Meniu">
          <i id="burger-icon" class="fas fa-bars text-xl"></i>
        </button>')

    # 4. Inject mobile menu after </nav>
    if ($c -notmatch 'mobile-menu') {
        $c = $c.Replace('</nav>', '</nav>' + $mobileMenu)
    }

    # 5. Inject floating CTA before </body>
    if ($c -notmatch 'MOBILE FLOATING CTA') {
        $c = $c.Replace('</body>', $floatingCta + "`n</body>")
    }

    [System.IO.File]::WriteAllText($f.FullName, $c, $enc)
    Write-Host "  [mobile] $($f.Name)"
}

# ══════════════════════════════════════════════════════════════════════════════
# INDEX.HTML — extra mobile improvements
# ══════════════════════════════════════════════════════════════════════════════

$idx = "$base\index.html"
$c   = [System.IO.File]::ReadAllText($idx, [System.Text.Encoding]::UTF8)

# Hero heading: scale down on mobile
$c = $c.Replace(
    'class="text-5xl md:text-6xl font-bold text-white leading-[1.08] mb-6"',
    'class="text-[2rem] sm:text-4xl md:text-5xl lg:text-6xl font-bold text-white leading-[1.1] mb-5"')

# Hero paragraph: smaller on mobile
$c = $c.Replace(
    'class="text-gray-300 text-lg leading-relaxed mb-10 max-w-lg"',
    'class="text-gray-300 text-base leading-relaxed mb-8 max-w-lg"')

# Hero buttons: column on mobile, row on sm+
$c = $c.Replace(
    'class="flex flex-wrap gap-4"',
    'class="flex flex-col sm:flex-row gap-3"')

# About: tighten gap on mobile
$c = $c.Replace(
    'class="grid md:grid-cols-2 gap-16 items-center"',
    'class="grid md:grid-cols-2 gap-10 md:gap-16 items-center"')

# About badge: avoid going off-screen on small devices
$c = $c.Replace(
    'class="absolute -bottom-5 -left-5 bg-red-600',
    'class="absolute -bottom-4 -left-4 sm:-bottom-5 sm:-left-5 bg-red-600')

# Emergency cards: 2 cols on mobile instead of 1
$c = $c.Replace(
    'class="grid md:grid-cols-4 gap-6"',
    'class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6"')

# Section padding: reduce on mobile
$c = $c.Replace('class="py-24 bg-white"',   'class="py-14 md:py-24 bg-white"')
$c = $c.Replace('class="py-24 bg-gray-50"', 'class="py-14 md:py-24 bg-gray-50"')
$c = $c.Replace('class="py-24 bg-navy-800"','class="py-14 md:py-24 bg-navy-800"')

# Section heading: scale on mobile
$c = $c.Replace(
    'class="text-4xl font-bold text-gray-900 max-w-2xl mx-auto leading-tight"',
    'class="text-2xl sm:text-3xl md:text-4xl font-bold text-gray-900 max-w-2xl mx-auto leading-tight"')

[System.IO.File]::WriteAllText($idx, $c, $enc)
Write-Host "  [index-mobile-extra] index.html"

# ══════════════════════════════════════════════════════════════════════════════
# SERVICII.HTML — mobile layout tweaks
# ══════════════════════════════════════════════════════════════════════════════

$srv = "$base\servicii.html"
$c   = [System.IO.File]::ReadAllText($srv, [System.Text.Encoding]::UTF8)

$c = $c.Replace('class="py-24 bg-white"',   'class="py-14 md:py-24 bg-white"')
$c = $c.Replace('class="py-24 bg-gray-50"', 'class="py-14 md:py-24 bg-gray-50"')
$c = $c.Replace('class="py-24 bg-navy-800"','class="py-14 md:py-24 bg-navy-800"')
$c = $c.Replace(
    'class="text-4xl font-bold text-gray-900 max-w-2xl mx-auto leading-tight"',
    'class="text-2xl sm:text-3xl md:text-4xl font-bold text-gray-900 max-w-2xl mx-auto leading-tight"')
$c = $c.Replace(
    'class="text-3xl font-bold text-gray-900 mb-4"',
    'class="text-2xl md:text-3xl font-bold text-gray-900 mb-4"')
$c = $c.Replace(
    'class="grid md:grid-cols-2 gap-12 items-center mb-20"',
    'class="grid md:grid-cols-2 gap-8 md:gap-12 items-center mb-12 md:mb-20"')

[System.IO.File]::WriteAllText($srv, $c, $enc)
Write-Host "  [svc-mobile] servicii.html"

# ══════════════════════════════════════════════════════════════════════════════
# DESPRE.HTML — mobile tweaks
# ══════════════════════════════════════════════════════════════════════════════

$dsp = "$base\despre.html"
$c   = [System.IO.File]::ReadAllText($dsp, [System.Text.Encoding]::UTF8)

$c = $c.Replace('class="py-24 bg-white"',   'class="py-14 md:py-24 bg-white"')
$c = $c.Replace('class="py-24 bg-gray-50"', 'class="py-14 md:py-24 bg-gray-50"')
$c = $c.Replace(
    'class="grid md:grid-cols-2 gap-16 items-center"',
    'class="grid md:grid-cols-2 gap-10 md:gap-16 items-center"')
$c = $c.Replace(
    'class="text-4xl font-bold text-gray-900 leading-tight mb-6"',
    'class="text-2xl sm:text-3xl md:text-4xl font-bold text-gray-900 leading-tight mb-6"')

[System.IO.File]::WriteAllText($dsp, $c, $enc)
Write-Host "  [dsp-mobile] despre.html"

# ══════════════════════════════════════════════════════════════════════════════
# BLOG.HTML — mobile tweaks
# ══════════════════════════════════════════════════════════════════════════════

$blg = "$base\blog.html"
$c   = [System.IO.File]::ReadAllText($blg, [System.Text.Encoding]::UTF8)

$c = $c.Replace('class="py-24 bg-gray-50"', 'class="py-14 md:py-24 bg-gray-50"')
# Featured post: stack on mobile
$c = $c.Replace(
    'class="md:flex"',
    'class="md:flex flex-col"')

[System.IO.File]::WriteAllText($blg, $c, $enc)
Write-Host "  [blg-mobile] blog.html"

# ══════════════════════════════════════════════════════════════════════════════
# CONTACT.HTML — mobile tweaks
# ══════════════════════════════════════════════════════════════════════════════

$cnt = "$base\contact.html"
$c   = [System.IO.File]::ReadAllText($cnt, [System.Text.Encoding]::UTF8)

$c = $c.Replace('class="py-24 bg-gray-50"', 'class="py-14 md:py-24 bg-gray-50"')
$c = $c.Replace('class="py-20 bg-white"',   'class="py-12 md:py-20 bg-white"')

[System.IO.File]::WriteAllText($cnt, $c, $enc)
Write-Host "  [cnt-mobile] contact.html"

Write-Host "`n✅ Mobile patch complete."
