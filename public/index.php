<?php
$version = '0.2.0';
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

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="/assets/css/style.css">

    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
</head>
<body>

<div class="background-glow"></div>

<nav class="navbar glassy">
    <div class="nav-left">
        <img src="https://cdn.wanalike.com/assets/v1/brands/novalike/logo/logo.webp" class="nav-logo" alt="NovaLike">
        <span class="nav-title">NovaLike</span>
    </div>

    <div class="nav-links">
        <a href="#features"><i class="fa-solid fa-sparkles"></i> Fonctionnalités</a>
        <a href="#integrations"><i class="fa-solid fa-plug"></i> Intégrations</a>
        <a href="/api/health.php"><i class="fa-solid fa-heart-pulse"></i> API</a>
    </div>
</nav>

<main class="container">

<section class="hero glassy">

    <div class="hero-content">
        <div class="badge">✨ IA communautaire officielle WanaLike</div>

        <h1>NovaLike</h1>

        <p class="lead">
            Accueil, animation, assistance et présence intelligente pour garder la communauté WanaLike vivante.
        </p>

        <div class="actions">
            <a href="/api/health.php" class="button primary">
                <i class="fa-solid fa-heart-pulse"></i>
                API Health
            </a>

            <a href="/openapi/novalike-actions.yaml" class="button secondary">
                <i class="fa-solid fa-robot"></i>
                OpenAPI GPT
            </a>
        </div>
    </div>

    <div class="hero-image">
        <img src="https://cdn.wanalike.com/assets/v1/brands/novalike/logo/banner.webp" alt="NovaLike Banner">
    </div>

</section>

<section id="features" class="cards-grid">

    <article class="feature-card glassy">
        <i class="fa-solid fa-user-group"></i>
        <h2>Accueille</h2>
        <p>Guide les nouveaux membres dès leur arrivée sans friction inutile.</p>
    </article>

    <article class="feature-card glassy">
        <i class="fa-solid fa-comments"></i>
        <h2>Anime</h2>
        <p>Relance intelligemment les salons et maintient une présence active.</p>
    </article>

    <article class="feature-card glassy">
        <i class="fa-solid fa-headset"></i>
        <h2>Assiste</h2>
        <p>Répond aux questions et oriente vers les bons espaces.</p>
    </article>

</section>

<section id="integrations" class="integrations glassy">
    <h2>Écosystème WanaLike</h2>

    <div class="integration-grid">
        <div><i class="fa-solid fa-radio"></i> WanaFM</div>
        <div><i class="fa-solid fa-chess-knight"></i> WanaChess</div>
        <div><i class="fa-brands fa-discord"></i> Discord</div>
        <div><i class="fa-solid fa-server"></i> XtraVerseRP</div>
    </div>
</section>

</main>

<footer class="footer glassy">
    <div>NovaLike v<?= htmlspecialchars($version) ?> · statut <?= htmlspecialchars($status) ?></div>
    <div>Créé par KoS_ / WanaLike</div>
</footer>

<script>
$(function() {
    console.log('NovaLike UI loaded');
});
</script>

</body>
</html>
