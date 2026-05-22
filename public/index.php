<?php
$version = '0.1.0';
$status = 'online';
?>
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>NovaLike — IA communautaire WanaLike</title>
    <meta name="description" content="NovaLike est l’IA communautaire francophone de WanaLike : accueil, animation, assistance et présence Discord.">
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
    <main class="shell">
        <section class="hero">
            <div class="badge">IA communautaire officielle WanaLike</div>
            <h1>NovaLike</h1>
            <p class="lead">Accueil, animation, assistance et présence intelligente pour garder la communauté vivante.</p>
            <div class="actions">
                <a href="/api/health.php" class="button">API Health</a>
                <a href="/openapi/novalike-actions.yaml" class="button secondary">OpenAPI GPT</a>
            </div>
        </section>

        <section class="cards">
            <article>
                <h2>Accueille</h2>
                <p>Guide les nouveaux membres dès leur arrivée, sans friction inutile.</p>
            </article>
            <article>
                <h2>Anime</h2>
                <p>Relance les salons calmes et propose des interactions simples.</p>
            </article>
            <article>
                <h2>Assiste</h2>
                <p>Répond aux questions communautaires et oriente vers les bons espaces.</p>
            </article>
        </section>

        <footer>
            NovaLike v<?= htmlspecialchars($version) ?> · statut <?= htmlspecialchars($status) ?> · Créé par KoS_ / WanaLike
        </footer>
    </main>
</body>
</html>
