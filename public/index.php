<?php
$version = '0.3.0';
$status = 'online';
$currentYear = date('Y');
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
        <a href="/" class="brand-block ajax-link" data-page="home" aria-label="NovaLike accueil">
            <img src="https://cdn.wanalike.com/assets/v1/brands/novalike/logo/logo.webp" class="brand-logo" alt="NovaLike">
            <span class="brand-copy"><strong>NovaLike</strong><small>IA communautaire</small></span>
        </a>
        <button class="nav-toggle" type="button" aria-label="Ouvrir le menu"><i class="fa-solid fa-bars"></i></button>
        <div class="nav-menu">
            <a href="/" class="nav-link ajax-link active" data-page="home"><i class="fa-solid fa-house"></i> Accueil</a>
            <a href="/features" class="nav-link ajax-link" data-page="features"><i class="fa-solid fa-wand-magic-sparkles"></i> Fonctionnalités</a>
            <a href="/ecosystem" class="nav-link ajax-link" data-page="ecosystem"><i class="fa-solid fa-network-wired"></i> Écosystème</a>
            <a href="/community" class="nav-link ajax-link" data-page="community"><i class="fa-brands fa-discord"></i> Communauté</a>
        </div>
        <div class="nav-actions">
            <a href="/api/health.php" class="status-pill"><span></span> API <?= htmlspecialchars($status) ?></a>
            <a href="https://wanalike.com" class="nav-cta"><i class="fa-solid fa-arrow-up-right-from-square"></i> WanaLike</a>
        </div>
    </nav>
</header>
<main id="app-content" class="container ajax-content" aria-live="polite"></main>
<footer class="site-footer glassy">
    <div class="footer-brand">
        <img src="https://cdn.wanalike.com/assets/v1/brands/novalike/logo/logo.webp" alt="NovaLike">
        <div><strong>NovaLike</strong><p>L’IA communautaire qui garde WanaLike vivant, humain et actif.</p></div>
    </div>
    <div class="footer-columns">
        <div>
            <h3><i class="fa-solid fa-compass"></i> Navigation</h3>
            <a href="/" class="ajax-link" data-page="home"><i class="fa-solid fa-house"></i> Accueil</a>
            <a href="/features" class="ajax-link" data-page="features"><i class="fa-solid fa-wand-magic-sparkles"></i> Fonctionnalités</a>
            <a href="/ecosystem" class="ajax-link" data-page="ecosystem"><i class="fa-solid fa-network-wired"></i> Écosystème</a>
        </div>
        <div>
            <h3><i class="fa-solid fa-code"></i> Technique</h3>
            <a href="/api/health.php"><i class="fa-solid fa-heart-pulse"></i> API Health</a>
            <a href="/openapi/novalike-actions.yaml"><i class="fa-solid fa-file-code"></i> OpenAPI GPT</a>
        </div>
        <div>
            <h3><i class="fa-solid fa-globe"></i> WanaLike</h3>
            <a href="https://wanalike.com"><i class="fa-solid fa-earth-europe"></i> Hub</a>
            <a href="https://fm.wanalike.com"><i class="fa-solid fa-radio"></i> WanaFM</a>
            <a href="https://wanachess.wanalike.com"><i class="fa-solid fa-chess-knight"></i> WanaChess</a>
        </div>
    </div>
    <div class="footer-bottom">
        <span><i class="fa-solid fa-microchip"></i> NovaLike v<?= htmlspecialchars($version) ?> · statut <?= htmlspecialchars($status) ?></span>
        <span>© 2015-<?= htmlspecialchars($currentYear) ?> Hardcodé par KoS_ avec ❤️ pour WanaLike — NovaLike est une marque de WanaLike.</span>
    </div>
</footer>
<script src="/assets/js/app.js"></script>
</body>
</html>
