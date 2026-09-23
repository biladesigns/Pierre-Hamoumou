# SEO-JOURNAL — pierrehamoumou-avocat.fr

Conversion suivie : formulaire de contact (contact-2.html), appel téléphonique (07 70 28 25 46), email direct.

## Partie A — Décisions engageantes

### 2026-09-08 — Corriger les 3 dernières 404 WordPress restantes
Le commit `ca3aa66` (05/09) prétendait corriger "7 pages en 404 dans la GSC" mais le `.htaccess`
ne contenait que 5 redirections. Vérifié en direct (curl) : `/droit-de-la-securite-sociale/`,
`/droit-du-dommage-corporel/` et `/droit-des-assurances/` renvoient un vrai 404 aujourd'hui.
Ajout de 3 redirections 301 :
- `/droit-de-la-securite-sociale/` → `/droit-de-la-s-curit-sociale-2.html` (page actuelle
  correspondante, thème identique)
- `/droit-du-dommage-corporel/` et `/droit-des-assurances/` → `/` (aucune page actuelle ne
  couvre ces thèmes — vérifié par grep sur tout le site avant de choisir la cible ; pas de
  practice area "dommage corporel" ou "assurances" chez Me Hamoumou aujourd'hui, donc pas de
  redirection thématique possible, direction accueil pour éviter la déperdition pure)

### 2026-09-08 — Ne repropose pas de réécrire postulation-et-substitution.html
Requêtes "avocat postulation lyon" (17 impr, position 40,8), "postulation avocat lyon" (14 impr,
44,1), "postulation lyon" (11 impr, 43,3), "avocat substitution lyon" (10 impr, 31,5) : 0 clic
sur toutes, positions 31-45. La page existe déjà et est technique­ment complète (canonical, OG,
H1, JSON-LD FAQ — vérifié via tools/seo-check.py). La SERP réelle sur "avocat postulation lyon"
montre une dizaine de confrères lyonnais, chacun avec sa propre page dédiée "postulation Lyon",
certains avec 150-190 avis Google (ex. Cabinet FACCHINI, 4,9/190). Le Google
Business Profile de Me Hamoumou n'a que 6 avis. Le problème n'est pas la page (déjà au niveau des
concurrents), c'est l'autorité locale/le nombre d'avis. Réécrire le texte ne comblera pas 30
positions face à des confrères avec 20x plus d'avis. Ne pas reproposer une réécriture de cette
page tant que l'écart d'avis n'a pas bougé.

### 2026-09-08 — Ne pas traiter le doublon http/https de la page d'accueil
`https://` (249 impr/32 clics) et `http://` (419 impr/6 clics) apparaissent tous les deux dans le
rapport Pages de la GSC. Vérifié en direct : `http://` redirige bien en 301 vers `https://`
(le serveur Hostinger le fait en amont, rien à changer côté site). C'est Google qui teste encore
l'ancienne URL http, pas un bug corrigible côté code. À surveiller, pas à corriger.

### 2026-09-08 — Ne pas courir après la position moyenne 4,3 sur "hamoumou"
Le nom de famille est partagé avec Mohand Hamoumou (ancien maire de Volvic, forte couverture
presse). Recherche directe sur "hamoumou" : le site de Me Hamoumou ressort bien en 1ère position
aujourd'hui. La moyenne à 4,3 vient probablement de variations géographiques/SERP, pas d'un vrai
problème, et le volume est faible (7 impressions/3 mois). Pas d'action tant qu'aucune preuve
contraire n'apparaît.

### 2026-09-08 — Ne pas reproposer "le contenu ne suffit pas" sans vérifier l'indexation d'abord
En creusant "avocat postulation lyon", découvert que `postulation-et-substitution.html` n'était
même pas reconnue par l'inspection d'URL Google ("Google ne reconnaît pas cette URL"), alors
qu'elle est dans le sitemap, liée depuis l'accueil, et déjà techniquement complète. Le test en
ligne confirme la page accessible et indexable — donc pas un blocage technique, juste jamais
crawlée/indexée sérieusement. `droit-de-la-s-curit-sociale-2.html` : "Détectée, actuellement non
indexée" (connue via sitemap, jamais explorée). Demande d'indexation manuelle envoyée pour les
deux via Search Console. Prochaine revue : vérifier si elles sont passées "Dans l'index" avant de
retoucher quoi que ce soit sur le contenu ou l'autorité — inutile de discuter position tant
qu'une page n'est pas indexée du tout.

⚠️ Fiabilité outil notée en passant : l'inspection d'URL dans ce navigateur a renvoyé plusieurs
résultats visiblement périmés (URL affichée correcte, contenu du panneau resté sur la requête
précédente) avant de se rafraîchir correctement. Si un résultat surprend le mois prochain,
recliquer sur la loupe ou "Tester l'URL active" avant de le prendre pour argent comptant.

### 2026-09-23 — Le client a reçu un audit externe qui pointe "seulement 3 pages indexées"
Un cabinet SEO tiers a fait un audit pour Mathieu/le client et relevé que peu de pages sont
indexées. Vérifié : c'est exact (3/9 "Dans l'index" ce jour), mais la cause n'est pas un défaut
de travail sur le site (canonical/OG/H1/JSON-LD/sitemap toujours propres, cf. audit du 08/09).
C'est un jeune domaine à faible autorité, donc crawl budget minimal de Google. Les 2 pages
demandées manuellement le 08/09 (postulation, droit sécu sociale) sont bien passées à l'index
depuis, preuve que la demande manuelle fonctionne. Action : demande d'indexation manuelle pour
les 6 pages restantes (a-propos, faq, honoraires, contact-2, mentions-legales,
politique-de-confidentialite) pour couvrir les 9 pages du sitemap. Ne pas laisser un audit
externe faire croire que c'est un problème de qualité de site : c'est un problème de temps/
autorité, déjà engagé dans la bonne direction avant l'audit.

## Partie B — Journal daté

- 2026-09-08 : ajout de 3 redirections 301 dans `.htaccess` (droit-de-la-securite-sociale,
  droit-du-dommage-corporel, droit-des-assurances). Effet attendu : disparition de ces 3 lignes
  du rapport Indexation "Introuvable (404)" d'ici le 08/10/2026. Invalidé si elles réapparaissent
  en 404 après déploiement (vérifier que le .htaccess est bien celui servi en prod, pas un
  ancien cache Hostinger).
- 2026-09-08 : demande d'indexation manuelle pour `postulation-et-substitution.html` et
  `droit-de-la-s-curit-sociale-2.html` (les deux pages de service principales, ni l'une ni
  l'autre "Dans l'index" selon le rapport Indexation). Effet attendu : passage en "Dans l'index"
  sous 1-2 semaines. Vérifier le 08/10/2026. Invalidé si elles restent hors index passé ce délai
  — indiquerait un problème d'autorité de domaine plus sérieux qu'un simple manque de crawl.
- 2026-09-23 : confirmé, les 2 pages ci-dessus sont passées "Dans l'index" (3/9 pages indexées ce
  jour, contre 1/9 le 08/09). Demande d'indexation manuelle envoyée pour les 6 pages restantes
  (a-propos.html, faq.html, honoraires-individualis-s.html, contact-2.html, mentions-legales/,
  politique-de-confidentialite/). Au passage : mentions-legales/ et politique-de-confidentialite/
  affichaient un statut "404"/"URL inconnue" périmé dans la GSC alors qu'elles répondent en 200
  en direct (vérifié curl) — pas un vrai problème, juste un recrawl à forcer. Vérifier le
  07/10/2026 si les 9 pages sont passées à l'index.
