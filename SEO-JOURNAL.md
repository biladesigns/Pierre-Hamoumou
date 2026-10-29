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

### 2026-10-05 — Maillage interne : la money page n'émettait aucun lien
Audit des liens contextuels, c'est-à-dire hors menu et pied de page, qui sont identiques sur
toutes les pages et n'orientent donc rien. `faq.html` était totalement isolée (0 entrant,
0 sortant) et `droit-de-la-securite-sociale.html`, la page la plus stratégique, recevait 3 liens
sans jamais en émettre. Corrigé : section « Dernières analyses » sur la page sécurité sociale,
section « Pour aller plus loin » en bas de FAQ, liens FAQ en fin d'article. La FAQ passe à
3 entrants et 3 sortants, la page sécurité sociale à 4 et 4, plus aucune page orpheline.
**How to apply:** compter les liens du menu et du pied de page dans un audit de maillage donne
une fausse impression de bonne santé. Les exclure avant de conclure.

### 2026-10-05 — Toute régénération du CSS impose de changer la version dans l'URL
L'hébergeur sert `tailwind.css` avec un cache de 7 jours. Après régénération, un visiteur
récurrent gardait l'ancienne feuille et voyait les sections récentes mal mises en page, car leurs
classes utilitaires n'y figuraient pas. L'URL porte désormais l'empreinte du fichier
(`?v=02f5c867`). `tools/seo-check.py` compare l'empreinte réelle à celle référencée dans les
pages et signale tout écart. **How to apply:** après chaque ajout de classes Tailwind au HTML,
régénérer le CSS **et** mettre à jour `?v=`, sinon le rendu casse pour les visiteurs en cache.

### 2026-10-15 — Deux optimisations tirées de la donnée, pas de l'intuition
`avocat urssaf lyon` génère 87 impressions et aucun clic. Vérification de la SERP réelle : le
site y ressort en page 1, autour de la 8e place, face à des cabinets lyonnais comparables, sans
média ni mur d'autorité. Son title ne contenait pas le mot « avocat », que les cinq concurrents
classés devant ont tous. Corrigé en « Avocat URSSAF à Lyon | Contrôle et redressement ».
Par ailleurs `redressement urssaf sur combien d'années` plaçait le site en position 15 alors que
le sujet n'était traité sur aucune page : question ajoutée à la FAQ, contenu visible et schema
FAQPage, avec les articles L. 244-3 et L. 244-11 du code de la sécurité sociale vérifiés à la
source. **How to apply:** la position moyenne de la GSC est une moyenne tous appareils et toutes
localisations ; elle peut afficher 22 alors que le site est en page 1 depuis Lyon. Toujours
ouvrir la SERP réelle avant de conclure qu'une requête est hors de portée.

### 2026-10-15 — Le compteur d'indexation s'est enfin rafraîchi
Le rapport Indexation affiche 13 pages indexées contre 3 pendant des semaines. Confirmation
rétrospective que le compteur était simplement en retard et qu'il n'y a jamais eu de bug.

### 2026-10-15 — Le clone local de Mathieu était corrompu, pas seulement en retard
`~/Documents/GitHub/Pierre-Hamoumou` était resté 54 commits en arrière et son dépôt git tombait
en timeout sur `.git/logs` et sur `mmap` (dossier protégé par macOS). Remplacé par un clone neuf,
branche `veille-juridique` reconstruite depuis les fichiers extraits, ancien dossier conservé
sous `Pierre-Hamoumou.corrompu-20261015`. **How to apply:** `~/Documents` est protégé par macOS,
un serveur de prévisualisation lancé dessus renvoie 404. Prévisualiser depuis une copie hors de
ce dossier.

### 2026-10-29 — Renommage de la money page : accepté, mais c'était le dernier

Le client a demandé de renommer `droit-de-la-securite-sociale.html` en
`droit-securite-sociale-avocat-urssaf.html`, pour mettre les mots clés dans l'URL. Accepté et fait,
avec un 301 propre et les anciennes URL aplaties (`/droit-de-la-s-curit-sociale-2.html` et
`/droit-de-la-securite-sociale/` pointent désormais directement sur la nouvelle, sans chaîne).

**Pourquoi** : le mot clé dans l'URL est un facteur très faible, et la page venait d'être renommée
le 23/09/2026 puis indexée. Un second renommage en cinq semaines coûte une période de réévaluation
par Google. Ce qui a fait pencher la balance : le renommage était groupé avec la création des 8
pages filles, donc un seul épisode de recrawl au lieu de deux.

**How to apply** : ne pas reproposer de renommer cette page. Si le client redemande un changement
d'URL sur une page indexée, dire que le gain est marginal et que le coût est réel, et proposer à la
place de créer une page dédiée sur le mot clé visé. Noter aussi que la demande initiale contenait
des accents (`droit-sécurité-sociale-avocat-urssaf`) : les URL accentuées sont exactement le bug
corrigé le 23/09/2026, elles ne doivent jamais être mises en production.

### 2026-10-29 — Une page par prestation, le hub devient un hub

Les 9 items de la page sécurité sociale ont donné 8 pages dédiées (le 9e, « accompagnement
général », était trop générique et aurait dupliqué le hub). Chaque page fait 930 à 1 290 mots de
contenu original, avec schema Service + BreadcrumbList + FAQPage, un encadré « délai clé » et, pour
les 4 pages de procédure, un composant de parcours qui situe le lecteur dans la chaîne avis,
observations, mise en demeure, contrainte.

**Pourquoi** : la comparaison GSC avec auravocats.com du 22/10 a montré que l'écart d'impressions
(21 600 contre 1 010) ne venait ni du CTR ni de la position, meilleurs chez Hamoumou, mais du
nombre de requêtes couvertes : 958 contre 42. Le levier est la surface, pas la qualité.

**How to apply** : les pages sont générées par `tools/gen-prestations.py`, contenu compris. Pour
modifier une page, modifier le script et le relancer, jamais le HTML directement. Le script refuse
d'écrire s'il détecte un tiret cadratin ou demi-cadratin.

### 2026-10-29 — Toujours exiger le numéro de pourvoi, et vérifier les délais en double source

Les délais cités sur les nouvelles pages (30 jours pour l'avis, 30 ou 60 pour les observations,
2 mois pour la CRA, 15 jours pour l'opposition, 3 mois de durée de contrôle, prescription 3 ou 5
ans) ont tous été recoupés sur au moins deux sources indépendantes. Légifrance bloque
l'automatisation, les identifiants LEGIARTI renvoient des 404.

**How to apply** : passer par les décisions relayées sur doctrine.fr, les analyses de cabinets et
les fiches officielles, et ne jamais publier un délai vu sur une seule source. Attention aux
délais périmés qui circulent encore : 15 jours pour l'avis de contrôle (devenu 30 en avril 2023) et
1 mois pour la CRA (devenu 2 mois au 1er janvier 2017).

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
- 2026-10-05 : `droit-de-la-securite-sociale.html` confirmée dans l'index, la demande du 04/10 a
  fonctionné. `honoraires.html` apparaît encore sous son ancienne URL dans les résultats, la 301
  n'est pas encore digérée, c'est normal et sans action.
- 2026-10-05 : maillage interne repris, versionnement du CSS mis en place, contrôle d'empreinte
  ajouté au script mensuel. Vérifier au prochain passage si les deux articles et la page
  honoraires sont passés à leur URL définitive dans l'index.
- 2026-10-15 : 28 derniers jours contre les 28 précédents : 32 clics contre 16, 560 impressions
  contre 245. Les deux articles pèsent 6 clics et 107 impressions à eux seuls, soit plus que la
  page postulation sur trois mois. Title de la page URSSAF réécrit et question sur la
  prescription ajoutée à la FAQ, recrawl demandé. Vérifier le 15/11 si `avocat urssaf lyon`
  commence à convertir des impressions en clics.
- 2026-10-15 : deux articles d'octobre rédigés à la demande du client (réponse à la veille
  d'octobre) : opposition à contrainte après le décret n° 2026-683 (substitution du jugement,
  prescription 3 ans / 10 ans, Cass. 2e civ. 04/11/2021 n° 20-18.355 vérifié sur Judilibre) et
  charte du cotisant contrôlé (Cass. 2e civ. 24/09/2026 n° 24-12.226 F-B, et CA Metz 24/09/2026
  RG 23/00323, dossier plaidé par le cabinet, tous deux vérifiés sur Judilibre). Hub, section
  « Dernières analyses » et sitemap mis à jour. Publiés le 19/10 sur demande de Mathieu,
  sans attendre la relecture du client (brouillon de relecture préparé). Demander l'indexation
  des deux URL. Vérifier le 19/11 leur indexation et leurs premières impressions.
- 2026-10-29 : à la demande du client, création de 8 pages de prestation à partir des items de la
  page sécurité sociale, et renommage du hub en `droit-securite-sociale-avocat-urssaf.html`.
  Le site passe de 14 à 22 URL au sitemap. Maillage : chaque nouvelle page reçoit 2 à 8 liens
  éditoriaux (hub, FAQ, articles, pages soeurs), aucune page orpheline. Effet attendu : hausse du
  nombre de requêtes couvertes en GSC, qui est le vrai écart avec auravocats.com. Mesure le
  2026-11-29 : le nombre de requêtes distinctes doit dépasser 70 (contre 42 au 22/10), et au moins
  4 des 8 nouvelles pages doivent générer des impressions. Invalidé si, passé un mois, les pages
  sont indexées mais ne remontent sur aucune requête, ce qui signifierait que le sujet est trop
  concurrentiel pour l'autorité actuelle du domaine et qu'il faut viser des requêtes plus longues.
- 2026-10-29 : corrigé au passage, la politique de confidentialité déclarait encore Google Fonts
  comme destinataire alors que les polices sont auto-hébergées depuis le 23/09/2026. Page de nature
  juridique, l'information était devenue fausse.
- 2026-10-29 : la page liquidation judiciaire mentionne le tribunal des activités économiques de
  Lyon, et non le tribunal de commerce. Depuis le 1er janvier 2025 et jusqu'au 31 décembre 2028,
  12 tribunaux de commerce dont celui de Lyon fonctionnent sous cette dénomination à titre
  expérimental et connaissent seuls des procédures collectives, quel que soit le statut du
  professionnel. Le texte du hub, antérieur, parlait encore du tribunal de commerce.
