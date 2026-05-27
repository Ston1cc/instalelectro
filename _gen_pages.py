import os

base = r'w:\website_projects\instalelectro'

# ─── SHARED COMPONENTS ──────────────────────────────────────────────────────

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config={{theme:{{extend:{{colors:{{primary:"#00254a","primary-dark":"#001a35",accent:"#0d6efd","accent-h":"#0a58ca",body:"#727272",dark:"#16171a",g1:"#f5f7fa"}},fontFamily:{{sans:["\\"DM Sans\\"","sans-serif"]}}}}}}}}
  </script>
  <style>
    *{{box-sizing:border-box;margin:0;padding:0}}
    html{{scroll-behavior:smooth}}
    body{{font-family:"DM Sans",sans-serif;color:#727272;background:#fff;overflow-x:hidden}}
    img{{max-width:100%}}a{{-webkit-tap-highlight-color:transparent}}
    .reveal{{opacity:0;transform:translateY(28px);transition:opacity .65s cubic-bezier(.4,0,.2,1),transform .65s cubic-bezier(.4,0,.2,1)}}
    .reveal.visible{{opacity:1;transform:none}}
    .dnav-link{{position:relative;font-size:.875rem;font-weight:500;color:rgba(255,255,255,.72);transition:color .2s;padding:4px 0}}
    .dnav-link::after{{content:"";position:absolute;bottom:-4px;left:0;width:0;height:2px;background:#0d6efd;transition:width .25s}}
    .dnav-link:hover,.dnav-link.active{{color:#fff}}
    .dnav-link:hover::after,.dnav-link.active::after{{width:100%}}
    .icon-circle{{width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 14px}}
    .stag{{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#0d6efd;margin-bottom:10px}}
    #mobile-menu{{max-height:0;overflow:hidden;transition:max-height .35s cubic-bezier(.4,0,.2,1)}}
    .mob-link{{display:flex;align-items:center;padding:.7rem .75rem;color:#495057;font-size:.875rem;font-weight:500;border-radius:4px;transition:background .15s,color .15s}}
    .mob-link:hover,.mob-link.active{{color:#00254a;background:#f5f7fa;font-weight:600}}
    @media(max-width:1023px){{body{{padding-bottom:68px}}}}
    .form-input{{width:100%;border:1.5px solid #e9ecef;border-radius:6px;padding:13px 16px;font-size:.875rem;font-family:"DM Sans",sans-serif;color:#16171a;transition:border-color .2s;outline:none}}
    .form-input:focus{{border-color:#0d6efd}}
    .form-input::placeholder{{color:#adb5bd}}
    .btn-p{{display:inline-flex;align-items:center;gap:8px;background:#00254a;color:#fff;font-weight:700;font-family:"DM Sans",sans-serif;padding:14px 28px;border-radius:6px;transition:background .2s;border:none;cursor:pointer;text-decoration:none;font-size:.875rem}}
    .btn-p:hover{{background:#001a35}}
    .btn-a{{display:inline-flex;align-items:center;gap:8px;background:#0d6efd;color:#fff;font-weight:700;font-family:"DM Sans",sans-serif;padding:14px 28px;border-radius:6px;transition:background .2s;text-decoration:none;font-size:.875rem}}
    .btn-a:hover{{background:#0a58ca}}
    .card-hover{{transition:transform .3s,box-shadow .3s}}
    .card-hover:hover{{transform:translateY(-4px);box-shadow:0 14px 44px rgba(0,37,74,.13)}}
    .page-hero{{padding:80px 0;background:#00254a;position:relative;overflow:hidden}}
    .page-hero::after{{content:"";position:absolute;inset:0;background:url('img/hero_img.jpg') center/cover no-repeat;opacity:.1;z-index:0}}
    .page-hero>*{{position:relative;z-index:1}}
  </style>
</head>
<body>
'''

def topbar():
    return '''<!-- TOP BAR -->
<div class="hidden sm:block" style="background:#00254a;border-bottom:1px solid rgba(255,255,255,.07)">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 flex items-center justify-between">
    <div class="flex items-center gap-5 text-xs" style="color:rgba(255,255,255,.65)">
      <a href="tel:+37368557199" class="flex items-center gap-1.5 hover:text-white transition-colors"><i class="fas fa-phone text-[10px]" style="color:#0d6efd"></i> +373 68 557 199</a>
      <a href="mailto:info@instalelectro.md" class="flex items-center gap-1.5 hover:text-white transition-colors"><i class="fas fa-envelope text-[10px]" style="color:#0d6efd"></i> info@instalelectro.md</a>
      <span class="hidden md:flex items-center gap-1.5"><i class="fas fa-location-dot text-[10px]" style="color:#0d6efd"></i> Bd. Mircea Costin 23, Chi&#537;in&#259;u</span>
    </div>
    <div class="flex items-center gap-3" style="color:rgba(255,255,255,.6)">
      <a href="#" class="hover:text-white transition-colors"><i class="fab fa-facebook-f text-xs"></i></a>
      <a href="#" class="hover:text-white transition-colors"><i class="fab fa-instagram text-xs"></i></a>
      <a href="#" class="hover:text-white transition-colors"><i class="fab fa-tiktok text-xs"></i></a>
    </div>
  </div>
</div>
'''

def nav(active):
    pages = [
        ('index.html',            'Acas&#259;'),
        ('despre.html',           'Despre'),
        ('servicii.html',         'Servicii'),
        ('servicii.html#preturi', 'Pre&#539;uri'),
        ('blog.html',             'Blog'),
        ('contact.html',          'Contact'),
    ]
    links = ''
    mob_links = ''
    for href, label in pages:
        is_active = ' active' if href == active or (active == 'servicii.html#preturi' and href == active) else ''
        links += f'<a href="{href}" class="dnav-link{is_active}">{label}</a>\n        '
        mob_links += f'<a href="{href}" class="mob-link{is_active}">{label}</a>\n        '
    return f'''<!-- NAV -->
<nav class="sticky top-0 z-50" style="background:#00254a;box-shadow:0 4px 24px rgba(0,37,74,.45)">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-[68px]">
      <a href="index.html" class="flex items-center gap-3 shrink-0">
        <img src="img/605603934_18090167021296504_5017235545341432250_n.jpg" alt="InstalElectro" class="h-11 w-auto">
        <span class="hidden sm:block font-bold text-white text-[17px]">Instal<span style="color:#0d6efd">Electro</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-7">
        {links}
      </div>
      <div class="hidden lg:flex items-center gap-2">
        <a href="contact.html" class="text-sm font-semibold border border-white/20 hover:border-white/50 hover:text-white px-5 py-2.5 rounded-md transition-all" style="color:rgba(255,255,255,.8)">Solicit&#259; ofert&#259;</a>
        <a href="tel:+37368557199" class="flex items-center gap-2 text-white text-sm font-bold px-5 py-2.5 rounded-md" style="background:#0d6efd"><i class="fas fa-phone text-xs"></i> APELA&#538;I</a>
      </div>
      <button id="burger" onclick="toggleMobileMenu()" class="lg:hidden text-white p-2 -mr-2" aria-label="Meniu">
        <i id="burger-icon" class="fas fa-bars text-xl"></i>
      </button>
    </div>
  </div>
  <div id="mobile-menu">
    <div style="background:#001a35;border-top:1px solid rgba(255,255,255,.08)" class="px-4 pt-3 pb-5">
      <div class="space-y-0.5 mb-4">
        {mob_links}
      </div>
      <div class="grid grid-cols-2 gap-2 pt-3" style="border-top:1px solid rgba(255,255,255,.08)">
        <a href="contact.html" class="flex items-center justify-center gap-2 text-white border border-white/25 text-sm font-semibold py-3 rounded-md"><i class="fas fa-envelope text-xs"></i> Ofert&#259;</a>
        <a href="tel:+37368557199" class="flex items-center justify-center gap-2 text-white text-sm font-bold py-3 rounded-md" style="background:#0d6efd"><i class="fas fa-phone text-xs"></i> Sun&#259; acum</a>
      </div>
    </div>
  </div>
</nav>
'''

def footer():
    return '''<!-- FOOTER -->
<footer style="background:#00254a">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
    <div class="grid md:grid-cols-12 gap-10">
      <div class="md:col-span-4">
        <div class="flex items-center gap-3 mb-4">
          <img src="img/605603934_18090167021296504_5017235545341432250_n.jpg" alt="InstalElectro" class="h-11 w-auto">
          <span class="font-bold text-white text-lg">Instal<span style="color:#0d6efd">Electro</span></span>
        </div>
        <p class="text-sm leading-relaxed mb-5" style="color:rgba(255,255,255,.55)">Servicii electrice profesioniste &icirc;n Chi&#537;in&#259;u &#537;i &icirc;mprejurimi. Calitate garantat&#259;, disponibilitate 24/7.</p>
        <div class="flex items-center gap-2.5">
          <a href="#" class="w-9 h-9 rounded-full flex items-center justify-center text-white text-sm" style="background:rgba(255,255,255,.1)"><i class="fab fa-facebook-f"></i></a>
          <a href="#" class="w-9 h-9 rounded-full flex items-center justify-center text-white text-sm" style="background:rgba(255,255,255,.1)"><i class="fab fa-instagram"></i></a>
          <a href="#" class="w-9 h-9 rounded-full flex items-center justify-center text-white text-sm" style="background:rgba(255,255,255,.1)"><i class="fab fa-tiktok"></i></a>
        </div>
      </div>
      <div class="md:col-span-2">
        <h4 class="font-bold text-white text-xs uppercase tracking-widest mb-5">Pagini</h4>
        <ul class="space-y-3">
          <li><a href="index.html"    class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Acas&#259;</a></li>
          <li><a href="despre.html"   class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Despre</a></li>
          <li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Servicii</a></li>
          <li><a href="blog.html"     class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Blog</a></li>
          <li><a href="contact.html"  class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Contact</a></li>
        </ul>
      </div>
      <div class="md:col-span-3">
        <h4 class="font-bold text-white text-xs uppercase tracking-widest mb-5">Servicii</h4>
        <ul class="space-y-3">
          <li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Instal&#259;ri electrice</a></li>
          <li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Repara&#539;ii electrice</a></li>
          <li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Panou electric</a></li>
          <li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Urgen&#539;e electrice 24/7</a></li>
          <li><a href="contact.html"  class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Consultan&#539;&#259; gratuit&#259;</a></li>
        </ul>
      </div>
      <div class="md:col-span-3">
        <h4 class="font-bold text-white text-xs uppercase tracking-widest mb-5">Contact</h4>
        <ul class="space-y-3.5">
          <li class="flex items-start gap-2.5"><i class="fas fa-phone text-xs mt-1 shrink-0" style="color:#0d6efd"></i><a href="tel:+37368557199" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">+373 68 557 199</a></li>
          <li class="flex items-start gap-2.5"><i class="fas fa-envelope text-xs mt-1 shrink-0" style="color:#0d6efd"></i><a href="mailto:info@instalelectro.md" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">info@instalelectro.md</a></li>
          <li class="flex items-start gap-2.5"><i class="fas fa-location-dot text-xs mt-1 shrink-0" style="color:#0d6efd"></i><div><p class="text-sm" style="color:rgba(255,255,255,.55)">Bd. Mircea Costin 23, Chi&#537;in&#259;u</p><p class="text-xs font-semibold mt-0.5" style="color:#0d6efd">Deserv&#259;m Chi&#537;in&#259;u &#537;i raza Chi&#537;in&#259;ului</p></div></li>
        </ul>
      </div>
    </div>
  </div>
  <div style="border-top:1px solid rgba(255,255,255,.08)">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 flex flex-col sm:flex-row items-center justify-between gap-3">
      <p class="text-xs" style="color:rgba(255,255,255,.35)">Copyright 2025 InstalElectro. Servicii electrice profesioniste &icirc;n Chi&#537;in&#259;u. Toate drepturile rezervate.</p>
      <a href="contact.html" class="text-xs font-semibold hover:text-white transition-colors" style="color:#0d6efd">Apeleaz&#259; pentru o problem&#259; electric&#259; &rarr;</a>
    </div>
  </div>
</footer>
'''

def floating_cta():
    return '''<!-- MOBILE FLOATING CTA -->
<div class="lg:hidden fixed bottom-0 inset-x-0 z-40 flex" style="box-shadow:0 -4px 24px rgba(0,0,0,.3)">
  <a href="tel:+37368557199" class="flex-1 flex items-center justify-center gap-2.5 text-white font-bold py-4 text-sm" style="background:#00254a"><i class="fas fa-phone"></i> Sun&#259; acum</a>
  <a href="contact.html" class="flex-1 flex items-center justify-center gap-2.5 text-white font-semibold py-4 text-sm" style="background:#0d6efd"><i class="fas fa-envelope"></i> Solicit&#259; ofert&#259;</a>
</div>
'''

def scripts():
    return '''<script>
  function toggleMobileMenu(){var m=document.getElementById('mobile-menu'),i=document.getElementById('burger-icon'),open=m.style.maxHeight&&m.style.maxHeight!=='0px';m.style.maxHeight=open?'0px':'520px';if(i)i.className=open?'fas fa-bars text-xl':'fas fa-times text-xl';}
  document.addEventListener('click',function(e){var m=document.getElementById('mobile-menu'),b=document.getElementById('burger');if(m&&b&&!b.contains(e.target)&&!m.contains(e.target)&&m.style.maxHeight!=='0px'){m.style.maxHeight='0px';var i=document.getElementById('burger-icon');if(i)i.className='fas fa-bars text-xl';}});
  var ro=new IntersectionObserver(function(e){e.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');ro.unobserve(e.target);}});},{threshold:.08,rootMargin:'0px 0px -40px 0px'});
  document.querySelectorAll('.reveal').forEach(function(el){ro.observe(el);});
</script>
</body></html>'''

# ─── DESPRE.HTML ─────────────────────────────────────────────────────────────

despre = head('InstalElectro &mdash; Despre Noi | Electricieni Autoriza&#539;i Chi&#537;in&#259;u',
              'Echipa InstalElectro &mdash; electricieni autorizati din Chisinau cu peste 10 ani experienta. Aflati mai mult despre noi.') + \
topbar() + nav('despre.html') + '''

<!-- PAGE HERO -->
<div class="page-hero">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="stag mb-2">ECHIPA NOASTR&#258;</p>
    <h1 class="text-3xl sm:text-5xl font-bold text-white mb-4">Despre InstalElectro</h1>
    <p class="text-white/65 text-base max-w-xl mx-auto">Echip&#259; de electricieni autoriza&#539;i din Chi&#537;in&#259;u cu experien&#539;&#259; vast&#259; &#537;i dedica&#539;i calit&#259;&#539;ii.</p>
    <div class="flex items-center justify-center gap-2 mt-5 text-sm" style="color:rgba(255,255,255,.5)">
      <a href="index.html" class="hover:text-white transition-colors">Acas&#259;</a>
      <i class="fas fa-chevron-right text-[10px]"></i>
      <span class="text-white">Despre</span>
    </div>
  </div>
</div>

<!-- STORY -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-2 gap-12 md:gap-16 items-center">
      <div class="relative reveal">
        <img src="img/SaveClip.App_686044914_18104045105296504_8299296285579802293_n.jpg" alt="Povestea InstalElectro" class="rounded-xl w-full object-cover shadow-xl" style="max-height:420px">
        <div class="absolute -bottom-4 -left-4 text-white rounded-xl px-6 py-4 shadow-xl" style="background:#0d6efd">
          <p class="text-2xl font-bold">10<span class="text-sm font-normal">+</span></p>
          <p class="text-xs font-medium opacity-90">Ani de experien&#539;&#259;</p>
        </div>
      </div>
      <div class="reveal">
        <span class="stag">POVESTEA NOASTR&#258;</span>
        <h2 class="text-3xl md:text-4xl font-bold leading-tight mt-2 mb-5" style="color:#00254a">De la pasiune la profesionism &mdash; 10 ani de servicii electrice &icirc;n Chi&#537;in&#259;u</h2>
        <p class="text-sm leading-relaxed mb-4" style="color:#727272">InstalElectro a luat na&#537;tere din dorin&#539;a de a oferi servicii electrice de calitate superioar&#259; &#537;i la pre&#539;uri accesibile cet&#259;&#539;enilor din Chi&#537;in&#259;u. &#206;n cei peste 10 ani de activitate, am deservit sute de clien&#539;i mul&#539;umi&#539;i.</p>
        <p class="text-sm leading-relaxed mb-6" style="color:#727272">Echipa noastr&#259; este format&#259; din electricieni autoriza&#539;i, cu preg&#259;tire continu&#259; &#537;i experien&#539;&#259; practic&#259; &icirc;n toate tipurile de instala&#539;ii electrice, de la renovare apartamente p&acirc;n&#259; la proiecte industriale complexe.</p>
        <div class="grid grid-cols-2 gap-4 mb-7">
          <div class="p-4 rounded-xl" style="background:#f5f7fa">
            <p class="text-3xl font-bold" style="color:#00254a">500<span style="color:#0d6efd">+</span></p>
            <p class="text-xs mt-1" style="color:#727272">Clien&#539;i mul&#539;umi&#539;i</p>
          </div>
          <div class="p-4 rounded-xl" style="background:#f5f7fa">
            <p class="text-3xl font-bold" style="color:#00254a">1200<span style="color:#0d6efd">+</span></p>
            <p class="text-xs mt-1" style="color:#727272">Lucr&#259;ri finalizate</p>
          </div>
        </div>
        <a href="contact.html" class="btn-a">Lucreaz&#259; cu noi <i class="fas fa-arrow-right text-sm"></i></a>
      </div>
    </div>
  </div>
</section>

<!-- STATS -->
<section class="py-16" style="background:#00254a">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
      <div class="reveal"><p class="text-5xl font-bold text-white">10<span style="color:#0d6efd">+</span></p><p class="text-sm mt-2" style="color:rgba(255,255,255,.6)">Ani experien&#539;&#259;</p></div>
      <div class="reveal"><p class="text-5xl font-bold text-white">500<span style="color:#0d6efd">+</span></p><p class="text-sm mt-2" style="color:rgba(255,255,255,.6)">Clien&#539;i mul&#539;umi&#539;i</p></div>
      <div class="reveal"><p class="text-5xl font-bold text-white">1200<span style="color:#0d6efd">+</span></p><p class="text-sm mt-2" style="color:rgba(255,255,255,.6)">Lucr&#259;ri finalizate</p></div>
      <div class="reveal"><p class="text-5xl font-bold text-white">24<span style="color:#0d6efd">/7</span></p><p class="text-sm mt-2" style="color:rgba(255,255,255,.6)">Disponibilitate</p></div>
    </div>
  </div>
</section>

<!-- VALUES -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 reveal">
      <span class="stag">VALORILE NOASTRE</span>
      <h2 class="text-3xl md:text-4xl font-bold leading-tight mt-2" style="color:#00254a">Ce ne diferen&#539;iaz&#259; de al&#539;i electricieni din Chi&#537;in&#259;u</h2>
    </div>
    <div class="grid md:grid-cols-3 gap-6">
      <div class="card-hover p-6 rounded-xl reveal" style="border:1px solid #f0f0f0">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-certificate text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-base mb-2 text-center" style="color:#00254a">Autoriza&#539;ie oficial&#259;</h3>
        <p class="text-xs leading-relaxed text-center" style="color:#727272">To&#539;i electricienii no&#537;tri sunt autoriza&#539;i ANRE &#537;i lucreaz&#259; conform normativelor &icirc;n vigoare.</p>
      </div>
      <div class="card-hover p-6 rounded-xl reveal" style="border:1px solid #f0f0f0">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-clock text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-base mb-2 text-center" style="color:#00254a">Punctualitate garantat&#259;</h3>
        <p class="text-xs leading-relaxed text-center" style="color:#727272">Respect&#259;m termenele stabilite. Dac&#259; &#238;nt&acirc;rziem, v&#259; oferim o reducere automat&#259;.</p>
      </div>
      <div class="card-hover p-6 rounded-xl reveal" style="border:1px solid #f0f0f0">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-shield-halved text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-base mb-2 text-center" style="color:#00254a">Garan&#539;ie 2 ani</h3>
        <p class="text-xs leading-relaxed text-center" style="color:#727272">Oferim garan&#539;ie de 2 ani pentru toate lucr&#259;rile electrice executate de echipa noastr&#259;.</p>
      </div>
      <div class="card-hover p-6 rounded-xl reveal" style="border:1px solid #f0f0f0">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-euro-sign text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-base mb-2 text-center" style="color:#00254a">Pre&#539;uri transparente</h3>
        <p class="text-xs leading-relaxed text-center" style="color:#727272">Estimare gratuit&#259; &#537;i pre&#539;uri fixe f&#259;r&#259; surprize. Ce stabilim, aceea pl&#259;te&#537;ti.</p>
      </div>
      <div class="card-hover p-6 rounded-xl reveal" style="border:1px solid #f0f0f0">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-tools text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-base mb-2 text-center" style="color:#00254a">Materiale premium</h3>
        <p class="text-xs leading-relaxed text-center" style="color:#727272">Folosim exclusiv materiale certificate, de la furnizori de &icirc;ncredere, pentru siguran&#539;a instala&#539;iei tale.</p>
      </div>
      <div class="card-hover p-6 rounded-xl reveal" style="border:1px solid #f0f0f0">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-headset text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-base mb-2 text-center" style="color:#00254a">Suport post-lucrare</h3>
        <p class="text-xs leading-relaxed text-center" style="color:#727272">Suntem disponibili dup&#259; finalizarea lucr&#259;rii pentru orice &icirc;ntreb&#259;ri sau ajust&#259;ri necesare.</p>
      </div>
    </div>
  </div>
</section>

<!-- TEAM -->
<section class="py-20" style="background:#f5f7fa">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 reveal">
      <span class="stag">ECHIPA NOASTR&#258;</span>
      <h2 class="text-3xl md:text-4xl font-bold leading-tight mt-2" style="color:#00254a">Electricienii care lucreaz&#259; pentru tine &icirc;n Chi&#537;in&#259;u</h2>
    </div>
    <div class="grid md:grid-cols-3 gap-6">
      <div class="card-hover bg-white rounded-xl overflow-hidden text-center reveal" style="border:1px solid #f0f0f0">
        <img src="img/hero_img.jpg" alt="Electrician InstalElectro" class="w-full h-56 object-cover">
        <div class="p-5">
          <h3 class="font-bold text-base mb-1" style="color:#00254a">Alexandru Popescu</h3>
          <p class="text-xs font-semibold mb-3" style="color:#0d6efd">Electrician &#537;ef autorizat</p>
          <p class="text-xs leading-relaxed" style="color:#727272">15 ani experien&#539;&#259; &icirc;n instala&#539;ii industriale &#537;i reziden&#539;iale. Specialist &icirc;n tablouri electrice.</p>
        </div>
      </div>
      <div class="card-hover bg-white rounded-xl overflow-hidden text-center reveal" style="border:1px solid #f0f0f0">
        <img src="img/SaveClip.App_686044914_18104045105296504_8299296285579802293_n.jpg" alt="Electrician InstalElectro" class="w-full h-56 object-cover">
        <div class="p-5">
          <h3 class="font-bold text-base mb-1" style="color:#00254a">Mihai Lungu</h3>
          <p class="text-xs font-semibold mb-3" style="color:#0d6efd">Electrician autorizat</p>
          <p class="text-xs leading-relaxed" style="color:#727272">Specialist &icirc;n montare re&#539;ele electrice, prize &#537;i instala&#539;ii de iluminat pentru apartamente.</p>
        </div>
      </div>
      <div class="card-hover bg-white rounded-xl overflow-hidden text-center reveal" style="border:1px solid #f0f0f0">
        <img src="img/teamofelectricians.jpg" alt="Echipa InstalElectro" class="w-full h-56 object-cover">
        <div class="p-5">
          <h3 class="font-bold text-base mb-1" style="color:#00254a">Ion &#536;tefan</h3>
          <p class="text-xs font-semibold mb-3" style="color:#0d6efd">Electrician urgente 24/7</p>
          <p class="text-xs leading-relaxed" style="color:#727272">Disponibil non-stop pentru interven&#539;ii de urgen&#539;&#259;. Timp mediu de r&#259;spuns: 45 minute.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA BANNER -->
<section class="py-16" style="background:#0d6efd">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
    <h2 class="text-3xl font-bold text-white mb-4">Ai nevoie de un electrician autorizat &icirc;n Chi&#537;in&#259;u?</h2>
    <p class="text-white/80 text-base mb-8">Sun&#259;-ne acum sau solicit&#259; o ofert&#259; gratuit&#259;. R&#259;spundem &icirc;n maxim 30 minute.</p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="tel:+37368557199" class="inline-flex items-center justify-center gap-2 bg-white font-bold px-8 py-4 rounded-md transition-all text-sm" style="color:#00254a"><i class="fas fa-phone"></i> +373 68 557 199</a>
      <a href="contact.html" class="inline-flex items-center justify-center gap-2 border border-white/30 hover:border-white text-white font-semibold px-8 py-4 rounded-md transition-all text-sm">Solicit&#259; ofert&#259; gratuit&#259; <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>
''' + footer() + floating_cta() + scripts()

# ─── SERVICII.HTML ───────────────────────────────────────────────────────────

servicii = head('InstalElectro &mdash; Servicii Electrice Chi&#537;in&#259;u | Tarife &#537;i Pre&#539;uri',
                'Servicii electrice complete in Chisinau: instalari, reparatii, panou electric, urgente 24/7. Preturi transparente, garantie 100%.') + \
topbar() + nav('servicii.html') + '''

<!-- PAGE HERO -->
<div class="page-hero">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="stag mb-2">SERVICII ELECTRICE</p>
    <h1 class="text-3xl sm:text-5xl font-bold text-white mb-4">Servicii &amp; Pre&#539;uri</h1>
    <p class="text-white/65 text-base max-w-xl mx-auto">Servicii electrice complete pentru locuin&#539;e &#537;i spa&#539;ii comerciale &icirc;n Chi&#537;in&#259;u. Pre&#539;uri transparente &#537;i garantate.</p>
    <div class="flex items-center justify-center gap-2 mt-5 text-sm" style="color:rgba(255,255,255,.5)">
      <a href="index.html" class="hover:text-white transition-colors">Acas&#259;</a>
      <i class="fas fa-chevron-right text-[10px]"></i>
      <span class="text-white">Servicii</span>
    </div>
  </div>
</div>

<!-- SERVICE 1 -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-2 gap-12 items-center">
      <div class="reveal">
        <img src="img/Electrical-Installation-services-1024x683.jpeg" alt="Instalari electrice Chisinau" class="rounded-xl shadow-lg w-full object-cover" style="max-height:380px">
      </div>
      <div class="reveal">
        <span class="stag">SERVICIUL 01</span>
        <h2 class="text-3xl font-bold leading-tight mt-2 mb-4" style="color:#00254a">Instal&#259;ri &amp; Repara&#539;ii Electrice Chi&#537;in&#259;u</h2>
        <p class="text-sm leading-relaxed mb-5" style="color:#727272">Oferim servicii complete de instalare &#537;i repara&#539;ii electrice pentru locuin&#539;e &#537;i spa&#539;ii comerciale. Echipa noastr&#259; autorizat&#259; asigur&#259; c&#259; fiecare lucrare respect&#259; standardele de siguran&#539;&#259;.</p>
        <ul class="space-y-2.5 mb-7">
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Montare prize &#537;i &icirc;ntrerup&#259;toare</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Instalare corpuri de iluminat &#537;i lustre</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Reparatii tablou electric</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Schimbare cabluri &#537;i conducte electrice</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Diagnoz&#259; &#537;i depanare instala&#539;ii</li>
        </ul>
        <a href="contact.html" class="btn-a">Solicit&#259; ofert&#259; <i class="fas fa-arrow-right text-sm"></i></a>
      </div>
    </div>
  </div>
</section>

<!-- SERVICE 2 -->
<section class="py-20" style="background:#f5f7fa">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-2 gap-12 items-center">
      <div class="md:order-2 reveal">
        <img src="img/Montarea Re&#x21b;elei Electrice Chi&#x219;in&#x103;u.webp" alt="Montarea retelei electrice" class="rounded-xl shadow-lg w-full object-cover" style="max-height:380px">
      </div>
      <div class="md:order-1 reveal">
        <span class="stag">SERVICIUL 02</span>
        <h2 class="text-3xl font-bold leading-tight mt-2 mb-4" style="color:#00254a">Montarea Re&#539;elei Electrice Chi&#537;in&#259;u</h2>
        <p class="text-sm leading-relaxed mb-5" style="color:#727272">Proiect&#259;m &#537;i instal&#259;m re&#539;ele electrice complete pentru apartamente, case &#537;i spa&#539;ii comerciale. Fiecare proiect este realizat conform planurilor tehnice &#537;i normelor &icirc;n vigoare.</p>
        <ul class="space-y-2.5 mb-7">
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Proiectare re&#539;ea electric&#259; complet&#259;</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Montare tablou electric &#537;i automatice</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Instalare cablu NYM, PVVG &#537;i NYY</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Racordare la re&#539;eaua electric&#259; public&#259;</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Eliberare documenta&#539;ie tehnic&#259;</li>
        </ul>
        <a href="contact.html" class="btn-a">Solicit&#259; ofert&#259; <i class="fas fa-arrow-right text-sm"></i></a>
      </div>
    </div>
  </div>
</section>

<!-- SERVICE 3 -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-2 gap-12 items-center">
      <div class="reveal">
        <img src="img/consulting.jpg" alt="Consultanta electrica" class="rounded-xl shadow-lg w-full object-cover" style="max-height:380px">
      </div>
      <div class="reveal">
        <span class="stag">SERVICIUL 03</span>
        <h2 class="text-3xl font-bold leading-tight mt-2 mb-4" style="color:#00254a">Consultan&#539;&#259; &#537;i Servicii Speciale Electrice</h2>
        <p class="text-sm leading-relaxed mb-5" style="color:#727272">Oferim consultan&#539;&#259; electric&#259; gratuit&#259; &#537;i solu&#539;ii personalizate pentru optimizarea instala&#539;iei electrice. Expertiza noastr&#259; v&#259; ajut&#259; s&#259; economisi&#539;i energie &#537;i bani.</p>
        <ul class="space-y-2.5 mb-7">
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Audit energetic &#537;i consultan&#539;&#259; gratuit&#259;</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Sisteme de automatizare cas&#259; inteligent&#259;</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Instalare generatoare &#537;i UPS</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Sisteme panouri solare fotovoltaice</li>
          <li class="flex items-center gap-2.5 text-sm" style="color:#727272"><i class="fas fa-circle-check text-sm shrink-0" style="color:#0d6efd"></i> Instalare sta&#539;ii &icirc;nc&#259;rcare vehicule electrice</li>
        </ul>
        <a href="contact.html" class="btn-a">Solicit&#259; consultan&#539;&#259; <i class="fas fa-arrow-right text-sm"></i></a>
      </div>
    </div>
  </div>
</section>

<!-- PRICING -->
<section id="preturi" class="py-20" style="background:#00254a">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 reveal">
      <span class="stag">TARIFE 2025</span>
      <h2 class="text-3xl md:text-4xl font-bold leading-tight mt-2 text-white">Pre&#539;uri orientative pentru servicii electrice &icirc;n Chi&#537;in&#259;u</h2>
      <p class="mt-3 text-sm" style="color:rgba(255,255,255,.6)">Estimare gratuit&#259; la domiciliu. Pre&#539;urile finale pot varia &icirc;n func&#539;ie de complexitatea lucr&#259;rii.</p>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
      <div class="card-hover bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-plug text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Montare priz&#259;</h4><p class="text-lg font-bold mb-1" style="color:#0d6efd">150+ MDL</p><p class="text-xs" style="color:#727272">per priz&#259; montat&#259;</p></div>
      <div class="card-hover bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-lightbulb text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Instalare lustr&#259;</h4><p class="text-lg font-bold mb-1" style="color:#0d6efd">200+ MDL</p><p class="text-xs" style="color:#727272">per corp de iluminat</p></div>
      <div class="card-hover bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-bolt text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Schimbare cablu</h4><p class="text-lg font-bold mb-1" style="color:#0d6efd">300+ MDL</p><p class="text-xs" style="color:#727272">per circuit</p></div>
      <div class="card-hover bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-screwdriver-wrench text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Panou electric</h4><p class="text-lg font-bold mb-1" style="color:#0d6efd">400+ MDL</p><p class="text-xs" style="color:#727272">reparatii &#537;i &icirc;nlocuiri</p></div>
      <div class="card-hover bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-home text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Re&#539;ea apartament</h4><p class="text-lg font-bold mb-1" style="color:#0d6efd">3000+ MDL</p><p class="text-xs" style="color:#727272">apartament 2 camere</p></div>
      <div class="card-hover bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-building text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Re&#539;ea cas&#259;</h4><p class="text-lg font-bold mb-1" style="color:#0d6efd">8000+ MDL</p><p class="text-xs" style="color:#727272">cas&#259; individual&#259;</p></div>
      <div class="card-hover bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-triangle-exclamation text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Urgen&#539;&#259; 24/7</h4><p class="text-lg font-bold mb-1" style="color:#0d6efd">500+ MDL</p><p class="text-xs" style="color:#727272">deplasare urgenta</p></div>
      <div class="card-hover bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-clipboard-check text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Consultan&#539;&#259;</h4><p class="text-lg font-bold mb-1" style="color:#0d6efd">GRATUIT</p><p class="text-xs" style="color:#727272">evaluare la domiciliu</p></div>
    </div>
    <p class="text-center text-sm mt-4 reveal" style="color:rgba(255,255,255,.6)"><i class="fas fa-circle-check mr-1.5" style="color:#0d6efd"></i>Pre&#539;urile sunt orientative. Contacta&#539;i-ne pentru o estimare exact&#259; gratuit&#259;.</p>
  </div>
</section>

<!-- FAQ -->
<section class="py-20 bg-white">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 reveal">
      <span class="stag">&#206;NTREB&#258;RI FRECVENTE</span>
      <h2 class="text-3xl md:text-4xl font-bold leading-tight mt-2" style="color:#00254a">&#206;ntreb&#259;ri despre serviciile electrice &icirc;n Chi&#537;in&#259;u</h2>
    </div>
    <div class="space-y-3 reveal">
      <details class="border rounded-xl overflow-hidden" style="border-color:#e9ecef">
        <summary class="px-6 py-4 font-semibold cursor-pointer flex items-center justify-between" style="color:#00254a;list-style:none">
          Oferi&#539;i garan&#539;ie pentru lucr&#259;rile electrice?
          <i class="fas fa-chevron-down text-xs" style="color:#0d6efd"></i>
        </summary>
        <div class="px-6 pb-5 text-sm leading-relaxed" style="color:#727272">Da, oferim garan&#539;ie de 2 ani pentru toate lucr&#259;rile executate. &Icirc;n caz de probleme ap&#259;rute &icirc;n perioada de garan&#539;ie, intervenim gratuit.</div>
      </details>
      <details class="border rounded-xl overflow-hidden" style="border-color:#e9ecef">
        <summary class="px-6 py-4 font-semibold cursor-pointer flex items-center justify-between" style="color:#00254a;list-style:none">
          C&acirc;t dureaz&#259; o evaluare gratuit&#259;?
          <i class="fas fa-chevron-down text-xs" style="color:#0d6efd"></i>
        </summary>
        <div class="px-6 pb-5 text-sm leading-relaxed" style="color:#727272">Evaluarea la domiciliu dureaz&#259; de obicei 30-60 minute, &icirc;n func&#539;ie de complexitatea proiectului. Electricianul nostru va examina instala&#539;ia &#537;i va oferi o estimare de pre&#539; pe loc.</div>
      </details>
      <details class="border rounded-xl overflow-hidden" style="border-color:#e9ecef">
        <summary class="px-6 py-4 font-semibold cursor-pointer flex items-center justify-between" style="color:#00254a;list-style:none">
          Lucra&#539;i &#537;i &icirc;n weekend sau noapte?
          <i class="fas fa-chevron-down text-xs" style="color:#0d6efd"></i>
        </summary>
        <div class="px-6 pb-5 text-sm leading-relaxed" style="color:#727272">Da! Suntem disponibili 24/7 pentru urgen&#539;e electrice, inclusiv &icirc;n weekend &#537;i s&#259;rb&#259;tori. Pentru lucr&#259;ri planificate &icirc;n afara orelor de program, rugam s&#259; contacta&#539;i cu 24h &icirc;nainte.</div>
      </details>
      <details class="border rounded-xl overflow-hidden" style="border-color:#e9ecef">
        <summary class="px-6 py-4 font-semibold cursor-pointer flex items-center justify-between" style="color:#00254a;list-style:none">
          Deservi&#539;i &#537;i localit&#259;&#539;ile din afara Chi&#537;in&#259;ului?
          <i class="fas fa-chevron-down text-xs" style="color:#0d6efd"></i>
        </summary>
        <div class="px-6 pb-5 text-sm leading-relaxed" style="color:#727272">Deserv&#259;m Chi&#537;in&#259;ul &#537;i raza Chi&#537;in&#259;ului, incluz&acirc;nd localit&#259;&#539;ile din &#238;mprejurimi. Pentru localit&#259;&#539;i mai &icirc;ndep&#259;rtate, contacta&#539;i-ne pentru detalii despre disponibilitate &#537;i costuri de deplasare.</div>
      </details>
      <details class="border rounded-xl overflow-hidden" style="border-color:#e9ecef">
        <summary class="px-6 py-4 font-semibold cursor-pointer flex items-center justify-between" style="color:#00254a;list-style:none">
          Ce materiale folosesc electricienii vo&#537;tri?
          <i class="fas fa-chevron-down text-xs" style="color:#0d6efd"></i>
        </summary>
        <div class="px-6 pb-5 text-sm leading-relaxed" style="color:#727272">Folosim exclusiv materiale certificate de la furnizori verifica&#539;i: cabluri NYM, prize &#537;i &icirc;ntrerup&#259;toare Legrand, Schneider, ABB. Toate materialele vin cu certific&#259;ri de calitate &#537;i siguran&#539;&#259;.</div>
      </details>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="py-16" style="background:#0d6efd">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
    <h2 class="text-3xl font-bold text-white mb-4">Solicita&#539;i o estimare gratuit&#259; acum</h2>
    <p class="text-white/80 text-base mb-8">Complete&#539;i formularul sau suna&#539;i direct. R&#259;spundem &icirc;n maxim 30 minute.</p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="tel:+37368557199" class="inline-flex items-center justify-center gap-2 bg-white font-bold px-8 py-4 rounded-md text-sm" style="color:#00254a"><i class="fas fa-phone"></i> +373 68 557 199</a>
      <a href="contact.html" class="inline-flex items-center justify-center gap-2 border border-white/30 hover:border-white text-white font-semibold px-8 py-4 rounded-md text-sm">Formular ofert&#259; <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>
''' + footer() + floating_cta() + scripts()

# ─── BLOG.HTML ───────────────────────────────────────────────────────────────

blog_posts = [
    ('img/factura electrica.webp',  'Sfaturi', 'Cum s&#259; &icirc;&#539;i reduci factura electric&#259; &icirc;n 2025', 'Sfaturi practice &#537;i solu&#539;ii simple pentru reducerea consumului de energie electric&#259; acas&#259;.', '15 Mai 2025'),
    ('img/energieeficienta.webp',   'Eficien&#539;&#259;', 'Sisteme de iluminat LED &mdash; investi&#539;ie sau cost?', 'Analiz&#259; complet&#259; a eficien&#539;ei sistemelor LED fa&#539;&#259; de sursele clasice de iluminat.', '8 Mai 2025'),
    ('img/Electrical-Installation-services-1024x683.jpeg', 'Ghid', 'Semne c&#259; instala&#539;ia electric&#259; trebuie verificat&#259; urgent', 'Cum recuno&#537;ti problemele electrice &icirc;nainte s&#259; devin&#259; periculoase pentru familia ta.', '1 Mai 2025'),
    ('img/SaveClip.App_686044914_18104045105296504_8299296285579802293_n.jpg', 'Nout&#259;&#539;i', 'InstalElectro &mdash; 10 ani de servicii electrice &icirc;n Chi&#537;in&#259;u', 'Povestea echipei InstalElectro &#537;i cum am crescut &icirc;mpreun&#259; cu clien&#539;ii no&#537;tri.', '20 Aprilie 2025'),
    ('img/hero_img.jpg',            'Sfaturi', 'Cum s&#259; alegi un electrician autorizat &icirc;n Chi&#537;in&#259;u', 'Ghid complet pentru g&#259;sirea unui electrician de &icirc;ncredere &icirc;n Chi&#537;in&#259;u.', '10 Aprilie 2025'),
    ('img/consulting.jpg',          'Tehnologie', 'Casa inteligent&#259; &mdash; cum automatizezi instala&#539;ia electric&#259;', 'Solu&#539;ii Smart Home pentru locuin&#539;a ta din Chi&#537;in&#259;u la pre&#539;uri accesibile.', '2 Aprilie 2025'),
]

blog_cards = ''
for img, cat, title, desc, date in blog_posts:
    blog_cards += f'''
      <article class="bg-white rounded-xl overflow-hidden reveal" style="border:1px solid #f0f0f0;transition:transform .3s,box-shadow .3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 14px 44px rgba(0,0,0,.09)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
        <div class="overflow-hidden h-48"><img src="{img}" alt="{title}" class="w-full h-full object-cover" style="transition:transform .5s" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform=''"></div>
        <div class="p-5">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold uppercase tracking-widest" style="color:#0d6efd">{cat}</span>
            <span class="text-[11px]" style="color:#adb5bd">{date}</span>
          </div>
          <h3 class="font-bold text-[15px] mb-2 leading-snug" style="color:#00254a">{title}</h3>
          <p class="text-xs leading-relaxed mb-4" style="color:#727272">{desc}</p>
          <a href="#" class="inline-flex items-center gap-1.5 text-xs font-bold" style="color:#0d6efd">Cite&#537;te articolul <i class="fas fa-arrow-right text-[10px]"></i></a>
        </div>
      </article>'''

blog = head('InstalElectro &mdash; Blog | Stiri si Sfaturi Electrice Chisinau',
            'Blog InstalElectro: sfaturi electrice, ghiduri, noutati si articole despre servicii electrice in Chisinau.') + \
topbar() + nav('blog.html') + f'''

<!-- PAGE HERO -->
<div class="page-hero">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="stag mb-2">ARTICOLE &#536;I &#536;TIRI</p>
    <h1 class="text-3xl sm:text-5xl font-bold text-white mb-4">Blog InstalElectro</h1>
    <p class="text-white/65 text-base max-w-xl mx-auto">Sfaturi practice, ghiduri &#537;i nout&#259;&#539;i din lumea serviciilor electrice din Chi&#537;in&#259;u.</p>
    <div class="flex items-center justify-center gap-2 mt-5 text-sm" style="color:rgba(255,255,255,.5)">
      <a href="index.html" class="hover:text-white transition-colors">Acas&#259;</a>
      <i class="fas fa-chevron-right text-[10px]"></i>
      <span class="text-white">Blog</span>
    </div>
  </div>
</div>

<!-- FEATURED POST -->
<section class="py-14" style="background:#f5f7fa">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-white rounded-xl overflow-hidden reveal" style="border:1px solid #f0f0f0">
      <div class="md:flex">
        <div class="md:w-1/2 overflow-hidden" style="max-height:360px">
          <img src="img/SaveClip.App_705988781_18106225730296504_6646898435395370222_n.jpg" alt="InstalElectro featured" class="w-full h-full object-cover">
        </div>
        <div class="md:w-1/2 p-8 md:p-10 flex flex-col justify-center">
          <span class="text-[11px] font-bold uppercase tracking-widest mb-3 block" style="color:#0d6efd">ARTICOL PRINCIPAL</span>
          <h2 class="text-2xl md:text-3xl font-bold leading-tight mb-4" style="color:#00254a">Ghid complet pentru renovarea instala&#539;iei electrice &icirc;n apartament &icirc;n 2025</h2>
          <p class="text-sm leading-relaxed mb-6" style="color:#727272">Tot ce trebuie s&#259; &#537;tii despre renovarea instala&#539;iei electrice: de la planificare &#537;i buget, p&acirc;n&#259; la materiale &#537;i ce s&#259; ceri electricianului.</p>
          <div class="flex items-center gap-4 mb-6 text-xs" style="color:#adb5bd">
            <span><i class="fas fa-calendar mr-1.5"></i> 20 Mai 2025</span>
            <span><i class="fas fa-clock mr-1.5"></i> 8 min citire</span>
          </div>
          <a href="#" class="btn-p self-start">Cite&#537;te articolul <i class="fas fa-arrow-right text-sm"></i></a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- BLOG GRID -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between mb-10 reveal">
      <h2 class="text-2xl font-bold" style="color:#00254a">Toate articolele</h2>
      <div class="flex gap-2 flex-wrap">
        <button class="text-xs font-semibold px-4 py-2 rounded-full text-white" style="background:#00254a">Toate</button>
        <button class="text-xs font-semibold px-4 py-2 rounded-full border hover:bg-gray-50 transition-colors" style="color:#727272;border-color:#e9ecef">Sfaturi</button>
        <button class="text-xs font-semibold px-4 py-2 rounded-full border hover:bg-gray-50 transition-colors" style="color:#727272;border-color:#e9ecef">Ghiduri</button>
        <button class="text-xs font-semibold px-4 py-2 rounded-full border hover:bg-gray-50 transition-colors" style="color:#727272;border-color:#e9ecef">Nout&#259;&#539;i</button>
      </div>
    </div>
    <div class="grid md:grid-cols-3 gap-6">
      {blog_cards}
    </div>
    <div class="flex items-center justify-center gap-2 mt-12 reveal">
      <button class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm text-white" style="background:#00254a">1</button>
      <button class="w-10 h-10 rounded-full flex items-center justify-center font-semibold text-sm border hover:bg-gray-50 transition-colors" style="color:#727272;border-color:#e9ecef">2</button>
      <button class="w-10 h-10 rounded-full flex items-center justify-center font-semibold text-sm border hover:bg-gray-50 transition-colors" style="color:#727272;border-color:#e9ecef"><i class="fas fa-chevron-right text-xs"></i></button>
    </div>
  </div>
</section>
''' + footer() + floating_cta() + scripts()

# ─── CONTACT.HTML ─────────────────────────────────────────────────────────────

contact = head('InstalElectro &mdash; Contact | Electricieni Chi&#537;in&#259;u +373 68 557 199',
               'Contactati InstalElectro pentru servicii electrice in Chisinau. Tel: +373 68 557 199. Raspundem in 30 minute.') + \
topbar() + nav('contact.html') + '''

<!-- PAGE HERO -->
<div class="page-hero">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="stag mb-2">SUNTEM AICI PENTRU TINE</p>
    <h1 class="text-3xl sm:text-5xl font-bold text-white mb-4">Contact InstalElectro</h1>
    <p class="text-white/65 text-base max-w-xl mx-auto">Contacta&#539;i-ne oricand pentru o estimare gratuit&#259; sau o urgen&#539;&#259; electric&#259; &icirc;n Chi&#537;in&#259;u.</p>
    <div class="flex items-center justify-center gap-2 mt-5 text-sm" style="color:rgba(255,255,255,.5)">
      <a href="index.html" class="hover:text-white transition-colors">Acas&#259;</a>
      <i class="fas fa-chevron-right text-[10px]"></i>
      <span class="text-white">Contact</span>
    </div>
  </div>
</div>

<!-- QUICK CONTACT CARDS -->
<section class="py-14" style="background:#f5f7fa">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-3 gap-5">
      <div class="card-hover bg-white rounded-xl p-6 text-center reveal" style="border:1px solid #f0f0f0">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-phone text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-base mb-2" style="color:#00254a">Telefon</h3>
        <a href="tel:+37368557199" class="text-sm font-semibold block mb-1" style="color:#0d6efd">+373 68 557 199</a>
        <p class="text-xs" style="color:#727272">Disponibil 24/7 pentru urgen&#539;e</p>
      </div>
      <div class="card-hover bg-white rounded-xl p-6 text-center reveal" style="border:1px solid #f0f0f0">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-envelope text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-base mb-2" style="color:#00254a">Email</h3>
        <a href="mailto:info@instalelectro.md" class="text-sm font-semibold block mb-1" style="color:#0d6efd">info@instalelectro.md</a>
        <p class="text-xs" style="color:#727272">R&#259;spundem &icirc;n maxim 2 ore</p>
      </div>
      <div class="card-hover bg-white rounded-xl p-6 text-center reveal" style="border:1px solid #f0f0f0">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-location-dot text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-base mb-2" style="color:#00254a">Adres&#259;</h3>
        <p class="text-sm font-semibold mb-1" style="color:#0d6efd">Bd. Mircea Costin 23</p>
        <p class="text-xs" style="color:#727272">Deserv&#259;m Chi&#537;in&#259;u &#537;i raza Chi&#537;in&#259;ului</p>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT FORM + INFO -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-12 gap-12">

      <!-- INFO -->
      <div class="md:col-span-4 reveal">
        <span class="stag">TRIMITE-NE UN MESAJ</span>
        <h2 class="text-2xl font-bold mt-2 mb-3 leading-snug" style="color:#00254a">Descrie&#539;i problema electric&#259; &mdash; V&#259; contact&#259;m imediat</h2>
        <p class="text-sm leading-relaxed mb-7" style="color:#727272">Completa&#539;i formularul &#537;i un electrician autorizat v&#259; va contacta &icirc;n maxim 30 minute pentru a stabili detaliile &#537;i o estimare gratuit&#259;.</p>
        <div class="space-y-5 mb-8">
          <div class="flex items-start gap-3.5">
            <div class="w-11 h-11 rounded-full flex items-center justify-center shrink-0" style="background:rgba(13,110,253,.1)"><i class="fas fa-phone text-sm" style="color:#0d6efd"></i></div>
            <div><p class="font-semibold text-sm mb-0.5" style="color:#00254a">Telefon</p><a href="tel:+37368557199" class="text-sm" style="color:#727272">+373 68 557 199</a></div>
          </div>
          <div class="flex items-start gap-3.5">
            <div class="w-11 h-11 rounded-full flex items-center justify-center shrink-0" style="background:rgba(13,110,253,.1)"><i class="fas fa-envelope text-sm" style="color:#0d6efd"></i></div>
            <div><p class="font-semibold text-sm mb-0.5" style="color:#00254a">Email</p><a href="mailto:info@instalelectro.md" class="text-sm" style="color:#727272">info@instalelectro.md</a></div>
          </div>
          <div class="flex items-start gap-3.5">
            <div class="w-11 h-11 rounded-full flex items-center justify-center shrink-0" style="background:rgba(13,110,253,.1)"><i class="fas fa-location-dot text-sm" style="color:#0d6efd"></i></div>
            <div><p class="font-semibold text-sm mb-0.5" style="color:#00254a">Adres&#259;</p><p class="text-sm" style="color:#727272">Bd. Mircea Costin 23, Chi&#537;in&#259;u</p><p class="text-xs font-semibold mt-0.5" style="color:#0d6efd">Deserv&#259;m Chi&#537;in&#259;u &#537;i raza Chi&#537;in&#259;ului</p></div>
          </div>
          <div class="flex items-start gap-3.5">
            <div class="w-11 h-11 rounded-full flex items-center justify-center shrink-0" style="background:rgba(13,110,253,.1)"><i class="fas fa-clock text-sm" style="color:#0d6efd"></i></div>
            <div><p class="font-semibold text-sm mb-0.5" style="color:#00254a">Program</p><p class="text-sm" style="color:#727272">Lun&ndash;Dum: 08:00&ndash;22:00</p><p class="text-xs font-semibold mt-0.5" style="color:#0d6efd">Urgen&#539;e: 24/7</p></div>
          </div>
        </div>
        <div class="flex items-center gap-2.5">
          <a href="#" class="w-10 h-10 rounded-full flex items-center justify-center text-white text-sm" style="background:#00254a"><i class="fab fa-facebook-f"></i></a>
          <a href="#" class="w-10 h-10 rounded-full flex items-center justify-center text-white text-sm" style="background:#00254a"><i class="fab fa-instagram"></i></a>
          <a href="#" class="w-10 h-10 rounded-full flex items-center justify-center text-white text-sm" style="background:#00254a"><i class="fab fa-tiktok"></i></a>
        </div>
      </div>

      <!-- FORM -->
      <div class="md:col-span-8 reveal">
        <div class="bg-white rounded-xl p-8" style="border:1.5px solid #e9ecef">
          <h3 class="text-xl font-bold mb-6" style="color:#00254a">Solicit&#259; ofert&#259; gratuit&#259;</h3>
          <form class="space-y-4" onsubmit="return false">
            <div class="grid md:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-semibold mb-1.5" style="color:#00254a">Numele dvs. *</label>
                <input type="text" placeholder="Ion Popescu" class="form-input">
              </div>
              <div>
                <label class="block text-xs font-semibold mb-1.5" style="color:#00254a">Telefon *</label>
                <input type="tel" placeholder="+373 68 000 000" class="form-input">
              </div>
            </div>
            <div>
              <label class="block text-xs font-semibold mb-1.5" style="color:#00254a">Email</label>
              <input type="email" placeholder="email@exemplu.md" class="form-input">
            </div>
            <div>
              <label class="block text-xs font-semibold mb-1.5" style="color:#00254a">Tipul serviciului</label>
              <select class="form-input" style="cursor:pointer">
                <option value="">Selecta&#539;i tipul serviciului</option>
                <option>Instalare/reparatie prize &amp; &icirc;ntrerup&#259;toare</option>
                <option>Montare tablou electric</option>
                <option>Re&#539;ea electric&#259; complet&#259;</option>
                <option>Urgen&#539;&#259; electric&#259; 24/7</option>
                <option>Consultan&#539;&#259; gratuit&#259;</option>
                <option>Alt serviciu</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-semibold mb-1.5" style="color:#00254a">Descriere problem&#259; sau lucrare</label>
              <textarea rows="4" placeholder="Descrie&#539;i problema sau lucrarea electric&#259; de care ave&#539;i nevoie..." class="form-input" style="resize:none"></textarea>
            </div>
            <button type="submit" class="btn-p w-full justify-center uppercase tracking-wide">
              <i class="fas fa-paper-plane text-sm"></i> Trimite Solicitarea
            </button>
            <p class="text-center text-xs" style="color:#adb5bd">R&#259;spundem &icirc;n maxim 30 minute. Datele dvs. sunt confiden&#539;iale.</p>
          </form>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- MAP PLACEHOLDER -->
<section class="bg-white pb-20">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="rounded-xl overflow-hidden reveal" style="height:320px;background:#f5f7fa;border:1.5px solid #e9ecef;display:flex;align-items:center;justify-content:center">
      <div class="text-center">
        <div class="icon-circle mx-auto" style="background:rgba(13,110,253,.1)"><i class="fas fa-map-location-dot text-3xl" style="color:#0d6efd"></i></div>
        <p class="font-bold mt-2" style="color:#00254a">Bd. Mircea Costin 23, Chi&#537;in&#259;u</p>
        <p class="text-sm mt-1" style="color:#727272">Deserv&#259;m Chi&#537;in&#259;u &#537;i raza Chi&#537;in&#259;ului</p>
        <a href="https://maps.google.com/?q=Chisinau+Moldova" target="_blank" class="inline-flex items-center gap-2 mt-4 btn-a text-sm py-2.5 px-5">
          <i class="fas fa-map-marker-alt"></i> Deschide &icirc;n Google Maps
        </a>
      </div>
    </div>
  </div>
</section>
''' + footer() + floating_cta() + scripts()

# ─── WRITE ALL FILES ─────────────────────────────────────────────────────────

pages = {
    'despre.html':   despre,
    'servicii.html': servicii,
    'blog.html':     blog,
    'contact.html':  contact,
}

for fname, content in pages.items():
    path = os.path.join(base, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  {fname}: {len(content):,} chars")

print("\nAll pages written.")
