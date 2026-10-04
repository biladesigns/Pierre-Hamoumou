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

### 2026-09-23 — Audit externe : le "profil de liens toxique" est une fausse alerte
Un cabinet tiers (Meera Marketing) a démarché le client avec un audit annonçant 160 backlinks /
91 domaines référents de mauvaise qualité, Authority Score SEMrush 2/100, et recommandant en
priorité absolue un désaveu de liens. Vérifié à la source : le rapport Liens de la GSC affiche
**6 liens externes / 5 domaines référents** (biladesigns.com, consulter-avocat.fr, addurl.in,
findit.co.in, x.com), et les Actions manuelles indiquent "aucun problème détecté". Aucun désaveu
ne sera fait. **Why:** SEMrush indexe son propre historique de crawl, pas ce que Google compte ;
un AS bas sur un domaine de moins d'un an est mécanique, pas un symptôme. **How to apply:** ne
jamais rouvrir ce sujet sans une action manuelle avérée dans la GSC. Le disavow est déconseillé
par Google hors pénalité.

### 2026-09-23 — URLs à encodage cassé corrigées, contact-2.html volontairement laissée
`droit-de-la-s-curit-sociale-2.html` → `droit-de-la-securite-sociale.html` et
`honoraires-individualis-s.html` → `honoraires.html`, avec 301 et maillage interne repris.
`contact-2.html` n'est pas renommée : conflit avec le répertoire `/contact/` (déjà cible d'une
301) et aucun enjeu de mot-clé sur une page contact. **How to apply:** ne pas reproposer ce
renommage chaque mois, le gain est nul et le risque technique réel.

### 2026-10-04 — Le compteur « 3 pages indexées » de la GSC est un faux signal
Le rapport Indexation affichait 3 pages indexées, données figées au 19/09, soit avant tout le
travail du 23/09. Trois sources le contredisent : la recherche `site:` liste 10 URL dans l'index,
le rapport HTTPS de la GSC en compte 10, et le rapport Fils d'Ariane détecte le schema posé le
23/09. **How to apply:** ne jamais conclure à partir du seul rapport Indexation, toujours
recouper avec `site:` et l'inspection d'URL. Vérifier la date de dernière mise à jour du rapport
avant de l'interpréter.

### 2026-10-04 — Poids du site divisé par onze, sans changement de mise en page
La page d'accueil chargeait 2,5 Mo. Causes : 4,8 Mo d'images dans le dépôt (dont un doublon
exact de 1,6 Mo et 2,2 Mo de fichiers orphelins), des logos de 1482 px servis pour un affichage
en 48 px, et surtout `cdn.tailwindcss.com`, soit 397 Ko de JavaScript recompilant le CSS dans le
navigateur à chaque visite. Corrigé : WebP avec repli JPEG via `<picture>`, lazy loading,
dimensions déclarées, et Tailwind compilé en 27 Ko de CSS. Accueil ramené à 214 Ko.
**How to apply:** ne pas remettre de CDN Tailwind. Si une classe utilitaire nouvelle est ajoutée
au HTML, régénérer `tailwind.css` (Tailwind v3, scan des fichiers HTML) sinon elle n'aura aucun
effet.

### 2026-10-04 — Cormorant Garamond ne s'appliquait pas aux titres
Effet de bord découvert en compilant le CSS : le style injecté par le CDN écrasait la règle du
site appliquant Cormorant Garamond aux titres, qui s'affichaient donc dans la serif système
alors que la police était bien téléchargée depuis Google Fonts. La bascule en CSS compilé
restaure la typographie prévue. Seul changement visuel de l'opération, hauteur de page identique
au pixel.

### 2026-10-04 — Les polices du site ne se chargeaient pas, depuis l'origine
L'URL Google Fonts du site renvoyait **HTTP 400**. Avec deux axes variables, chaque graisse doit
être un tuple complet : `opsz,wght@9..40,300;400;500` est invalide, il fallait
`9..40,300;9..40,400;9..40,500`. La requête entière échouait, donc ni DM Sans ni Cormorant
Garamond n'étaient téléchargées et le site s'affichait en polices système.
Mis en évidence par mesure : un texte en Cormorant Garamond faisait exactement la même largeur
qu'en serif générique (773 px), et `document.fonts` était vide.
Les deux polices sont désormais hébergées sur le site (2 fichiers variables, 97 Ko).
**How to apply:** ne jamais se fier au `font-family` calculé pour conclure qu'une police est
active, il reflète la déclaration CSS et non le téléchargement. Mesurer la largeur d'un texte
témoin ou lire `document.fonts`.

### 2026-10-04 — Dépendances externes supprimées, rien ne sort plus du domaine
Tailwind CDN, Iconify et Google Fonts chargeaient du code tiers à chaque visite. Tout est
désormais servi depuis le domaine. Seule connexion externe restante : les 4 iframes Google Maps,
déjà en `loading="lazy"`. **À arbitrer avec le client :** ces iframes transmettent l'IP du
visiteur à Google et déposent des cookies sans consentement préalable, ce qui mérite un avis
pour un cabinet d'avocats. Une façade cliquable réglerait le point, c'est une décision de sa part.

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
- 2026-09-23 : audit externe reçu via le client. Seul point fondé retenu et corrigé (URLs à
  encodage cassé). Fausse alerte sur les liens toxiques documentée ci-dessus. Le second document
  du même cabinet affirmait l'absence de sitemap, contredit en direct.
- 2026-09-23 : création de la rubrique `/articles/` (hub + 2 analyses) dans la DA du site, avec
  schema Article et BreadcrumbList, CTA de contact en fin d'article, lien Actualités ajouté à la
  nav des 9 pages, sitemap porté à 12 URL et resoumis dans la GSC.
  Articles : TJ Poitiers 10/07/2026 n° 25/00289 (traitements automatisés, R. 243-59-1, dossier
  plaidé par le cabinet) et Cass. 2e civ. 03/09/2026 n° 24-11.310 (multi-établissements : taux
  unique illicite, charge de la preuve sur l'URSSAF, annulation totale du chef calculé
  irrégulièrement). Vérifier le 23/10/2026 s'ils sont indexés et s'ils génèrent des impressions.
- 2026-09-23 : **piège jurisprudence noté.** La 2e chambre civile a rendu plusieurs arrêts le
  3 septembre 2026 en matière de sécurité sociale (23-22.988 faute inexcusable, 23-23.281,
  24-11.310 contrôle URSSAF, 24-13.178). Un premier article avait été écrit sur le 23-22.988,
  qui n'était pas celui retenu par le client, et a été retiré avant toute exploration par Google.
  **How to apply:** pour toute décision fournie par le client, exiger le numéro de pourvoi et le
  vérifier à la source avant d'écrire. Une date et une chambre ne suffisent pas à identifier un
  arrêt. Légifrance bloque l'accès automatisé, passer par courdecassation.fr (Judilibre).
- 2026-09-23 : demande d'indexation faite pour `/articles/`. **Quota journalier Google atteint**
  avant de pouvoir soumettre les deux articles eux-mêmes. À refaire au prochain passage.
- 2026-09-23 : `tools/seo-check.py` corrigé, il ne scannait que `*/index.html` et levait une
  fausse alerte "URL fantôme" sur tout article en sous-répertoire.
- 2026-10-04 : demande d'indexation pour `droit-de-la-securite-sociale.html`, sortie de l'index
  après le renommage du 23/09. L'article multi-établissements, lui, était déjà indexé.
- 2026-10-04 : optimisation des médias (4,8 Mo -> 409 Ko) et passage de Tailwind CDN à une
  feuille compilée de 27 Ko. Accueil : 2503 Ko -> 214 Ko. Vérifier au prochain passage si les
  Core Web Vitals sortent de « Aucune donnée » dans la GSC, ce qui demande un minimum de trafic.
- 2026-10-04 : chaîne de dépendances externes supprimée (Tailwind CDN 397 Ko, Iconify 21 Ko,
  Google Fonts en erreur 400). Page d'accueil : 2503 Ko théoriques avant, 109 Ko réellement
  transférés après (Brotli actif, cache public 7 jours). 7 requêtes au total.
- 2026-10-04 : vérifié et sans suite, compression Brotli et cache serveur déjà bien configurés
  chez l'hébergeur, les 4 iframes Maps déjà en chargement différé. Ne pas reproposer.
