# TODO NovaLike

## Priorité actuelle

1. Stabiliser le runtime NovaLike : bot Discord + FastAPI + reverse proxy.
2. Brancher WanaLike Publisher.
3. Brancher Pooshy / Pooshy-Data pour préparer le pont IRC ↔ Discord.
4. Ajouter les contextes WanaFM / WanaChess.
5. Brancher Plesk/logs/sécurité ensuite, quand le socle est stable.

## Runtime / Services

- Mettre FastAPI sous systemd.
- Mettre le bot Discord sous systemd.
- Ajouter restart automatique en cas de crash.
- Garder l’API FastAPI disponible via `127.0.0.1:9010` + reverse proxy nginx/Plesk.
- Ajouter logs séparés :
  - `logs/api.log`
  - `logs/bot.log`
  - `logs/security.log`
  - `logs/publisher.log`
  - `logs/pooshy.log`
- Ajouter rotation des logs.
- Ajouter un endpoint `/health/full` avec statut bot/API/queue/config/connecteurs.

## Discord / Communauté

- Garder le GPT NovaLike comme panneau de contrôle privé, pas comme accès IA public libre.
- Réserver les interactions IA avancées au rôle Discord `Nova-Testers`.
- Ajouter des commandes Discord propres :
  - `!nova status`
  - `!nova debug`
  - `!nova reload`
  - `!nova say`
  - `!nova announce`
  - `!nova channels`
  - `!nova publisher status`
  - `!nova pooshy status`
- Ajouter des logs Python plus détaillés : messages reçus, réponses envoyées, erreurs API, cooldowns, actions admin.
- Ajouter un système de cooldown par utilisateur et par salon.
- Ajouter un mode silence par salon.
- Ajouter une configuration par salon : accueil, règlement, radio, suggestions, staff, dev, annonces.
- Améliorer les réponses humaines sans brancher OpenAI par défaut.
- Garder les réponses publiques majoritairement locales/templates pour éviter les abus et les coûts API.

## WanaLike Publisher — priorité avant Plesk

- Prévoir une intégration avec WanaLike Publisher avant la partie Plesk/logs.
- Objectifs :
  - générer des brouillons d’annonces
  - préparer des brouillons d’articles
  - publier des news communautaires après validation humaine
  - relayer les articles importants dans Discord
  - proposer des résumés d’activité serveur
  - transformer une discussion Discord intéressante en brouillon blog
  - préparer des contenus depuis événements Discord/IRC/WanaFM/WanaChess
- Ajouter validation humaine obligatoire avant publication publique.
- Prévoir des endpoints NovaLike internes :
  - `GET /publisher/status`
  - `POST /publisher/draft`
  - `POST /publisher/announce-draft`
  - `POST /publisher/discord-summary-draft`
  - `POST /publisher/publish` plus tard, réservé admin
- Ne jamais publier directement sans confirmation admin au début.

## Pooshy / Pooshy-Data / IRC Bridge — priorité après Publisher

- Prévoir une interaction avec Pooshy-Data.
- Pooshy étant déjà côté IRC, NovaLike pourra interagir avec lui via le bridge Discord ↔ IRC.
- Objectifs :
  - récupérer contexte IRC
  - relayer certains événements IRC vers Discord
  - envoyer certaines annonces Discord vers IRC
  - synchroniser informations utiles entre Pooshy et NovaLike
  - éviter de dupliquer toute la logique Pooshy
- NovaLike doit pouvoir consulter des données internes validées au lieu d’improviser.
- Prévoir des endpoints internes :
  - `GET /pooshy/status`
  - `GET /pooshy/context`
  - `POST /pooshy/event`
  - `POST /pooshy/relay`
- Prévoir des données :
  - contexte serveur
  - mémoire communautaire
  - statut services
  - historique événements
  - données radio/WanaFM
  - infos WanaLike Publisher

## WanaFM / WanaChess context

- Ajouter un connecteur WanaFM pour statut radio, titre courant, audience et annonces.
- Ajouter un connecteur WanaChess pour statut projet, annonces et intégrations communautaires.
- NovaLike doit pouvoir répondre localement sur l’écosystème WanaLike sans OpenAI.

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

## Plesk / Logs / Sécurité — après Publisher et Pooshy

- Étudier l’intégration de Plesk avec NovaLike via API/hooks/logs existants.
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
- Ajouter une proposition d’action : surveiller, ignorer, bannir temporairement, bannir définitivement.
- Prévoir un système de ban applicatif ou firewall plus tard : fichier denylist, fail2ban, nginx deny, Cloudflare API, Plesk firewall si pertinent.
- Ne jamais bannir automatiquement sans confirmation admin au début.
- Ajouter garde-fous anti auto-ban : whitelist IP admin, IP serveur, Cloudflare, localhost, monitoring.

## Vision long terme

- NovaLike = assistant communautaire + panneau de contrôle WanaLike + passerelle Publisher/Pooshy + vigie infra.
- Ne pas en faire un ChatGPT public gratuit.
- Garder l’IA générative coûteuse sous contrôle strict.
- Prioriser logique locale, sécurité, logs, contexte et intégrations internes.
