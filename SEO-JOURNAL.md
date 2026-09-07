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

## Partie B — Journal daté

- 2026-09-08 : ajout de 3 redirections 301 dans `.htaccess` (droit-de-la-securite-sociale,
  droit-du-dommage-corporel, droit-des-assurances). Effet attendu : disparition de ces 3 lignes
  du rapport Indexation "Introuvable (404)" d'ici le 08/10/2026. Invalidé si elles réapparaissent
  en 404 après déploiement (vérifier que le .htaccess est bien celui servi en prod, pas un
  ancien cache Hostinger).
