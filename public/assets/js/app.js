const appContent = $('#app-content');

async function loadPage(page, push = true) {
    try {
        $('.nav-link').removeClass('active');
        $(`.ajax-link[data-page="${page}"]`).addClass('active');

        const response = await fetch(`/pages/${page}.php`);

        if (!response.ok) {
            throw new Error('Page introuvable');
        }

        const html = await response.text();

        appContent.fadeOut(120, function () {
            appContent.html(html).fadeIn(180);
        });

        if (push) {
            const path = page === 'home' ? '/' : `/${page}`;
            window.history.pushState({ page }, '', path);
        }

        window.scrollTo({ top: 0, behavior: 'smooth' });

    } catch (e) {
        appContent.html(`
            <section class="hero glassy">
                <div class="hero-content">
                    <div class="badge">⚠️ Erreur</div>
                    <h1>404</h1>
                    <p class="lead">Impossible de charger la page demandée.</p>
                </div>
            </section>
        `);
    }
}

$(document).on('click', '.ajax-link', function (e) {
    const page = $(this).data('page');

    if (!page) {
        return;
    }

    e.preventDefault();

    loadPage(page);

    $('.nav-menu, .nav-actions').removeClass('open');
});

window.addEventListener('popstate', (event) => {
    const page = event.state?.page || 'home';
    loadPage(page, false);
});

$(function () {
    $('.nav-toggle').on('click', function () {
        $('.nav-menu, .nav-actions').toggleClass('open');
    });

    let currentPage = window.location.pathname.replace(/^\//, '');

    if (!currentPage) {
        currentPage = 'home';
    }

    loadPage(currentPage, false);
});
