<?php
$version = '0.2.2';
$status = 'online';
?>
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>NovaLike — IA communautaire WanaLike</title>
    <meta name="description" content="NovaLike est l’IA communautaire officielle de WanaLike.">
    <meta name="theme-color" content="#8a5cf6">
    <link rel="icon" type="image/png" sizes="32x32" href="https://cdn.wanalike.com/assets/v1/brands/novalike/favicon/favicon-32x32.png">
    <link rel="icon" href="https://cdn.wanalike.com/assets/v1/brands/novalike/favicon/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="https://cdn.wanalike.com/assets/v1/brands/novalike/favicon/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="/assets/css/style.css">
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
</head>
<body>
<div class="background-glow"></div>
<header class="site-header">
    <nav class="ecosystem-nav glassy">
        <a href="/" class="brand-block" aria-label="NovaLike accueil">
            <img src="https://cdn.wanalike.com/assets/v1/brands/novalike/logo/logo.webp" class="brand-logo" alt="NovaLike">
            <span class="brand-copy"><strong>NovaLike</strong><small>IA communautaire</small></span>
        </a>
        <button class="nav-toggle" type="button" aria-label="Ouvrir le menu"><i class="fa-solid fa-bars"></i></button>
        <div class="nav-menu">
            <a href="#top" class="nav-link active"><i class="fa-solid fa-house"></i> Accueil</a>
            <a href="#features" class="nav-link"><i class="fa-solid fa-sparkles"></i> Fonctions</a>
            <a href="#integrations" class="nav-link"><i class="fa-solid fa-network-wired"></i> Écosystème</a>
            <a href="#community" class="nav-link"><i class="fa-brands fa-discord"></i> Communauté</a>
        </div>
        <div class="nav-actions">
            <a href="/api/health.php" class="status-pill"><span></span> API <?= htmlspecialchars($status) ?></a>
            <a href="https://wanalike.com" class="nav-cta"><i class="fa-solid fa-arrow-up-right-from-square"></i> WanaLike</a>
        </div>
    </nav>
</header>
<main id="top" class="container">
<section class="hero glassy">
    <div class="hero-content">
        <div class="badge">✨ IA communautaire officielle WanaLike</div>
        <h1>NovaLike</h1>
        <p class="lead">Accueil, animation, assistance et présence intelligente pour garder la communauté WanaLike vivante.</p>
        <div class="actions">
            <a href="#features" class="button primary"><i class="fa-solid fa-sparkles"></i> Découvrir NovaLike</a>
            <a href="https://wanalike.com" class="button secondary"><i class="fa-solid fa-users"></i> Rejoindre WanaLike</a>
        </div>
    </div>
    <div class="hero-image"><img src="https://cdn.wanalike.com/assets/v1/brands/novalike/logo/banner.webp" alt="NovaLike Banner"></div>
</section>
<section id="features" class="cards-grid">
    <article class="feature-card glassy"><i class="fa-solid fa-user-group"></i><h2>Accueille</h2><p>Guide les nouveaux membres dès leur arrivée sans friction inutile.</p></article>
    <article class="feature-card glassy"><i class="fa-solid fa-comments"></i><h2>Anime</h2><p>Relance intelligemment les salons et maintient une présence active.</p></article>
    <article class="feature-card glassy"><i class="fa-solid fa-headset"></i><h2>Assiste</h2><p>Répond aux questions et oriente vers les bons espaces.</p></article>
</section>
<section id="integrations" class="integrations glassy">
    <div><span class="section-kicker">Intégrations futures</span><h2>Écosystème WanaLike</h2></div>
    <div class="integration-grid">
        <a href="https://fm.wanalike.com"><i class="fa-solid fa-radio"></i> WanaFM</a>
        <a href="https://wanachess.wanalike.com"><i class="fa-solid fa-chess-knight"></i> WanaChess</a>
        <a href="https://wanalike.com"><i class="fa-brands fa-discord"></i> Discord</a>
        <a href="#"><i class="fa-solid fa-server"></i> XtraVerseRP</a>
    </div>
</section>
<section id="community" class="community-strip glassy">
    <div><span class="section-kicker">Communauté</span><h2>Une présence IA pensée pour Discord</h2><p>NovaLike accompagne les nouveaux, garde le serveur lisible et aide l’équipe à maintenir une ambiance active.</p></div>
    <a href="https://wanalike.com" class="button primary"><i class="fa-brands fa-discord"></i> Accéder au hub</a>
</section>
</main>
<footer class="site-footer glassy">
    <div class="footer-brand">
        <img src="https://cdn.wanalike.com/assets/v1/brands/novalike/logo/logo.webp" alt="NovaLike">
        <div><strong>NovaLike</strong><p>L’IA communautaire qui garde WanaLike vivant, humain et actif.</p></div>
    </div>
    <div class="footer-columns">
        <div><h3>Navigation</h3><a href="#top">Accueil</a><a href="#features">Fonctionnalités</a><a href="#integrations">Écosystème</a></div>
        <div><h3>Technique</h3><a href="/api/health.php">API Health</a><a href="/openapi/novalike-actions.yaml">OpenAPI GPT</a></div>
        <div><h3>WanaLike</h3><a href="https://wanalike.com">Hub</a><a href="https://fm.wanalike.com">WanaFM</a><a href="https://wanachess.wanalike.com">WanaChess</a></div>
    </div>
    <div class="footer-bottom"><span>NovaLike v<?= htmlspecialchars($version) ?> · statut <?= htmlspecialchars($status) ?></span><span>© 2026 WanaLike · Créé par KoS_</span></div>
</footer>
<script>
$(function(){
    $('.nav-toggle').on('click',function(){ $('.nav-menu, .nav-actions').toggleClass('open'); });
    $('a[href^="#"]').on('click',function(e){ const target=$($(this).attr('href')); if(target.length){ e.preventDefault(); $('html, body').animate({scrollTop:target.offset().top-105},350); $('.nav-menu, .nav-actions').removeClass('open'); }});
});
</script>
</body>
</html>
