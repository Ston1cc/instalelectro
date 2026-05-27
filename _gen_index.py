
html = open('index.html', encoding='utf-8').read()
# We'll overwrite with new content
pass

content = '''<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>InstalElectro &mdash; Servicii Electrice Profesioniste &icirc;n Chi&#537;in&#259;u</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config={theme:{extend:{colors:{primary:"#00254a","primary-dark":"#001a35",accent:"#0d6efd","accent-h":"#0a58ca",body:"#727272",dark:"#16171a",g1:"#f5f7fa"},fontFamily:{sans:["\\"DM Sans\\"","sans-serif"]}}}}
  </script>
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    html{scroll-behavior:smooth}
    body{font-family:"DM Sans",sans-serif;color:#727272;background:#fff;overflow-x:hidden}
    img{max-width:100%}a{-webkit-tap-highlight-color:transparent}
    .reveal{opacity:0;transform:translateY(28px);transition:opacity .65s cubic-bezier(.4,0,.2,1),transform .65s cubic-bezier(.4,0,.2,1)}
    .reveal.visible{opacity:1;transform:none}
    .dnav-link{position:relative;font-size:.875rem;font-weight:500;color:rgba(255,255,255,.72);transition:color .2s;padding:4px 0}
    .dnav-link::after{content:"";position:absolute;bottom:-4px;left:0;width:0;height:2px;background:#0d6efd;transition:width .25s}
    .dnav-link:hover,.dnav-link.active{color:#fff}
    .dnav-link:hover::after,.dnav-link.active::after{width:100%}
    .hero-swiper{height:620px}
    @media(max-width:767px){.hero-swiper{height:500px}}
    .swiper-slide{position:relative}
    .slide-bg{position:absolute;inset:0;background-size:cover;background-position:center}
    .slide-overlay{position:absolute;inset:0;background:linear-gradient(105deg,rgba(0,37,74,.88) 45%,rgba(0,37,74,.42) 100%)}
    .slide-content{position:relative;z-index:2;height:100%;display:flex;align-items:center}
    .swiper-button-next,.swiper-button-prev{width:48px;height:48px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);border-radius:50%;color:#fff;transition:background .2s}
    .swiper-button-next:hover,.swiper-button-prev:hover{background:rgba(13,110,253,.75)}
    .swiper-button-next::after,.swiper-button-prev::after{font-size:14px;font-weight:800}
    .swiper-pagination-bullet{background:#fff;opacity:.5}
    .swiper-pagination-bullet-active{opacity:1;background:#0d6efd}
    .feat-card{transition:transform .3s,box-shadow .3s}
    .feat-card:hover{transform:translateY(-5px);box-shadow:0 16px 48px rgba(0,37,74,.12)}
    .svc-card{border:1px solid #f0f0f0;transition:box-shadow .3s}
    .svc-card:hover{box-shadow:0 12px 40px rgba(0,37,74,.13)}
    .svc-card .svc-img img{transition:transform .5s;width:100%;height:100%;object-fit:cover}
    .svc-card:hover .svc-img img{transform:scale(1.06)}
    .price-card{transition:transform .3s,box-shadow .3s}
    .price-card:hover{transform:translateY(-4px);box-shadow:0 12px 40px rgba(0,37,74,.14)}
    .blog-card{border:1px solid #f0f0f0;transition:transform .3s,box-shadow .3s}
    .blog-card:hover{transform:translateY(-5px);box-shadow:0 16px 48px rgba(0,0,0,.09)}
    .blog-card .blog-img img{transition:transform .5s;width:100%;height:100%;object-fit:cover}
    .blog-card:hover .blog-img img{transform:scale(1.06)}
    .testi-card{background:#fff;border-radius:10px;padding:28px;box-shadow:0 2px 20px rgba(0,0,0,.06);transition:box-shadow .3s}
    .testi-card:hover{box-shadow:0 10px 40px rgba(0,0,0,.12)}
    .icon-circle{width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px}
    .stag{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#0d6efd;margin-bottom:10px}
    #mobile-menu{max-height:0;overflow:hidden;transition:max-height .35s cubic-bezier(.4,0,.2,1)}
    .mob-link{display:flex;align-items:center;padding:.7rem .75rem;color:#495057;font-size:.875rem;font-weight:500;border-radius:4px;transition:background .15s,color .15s}
    .mob-link:hover,.mob-link.active{color:#00254a;background:#f5f7fa;font-weight:600}
    @media(max-width:1023px){body{padding-bottom:68px}}
    .form-input{width:100%;border:1.5px solid #e9ecef;border-radius:6px;padding:13px 16px;font-size:.875rem;font-family:"DM Sans",sans-serif;color:#16171a;transition:border-color .2s;outline:none}
    .form-input:focus{border-color:#0d6efd}
    .form-input::placeholder{color:#adb5bd}
    .btn-p{display:inline-flex;align-items:center;gap:8px;background:#00254a;color:#fff;font-weight:700;font-family:"DM Sans",sans-serif;padding:14px 28px;border-radius:6px;transition:background .2s;border:none;cursor:pointer;text-decoration:none;font-size:.875rem}
    .btn-p:hover{background:#001a35}
    .btn-a{display:inline-flex;align-items:center;gap:8px;background:#0d6efd;color:#fff;font-weight:700;font-family:"DM Sans",sans-serif;padding:14px 28px;border-radius:6px;transition:background .2s;text-decoration:none;font-size:.875rem}
    .btn-a:hover{background:#0a58ca}
  </style>
</head>
<body>

<!-- TOP BAR -->
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

<!-- NAV -->
<nav class="sticky top-0 z-50" style="background:#00254a;box-shadow:0 4px 24px rgba(0,37,74,.45)">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-[68px]">
      <a href="index.html" class="flex items-center gap-3 shrink-0">
        <img src="img/605603934_18090167021296504_5017235545341432250_n.jpg" alt="InstalElectro" class="h-11 w-auto">
        <span class="hidden sm:block font-bold text-white text-[17px]">Instal<span style="color:#0d6efd">Electro</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-7">
        <a href="index.html"            class="dnav-link active">Acas&#259;</a>
        <a href="despre.html"           class="dnav-link">Despre</a>
        <a href="servicii.html"         class="dnav-link">Servicii</a>
        <a href="servicii.html#preturi" class="dnav-link">Pre&#539;uri</a>
        <a href="blog.html"             class="dnav-link">Blog</a>
        <a href="contact.html"          class="dnav-link">Contact</a>
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
        <a href="index.html"            class="mob-link active">Acas&#259;</a>
        <a href="despre.html"           class="mob-link">Despre</a>
        <a href="servicii.html"         class="mob-link">Servicii</a>
        <a href="servicii.html#preturi" class="mob-link">Pre&#539;uri</a>
        <a href="blog.html"             class="mob-link">Blog</a>
        <a href="contact.html"          class="mob-link">Contact</a>
      </div>
      <div class="grid grid-cols-2 gap-2 pt-3" style="border-top:1px solid rgba(255,255,255,.08)">
        <a href="contact.html" class="flex items-center justify-center gap-2 text-white border border-white/25 text-sm font-semibold py-3 rounded-md"><i class="fas fa-envelope text-xs"></i> Ofert&#259;</a>
        <a href="tel:+37368557199" class="flex items-center justify-center gap-2 text-white text-sm font-bold py-3 rounded-md" style="background:#0d6efd"><i class="fas fa-phone text-xs"></i> Sun&#259; acum</a>
      </div>
    </div>
  </div>
</nav>

<!-- HERO -->
<section class="hero-swiper swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <div class="slide-bg" style="background-image:url(\'img/hero_img.jpg\')"></div>
      <div class="slide-overlay"></div>
      <div class="slide-content">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
          <div class="max-w-2xl">
            <p class="stag mb-3">ELECTRIC CHI&#536;IN&#258;U &mdash; PENTRU CASA TA</p>
            <h1 class="text-[2.1rem] sm:text-5xl lg:text-[3.4rem] font-bold text-white leading-[1.1] mb-6">Solu&#539;ii Electrice de <span style="color:#0d6efd">&#206;ncredere</span> &icirc;n Chi&#537;in&#259;u</h1>
            <p class="text-base sm:text-lg leading-relaxed mb-8 max-w-lg" style="color:rgba(255,255,255,.7)">Instal&#259;ri, repara&#539;ii &#537;i urgen&#539;e electrice &icirc;n Chi&#537;in&#259;u. Echip&#259; autorizat&#259;, garan&#539;ie 100%, disponibili 24/7.</p>
            <div class="flex flex-col sm:flex-row gap-3">
              <a href="tel:+37368557199" class="btn-a justify-center"><i class="fas fa-phone text-sm"></i> APELA&#538;I ACUM</a>
              <a href="servicii.html" class="inline-flex items-center justify-center gap-2 border border-white/30 hover:border-white text-white font-semibold px-7 py-3.5 rounded-md transition-all text-sm">Serviciile noastre <i class="fas fa-arrow-right text-sm"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="swiper-slide">
      <div class="slide-bg" style="background-image:url(\'img/teamofelectricians.jpg\')"></div>
      <div class="slide-overlay"></div>
      <div class="slide-content">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
          <div class="max-w-2xl">
            <p class="stag mb-3">ECHIP&#258; AUTORIZAT&#258; CHI&#536;IN&#258;U</p>
            <h1 class="text-[2.1rem] sm:text-5xl lg:text-[3.4rem] font-bold text-white leading-[1.1] mb-6">Exper&#539;i &icirc;n Instala&#539;ii &#537;i Repara&#539;ii Electrice</h1>
            <p class="text-base leading-relaxed mb-8 max-w-lg" style="color:rgba(255,255,255,.7)">Profesioni&#537;ti cu experien&#539;&#259; &icirc;n modernizarea &#537;i &icirc;ntre&#539;inerea instala&#539;iilor electrice.</p>
            <a href="contact.html" class="btn-a">Solicit&#259; ofert&#259; gratuit&#259; <i class="fas fa-arrow-right text-sm"></i></a>
          </div>
        </div>
      </div>
    </div>
    <div class="swiper-slide">
      <div class="slide-bg" style="background-image:url(\'img/Electrical-Installation-services-1024x683.jpeg\')"></div>
      <div class="slide-overlay"></div>
      <div class="slide-content">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
          <div class="max-w-2xl">
            <p class="stag mb-3">URGEN&#538;E 24/7</p>
            <h1 class="text-[2.1rem] sm:text-5xl lg:text-[3.4rem] font-bold text-white leading-[1.1] mb-6">Interven&#539;ii Rapide pentru Orice Problem&#259; Electric&#259;</h1>
            <p class="text-base leading-relaxed mb-8 max-w-lg" style="color:rgba(255,255,255,.7)">Disponibili non-stop pentru urgen&#539;e electrice. Timp de r&#259;spuns garantat &icirc;n Chi&#537;in&#259;u.</p>
            <a href="tel:+37368557199" class="btn-a"><i class="fas fa-phone"></i> +373 68 557 199</a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
  <div class="swiper-pagination" style="bottom:20px"></div>
</section>

<!-- FEATURES -->
<section class="py-14" style="background:#f5f7fa">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-5">
      <div class="feat-card bg-white rounded-xl p-6 text-center reveal">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-tag text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-[15px] mb-2" style="color:#00254a">Pre&#539;uri accesibile</h3>
        <p class="text-xs leading-relaxed" style="color:#727272">Oferte competitive &#537;i transparente pentru orice tip de lucrare</p>
      </div>
      <div class="feat-card bg-white rounded-xl p-6 text-center reveal">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-shield-halved text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-[15px] mb-2" style="color:#00254a">Garan&#539;ie 100%</h3>
        <p class="text-xs leading-relaxed" style="color:#727272">Toate lucr&#259;rile sunt garantate &#537;i certificate oficial</p>
      </div>
      <div class="feat-card rounded-xl p-6 text-center reveal" style="background:#00254a">
        <div class="icon-circle" style="background:rgba(255,255,255,.12)"><i class="fas fa-clock text-2xl text-white"></i></div>
        <h3 class="font-bold text-[15px] mb-2 text-white">Disponibil 24/7</h3>
        <p class="text-xs leading-relaxed" style="color:rgba(255,255,255,.65)">Interven&#539;ii de urgen&#539;&#259; &icirc;n orice moment al zilei</p>
      </div>
      <div class="feat-card bg-white rounded-xl p-6 text-center reveal">
        <div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-star text-2xl" style="color:#0d6efd"></i></div>
        <h3 class="font-bold text-[15px] mb-2" style="color:#00254a">Calitate &icirc;nalt&#259;</h3>
        <p class="text-xs leading-relaxed" style="color:#727272">Materiale premium &#537;i execu&#539;ie profesionist&#259; garantat&#259;</p>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 reveal">
      <span class="stag">SERVICII ELECTRICE CHI&#536;IN&#258;U</span>
      <h2 class="text-3xl md:text-4xl font-bold leading-tight max-w-2xl mx-auto mt-2" style="color:#00254a">Montaj electric, repara&#539;ii electrice &#537;i moderniz&#259;ri electrice &icirc;n Chi&#537;in&#259;u</h2>
    </div>
    <div class="grid md:grid-cols-3 gap-6">
      <div class="svc-card bg-white rounded-xl overflow-hidden reveal">
        <div class="svc-img h-52 overflow-hidden"><img src="img/Electrical-Installation-services-1024x683.jpeg" alt="Instalari electrice"></div>
        <div class="p-6">
          <h3 class="font-bold text-lg mb-3 leading-snug" style="color:#00254a">Instal&#259;ri &amp; Repara&#539;ii Electrice Chi&#537;in&#259;u</h3>
          <p class="text-sm leading-relaxed mb-5" style="color:#727272">Servicii complete de instalare &#537;i repara&#539;ii electrice pentru locuin&#539;e &#537;i spa&#539;ii comerciale din Chi&#537;in&#259;u.</p>
          <a href="servicii.html" class="inline-flex items-center gap-2 font-semibold text-sm" style="color:#0d6efd">Detalii <i class="fas fa-arrow-right text-xs"></i></a>
        </div>
      </div>
      <div class="svc-card bg-white rounded-xl overflow-hidden reveal">
        <div class="svc-img h-52 overflow-hidden"><img src="img/Montarea Re&#x21b;elei Electrice Chi&#x219;in&#x103;u.webp" alt="Montarea retelei"></div>
        <div class="p-6">
          <h3 class="font-bold text-lg mb-3 leading-snug" style="color:#00254a">Montarea Re&#539;elei Electrice Chi&#537;in&#259;u</h3>
          <p class="text-sm leading-relaxed mb-5" style="color:#727272">Proiect&#259;m &#537;i instal&#259;m re&#539;ele electrice complete, respect&acirc;nd toate normele &#537;i standardele de siguran&#539;&#259;.</p>
          <a href="servicii.html" class="inline-flex items-center gap-2 font-semibold text-sm" style="color:#0d6efd">Detalii <i class="fas fa-arrow-right text-xs"></i></a>
        </div>
      </div>
      <div class="svc-card bg-white rounded-xl overflow-hidden reveal">
        <div class="svc-img h-52 overflow-hidden"><img src="img/consulting.jpg" alt="Consultanta electrica"></div>
        <div class="p-6">
          <h3 class="font-bold text-lg mb-3 leading-snug" style="color:#00254a">Consultan&#539;&#259; &#537;i Servicii Speciale Electrice</h3>
          <p class="text-sm leading-relaxed mb-5" style="color:#727272">Consultan&#539;&#259; electric&#259; specializat&#259; &#537;i solu&#539;ii personalizate adaptate nevoilor fiec&#259;rui client.</p>
          <a href="servicii.html" class="inline-flex items-center gap-2 font-semibold text-sm" style="color:#0d6efd">Detalii <i class="fas fa-arrow-right text-xs"></i></a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ABOUT DARK -->
<section class="py-20" style="background:#00254a">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-2 gap-12 md:gap-16 items-center">
      <div class="reveal">
        <span class="stag">DESPRE NOI</span>
        <h2 class="text-3xl md:text-4xl font-bold text-white leading-tight mt-2 mb-5">Peste 10 ani de experien&#539;&#259; &icirc;n servicii electrice &icirc;n Chi&#537;in&#259;u</h2>
        <p class="text-base leading-relaxed mb-6" style="color:rgba(255,255,255,.65)">InstalElectro este echipa de electricieni autoriza&#539;i din Chi&#537;in&#259;u cu experien&#539;&#259; vast&#259; &icirc;n instal&#259;ri, repara&#539;ii &#537;i urgen&#539;e electrice. Lucr&#259;m cu materiale certificate &#537;i respect&#259;m toate standardele de siguran&#539;&#259;.</p>
        <div class="grid grid-cols-3 gap-6 mb-8">
          <div><p class="text-4xl font-bold text-white">10<span style="color:#0d6efd">+</span></p><p class="text-sm mt-1" style="color:rgba(255,255,255,.6)">Ani experien&#539;&#259;</p></div>
          <div><p class="text-4xl font-bold text-white">500<span style="color:#0d6efd">+</span></p><p class="text-sm mt-1" style="color:rgba(255,255,255,.6)">Clien&#539;i mul&#539;umi&#539;i</p></div>
          <div><p class="text-4xl font-bold text-white">24<span style="color:#0d6efd">/7</span></p><p class="text-sm mt-1" style="color:rgba(255,255,255,.6)">Disponibilitate</p></div>
        </div>
        <a href="despre.html" class="btn-a">Afl&#259; mai mult <i class="fas fa-arrow-right text-sm"></i></a>
      </div>
      <div class="relative reveal">
        <img src="img/SaveClip.App_686044914_18104045105296504_8299296285579802293_n.jpg" alt="Echipa InstalElectro" class="rounded-xl w-full object-cover" style="max-height:380px">
        <div class="absolute -bottom-4 -right-4 text-white rounded-xl px-6 py-4 shadow-xl" style="background:#0d6efd">
          <p class="text-2xl font-bold">1200<span class="text-sm font-normal">+</span></p>
          <p class="text-xs font-medium opacity-90">Lucr&#259;ri finalizate</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PRICING -->
<section id="preturi" class="py-20" style="background:#f5f7fa">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 reveal">
      <span class="stag">TARIFE ELECTRICA</span>
      <h2 class="text-3xl md:text-4xl font-bold leading-tight max-w-2xl mx-auto mt-2" style="color:#00254a">Pre&#539;uri orientative &#537;i oferte speciale pentru servicii electrice &icirc;n Chi&#537;in&#259;u</h2>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
      <div class="price-card bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="width:52px;height:52px;background:rgba(13,110,253,.1)"><i class="fas fa-plug text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Montare priz&#259; Chi&#537;in&#259;u</h4><p class="text-xs" style="color:#727272">De la 150 MDL</p></div>
      <div class="price-card bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="width:52px;height:52px;background:rgba(13,110,253,.1)"><i class="fas fa-lightbulb text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Instalare lustr&#259; Chi&#537;in&#259;u</h4><p class="text-xs" style="color:#727272">De la 200 MDL</p></div>
      <div class="price-card bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="width:52px;height:52px;background:rgba(13,110,253,.1)"><i class="fas fa-bolt text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Schimbare cablu electric</h4><p class="text-xs" style="color:#727272">De la 300 MDL</p></div>
      <div class="price-card bg-white rounded-xl p-5 text-center reveal"><div class="icon-circle" style="width:52px;height:52px;background:rgba(13,110,253,.1)"><i class="fas fa-screwdriver-wrench text-xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm mb-1" style="color:#00254a">Repara&#539;ii panou electric</h4><p class="text-xs" style="color:#727272">De la 400 MDL</p></div>
    </div>
    <div class="grid md:grid-cols-2 gap-4 mb-8">
      <div class="price-card rounded-xl p-6 text-center reveal" style="background:#00254a"><div class="icon-circle" style="width:52px;height:52px;background:rgba(255,255,255,.12)"><i class="fas fa-home text-xl text-white"></i></div><h4 class="font-bold text-white text-base mb-2">Pachet complet pentru apartament Chi&#537;in&#259;u</h4><p class="text-sm mb-4" style="color:rgba(255,255,255,.6)">Solu&#539;ie all-inclusive pentru renovare electric&#259; complet&#259;</p><a href="contact.html" class="inline-flex items-center gap-2 text-white text-xs font-bold px-5 py-2.5 rounded-md" style="background:#0d6efd">Solicit&#259; ofert&#259; <i class="fas fa-arrow-right text-xs"></i></a></div>
      <div class="price-card rounded-xl p-6 text-center reveal" style="background:#00254a"><div class="icon-circle" style="width:52px;height:52px;background:rgba(255,255,255,.12)"><i class="fas fa-clipboard-check text-xl text-white"></i></div><h4 class="font-bold text-white text-base mb-2">Consultan&#539;&#259; electric&#259; gratuit&#259; Chi&#537;in&#259;u</h4><p class="text-sm mb-4" style="color:rgba(255,255,255,.6)">Evaluare &#537;i planificare gratuit&#259; direct la sediul dvs.</p><a href="tel:+37368557199" class="inline-flex items-center gap-2 text-white text-xs font-bold px-5 py-2.5 rounded-md" style="background:#0d6efd"><i class="fas fa-phone text-xs"></i> Sun&#259; acum</a></div>
    </div>
    <p class="text-center text-sm reveal" style="color:#727272"><i class="fas fa-circle-check mr-1.5" style="color:#0d6efd"></i>Transparen&#539;&#259; complet&#259; &icirc;n cheltuieli. Estimare gratuit&#259; pentru orice lucrare electric&#259;.</p>
  </div>
</section>

<!-- EMERGENCY -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 reveal">
      <span class="stag">SPECIALIST &Icirc;N URGEN&#538;E ELECTRICE</span>
      <h2 class="text-3xl md:text-4xl font-bold leading-tight max-w-2xl mx-auto mt-2" style="color:#00254a">Interven&#539;ii rapide &#537;i servicii de urgen&#539;&#259; electric&#259; &icirc;n Chi&#537;in&#259;u</h2>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-5">
      <div class="text-center p-5 rounded-xl reveal" style="border:1px solid #e9ecef"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-wrench text-2xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm leading-snug mb-2" style="color:#00254a">Repararea prizelor &#537;i &icirc;ntrerup&#259;toarelor electrice Chi&#537;in&#259;u</h4><p class="text-xs" style="color:#727272">Interven&#539;ie rapid&#259; garantat&#259;</p></div>
      <div class="text-center p-5 rounded-xl reveal" style="border:1px solid #e9ecef"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-bolt text-2xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm leading-snug mb-2" style="color:#00254a">&Icirc;nlocuirea echipamentelor din panoul electric Chi&#537;in&#259;u</h4><p class="text-xs" style="color:#727272">Disponibil 24/7</p></div>
      <div class="text-center p-5 rounded-xl reveal" style="border:1px solid #e9ecef"><div class="icon-circle" style="background:rgba(13,110,253,.1)"><i class="fas fa-plug text-2xl" style="color:#0d6efd"></i></div><h4 class="font-bold text-sm leading-snug mb-2" style="color:#00254a">Conectarea echipamentelor electrice Chi&#537;in&#259;u</h4><p class="text-xs" style="color:#727272">Rapid &#537;i 100% sigur</p></div>
      <div class="text-center p-5 rounded-xl reveal" style="background:#fff3f3;border:1px solid #ffd0d0"><div class="icon-circle" style="background:rgba(220,53,69,.12)"><i class="fas fa-triangle-exclamation text-2xl" style="color:#dc3545"></i></div><h4 class="font-bold text-sm leading-snug mb-2" style="color:#dc3545">Servicii de urgen&#539;&#259; electric&#259; Chi&#537;in&#259;u</h4><a href="tel:+37368557199" class="text-xs font-bold" style="color:#dc3545"><i class="fas fa-phone text-[10px]"></i> +373 68 557 199</a></div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section class="py-20" style="background:#f5f7fa">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 reveal">
      <span class="stag">RECENZII CLIEN&#538;I</span>
      <h2 class="text-3xl md:text-4xl font-bold leading-tight max-w-2xl mx-auto mt-2" style="color:#00254a">Ce spun clien&#539;ii despre serviciile electrice din Chi&#537;in&#259;u</h2>
    </div>
    <div class="grid md:grid-cols-2 gap-6">
      <div class="testi-card reveal">
        <div class="flex gap-1 mb-4"><i class="fas fa-star text-sm" style="color:#ffc107"></i><i class="fas fa-star text-sm" style="color:#ffc107"></i><i class="fas fa-star text-sm" style="color:#ffc107"></i><i class="fas fa-star text-sm" style="color:#ffc107"></i><i class="fas fa-star text-sm" style="color:#ffc107"></i></div>
        <p class="text-sm leading-relaxed mb-6 italic" style="color:#727272">"Sunt extrem de mul&#539;umit&#259; de serviciile InstalElectro din Chi&#537;in&#259;u &ndash; au fost profesioni&#537;ti adev&#259;ra&#539;i. Au venit rapid, au diagnosticat problema &#537;i au rezolvat-o eficient. Recomand cu &icirc;ncredere!"</p>
        <div class="flex items-center gap-3.5"><img src="img/hero_img.jpg" alt="Elena" class="w-12 h-12 rounded-full object-cover" style="border:2px solid rgba(13,110,253,.2)"><div><p class="font-bold text-sm" style="color:#00254a">Elena, Ri&#537;cani</p><p class="text-xs" style="color:#727272">Client verificat InstalElectro</p></div></div>
      </div>
      <div class="testi-card reveal">
        <div class="flex gap-1 mb-4"><i class="fas fa-star text-sm" style="color:#ffc107"></i><i class="fas fa-star text-sm" style="color:#ffc107"></i><i class="fas fa-star text-sm" style="color:#ffc107"></i><i class="fas fa-star text-sm" style="color:#ffc107"></i><i class="fas fa-star text-sm" style="color:#ffc107"></i></div>
        <p class="text-sm leading-relaxed mb-6 italic" style="color:#727272">"Recomand cu toat&#259; &icirc;ncrederea InstalElectro din Chi&#537;in&#259;u &ndash; au realizat instala&#539;ia electric&#259; complet&#259; a apartamentului meu. Profesionalism des&#259;v&acirc;r&#537;it, punctualitate &#537;i pre&#539;uri corecte."</p>
        <div class="flex items-center gap-3.5"><img src="img/teamofelectricians.jpg" alt="Victor" class="w-12 h-12 rounded-full object-cover" style="border:2px solid rgba(13,110,253,.2)"><div><p class="font-bold text-sm" style="color:#00254a">Victor, Botanica</p><p class="text-xs" style="color:#727272">Client verificat InstalElectro</p></div></div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-12 gap-12 items-start">
      <div class="md:col-span-4 reveal">
        <span class="stag">CONTACT RAPID</span>
        <h2 class="text-2xl font-bold mt-2 mb-6 leading-snug" style="color:#00254a">Descrie&#539;i Problema &mdash; V&#259; Contact&#259;m Imediat</h2>
        <div class="space-y-4">
          <a href="tel:+37368557199" class="flex items-center gap-3.5"><div class="w-11 h-11 rounded-full flex items-center justify-center shrink-0" style="background:rgba(13,110,253,.1)"><i class="fas fa-phone text-sm" style="color:#0d6efd"></i></div><span class="text-sm" style="color:#727272">+373 68 557 199</span></a>
          <a href="mailto:info@instalelectro.md" class="flex items-center gap-3.5"><div class="w-11 h-11 rounded-full flex items-center justify-center shrink-0" style="background:rgba(13,110,253,.1)"><i class="fas fa-envelope text-sm" style="color:#0d6efd"></i></div><span class="text-sm" style="color:#727272">info@instalelectro.md</span></a>
          <div class="flex items-start gap-3.5"><div class="w-11 h-11 rounded-full flex items-center justify-center shrink-0 mt-0.5" style="background:rgba(13,110,253,.1)"><i class="fas fa-location-dot text-sm" style="color:#0d6efd"></i></div><div><p class="text-sm" style="color:#727272">Bd. Mircea Costin 23, Chi&#537;in&#259;u</p><p class="text-xs font-semibold mt-0.5" style="color:#0d6efd">Deserv&#259;m Chi&#537;in&#259;u &#537;i raza Chi&#537;in&#259;ului</p></div></div>
        </div>
        <div class="flex items-center gap-2.5 mt-7">
          <a href="#" class="w-10 h-10 rounded-full flex items-center justify-center text-white text-sm" style="background:#00254a"><i class="fab fa-facebook-f"></i></a>
          <a href="#" class="w-10 h-10 rounded-full flex items-center justify-center text-white text-sm" style="background:#00254a"><i class="fab fa-instagram"></i></a>
          <a href="#" class="w-10 h-10 rounded-full flex items-center justify-center text-white text-sm" style="background:#00254a"><i class="fab fa-tiktok"></i></a>
        </div>
      </div>
      <div class="md:col-span-8 reveal">
        <form class="space-y-4" onsubmit="return false">
          <div class="grid md:grid-cols-2 gap-4">
            <input type="text" placeholder="Numele dvs." class="form-input">
            <input type="tel" placeholder="Telefon de contact" class="form-input">
          </div>
          <input type="email" placeholder="Email (op&#539;ional)" class="form-input">
          <input type="text" placeholder="Tipul serviciului dorit" class="form-input">
          <textarea rows="4" placeholder="Descrie&#539;i problema sau lucrarea necesar&#259;..." class="form-input" style="resize:none"></textarea>
          <button type="submit" class="btn-p w-full justify-center uppercase tracking-wide"><i class="fas fa-paper-plane text-sm"></i> Trimite Solicitarea</button>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- PARTNERS -->
<section class="py-14" style="background:#f5f7fa">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-10 reveal"><h2 class="text-2xl font-bold" style="color:#00254a">Partenerii no&#537;tri</h2></div>
    <div class="flex items-center justify-center gap-10 md:gap-16 flex-wrap reveal">
      <img src="img/605603934_18090167021296504_5017235545341432250_n.jpg" alt="InstalElectro" class="h-10 w-auto" style="filter:grayscale(1) opacity(.5);transition:filter .3s" onmouseover="this.style.filter=\'grayscale(0) opacity(1)\'" onmouseout="this.style.filter=\'grayscale(1) opacity(.5)\'">
      <span class="text-2xl font-black tracking-widest" style="color:#ced4da;transition:color .3s;cursor:default" onmouseover="this.style.color=\'#00254a\'" onmouseout="this.style.color=\'#ced4da\'">eNERGIA</span>
      <span class="text-2xl font-black tracking-widest" style="color:#ced4da;transition:color .3s;cursor:default" onmouseover="this.style.color=\'#00254a\'" onmouseout="this.style.color=\'#ced4da\'">VOLTEX</span>
      <span class="text-2xl font-black tracking-widest" style="color:#ced4da;transition:color .3s;cursor:default" onmouseover="this.style.color=\'#00254a\'" onmouseout="this.style.color=\'#ced4da\'">ELCON</span>
    </div>
  </div>
</section>

<!-- BLOG PREVIEW -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-14 reveal">
      <span class="stag">ARTICOLE &#536;I &#536;TIRI</span>
      <h2 class="text-3xl md:text-4xl font-bold leading-tight mt-2" style="color:#00254a">Cele mai recente &#537;tiri &#537;i articole de pe blog</h2>
    </div>
    <div class="grid md:grid-cols-3 gap-6">
      <article class="blog-card bg-white rounded-xl overflow-hidden reveal"><div class="blog-img h-48 overflow-hidden"><img src="img/factura electrica.webp" alt="Factura electrica"></div><div class="p-5"><span class="text-[11px] font-bold uppercase tracking-widest" style="color:#0d6efd">Sfaturi</span><h3 class="font-bold text-[15px] mt-2 mb-2 leading-snug" style="color:#00254a">Cum s&#259; &icirc;&#539;i reduci factura electric&#259; &icirc;n 2025</h3><p class="text-xs leading-relaxed mb-4" style="color:#727272">Sfaturi practice &#537;i solu&#539;ii simple pentru reducerea consumului de energie electric&#259; acas&#259;.</p><a href="blog.html" class="inline-flex items-center gap-1.5 text-xs font-bold" style="color:#0d6efd">Cite&#537;te articolul <i class="fas fa-arrow-right text-[10px]"></i></a></div></article>
      <article class="blog-card bg-white rounded-xl overflow-hidden reveal"><div class="blog-img h-48 overflow-hidden"><img src="img/energieeficienta.webp" alt="Energie eficienta"></div><div class="p-5"><span class="text-[11px] font-bold uppercase tracking-widest" style="color:#0d6efd">Eficien&#539;&#259;</span><h3 class="font-bold text-[15px] mt-2 mb-2 leading-snug" style="color:#00254a">Sisteme de iluminat LED &mdash; investi&#539;ie sau cost?</h3><p class="text-xs leading-relaxed mb-4" style="color:#727272">Analiz&#259; complet&#259; a eficien&#539;ei sistemelor LED fa&#539;&#259; de sursele clasice.</p><a href="blog.html" class="inline-flex items-center gap-1.5 text-xs font-bold" style="color:#0d6efd">Cite&#537;te articolul <i class="fas fa-arrow-right text-[10px]"></i></a></div></article>
      <article class="blog-card bg-white rounded-xl overflow-hidden reveal"><div class="blog-img h-48 overflow-hidden"><img src="img/Electrical-Installation-services-1024x683.jpeg" alt="Instalatii"></div><div class="p-5"><span class="text-[11px] font-bold uppercase tracking-widest" style="color:#0d6efd">Ghid</span><h3 class="font-bold text-[15px] mt-2 mb-2 leading-snug" style="color:#00254a">Semne c&#259; instala&#539;ia electric&#259; trebuie verificat&#259; urgent</h3><p class="text-xs leading-relaxed mb-4" style="color:#727272">Cum recuno&#537;ti problemele electrice &icirc;nainte s&#259; devin&#259; periculoase.</p><a href="blog.html" class="inline-flex items-center gap-1.5 text-xs font-bold" style="color:#0d6efd">Cite&#537;te articolul <i class="fas fa-arrow-right text-[10px]"></i></a></div></article>
    </div>
    <div class="text-center mt-10 reveal"><a href="blog.html" class="btn-p">Toate articolele <i class="fas fa-arrow-right text-sm"></i></a></div>
  </div>
</section>

<!-- FOOTER -->
<footer style="background:#00254a">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
    <div class="grid md:grid-cols-12 gap-10">
      <div class="md:col-span-4">
        <div class="flex items-center gap-3 mb-4"><img src="img/605603934_18090167021296504_5017235545341432250_n.jpg" alt="InstalElectro" class="h-11 w-auto"><span class="font-bold text-white text-lg">Instal<span style="color:#0d6efd">Electro</span></span></div>
        <p class="text-sm leading-relaxed mb-5" style="color:rgba(255,255,255,.55)">Servicii electrice profesioniste &icirc;n Chi&#537;in&#259;u &#537;i &icirc;mprejurimi. Calitate garantat&#259;, disponibilitate 24/7.</p>
        <div class="flex items-center gap-2.5">
          <a href="#" class="w-9 h-9 rounded-full flex items-center justify-center text-white text-sm" style="background:rgba(255,255,255,.1)"><i class="fab fa-facebook-f"></i></a>
          <a href="#" class="w-9 h-9 rounded-full flex items-center justify-center text-white text-sm" style="background:rgba(255,255,255,.1)"><i class="fab fa-instagram"></i></a>
          <a href="#" class="w-9 h-9 rounded-full flex items-center justify-center text-white text-sm" style="background:rgba(255,255,255,.1)"><i class="fab fa-tiktok"></i></a>
        </div>
      </div>
      <div class="md:col-span-2"><h4 class="font-bold text-white text-xs uppercase tracking-widest mb-5">Pagini</h4><ul class="space-y-3"><li><a href="index.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Acas&#259;</a></li><li><a href="despre.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Despre</a></li><li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Servicii</a></li><li><a href="blog.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Blog</a></li><li><a href="contact.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Contact</a></li></ul></div>
      <div class="md:col-span-3"><h4 class="font-bold text-white text-xs uppercase tracking-widest mb-5">Servicii</h4><ul class="space-y-3"><li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Instal&#259;ri electrice</a></li><li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Repara&#539;ii electrice</a></li><li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Panou electric</a></li><li><a href="servicii.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Urgen&#539;e electrice 24/7</a></li><li><a href="contact.html" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">Consultan&#539;&#259; gratuit&#259;</a></li></ul></div>
      <div class="md:col-span-3"><h4 class="font-bold text-white text-xs uppercase tracking-widest mb-5">Contact</h4><ul class="space-y-3.5"><li class="flex items-start gap-2.5"><i class="fas fa-phone text-xs mt-1 shrink-0" style="color:#0d6efd"></i><a href="tel:+37368557199" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">+373 68 557 199</a></li><li class="flex items-start gap-2.5"><i class="fas fa-envelope text-xs mt-1 shrink-0" style="color:#0d6efd"></i><a href="mailto:info@instalelectro.md" class="text-sm hover:text-white transition-colors" style="color:rgba(255,255,255,.55)">info@instalelectro.md</a></li><li class="flex items-start gap-2.5"><i class="fas fa-location-dot text-xs mt-1 shrink-0" style="color:#0d6efd"></i><div><p class="text-sm" style="color:rgba(255,255,255,.55)">Bd. Mircea Costin 23, Chi&#537;in&#259;u</p><p class="text-xs font-semibold mt-0.5" style="color:#0d6efd">Deserv&#259;m Chi&#537;in&#259;u &#537;i raza Chi&#537;in&#259;ului</p></div></li></ul></div>
    </div>
  </div>
  <div style="border-top:1px solid rgba(255,255,255,.08)"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 flex flex-col sm:flex-row items-center justify-between gap-3"><p class="text-xs" style="color:rgba(255,255,255,.35)">Copyright 2025 InstalElectro. Servicii electrice profesioniste &icirc;n Chi&#537;in&#259;u. Toate drepturile rezervate.</p><a href="contact.html" class="text-xs font-semibold hover:text-white transition-colors" style="color:#0d6efd">Apeleaz&#259; pentru o problem&#259; electric&#259; &rarr;</a></div></div>
</footer>

<!-- MOBILE FLOATING CTA -->
<div class="lg:hidden fixed bottom-0 inset-x-0 z-40 flex" style="box-shadow:0 -4px 24px rgba(0,0,0,.3)">
  <a href="tel:+37368557199" class="flex-1 flex items-center justify-center gap-2.5 text-white font-bold py-4 text-sm" style="background:#00254a"><i class="fas fa-phone"></i> Sun&#259; acum</a>
  <a href="contact.html" class="flex-1 flex items-center justify-center gap-2.5 text-white font-semibold py-4 text-sm" style="background:#0d6efd"><i class="fas fa-envelope"></i> Solicit&#259; ofert&#259;</a>
</div>

<!-- POPUP -->
<div id="ie-popup" style="display:none;position:fixed;inset:0;z-index:9999;align-items:center;justify-content:center;padding:16px;background:rgba(0,37,74,.65);backdrop-filter:blur(4px)" onclick="if(event.target===this)ieClose()">
  <div style="background:#fff;border-radius:16px;padding:36px 32px;max-width:420px;width:100%;position:relative;box-shadow:0 24px 80px rgba(0,0,0,.3)" onclick="event.stopPropagation()">
    <button onclick="ieClose()" style="position:absolute;top:14px;right:14px;background:none;border:none;cursor:pointer;color:#adb5bd;font-size:18px"><i class="fas fa-times"></i></button>
    <div style="text-align:center">
      <div style="width:64px;height:64px;background:rgba(13,110,253,.1);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px"><i class="fas fa-bolt" style="font-size:28px;color:#0d6efd"></i></div>
      <h3 style="font-size:1.5rem;font-weight:800;color:#00254a;margin-bottom:8px">Ofert&#259; Special&#259;!</h3>
      <p style="color:#727272;font-size:.875rem;margin-bottom:20px;line-height:1.6">Beneficia&#539;i de <strong style="color:#00254a">10% reducere</strong> la prima comand&#259;. Copia&#539;i codul:</p>
      <div style="background:#f5f7fa;border:2px dashed rgba(13,110,253,.35);border-radius:10px;padding:16px 20px;margin-bottom:18px"><p style="font-size:1.75rem;font-weight:800;color:#0d6efd;letter-spacing:.1em">ELECTRO10</p></div>
      <button id="ie-copy-btn" onclick="ieCopy()" style="width:100%;background:#00254a;color:#fff;font-family:\'DM Sans\',sans-serif;font-weight:700;font-size:.875rem;border:none;border-radius:8px;padding:14px;cursor:pointer;margin-bottom:12px"><i class="fas fa-copy" style="margin-right:6px"></i> Copiaz&#259; codul</button>
      <button onclick="ieClose()" style="width:100%;background:none;border:none;color:#adb5bd;font-size:.8rem;cursor:pointer;font-family:\'DM Sans\',sans-serif">Nu, mul&#539;umesc</button>
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
  new Swiper(\'.hero-swiper\',{loop:true,speed:900,autoplay:{delay:5500,disableOnInteraction:false},navigation:{nextEl:\'.swiper-button-next\',prevEl:\'.swiper-button-prev\'},pagination:{el:\'.swiper-pagination\',clickable:true},effect:\'fade\',fadeEffect:{crossFade:true}});
  function toggleMobileMenu(){var m=document.getElementById(\'mobile-menu\'),i=document.getElementById(\'burger-icon\'),open=m.style.maxHeight&&m.style.maxHeight!==\'0px\';m.style.maxHeight=open?\'0px\':\'520px\';if(i)i.className=open?\'fas fa-bars text-xl\':\'fas fa-times text-xl\';}
  document.addEventListener(\'click\',function(e){var m=document.getElementById(\'mobile-menu\'),b=document.getElementById(\'burger\');if(m&&b&&!b.contains(e.target)&&!m.contains(e.target)&&m.style.maxHeight!==\'0px\'){m.style.maxHeight=\'0px\';var i=document.getElementById(\'burger-icon\');if(i)i.className=\'fas fa-bars text-xl\';}});
  var ro=new IntersectionObserver(function(e){e.forEach(function(e){if(e.isIntersecting){e.target.classList.add(\'visible\');ro.unobserve(e.target);}});},{threshold:.08,rootMargin:\'0px 0px -40px 0px\'});
  document.querySelectorAll(\'.reveal\').forEach(function(el){ro.observe(el);});
  function ieClose(){document.getElementById(\'ie-popup\').style.display=\'none\';}
  function ieCopy(){navigator.clipboard.writeText(\'ELECTRO10\').then(function(){var b=document.getElementById(\'ie-copy-btn\');b.innerHTML=\'<i class="fas fa-check" style="margin-right:6px"></i> Copiat!\';b.style.background=\'#198754\';setTimeout(function(){b.innerHTML=\'<i class="fas fa-copy" style="margin-right:6px"></i> Copiaz&#259; codul\';b.style.background=\'#00254a\';},2500);});}
  if(!sessionStorage.getItem(\'ie_popup\')){setTimeout(function(){document.getElementById(\'ie-popup\').style.display=\'flex\';sessionStorage.setItem(\'ie_popup\',\'1\');},4500);}
</script>
</body>
</html>'''

with open(r'w:\website_projects\instalelectro\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Done: {len(content)} chars")
