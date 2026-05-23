# TODO NovaLike

## Priorité actuelle

- Stabiliser le bot Discord NovaLike.
- Garder l’API FastAPI disponible via `127.0.0.1:9010` + reverse proxy nginx/Plesk.
- Garder le GPT NovaLike comme panneau de contrôle privé, pas comme accès IA public libre.
- Réserver les interactions IA avancées au rôle Discord `Nova-Testers`.

## Discord / Communauté

- Ajouter des commandes Discord propres :
  - `!nova status`
  - `!nova debug`
  - `!nova reload`
  - `!nova say`
  - `!nova announce`
  - `!nova channels`
- Ajouter des logs Python plus détaillés : messages reçus, réponses envoyées, erreurs API, cooldowns, actions admin.
- Ajouter un système de cooldown par utilisateur et par salon.
- Ajouter un mode silence par salon.
- Ajouter une configuration par salon : accueil, règlement, radio, suggestions, staff, dev, annonces.
- Améliorer les réponses humaines sans brancher OpenAI par défaut.
- Garder les réponses publiques majoritairement locales/templates pour éviter les abus et les coûts API.

## IA / Providers

- Garder OpenAI API désactivée par défaut et réservée aux cas exceptionnels.
- Étudier une intégration Groq pour certains rôles/salons uniquement.
- Ajouter une config :
  - `AI_PROVIDER`
  - `AI_PUBLIC_ENABLED=false`
  - `AI_ALLOWED_ROLE_IDS`
  - `AI_ALLOWED_CHANNEL_IDS`
  - `AI_COOLDOWN_SECONDS`
  - `AI_DAILY_REQUEST_LIMIT`
  - `AI_MAX_TOKENS`
- Prévoir fallback local si IA indisponible ou quota dépassé.

## Plesk / Logs / Sécurité

- Étudier l’intégration de Plesk avec NovaLike, en complément de l’intégration Slack déjà existante.
- Objectif : transformer NovaLike en vigie sécurité légère pour l’infra WanaLike.
- Récupérer/analyser les logs Plesk/nginx/apache/mail pertinents :
  - tentatives d’accès à fichiers sensibles (`.env`, backups, `.git`, dumps SQL, etc.)
  - erreurs 401/403/404/500/502 récurrentes
  - scans massifs par IP
  - tentatives sur WordPress/PHPMyAdmin/admin paths
  - attaques répétées sur endpoints API
- Produire des notifications Discord/NovaLike de type :
  - `X IP suspectes détectées sur nova.wanalike.com`
  - `Tentatives répétées sur /.env et /.git`
  - `Nginx retourne 502 sur /gpt/send-message`
  - `Plusieurs 401 OpenAPI/GPT détectés`
- Ajouter une commande admin pour lister les IP suspectes.
- Ajouter une proposition d’action :
  - surveiller seulement
  - ignorer
  - bannir temporairement
  - bannir définitivement
- Prévoir un système de ban applicatif ou firewall plus tard :
  - fichier local de denylist
  - intégration fail2ban
  - intégration nginx deny
  - intégration Cloudflare API
  - intégration Plesk firewall si pertinent
- Ne jamais bannir automatiquement sans confirmation admin au début.
- Ajouter garde-fous anti auto-ban : whitelist IP admin, IP serveur, Cloudflare, localhost, monitoring.

## Pooshy-Data

- Prévoir une interaction future avec Pooshy-Data.
- NovaLike doit pouvoir consulter des données internes validées au lieu d’improviser.
- Prévoir des endpoints internes :
  - contexte serveur
  - mémoire communautaire
  - statut services
  - historique événements
  - données radio/WanaFM
  - infos WanaLike Publisher

## WanaLike Publisher

- Prévoir une intégration avec WanaLike Publisher.
- Objectifs possibles :
  - générer des brouillons d’annonces
  - publier des news communautaires
  - relayer les articles importants dans Discord
  - proposer des résumés d’activité serveur
  - préparer des contenus blog depuis événements Discord
- Ajouter validation humaine obligatoire avant publication publique.

## Exploitation / Services

- Mettre FastAPI sous systemd.
- Mettre le bot Discord sous systemd.
- Ajouter restart automatique en cas de crash.
- Ajouter logs séparés :
  - `logs/api.log`
  - `logs/bot.log`
  - `logs/security.log`
- Ajouter rotation des logs.
- Ajouter un endpoint `/health/full` avec statut bot/API/queue/config.

## Vision long terme

- NovaLike = assistant communautaire + vigie infra + panneau de contrôle WanaLike.
- Ne pas en faire un ChatGPT public gratuit.
- Garder l’IA générative coûteuse sous contrôle strict.
- Prioriser logique locale, sécurité, logs, contexte et intégrations internes.
