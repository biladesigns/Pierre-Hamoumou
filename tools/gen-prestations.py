#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere les pages de prestation en droit de la securite sociale.

Chaque item de la page hub droit-securite-sociale-avocat-urssaf.html recoit sa
page dediee, avec une URL porteuse du mot cle de la procedure. La chrome (nav,
hero, CTA, footer) est identique a celle des articles pour rester dans le design
system du site.

Usage : python3 tools/gen-prestations.py
"""

import os
import re
import sys

BASE = "https://pierrehamoumou-avocat.fr"
CSS_VERSION = "3efdd4f2"
HUB = "/droit-securite-sociale-avocat-urssaf.html"
HUB_LABEL = "Droit de la securite sociale"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# Les quatre etapes de la procedure, dans l'ordre. Sert au composant parcours.
PARCOURS = [
    ("avis", "Avis de contrôle", "/avocat-avis-de-controle-urssaf.html"),
    ("observations", "Lettre d'observations", "/avocat-lettre-observations-urssaf.html"),
    ("demeure", "Mise en demeure", "/avocat-mise-en-demeure-urssaf.html"),
    ("contrainte", "Contrainte", "/avocat-contrainte-urssaf-opposition.html"),
]


# --------------------------------------------------------------------------
# Contenu
# --------------------------------------------------------------------------

PAGES = [
{
    "slug": "avocat-avis-de-controle-urssaf.html",
    "etape": "avis",
    "badge": "Procédure de contrôle",
    "h1": "Avis de contrôle URSSAF : que faire dès réception",
    "fil": "Avis de contrôle URSSAF",
    "title": "Avis de contrôle URSSAF : que faire dès réception | Avocat Lyon",
    "desc": "Vous avez reçu un avis de contrôle URSSAF. Délai de trente jours, mentions obligatoires, charte du cotisant contrôlé, durée du contrôle plafonnée. Maître Pierre Hamoumou, avocat à Lyon, intervient dès cette étape.",
    "og_desc": "Délai de trente jours, mentions obligatoires, charte du cotisant contrôlé, durée plafonnée à trois mois pour les entreprises de moins de vingt salariés. Ce qu'il faut vérifier et préparer dès la réception de l'avis.",
    "about": "Avis de contrôle URSSAF",
    "chapo": """L'avis de contrôle n'est pas une simple formalité administrative. Il fixe le
périmètre du contrôle, en déclenche le calendrier et contient des mentions dont l'absence peut
suffire à faire tomber l'intégralité du redressement. C'est aussi la seule fenêtre pendant laquelle
une entreprise peut encore préparer sereinement sa défense, avant que l'inspecteur n'ait formé son
opinion.""",
    "delai": ("30 jours", "L'avis doit être adressé au moins trente jours avant la date de la première visite de l'inspecteur."),
    "body": """
<p>
  Tout contrôle URSSAF doit être précédé d'un avis, adressé par un moyen donnant date certaine à sa
  réception. Depuis le décret du 12 avril 2023, cet avis doit parvenir au cotisant
  <strong>au moins trente jours avant la première visite</strong> de l'agent chargé du contrôle.
  Auparavant, le délai réglementaire n'était que de quinze jours, la charte du cotisant contrôlé
  retenant déjà trente jours en pratique.
</p>

<p>
  Une seule exception : la recherche d'une infraction de travail dissimulé dispense l'organisme
  d'adresser un avis préalable. En dehors de ce cas, l'absence d'avis, un délai de prévenance non
  respecté ou une erreur d'adresse constituent un vice de procédure susceptible d'entraîner
  l'annulation du contrôle dans son ensemble.
</p>

<h2>Les mentions que l'avis doit comporter</h2>

<p>
  L'article R. 243-59 du code de la sécurité sociale impose un contenu précis. L'avis doit indiquer
  la date de la première visite, la période soumise à vérification, la possibilité pour le cotisant
  de se faire assister du conseil de son choix, et faire état de l'existence d'un document intitulé
  « Charte du cotisant contrôlé », en précisant l'adresse électronique où il peut être consulté et
  en indiquant qu'il est adressé au cotisant sur sa demande.
</p>

<p>
  Les dispositions de cette charte sont opposables à l'URSSAF. Le défaut d'accès au document avant
  l'ouverture des opérations a longtemps constitué l'un des moyens de nullité les plus plaidés
  devant les pôles sociaux. Par un arrêt du 24 septembre 2026 publié au Bulletin, la deuxième
  chambre civile de la Cour de cassation a resserré ce moyen : dès lors que l'avis comporte les
  mentions réglementaires, l'URSSAF n'a pas à démontrer en outre que son site permettait
  effectivement de consulter et de télécharger la charte. Le même jour, la cour d'appel de Metz
  confirmait pourtant l'annulation d'un redressement sur ce terrain, dans un dossier plaidé par le
  Cabinet. La différence tenait aux diligences du cotisant et à ce qu'il était en mesure de prouver.
</p>

<p>
  Autrement dit, le moyen existe toujours, mais il se construit. Il suppose d'avoir conservé l'avis,
  son enveloppe, l'accusé de réception et la trace des démarches entreprises pour obtenir la charte.
</p>

<h2>La durée du contrôle est plafonnée</h2>

<p>
  Pour les entreprises versant des rémunérations à moins de vingt salariés et pour les travailleurs
  indépendants, l'article L. 243-13 du code de la sécurité sociale limite la durée du contrôle à
  <strong>trois mois</strong>. Cette limitation, d'abord expérimentale, a été pérennisée par la loi
  de financement de la sécurité sociale pour 2023. Les filiales d'un groupe employant au moins vingt
  salariés en sont exclues.
</p>

<p>
  Le délai court de la première visite de l'inspecteur, ou de la date de début des vérifications
  mentionnée sur l'avis en cas de contrôle sur pièces, jusqu'à l'envoi de la lettre d'observations.
  C'est bien la date d'envoi qui compte, et non celle imprimée sur le courrier : un jour de retard
  suffit à vicier la procédure. La période peut être prorogée une fois, à la demande expresse du
  cotisant ou de l'organisme.
</p>

<p>
  Le plafond tombe en revanche si l'une des situations limitativement énumérées par le texte est
  établie pendant le contrôle : travail dissimulé au sens des articles L. 8221-3 et L. 8221-5 du
  code du travail, obstacle à contrôle, abus de droit, comptabilité insuffisante, documentation
  inexploitable, ou report d'une visite demandé par le cotisant. Ces exceptions se constatent, elles
  ne se présument pas : une simple relance de l'inspecteur réclamant des pièces manquantes ne vaut
  pas constat d'une documentation inexploitable.
</p>

<h2>Préparer la visite</h2>

<p>
  Les trente jours qui précèdent la première visite servent à autre chose qu'à attendre. C'est la
  période utile pour identifier les postes exposés et reconstituer les justificatifs avant d'être
  interrogé dessus. Selon les dossiers, l'attention se porte sur les frais professionnels et leur
  justification, les avantages en nature, les indemnités de repas et de grand déplacement, le
  traitement des heures supplémentaires et des forfaits, la qualification des prestataires et des
  sous-traitants, les primes et gratifications, ou encore les taux de cotisation accidents du
  travail notifiés établissement par établissement.
</p>

<p>
  Une précision de méthode compte ici. La Cour de cassation a jugé le 25 juin 2026 que le cotisant
  ne peut pas produire pour la première fois devant le juge les pièces qu'il devait communiquer
  pendant le contrôle ou durant la phase contradictoire. Les documents utiles doivent donc être
  réunis et versés tôt, pas gardés en réserve pour l'audience.
</p>

<h2>Ce que fait le Cabinet à ce stade</h2>

<ul>
  <li>Vérification de la régularité de l'avis : délai de prévenance, mentions obligatoires, période visée, destinataire et preuve de réception.</li>
  <li>Analyse du périmètre annoncé et identification des postes de redressement probables au vu de l'activité et de la convention collective applicable.</li>
  <li>Préparation des pièces et de leur présentation, pour que les justificatifs soient disponibles au moment où l'inspecteur les demande.</li>
  <li>Cadrage des échanges avec l'inspecteur et présence du Cabinet aux étapes sensibles du contrôle.</li>
  <li>Suivi du calendrier et contrôle du respect du plafond de trois mois lorsqu'il est applicable.</li>
</ul>

<p>
  Intervenir dès l'avis coûte moins cher que contester un redressement établi. L'expérience des
  dossiers montre que la plupart des chefs de redressement se jouent sur des pièces qui existaient
  mais n'ont pas été produites au bon moment.
</p>
""",
    "faq": [
        ("Peut-on refuser un contrôle URSSAF ?",
         "Non. Le refus d'un contrôle caractérise un obstacle à contrôle, qui est sanctionné pénalement, fait tomber le plafond de durée de trois mois et autorise l'organisme à procéder par taxation forfaitaire. En revanche, il est possible de demander le report d'une visite, et il est toujours possible de contester la régularité de la procédure."),
        ("Que se passe-t-il si le délai de trente jours n'est pas respecté ?",
         "Le non-respect du délai de prévenance est un vice de procédure qui peut entraîner l'annulation du contrôle et du redressement qui en découle. Encore faut-il pouvoir établir la date de réception effective de l'avis : c'est à l'URSSAF de prouver le point de départ du délai, et l'absence de date sur l'accusé de réception a déjà suffi à faire annuler des redressements importants."),
        ("Un avis est-il obligatoire en cas de suspicion de travail dissimulé ?",
         "Non. La recherche d'une infraction de travail dissimulé dispense l'URSSAF d'adresser un avis préalable. Cette dispense s'apprécie au regard de l'objet réel du contrôle : un contrôle présenté comme portant sur le travail dissimulé mais qui porte en réalité sur l'assiette des cotisations doit respecter la procédure de droit commun."),
    ],
    "cta_h2": "Vous venez de recevoir un avis de contrôle ?",
    "cta_p": """Les trente jours qui vous séparent de la première visite sont la période la plus
utile de toute la procédure. Le Cabinet vérifie la régularité de l'avis, identifie les postes
exposés et prépare avec vous les pièces à produire.""",
    "liens": [
        ("/articles/charte-du-cotisant-controle-avis-de-controle-urssaf.html", "Charte du cotisant contrôlé : deux décisions du 24 septembre 2026, deux issues"),
        ("/avocat-lettre-observations-urssaf.html", "Étape suivante : répondre à la lettre d'observations"),
    ],
},

{
    "slug": "avocat-lettre-observations-urssaf.html",
    "etape": "observations",
    "badge": "Phase contradictoire",
    "h1": "Lettre d'observations URSSAF : répondre dans le délai de trente jours",
    "fil": "Lettre d'observations URSSAF",
    "title": "Lettre d'observations URSSAF : comment répondre | Avocat Lyon",
    "desc": "La lettre d'observations ouvre un délai de trente jours, prorogeable à soixante. Une réponse motivée peut faire abandonner tout ou partie du redressement. Maître Pierre Hamoumou, avocat à Lyon.",
    "og_desc": "Délai de trente jours prorogeable à soixante, contenu d'une réponse utile, pièces à produire impérativement à ce stade. L'étape où un redressement se gagne ou se perd.",
    "about": "Lettre d'observations URSSAF",
    "chapo": """La lettre d'observations est la pièce centrale du contrôle. Elle acte les
constatations de l'inspecteur, chiffre le redressement envisagé et ouvre la seule phase où le
cotisant peut encore discuter les griefs avant que l'URSSAF ne passe au recouvrement. C'est l'étape
où un dossier se gagne ou se perd, et c'est aussi celle que les entreprises traitent le plus
souvent seules.""",
    "delai": ("30 jours", "Délai de réponse à compter de la réception, porté à soixante jours sur simple demande formulée avant son expiration."),
    "body": """
<p>
  À l'issue de ses vérifications, l'inspecteur communique ses observations par lettre. Le document
  énumère les chefs de redressement, indique pour chacun le fondement juridique retenu, la période
  concernée et le montant correspondant. Il mentionne le délai de réponse et la possibilité de se
  faire assister du conseil de son choix.
</p>

<p>
  Le cotisant dispose de <strong>trente jours</strong> pour formuler ses observations. Tant que ce
  délai n'est pas expiré, et tant que l'inspecteur n'a pas répondu, l'URSSAF ne peut pas adresser de
  mise en demeure. Une mise en demeure envoyée prématurément est irrégulière.
</p>

<h2>Porter le délai à soixante jours</h2>

<p>
  Depuis le décret du 11 octobre 2019, le cotisant peut demander à disposer de soixante jours au
  lieu de trente. Deux conditions pratiques méritent d'être retenues. La demande doit
  <strong>parvenir à l'URSSAF avant l'expiration du délai initial</strong> de trente jours. Et
  l'absence de réponse de l'organisme vaut acceptation de la prolongation.
</p>

<p>
  La jurisprudence invite à la prudence sur la preuve. Dans une affaire jugée par la cour d'appel de
  Grenoble, la société soutenait avoir demandé la prorogation par courriel ; l'URSSAF soutenait ne
  l'avoir jamais reçue, l'adresse électronique utilisée étant erronée. La demande se fait donc par
  un moyen donnant date certaine à sa réception, et la preuve d'envoi se conserve.
</p>

<h2>Ce que contient une réponse utile</h2>

<p>
  Une réponse efficace n'est pas une lettre de contestation générale. Elle traite chaque chef de
  redressement séparément, et sur deux terrains distincts.
</p>

<p>
  Le premier terrain est celui de la procédure. L'avis de contrôle était-il régulier et son délai de
  prévenance respecté ? La durée du contrôle a-t-elle excédé le plafond légal lorsqu'il était
  applicable ? Les sommes réclamées sont-elles atteintes par la prescription de trois ans ? La
  lettre d'observations indique-t-elle, pour chaque chef, le mode de calcul retenu et les éléments
  qui le fondent ? Un redressement opéré par extrapolation ou par traitement automatisé respecte-t-il
  les conditions de l'article R. 243-59-1, qui subordonne cette méthode à l'accord du cotisant ?
</p>

<p>
  Le second terrain est celui du fond : la qualification juridique retenue, l'assiette appliquée, la
  convention collective ou l'accord d'entreprise opposable, les justificatifs de frais
  professionnels, les barèmes et les plafonds applicables à la période contrôlée. C'est sur ce
  terrain que les pièces comptent.
</p>

<p>
  L'article R. 243-59 impose à l'inspecteur de répondre de manière motivée à chaque observation
  formulée de façon circonstanciée. Une contestation précise oblige donc l'organisme à se
  positionner, et prépare le contentieux ultérieur. Une contestation vague n'oblige à rien.
</p>

<h2>Deux pièges à connaître</h2>

<p>
  <strong>Les pièces doivent être produites maintenant.</strong> Par un arrêt du 25 juin 2026, la
  Cour de cassation a jugé que le cotisant ne peut pas produire pour la première fois devant le juge
  les documents qu'il devait communiquer pendant le contrôle ou durant la phase contradictoire.
  Garder des justificatifs en réserve pour l'audience n'est plus une stratégie, c'est une perte de
  moyens.
</p>

<p>
  <strong>La réponse de l'inspecteur ne rouvre pas le débat.</strong> La Cour de cassation a précisé
  le 29 janvier 2026 que la réponse de l'inspecteur aux observations du cotisant n'ouvre pas, au
  bénéfice de ce dernier, une nouvelle période contradictoire. Il n'y a donc pas de second tour :
  tout ce qui doit être dit se dit dans la réponse initiale.
</p>

<h2>Ce que fait le Cabinet à ce stade</h2>

<ul>
  <li>Analyse chef par chef de la lettre d'observations, en distinguant les griefs contestables au fond de ceux qui ne le sont pas.</li>
  <li>Examen systématique de la régularité de la procédure suivie depuis l'avis de contrôle, et de la prescription des sommes réclamées.</li>
  <li>Demande de prorogation du délai lorsque le volume du dossier le justifie, par un moyen donnant date certaine.</li>
  <li>Rédaction de la réponse motivée, poste par poste, avec les pièces justificatives correspondantes.</li>
  <li>Échanges complémentaires avec l'inspecteur et, le cas échéant, préparation immédiate du recours devant la commission de recours amiable.</li>
</ul>

<p>
  Une réponse structurée conduit régulièrement à l'abandon de chefs de redressement entiers. Dans un
  dossier plaidé par le Cabinet devant le tribunal judiciaire de Poitiers, soixante-trois chefs de
  redressement ont été annulés et le montant initialement réclamé a été ramené à la baisse, le
  recours à un traitement automatisé n'ayant pas respecté les conditions légales.
</p>
""",
    "faq": [
        ("Faut-il obligatoirement répondre à une lettre d'observations ?",
         "Ce n'est pas une obligation, mais l'absence de réponse laisse le redressement en l'état et prive le cotisant d'un moyen utile. Surtout, elle le prive de la possibilité de produire des pièces : depuis l'arrêt du 25 juin 2026, les justificatifs qui devaient être communiqués pendant la phase contradictoire ne peuvent plus l'être pour la première fois devant le juge."),
        ("Combien de temps l'URSSAF a-t-elle pour répondre ?",
         "Aucun délai n'est imposé à l'inspecteur pour répondre aux observations du cotisant. En revanche, il doit répondre de manière motivée à chaque observation formulée de façon circonstanciée, et la mise en demeure ne peut pas être adressée avant cette réponse ni avant l'expiration du délai de réponse du cotisant."),
        ("Peut-on encore négocier après la lettre d'observations ?",
         "La phase contradictoire est précisément le moment des échanges. Des discussions complémentaires avec l'inspecteur sont possibles et fréquentes, notamment sur le chiffrage. En revanche, la réponse de l'inspecteur clôt le débat : elle n'ouvre pas de nouvelle période contradictoire."),
    ],
    "cta_h2": "Vous avez reçu une lettre d'observations ?",
    "cta_p": """Le délai est de trente jours, et il peut être porté à soixante à condition de le
demander à temps. Le Cabinet analyse chaque chef de redressement, vérifie la régularité de la
procédure et rédige la réponse motivée avec les pièces utiles.""",
    "liens": [
        ("/articles/controle-urssaf-traitements-automatises.html", "Redressement par traitement automatisé : soixante-trois chefs annulés"),
        ("/avocat-mise-en-demeure-urssaf.html", "Étape suivante : contester la mise en demeure"),
    ],
},

{
    "slug": "avocat-mise-en-demeure-urssaf.html",
    "etape": "demeure",
    "badge": "Recours amiable",
    "h1": "Mise en demeure URSSAF : contester dans le délai de deux mois",
    "fil": "Mise en demeure URSSAF",
    "title": "Mise en demeure URSSAF : contester devant la CRA | Avocat Lyon",
    "desc": "La mise en demeure ouvre un délai de deux mois pour saisir la commission de recours amiable. Passé ce délai, les voies de contestation se referment. Maître Pierre Hamoumou, avocat à Lyon.",
    "og_desc": "Délai de deux mois pour saisir la commission de recours amiable, mentions obligatoires, prescription de trois ans, conséquences d'un recours tardif.",
    "about": "Mise en demeure URSSAF",
    "chapo": """La mise en demeure est l'acte qui transforme des observations en créance exigible.
Elle conditionne toute action ultérieure de l'URSSAF et ouvre un délai de deux mois pour saisir la
commission de recours amiable. Laisser passer ce délai ne supprime pas la dette : cela supprime la
plupart des moyens de la discuter.""",
    "delai": ("2 mois", "Délai pour saisir la commission de recours amiable, à compter de la notification de la mise en demeure."),
    "body": """
<p>
  La mise en demeure intervient après la phase contradictoire. Elle invite le cotisant à régulariser
  sa situation et constitue le préalable obligatoire à toute mesure de recouvrement forcé. Son
  contenu est encadré : elle doit permettre à l'intéressé de connaître la nature, la cause et
  l'étendue de son obligation, en précisant la nature des cotisations réclamées, les périodes
  concernées, les montants en principal et en majorations, ainsi que les voies et délais de recours.
</p>

<p>
  Une mise en demeure insuffisamment motivée est irrégulière. De même, sa date d'envoi compte :
  c'est à l'URSSAF de justifier de cette date, et une mise en demeure tardive permet au cotisant
  d'opposer la prescription et de faire tomber une année de redressement.
</p>

<h2>Le recours devant la commission de recours amiable</h2>

<p>
  La contestation passe d'abord par la commission de recours amiable de l'organisme, saisie dans le
  délai de <strong>deux mois à compter de la notification</strong>. Ce délai était d'un mois
  jusqu'au 31 décembre 2016, ce qui explique que des sources anciennes circulent encore. La saisine
  se fait par écrit, et de préférence par lettre recommandée avec avis de réception afin de disposer
  d'une date certaine.
</p>

<p>
  Il faut veiller à contester le bon acte. Le tribunal judiciaire de Versailles a ainsi jugé
  prématurée une saisine dirigée contre un courrier de l'inspecteur et non contre la mise en
  demeure : le point de départ du délai de deux mois est la mise en demeure elle-même.
</p>

<p>
  La commission dispose de deux mois pour se prononcer. Son silence vaut rejet implicite, ce qui
  ouvre la voie du pôle social du tribunal judiciaire. Le recours juridictionnel doit alors être
  formé dans les deux mois de la décision, expresse ou tacite. Pour saisir le tribunal sur le
  fondement d'un rejet implicite, il faut pouvoir justifier que les deux mois se sont effectivement
  écoulés.
</p>

<h2>La prescription, à vérifier systématiquement</h2>

<p>
  Les cotisations et contributions sociales se prescrivent par <strong>trois ans</strong> à compter
  de la fin de l'année civile au titre de laquelle elles sont dues, en application des articles
  L. 244-3 et L. 244-11 du code de la sécurité sociale. Ce délai est porté à cinq ans en cas
  d'infraction de travail illégal, le travail dissimulé donnant par ailleurs lieu à une majoration de
  vingt-cinq pour cent des cotisations mises en recouvrement.
</p>

<p>
  La prescription est un moyen à soulever tôt, et à calculer précisément. Elle se vérifie poste par
  poste et période par période, car un même redressement peut être partiellement prescrit.
</p>

<h2>Le délai de deux mois est un verrou</h2>

<p>
  Le cotisant qui n'a pas contesté la mise en demeure devant la commission de recours amiable ne
  dispose plus, en pratique, que de l'opposition à contrainte pour faire valoir ses moyens de fond.
  La cour d'appel de Caen l'a rappelé : c'est alors la seule voie de recours effective qui lui
  reste. Encore faut-il qu'une contrainte soit effectivement signifiée, et le délai d'opposition
  n'est alors que de quinze jours.
</p>

<p>
  Il est donc rarement avisé d'attendre la contrainte en pensant se défendre plus tard. La fenêtre de
  deux mois est à la fois plus large et plus confortable.
</p>

<h2>Ce que fait le Cabinet à ce stade</h2>

<ul>
  <li>Contrôle de la validité de la mise en demeure : motivation, nature et périodes des cotisations, montants, voies de recours, date d'envoi et preuve de notification.</li>
  <li>Calcul de la prescription, poste par poste et période par période.</li>
  <li>Reprise des moyens de procédure nés en amont, depuis l'avis de contrôle jusqu'à la réponse de l'inspecteur.</li>
  <li>Rédaction et dépôt du recours devant la commission de recours amiable dans le délai de deux mois.</li>
  <li>Saisine du pôle social du tribunal judiciaire en cas de rejet, expresse ou implicite, et représentation à l'audience.</li>
  <li>En parallèle, demande de délais de paiement ou de remise de majorations lorsque la situation de trésorerie le justifie.</li>
</ul>
""",
    "faq": [
        ("La saisine de la commission de recours amiable est-elle obligatoire ?",
         "Oui, c'est un préalable à la saisine du pôle social du tribunal judiciaire. Un recours porté directement devant le tribunal, sans passage par la commission, est irrecevable."),
        ("Que faire si le délai de deux mois est dépassé ?",
         "La mise en demeure ne peut plus être contestée devant la commission de recours amiable. Il reste la voie de l'opposition, si et quand une contrainte est signifiée, dans un délai de quinze jours. Il reste aussi, selon les cas, la demande de remise de majorations de retard et la négociation d'un échéancier, qui ne portent pas sur le principe de la dette mais sur ses modalités."),
        ("La contestation suspend-elle l'obligation de payer ?",
         "Non. Le recours devant la commission de recours amiable ne suspend pas par lui-même le recouvrement. C'est pourquoi la contestation s'accompagne souvent d'une demande de délais de paiement, afin d'éviter des mesures d'exécution pendant l'instruction du dossier."),
    ],
    "cta_h2": "Vous avez reçu une mise en demeure de l'URSSAF ?",
    "cta_p": """Le délai pour saisir la commission de recours amiable est de deux mois. Le Cabinet
vérifie la validité de l'acte, calcule la prescription et porte le recours, puis vous représente
devant le pôle social en cas de rejet.""",
    "liens": [
        ("/faq.html", "Questions fréquentes sur le contrôle et le redressement URSSAF"),
        ("/avocat-contrainte-urssaf-opposition.html", "Étape suivante : former opposition à la contrainte"),
    ],
},

{
    "slug": "avocat-contrainte-urssaf-opposition.html",
    "etape": "contrainte",
    "badge": "Recouvrement forcé",
    "h1": "Contrainte URSSAF : former opposition dans les quinze jours",
    "fil": "Contrainte URSSAF",
    "title": "Contrainte URSSAF : opposition en quinze jours | Avocat Lyon",
    "desc": "La contrainte vaut titre exécutoire et permet les saisies. Le délai d'opposition devant le pôle social n'est que de quinze jours. Maître Pierre Hamoumou, avocat à Lyon, prend en charge la procédure.",
    "og_desc": "Délai de quinze jours, forme de l'opposition, calcul du délai, moyens de défense et réforme entrée en vigueur le 1er octobre 2026.",
    "about": "Opposition à contrainte URSSAF",
    "chapo": """La contrainte est l'outil de recouvrement forcé de l'URSSAF. Elle est souvent reçue
comme une formalité de plus après la mise en demeure, alors qu'elle vaut titre exécutoire et ouvre
la voie aux saisies. Le délai pour la contester est de quinze jours. Passé ce délai, elle comporte
tous les effets d'un jugement.""",
    "delai": ("15 jours", "Délai pour former opposition, à compter de la signification ou de la notification de la contrainte."),
    "body": """
<p>
  Lorsque la mise en demeure reste sans effet, le directeur de l'organisme peut décerner une
  contrainte, en application des articles L. 244-9 et R. 133-3 du code de la sécurité sociale. Le
  cotisant dispose alors de <strong>quinze jours</strong> à compter de sa signification par
  commissaire de justice, ou de sa notification, pour former opposition devant le pôle social du
  tribunal judiciaire.
</p>

<p>
  À défaut d'opposition dans ce délai, la contrainte comporte tous les effets d'un jugement et
  confère notamment le bénéfice de l'hypothèque judiciaire. Elle devient le titre sur lequel
  l'URSSAF s'appuie pour pratiquer des mesures d'exécution forcée : saisie des comptes bancaires,
  saisie-attribution auprès des clients, inscription de sûretés.
</p>

<h2>Calculer le délai correctement</h2>

<p>
  Le délai de quinze jours se compte selon les règles du code de procédure civile. Le jour de l'acte
  qui le fait courir ne compte pas, en application de l'article 641. Le délai expire le dernier jour
  à vingt-quatre heures, et s'il tombe un samedi, un dimanche ou un jour férié ou chômé, il est
  prorogé jusqu'au premier jour ouvrable suivant.
</p>

<p>
  Le point de départ est la date de signification lorsque la contrainte est délivrée par commissaire
  de justice. Une opposition formée au-delà est irrecevable pour forclusion, et la contrainte devient
  définitive. C'est le cas de figure le plus fréquent, et le plus difficile à rattraper.
</p>

<h2>La forme de l'opposition</h2>

<p>
  L'opposition se forme par inscription au secrétariat du tribunal compétent, ou par lettre
  recommandée avec demande d'avis de réception. Le tribunal compétent est celui du lieu où le
  débiteur est domicilié. L'opposition doit être <strong>motivée</strong>, et une copie de la
  contrainte contestée doit y être jointe. Le secrétariat informe ensuite l'organisme créancier dans
  les huit jours de la réception.
</p>

<p>
  L'acte de signification ou de notification doit lui-même, à peine de nullité, mentionner la
  référence de la contrainte et son montant, le délai dans lequel l'opposition doit être formée,
  l'adresse du tribunal compétent et les formes requises pour sa saisine. Ces mentions se vérifient.
</p>

<h2>Depuis le 1er octobre 2026, le jugement se substitue à la contrainte</h2>

<p>
  Le décret n° 2026-683 du 27 juillet 2026 a modifié l'article R. 133-3 : la décision du tribunal
  qui statue sur l'opposition se substitue désormais à la contrainte, et elle est exécutoire de
  droit à titre provisoire. La règle s'applique à toutes les décisions rendues depuis le 1er octobre
  2026, y compris sur des oppositions formées auparavant. Derrière une modification d'apparence
  technique, ce sont la durée des poursuites et la stratégie à adopter dès la signification qui sont
  en jeu.
</p>

<h2>Les moyens de défense</h2>

<p>
  L'opposition à contrainte permet de discuter l'ensemble de la chaîne, et pas seulement la
  contrainte elle-même. Sont utilement examinés la régularité de l'avis de contrôle et le respect du
  délai de prévenance, la durée du contrôle au regard du plafond légal, la motivation de la lettre
  d'observations et le respect de la phase contradictoire, la validité et la date d'envoi de la mise
  en demeure, la prescription des sommes réclamées, le bien-fondé de chaque chef de redressement, et
  enfin les mentions de la contrainte et de son acte de signification.
</p>

<p>
  Pour le cotisant qui n'a pas saisi la commission de recours amiable dans les deux mois de la mise
  en demeure, l'opposition à contrainte constitue la seule voie de recours effective sur le fond.
  Elle mérite d'autant plus d'être soignée.
</p>

<h2>Ce que fait le Cabinet à ce stade</h2>

<ul>
  <li>Vérification immédiate du délai et de sa computation, pour sécuriser la recevabilité de l'opposition.</li>
  <li>Contrôle des mentions de la contrainte et de l'acte de signification.</li>
  <li>Formation de l'opposition motivée devant le pôle social du tribunal judiciaire compétent, avec la copie de la contrainte.</li>
  <li>Construction des moyens sur toute la chaîne procédurale, de l'avis de contrôle à la contrainte, et examen de la prescription.</li>
  <li>Représentation à l'audience et plaidoirie pour l'annulation totale ou partielle du titre.</li>
  <li>Demande de délais de paiement ou de remise de majorations en parallèle lorsque la trésorerie l'impose.</li>
</ul>
""",
    "faq": [
        ("Le délai de quinze jours est dépassé, que faire ?",
         "L'opposition est en principe irrecevable pour forclusion et la contrainte devient définitive. Deux vérifications restent utiles. D'une part, le calcul du délai lui-même, car le jour de l'acte ne compte pas et un délai expirant un samedi, un dimanche ou un jour férié est prorogé au premier jour ouvrable. D'autre part, les mentions de l'acte de signification, dont l'absence est sanctionnée par la nullité."),
        ("L'opposition suspend-elle les saisies ?",
         "L'opposition conteste le titre, mais depuis le 1er octobre 2026 la décision statuant sur l'opposition est exécutoire de droit à titre provisoire. La situation s'apprécie au cas par cas, et il est souvent nécessaire d'engager en parallèle des démarches sur les mesures d'exécution déjà pratiquées."),
        ("Quel tribunal est compétent ?",
         "Le pôle social du tribunal judiciaire du lieu où le débiteur est domicilié. L'opposition se forme par inscription au secrétariat de ce tribunal ou par lettre recommandée avec avis de réception, et doit être motivée et accompagnée d'une copie de la contrainte."),
    ],
    "cta_h2": "Une contrainte vous a été signifiée ?",
    "cta_p": """Le délai d'opposition est de quinze jours et il ne se rattrape pas. Le Cabinet
examine la contrainte, la mise en demeure qui la précède et la prescription des sommes réclamées,
forme l'opposition et vous représente devant le pôle social.""",
    "liens": [
        ("/articles/opposition-contrainte-urssaf-jugement-se-substitue.html", "Ce que change la réforme du 1er octobre 2026 sur l'opposition à contrainte"),
        ("/assignation-liquidation-judiciaire-urssaf.html", "Si l'URSSAF assigne en liquidation judiciaire"),
    ],
},

{
    "slug": "controle-urssaf-secteurs-exposes.html",
    "etape": None,
    "badge": "Expertise sectorielle",
    "h1": "Contrôle URSSAF : les secteurs les plus exposés",
    "fil": "Secteurs exposés au contrôle URSSAF",
    "title": "Contrôle URSSAF par secteur : transport, BTP, sécurité, intérim | Avocat",
    "desc": "Transport routier, sécurité privée, BTP, propreté, travail temporaire, restauration : les postes de redressement URSSAF propres à chaque secteur et la défense adaptée. Maître Pierre Hamoumou, avocat à Lyon.",
    "og_desc": "Les postes de redressement URSSAF récurrents par secteur d'activité et les moyens de défense correspondants : transport routier, sécurité privée, BTP, propreté, travail temporaire, restauration.",
    "about": "Contrôle URSSAF sectoriel",
    "chapo": """Certains secteurs concentrent les contrôles URSSAF, parce que leur organisation du
travail produit mécaniquement des zones de friction : temps annexes, majorations conventionnelles,
frais professionnels, recours à la sous-traitance. Les chefs de redressement y sont prévisibles, ce
qui permet de les anticiper et de les contester sur le terrain de la convention collective
applicable.""",
    "delai": None,
    "body": """
<p>
  Un contrôle URSSAF ne se défend pas de la même manière dans une entreprise de transport et dans un
  restaurant. Le droit applicable est le même, mais les postes redressés, les pièces à produire et
  les arguments qui portent dépendent étroitement de la convention collective et des usages du
  secteur. Le Cabinet intervient particulièrement dans les activités suivantes.
</p>

<h2>Transport routier</h2>

<p>
  Les contrôles portent principalement sur le traitement des temps annexes : attente, chargement et
  déchargement, coupures, temps de liaison. La frontière entre temps de service et temps de repos,
  et la rémunération qui s'y attache, constitue la première source de redressement. Viennent ensuite
  les indemnités de repas et de grand déplacement, dont le régime d'exonération suppose des
  justificatifs précis et un déplacement effectif, ainsi que le traitement des heures
  d'équivalence et des majorations conventionnelles.
</p>

<h2>Sécurité privée</h2>

<p>
  Le secteur cumule les facteurs d'exposition : travail de nuit, dimanches et jours fériés,
  vacations longues, variabilité des plannings. Les redressements visent le plus souvent le calcul
  des majorations conventionnelles, les primes de panier et d'habillage, la qualification des temps
  de pause et de relève, et le traitement des heures supplémentaires sur des cycles irréguliers. La
  convention collective des entreprises de prévention et de sécurité contient des dispositions
  propres dont l'application exacte est régulièrement discutée.
</p>

<h2>Bâtiment et travaux publics</h2>

<p>
  Le BTP est au cœur des contrôles de lutte contre le travail dissimulé. La chaîne de
  sous-traitance expose le donneur d'ordre à une solidarité financière lorsqu'il n'a pas accompli
  ses obligations de vigilance, c'est-à-dire la vérification périodique de la régularité de ses
  sous-traitants. S'y ajoutent les indemnités de petit déplacement, de trajet et de transport,
  propres aux conventions du bâtiment, et le traitement des intempéries. L'enjeu est double :
  contester le redressement et démontrer que les diligences ont été accomplies.
</p>

<h2>Propreté</h2>

<p>
  La multifonctionnalité des salariés, les interventions sur plusieurs sites, la modulation du temps
  de travail et le transfert conventionnel des contrats en cas de changement de prestataire
  produisent des situations de paie complexes. Les contrôles portent sur la reconstitution des
  horaires, les temps de déplacement entre sites, le calcul des compléments d'heures et la reprise
  d'ancienneté lors des transferts.
</p>

<h2>Travail temporaire</h2>

<p>
  Les agences d'emploi supportent des obligations déclaratives propres et un risque de
  requalification élevé. Les contrôles examinent la justification du recours à l'intérim, le respect
  des cas légaux et des durées maximales, le calcul de l'indemnité de fin de mission et de
  l'indemnité compensatrice de congés payés, ainsi que l'assiette des cotisations sur les missions.
  Le régime applicable aux contrats de mission suppose une documentation rigoureuse mission par
  mission.
</p>

<h2>Restauration</h2>

<p>
  La convention collective des hôtels, cafés et restaurants concentre plusieurs postes sensibles :
  avantages en nature repas et leur évaluation, pourboires et leur régime social, extras et contrats
  d'usage, temps partiels et compléments d'heures, majorations pour travail de nuit et jours
  fériés. La reconstitution des effectifs et des horaires réels est souvent le point de départ du
  redressement.
</p>

<h2>Une défense construite sur la convention collective</h2>

<p>
  Dans tous ces secteurs, l'erreur la plus coûteuse consiste à discuter le redressement en droit
  commun alors qu'il se joue sur un texte conventionnel. Le Cabinet reprend donc systématiquement
  la convention collective et les accords d'entreprise applicables à la période contrôlée, et
  confronte la méthode de l'inspecteur aux stipulations opposables. C'est souvent là que les chefs
  de redressement tombent.
</p>

<ul>
  <li>Identification des postes exposés propres au secteur, en amont du contrôle lorsque c'est possible.</li>
  <li>Vérification de la méthode de calcul et de l'assiette retenues par l'inspecteur au regard du texte conventionnel.</li>
  <li>Contrôle du recours à l'extrapolation ou au traitement automatisé, qui suppose l'accord du cotisant.</li>
  <li>Construction du dossier de pièces justificatives adapté au secteur.</li>
  <li>Défense devant la commission de recours amiable puis devant le pôle social.</li>
</ul>
""",
    "faq": [
        ("Pourquoi certains secteurs sont-ils plus contrôlés que d'autres ?",
         "Les organismes de recouvrement orientent leurs contrôles selon des critères de risque, qui tiennent à l'organisation du travail du secteur : part des temps annexes, importance des frais professionnels exonérés, recours à la sous-traitance ou à l'intérim, complexité des majorations conventionnelles. Ces caractéristiques produisent mécaniquement davantage d'écarts, sans qu'il y ait de présomption de fraude."),
        ("Le donneur d'ordre peut-il être redressé pour son sous-traitant ?",
         "Oui, au titre de la solidarité financière, lorsqu'il n'a pas accompli ses obligations de vigilance à l'égard d'un sous-traitant en situation de travail dissimulé. La défense consiste à établir que les vérifications périodiques ont bien été effectuées et conservées, ce qui suppose une organisation documentaire en amont."),
        ("Un redressement peut-il être calculé par extrapolation ?",
         "Le recours à des méthodes de vérification par échantillonnage et extrapolation est encadré par l'article R. 243-59-1 du code de la sécurité sociale et suppose notamment que le cotisant ait été informé et n'y ait pas fait opposition. Le non-respect de ces conditions a déjà conduit à l'annulation de redressements entiers, y compris dans un dossier plaidé par le Cabinet."),
    ],
    "cta_h2": "Votre secteur est exposé aux contrôles URSSAF ?",
    "cta_p": """Transport, sécurité privée, BTP, propreté, travail temporaire, restauration : les
chefs de redressement y sont prévisibles, et donc contestables. Le Cabinet construit la défense sur
la convention collective applicable à votre activité.""",
    "liens": [
        ("/avocat-avis-de-controle-urssaf.html", "Se préparer dès la réception de l'avis de contrôle"),
        ("/articles/controle-urssaf-multi-etablissements-taux-unique.html", "Entreprise à plusieurs établissements : le taux unique est illicite"),
    ],
},

{
    "slug": "avocat-urssaf-travailleurs-independants.html",
    "etape": None,
    "badge": "Travailleurs indépendants",
    "h1": "Travailleurs indépendants : contester un appel de cotisations URSSAF",
    "fil": "Travailleurs indépendants et URSSAF",
    "title": "Cotisations URSSAF du travailleur indépendant : contester | Avocat Lyon",
    "desc": "Artisans, professions libérales, gérants majoritaires, auto-entrepreneurs : contester une régularisation, un appel provisionnel, une affiliation ou une mise en demeure URSSAF. Maître Pierre Hamoumou, avocat à Lyon.",
    "og_desc": "Régularisation, appels provisionnels, affiliation contestée, mise en demeure et contrainte : les recours ouverts au travailleur indépendant face à l'URSSAF, et leurs délais.",
    "about": "Cotisations sociales des travailleurs indépendants",
    "chapo": """Les travailleurs indépendants subissent un contentieux particulier, fait d'appels
provisionnels calculés sur des revenus anciens, de régularisations décalées dans le temps et de
mises en demeure dont les montants sont parfois sans rapport avec l'activité réelle. Les délais de
recours, eux, sont les mêmes que pour les entreprises, et tout aussi brefs.""",
    "delai": ("2 mois", "Délai pour saisir la commission de recours amiable après une mise en demeure, et quinze jours seulement pour s'opposer à une contrainte."),
    "body": """
<p>
  Artisans, commerçants, professions libérales, gérants majoritaires de société à responsabilité
  limitée, auto-entrepreneurs : les situations sont diverses mais les difficultés se répètent. Elles
  tiennent le plus souvent moins au principe de la cotisation qu'à son calcul, à sa base ou au
  rattachement de l'intéressé à un régime.
</p>

<h2>Appels provisionnels et régularisation</h2>

<p>
  Les cotisations sont d'abord appelées à titre provisionnel sur la base du revenu d'une année
  antérieure, puis régularisées lorsque le revenu réel est connu. Le mécanisme produit des écarts
  importants lorsque l'activité baisse, s'interrompt ou change de nature. Une régularisation peut
  ainsi réclamer des sommes considérables au titre d'une période où l'activité avait déjà cessé.
</p>

<p>
  Plusieurs vérifications s'imposent alors : le revenu retenu correspond-il à celui effectivement
  déclaré et à l'avis d'imposition ? La déclaration de revenus a-t-elle bien été prise en compte,
  ou l'organisme a-t-il procédé à une taxation d'office faute de déclaration ? La demande de
  recalcul des cotisations provisionnelles sur le revenu estimé de l'année en cours a-t-elle été
  formée et traitée ? Les périodes de cessation, de radiation ou de changement de régime ont-elles
  été enregistrées à la bonne date ?
</p>

<h2>Affiliation et rattachement contestés</h2>

<p>
  Un second contentieux porte sur le principe même de l'affiliation : exercice d'une activité
  regardée comme professionnelle alors qu'elle était occasionnelle, maintien d'une affiliation après
  la cessation réelle de l'activité, rattachement à un régime plutôt qu'à un autre, ou à l'inverse
  requalification d'une relation de prestation en contrat de travail, avec les conséquences qui s'y
  attachent pour le donneur d'ouvrage comme pour l'intéressé.
</p>

<p>
  Ces dossiers se jouent sur les faits et sur les pièces : contrats, factures, attestations,
  inscriptions et radiations aux registres, correspondances avec les organismes. Leur enjeu dépasse
  souvent le montant réclamé, puisqu'ils déterminent des droits à prestations.
</p>

<h2>Mise en demeure, contrainte et recouvrement</h2>

<p>
  Les voies de recours sont celles du contentieux général de la sécurité sociale. La mise en demeure
  se conteste devant la commission de recours amiable dans les <strong>deux mois</strong> de sa
  notification, puis devant le pôle social du tribunal judiciaire dans les deux mois de la décision,
  expresse ou tacite. La contrainte, elle, ne laisse que <strong>quinze jours</strong> pour former
  opposition.
</p>

<p>
  La prescription mérite une attention particulière dans ces dossiers : les cotisations se
  prescrivent par trois ans à compter de la fin de l'année civile au titre de laquelle elles sont
  dues, et un passif ancien réclamé tardivement est fréquemment prescrit pour partie.
</p>

<h2>Échéanciers et remises</h2>

<p>
  Indépendamment de la contestation au fond, la situation de trésorerie peut justifier une demande
  de délais de paiement, et une demande de remise des majorations de retard et pénalités. Ces
  démarches ne valent pas reconnaissance de la dette lorsqu'elles sont correctement formulées, et
  elles se mènent utilement en parallèle du recours, notamment pour éviter des mesures d'exécution
  pendant l'instruction du dossier.
</p>

<h2>Ce que fait le Cabinet</h2>

<ul>
  <li>Reconstitution du compte cotisant sur la période en litige et vérification des bases retenues au regard des revenus réellement déclarés.</li>
  <li>Analyse de l'affiliation, des dates de début et de cessation d'activité et du régime applicable.</li>
  <li>Calcul de la prescription et identification des sommes non recouvrables.</li>
  <li>Recours devant la commission de recours amiable, puis devant le pôle social du tribunal judiciaire.</li>
  <li>Opposition à contrainte dans le délai de quinze jours lorsque le recouvrement forcé est engagé.</li>
  <li>Négociation d'échéanciers et demandes de remise de majorations.</li>
</ul>
""",
    "faq": [
        ("Mes cotisations sont calculées sur un revenu que je n'ai plus, que faire ?",
         "Les cotisations provisionnelles sont appelées sur la base d'un revenu antérieur, mais le travailleur indépendant peut demander leur recalcul sur le revenu estimé de l'année en cours. Si cette demande a été formée et n'a pas été prise en compte, ou si la régularisation ultérieure retient un revenu erroné, la contestation porte sur la base de calcul et se mène devant la commission de recours amiable."),
        ("Puis-je contester une affiliation que je n'ai jamais demandée ?",
         "Oui. L'affiliation suppose l'exercice effectif d'une activité relevant du régime concerné. Elle se conteste en établissant l'absence d'activité, sa cessation à une date déterminée, ou son rattachement à un autre régime. Les délais de recours de droit commun s'appliquent, d'où l'intérêt de réagir dès la première mise en demeure."),
        ("Une demande d'échéancier vaut-elle reconnaissance de la dette ?",
         "Correctement formulée, une demande de délais de paiement n'implique pas renonciation à contester le fond. Il est en revanche prudent de l'exprimer expressément, et de mener la contestation dans ses propres délais sans attendre l'issue de la négociation."),
    ],
    "cta_h2": "Vous contestez un appel de cotisations ou une mise en demeure ?",
    "cta_p": """Régularisation calculée sur un revenu erroné, affiliation contestée, passif ancien
partiellement prescrit : ces dossiers se gagnent sur les pièces et sur les délais. Le Cabinet
reconstitue votre compte cotisant et porte le recours.""",
    "liens": [
        ("/avocat-mise-en-demeure-urssaf.html", "Contester une mise en demeure devant la commission de recours amiable"),
        ("/avocat-contrainte-urssaf-opposition.html", "Former opposition à une contrainte dans les quinze jours"),
    ],
},

{
    "slug": "assignation-liquidation-judiciaire-urssaf.html",
    "etape": None,
    "badge": "Procédure collective",
    "h1": "Assignation en liquidation judiciaire par l'URSSAF : réagir vite",
    "fil": "Assignation en liquidation judiciaire",
    "title": "URSSAF : assignation en liquidation judiciaire | Avocat Lyon",
    "desc": "L'URSSAF assigne votre entreprise en liquidation judiciaire pour un passif social. Contester la cessation des paiements, obtenir un redressement, négocier avant l'audience. Maître Pierre Hamoumou, avocat à Lyon.",
    "og_desc": "Ce que l'URSSAF doit établir, les moyens de défense devant le tribunal et le calendrier très court d'une assignation en liquidation judiciaire pour passif social.",
    "about": "Assignation en liquidation judiciaire par l'URSSAF",
    "chapo": """Lorsqu'un passif social s'installe, l'URSSAF peut demander l'ouverture d'une
liquidation judiciaire. L'assignation laisse peu de temps, et l'absence de l'entreprise à l'audience
conduit presque toujours à la liquidation. Pourtant, l'essentiel se joue avant : sur l'état réel de
la trésorerie, sur la créance invoquée et sur ce qui peut être négocié dans l'intervalle.""",
    "delai": None,
    "body": """
<p>
  L'URSSAF est un créancier qui agit. Lorsque les mises en demeure et les contraintes n'ont pas
  permis le recouvrement, elle peut assigner l'entreprise devant le tribunal compétent pour faire
  constater la cessation des paiements et obtenir l'ouverture d'une liquidation judiciaire, en
  demandant à titre subsidiaire un redressement judiciaire.
</p>

<p>
  À Lyon, cette assignation est portée devant le tribunal des activités économiques. Depuis le
  1er janvier 2025 et jusqu'au 31 décembre 2028, douze tribunaux de commerce, dont celui de Lyon,
  fonctionnent sous cette dénomination à titre expérimental et connaissent seuls des procédures
  amiables et collectives pour l'ensemble des professionnels, quel que soit leur statut ou leur
  activité. Les professions juridiques réglementées demeurent de la compétence du tribunal
  judiciaire. Le droit applicable, lui, est inchangé : seule la compétence se trouve modifiée.
</p>

<h2>Ce que l'URSSAF doit établir</h2>

<p>
  L'ouverture d'une procédure collective suppose la cessation des paiements, c'est-à-dire
  l'impossibilité pour le débiteur de faire face à son passif exigible avec son actif disponible.
  L'organisme s'appuie en pratique sur les mises en demeure et les contraintes émises pour établir
  une créance certaine, liquide et exigible, et sur l'absence de règlement pour en déduire la
  cessation des paiements.
</p>

<p>
  Ces deux points se discutent. La créance invoquée peut être contestée dans son montant, atteinte
  par la prescription pour partie, ou reposer sur un redressement lui-même contesté par une voie de
  recours encore pendante. Et la cessation des paiements ne se déduit pas d'un impayé : elle suppose
  une comparaison entre l'actif disponible et le passif exigible, qui se démontre par des pièces
  comptables et de trésorerie.
</p>

<h2>Les moyens de défense</h2>

<p>
  Plusieurs voies se combinent selon la situation réelle de l'entreprise.
</p>

<ul>
  <li><strong>Contester la cessation des paiements</strong>, en produisant la situation de trésorerie, les encours clients mobilisables, les lignes de financement disponibles et les concours obtenus.</li>
  <li><strong>Contester la créance</strong>, en reprenant les actes de recouvrement, leur régularité, la prescription applicable et l'existence d'un recours pendant contre le redressement qui la fonde.</li>
  <li><strong>Régler ou négocier avant l'audience</strong>, un paiement intégral ou un échéancier formalisé par écrit faisant disparaître le motif d'ouverture.</li>
  <li><strong>Demander l'ouverture d'un redressement judiciaire plutôt qu'une liquidation</strong>, lorsque l'activité peut être poursuivie et qu'un plan est envisageable.</li>
  <li><strong>Anticiper par une procédure amiable</strong>, mandat ad hoc ou conciliation, lorsque la difficulté est identifiée avant l'assignation.</li>
</ul>

<p>
  La date de cessation des paiements retenue par le jugement mérite une vigilance particulière. Les
  tribunaux la fixent fréquemment plusieurs mois, parfois plusieurs années, avant la décision, en
  considération de l'ancienneté de la créance. Cette date détermine la période suspecte et, avec
  elle, l'exposition du dirigeant aux actions en responsabilité et aux sanctions personnelles.
</p>

<h2>Le risque personnel du dirigeant</h2>

<p>
  Un passif social important expose le dirigeant au-delà de la société : action en responsabilité
  pour insuffisance d'actif, faillite personnelle, interdiction de gérer, et le cas échéant
  solidarité en cas de travail dissimulé. La défense sur l'assignation et la défense du dirigeant
  se préparent donc ensemble, et non l'une après l'autre.
</p>

<h2>Ce que fait le Cabinet</h2>

<ul>
  <li>Analyse immédiate de l'assignation, du calendrier d'audience et de la créance invoquée.</li>
  <li>Vérification des actes de recouvrement qui fondent la créance et de la prescription applicable.</li>
  <li>Constitution du dossier économique : trésorerie, actif disponible, passif exigible, perspectives d'activité.</li>
  <li>Négociation avec l'organisme avant l'audience, et formalisation écrite de tout échéancier obtenu.</li>
  <li>Représentation à l'audience, défense sur la cessation des paiements et sur la date retenue, demande subsidiaire de redressement.</li>
  <li>Accompagnement du dirigeant sur son exposition personnelle.</li>
</ul>

<p>
  Le point déterminant reste le délai. Une assignation reçue et traitée dès sa signification laisse
  des marges de négociation que la veille de l'audience ne laisse plus.
</p>
""",
    "faq": [
        ("Peut-on éviter la liquidation en payant avant l'audience ?",
         "Le règlement intégral de la créance, ou un échéancier accepté par l'organisme et formalisé par écrit, fait disparaître le motif d'ouverture invoqué. Encore faut-il que l'entreprise ne soit pas par ailleurs en cessation des paiements à l'égard d'autres créanciers, ce que le tribunal apprécie globalement."),
        ("Que se passe-t-il si l'entreprise ne se présente pas à l'audience ?",
         "Le tribunal statue par jugement réputé contradictoire, sur les seuls éléments produits par l'URSSAF. En pratique, l'absence conduit le plus souvent au prononcé de la liquidation, le redressement supposant des éléments sur la poursuite de l'activité que seule l'entreprise peut apporter."),
        ("Un recours contre le redressement URSSAF empêche-t-il l'assignation ?",
         "Non, un recours pendant ne fait pas par lui-même obstacle à l'action du créancier, mais il affecte le caractère certain de la créance invoquée et constitue un élément de défense à faire valoir devant le tribunal. C'est l'une des raisons pour lesquelles les délais de contestation du redressement doivent être tenus."),
    ],
    "cta_h2": "L'URSSAF vous a assigné en liquidation judiciaire ?",
    "cta_p": """Le calendrier est court et l'absence à l'audience conduit presque toujours à la
liquidation. Le Cabinet analyse l'assignation et la créance, constitue le dossier économique et
négocie avant l'audience lorsque c'est encore possible.""",
    "liens": [
        ("/avocat-contrainte-urssaf-opposition.html", "Contester la contrainte qui fonde la créance"),
        ("/contact-2.html", "Contacter le Cabinet en urgence"),
    ],
},

{
    "slug": "optimisation-charges-sociales-dirigeant.html",
    "etape": None,
    "badge": "Conseil et prévention",
    "h1": "Optimisation des charges sociales et choix du statut du dirigeant",
    "fil": "Optimisation des charges sociales",
    "title": "Optimisation des charges sociales du dirigeant | Avocat Lyon",
    "desc": "Choix du statut du dirigeant, assiette de rémunération, dispositifs d'exonération, sécurisation des pratiques avant contrôle URSSAF. Conseil en amont par Maître Pierre Hamoumou, avocat à Lyon.",
    "og_desc": "Choix du statut du dirigeant, arbitrage rémunération et dividendes, dispositifs d'exonération, audit de conformité avant contrôle. Le conseil en amont plutôt que le contentieux.",
    "about": "Optimisation des charges sociales",
    "chapo": """La plupart des redressements URSSAF sanctionnent des pratiques installées de longue
date, mises en place sans arbitrage juridique explicite. Le conseil en amont coûte une fraction de
ce que coûte un contrôle, et il porte sur les mêmes questions : le statut du dirigeant, l'assiette
de sa rémunération, et la conformité des avantages consentis aux salariés.""",
    "delai": None,
    "body": """
<p>
  L'optimisation des charges sociales n'est pas une affaire de montages. C'est un travail
  d'arbitrage entre des régimes qui existent, et de documentation des choix opérés. Un dispositif
  d'exonération mal justifié coûte plus cher qu'un dispositif non utilisé, puisqu'il sera redressé
  avec majorations et sur trois années.
</p>

<h2>Le choix du statut du dirigeant</h2>

<p>
  Le régime social du dirigeant dépend de la forme sociale retenue et de sa participation au
  capital. Gérant majoritaire de société à responsabilité limitée, gérant minoritaire ou égalitaire,
  président de société par actions simplifiée, entrepreneur individuel : les taux, les assiettes,
  les planchers de cotisation et les droits acquis diffèrent sensiblement, et l'écart ne joue pas
  toujours dans le sens attendu.
</p>

<p>
  L'arbitrage se fait sur plusieurs plans à la fois : le coût global du prélèvement social, les
  droits à retraite et à prévoyance acquis en contrepartie, la couverture en cas d'arrêt de travail,
  et la souplesse laissée pour moduler la rémunération. Un statut moins coûteux à court terme peut
  laisser le dirigeant sans couverture au moment où il en a besoin.
</p>

<h2>Assiette de rémunération et arbitrage avec les dividendes</h2>

<p>
  La répartition entre rémunération et distribution est l'une des questions les plus fréquemment
  posées, et l'une des plus mal traitées. Le régime applicable aux dividendes diffère selon la forme
  sociale et la qualité du bénéficiaire, et l'arbitrage a des conséquences sur les droits sociaux du
  dirigeant comme sur la trésorerie de la société. Il suppose un calcul, pas une règle générale.
</p>

<p>
  S'y ajoutent les éléments périphériques, qui constituent en pratique une part importante des
  redressements : véhicule, logement, outils de communication, frais de représentation, prise en
  charge de dépenses personnelles. Leur traitement social suppose une évaluation conforme et des
  justificatifs disponibles.
</p>

<h2>Les dispositifs à sécuriser</h2>

<p>
  Les mécanismes qui réduisent le coût du travail sont nombreux, et tous conditionnés. Réductions et
  exonérations de cotisations, dispositifs d'épargne salariale, titres-restaurant, prise en charge
  des frais de transport, frais professionnels remboursés au réel ou au forfait, avantages servis
  par le comité social et économique : chacun répond à des conditions de fond et de forme dont le
  non-respect entraîne la réintégration dans l'assiette.
</p>

<p>
  Le point commun de ces dispositifs est l'exigence de preuve. L'exonération se justifie, et elle se
  justifie au moment du contrôle, sur des pièces constituées à l'époque des faits. C'est
  précisément ce que l'audit en amont permet de vérifier.
</p>

<h2>L'audit de conformité avant le contrôle</h2>

<p>
  Un audit social consiste à passer en revue les pratiques de paie et les avantages consentis, à les
  confronter aux textes et à la convention collective applicable, puis à hiérarchiser les écarts
  selon leur coût potentiel et leur probabilité d'être relevés. Il aboutit à des correctifs, et à la
  constitution des justificatifs manquants.
</p>

<p>
  Mené avant un contrôle, cet exercice permet de corriger, de documenter et parfois de régulariser
  spontanément. Mené après la réception d'un avis de contrôle, il garde son utilité mais perd une
  partie de sa latitude.
</p>

<h2>Ce que fait le Cabinet</h2>

<ul>
  <li>Analyse du statut du dirigeant et chiffrage comparatif des régimes envisageables, droits sociaux compris.</li>
  <li>Arbitrage de la structure de rémunération et traitement des avantages en nature.</li>
  <li>Revue des dispositifs d'exonération appliqués et vérification de leurs conditions.</li>
  <li>Audit de conformité des pratiques de paie au regard de la convention collective applicable.</li>
  <li>Constitution et mise en forme des justificatifs destinés à être opposés en cas de contrôle.</li>
  <li>Accompagnement des projets de création, de transformation ou de restructuration sur leur volet social.</li>
</ul>
""",
    "faq": [
        ("Quel statut coûte le moins cher socialement ?",
         "La question ne se tranche pas en général. Le coût dépend du niveau de rémunération envisagé, de la forme sociale, de la répartition du capital et de l'arbitrage avec les distributions. Et le prélèvement le plus faible n'est pas toujours le choix le plus avantageux, puisqu'il ouvre des droits moindres en matière de retraite et de prévoyance. L'arbitrage se fait sur un chiffrage propre à la situation."),
        ("Un audit social peut-il être utilisé contre l'entreprise en cas de contrôle ?",
         "Les échanges entre un avocat et son client sont couverts par le secret professionnel. C'est une raison, parmi d'autres, de mener ce type de revue dans un cadre protégé : les constats internes sur des pratiques non conformes ont vocation à produire des correctifs, pas à alimenter un dossier."),
        ("Peut-on régulariser spontanément une pratique non conforme ?",
         "Oui, et c'est généralement préférable à l'attente d'un contrôle, tant sur le quantum des majorations que sur l'appréciation de la bonne foi. Les modalités dépendent de la nature de l'écart et de son ancienneté, la prescription de trois ans jouant ici aussi."),
    ],
    "cta_h2": "Vous souhaitez sécuriser vos pratiques avant un contrôle ?",
    "cta_p": """Choix du statut, structure de rémunération, dispositifs d'exonération, justificatifs
opposables : ces questions se traitent mieux en amont qu'au stade de la lettre d'observations. Le
Cabinet intervient en conseil comme en contentieux.""",
    "liens": [
        ("/honoraires.html", "Modalités d'intervention et honoraires du Cabinet"),
        ("/controle-urssaf-secteurs-exposes.html", "Les postes de redressement propres à votre secteur"),
    ],
},
]


# --------------------------------------------------------------------------
# Gabarit
# --------------------------------------------------------------------------

STYLE = """<style>
body { font-family: 'DM Sans', sans-serif; }
h1, h2, h3, h4, h5, h6, .font-serif { font-family: 'Cormorant Garamond', serif; }
#mobile-menu-toggle:checked ~ #mobile-menu { display: block; }
::selection { background-color: #AED18E; color: #2C6E68; }
.fade-in-up { animation: fadeInUp 0.8s ease-out forwards; opacity: 0; transform: translateY(20px); }
@keyframes fadeInUp { to { opacity: 1; transform: translateY(0); } }
.prose-cabinet p { margin-bottom: 1.5rem; line-height: 1.85; }
.prose-cabinet h2 { font-size: 1.875rem; color: #2C6E68; margin-top: 3.5rem; margin-bottom: 1.25rem; letter-spacing: -0.01em; }
.prose-cabinet h3 { font-size: 1.375rem; color: #2C6E68; margin-top: 2.5rem; margin-bottom: 1rem; }
.prose-cabinet ul { margin-bottom: 1.5rem; padding-left: 0; }
.prose-cabinet li { position: relative; padding-left: 1.5rem; margin-bottom: 0.85rem; line-height: 1.75; }
.prose-cabinet li::before { content: ''; position: absolute; left: 0; top: 0.65em; width: 6px; height: 6px; background-color: #AED18E; border-radius: 9999px; }
.prose-cabinet strong { color: #1a4541; font-weight: 500; }
</style>"""

NAV = """    <nav class="fixed top-0 left-0 w-full bg-white/90 backdrop-blur-md z-50 border-b border-stone-100">
      <div class="max-w-screen-xl mx-auto px-6 h-20 flex items-center justify-between">
        <a href="/" class="flex items-center gap-3 group">
          <img width="150" height="150" src="/logo-header.png" alt="Pierre Hamoumou Avocat" class="h-12 w-auto">
          <div class="hidden sm:flex flex-col">
            <span class="font-serif text-xl tracking-tight text-[#2C6E68] leading-none">Pierre Hamoumou</span>
            <span class="text-[0.65rem] tracking-widest text-stone-500 uppercase mt-1">Avocat à la Cour</span>
          </div>
        </a>

        <div class="hidden md:flex items-center gap-6 text-sm font-medium text-stone-600">
          <a href="/" class="hover:text-[#2C6E68] transition-colors">Accueil</a>
          <a href="/postulation-et-substitution.html" class="hover:text-[#2C6E68] transition-colors">Postulation et substitution</a>
          <a href="__HUB__" class="text-[#2C6E68] transition-colors">Droit de la sécurité sociale</a>
          <a href="/articles/" class="hover:text-[#2C6E68] transition-colors">Actualités</a>
          <a href="/faq.html" class="hover:text-[#2C6E68] transition-colors">FAQ</a>
          <a href="/honoraires.html" class="hover:text-[#2C6E68] transition-colors">Honoraires</a>
          <a href="/contact-2.html" class="px-5 py-2.5 bg-[#AED18E] text-[#1a4541] font-medium rounded-sm hover:bg-[#9dc47a] transition-colors duration-300">Contact</a>
        </div>

        <label for="mobile-menu-toggle" class="md:hidden cursor-pointer text-[#2C6E68]">
          <svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 5h16M4 12h16M4 19h16"/></svg>
        </label>
      </div>
      <input type="checkbox" id="mobile-menu-toggle" class="hidden peer">
      <div id="mobile-menu" class="hidden md:hidden absolute top-20 left-0 w-full bg-white border-b border-stone-100 p-6 shadow-lg">
        <div class="flex flex-col gap-4 text-center">
          <a href="/" class="text-stone-700 py-2">Accueil</a>
          <a href="/postulation-et-substitution.html" class="text-stone-700 py-2">Postulation et substitution</a>
          <a href="__HUB__" class="text-[#2C6E68] font-medium py-2">Droit de la sécurité sociale</a>
          <a href="/articles/" class="text-stone-700 py-2">Actualités</a>
          <a href="/faq.html" class="text-stone-700 py-2">FAQ</a>
          <a href="/honoraires.html" class="text-stone-700 py-2">Honoraires</a>
          <a href="/a-propos.html" class="text-stone-700 py-2">À propos</a>
          <a href="/contact-2.html" class="text-[#2C6E68] font-medium py-2">Contact</a>
        </div>
      </div>
    </nav>""".replace("__HUB__", HUB)

FOOTER = """    <footer class="bg-[#1a4541] text-stone-400 py-12 border-t border-[#2C6E68]">
      <div class="max-w-screen-xl mx-auto px-6">
        <div class="grid md:grid-cols-4 gap-8 mb-12 text-sm">
          <div class="col-span-1 md:col-span-2">
            <img loading="lazy" decoding="async" width="250" height="250" src="/logo-footer.png" alt="Pierre Hamoumou Avocat" class="h-20 w-auto mb-4">
            <p class="max-w-xs leading-relaxed text-stone-400 font-light">
              Avocat au Barreau de Lyon.<br>
              90 rue Servient, 69003 Lyon<br>
              Une expertise dédiée à la postulation et au droit de la sécurité sociale.
            </p>
          </div>
          <div>
            <h5 class="text-white font-serif text-lg mb-4">Navigation</h5>
            <ul class="space-y-2">
              <li><a href="/" class="hover:text-[#AED18E] transition-colors">Accueil</a></li>
              <li><a href="/postulation-et-substitution.html" class="hover:text-[#AED18E] transition-colors">Postulation et substitution</a></li>
              <li><a href="__HUB__" class="hover:text-[#AED18E] transition-colors">Droit de la sécurité sociale</a></li>
              <li><a href="/articles/" class="hover:text-[#AED18E] transition-colors">Actualités</a></li>
              <li><a href="/faq.html" class="hover:text-[#AED18E] transition-colors">FAQ</a></li>
              <li><a href="/honoraires.html" class="hover:text-[#AED18E] transition-colors">Honoraires</a></li>
              <li><a href="/a-propos.html" class="hover:text-[#AED18E] transition-colors">À propos</a></li>
              <li><a href="/contact-2.html" class="hover:text-[#AED18E] transition-colors">Contact</a></li>
            </ul>
          </div>
          <div>
            <h5 class="text-white font-serif text-lg mb-4">Informations</h5>
            <ul class="space-y-2">
              <li><a href="/mentions-legales/" class="hover:text-[#AED18E] transition-colors">Mentions légales</a></li>
              <li><a href="/politique-de-confidentialite/" class="hover:text-[#AED18E] transition-colors">Politique de confidentialité</a></li>
            </ul>
          </div>
        </div>
        <div class="pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4 text-xs tracking-wider">
          <p>© 2026 Cabinet Hamoumou. Tous droits réservés.</p>
          <div class="flex gap-4">
            <a href="#" class="hover:text-white transition-colors"><svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2a2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6M2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></g></svg></a>
          </div>
        </div>
      </div>
    </footer>""".replace("__HUB__", HUB)

CTA_ICON = '<svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"><path d="M12 3v18m7-13l3 8a5 5 0 0 1-6 0zV7"/><path d="M3 7h1a17 17 0 0 0 8-2a17 17 0 0 0 8 2h1M5 8l3 8a5 5 0 0 1-6 0zV7m2 14h10"/></g></svg>'


def esc(s):
    """Echappe pour un attribut HTML ou une chaine JSON-LD."""
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def json_esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def flat(s):
    """Replie un bloc de texte multiligne en une seule ligne propre."""
    return re.sub(r"\s+", " ", s).strip()


def build_parcours(current):
    """Composant de progression dans la procedure de controle."""
    items = []
    for i, (key, label, href) in enumerate(PARCOURS, start=1):
        if key == current:
            items.append(
                '          <li class="flex-1 min-w-[9rem] bg-[#2C6E68] text-white p-4 rounded-sm">\n'
                '            <span class="block text-[0.65rem] uppercase tracking-widest opacity-70 mb-1">Étape %d</span>\n'
                '            <span class="block font-medium text-sm">%s</span>\n'
                '            <span class="block text-[0.7rem] opacity-80 mt-1">Vous êtes ici</span>\n'
                '          </li>' % (i, label)
            )
        else:
            items.append(
                '          <li class="flex-1 min-w-[9rem] bg-white border border-stone-200 p-4 rounded-sm hover:border-[#AED18E] transition-colors">\n'
                '            <a href="%s" class="block">\n'
                '              <span class="block text-[0.65rem] uppercase tracking-widest text-stone-400 mb-1">Étape %d</span>\n'
                '              <span class="block font-medium text-sm text-[#2C6E68]">%s</span>\n'
                '            </a>\n'
                '          </li>' % (href, i, label)
            )
    return (
        '    <section class="px-6 pb-4" aria-label="Étapes de la procédure de contrôle">\n'
        '      <div class="max-w-3xl mx-auto">\n'
        '        <h2 class="text-sm uppercase tracking-widest text-stone-400 mb-4">Les étapes de la procédure</h2>\n'
        '        <ul class="flex flex-wrap gap-3 list-none p-0 m-0">\n'
        + "\n".join(items) + "\n"
        '        </ul>\n'
        '      </div>\n'
        '    </section>\n'
    )


def build_delai(delai):
    if not delai:
        return ""
    valeur, texte = delai
    return (
        '        <div class="bg-[#2C6E68] text-white p-6 md:p-8 mb-12 rounded-sm flex flex-col sm:flex-row items-start sm:items-center gap-6">\n'
        '          <div class="shrink-0">\n'
        '            <span class="block text-4xl md:text-5xl font-serif leading-none">%s</span>\n'
        '            <span class="block text-[0.65rem] uppercase tracking-widest opacity-70 mt-2">Délai clé</span>\n'
        '          </div>\n'
        '          <p class="text-white/90 leading-relaxed font-light text-sm md:text-base m-0">%s</p>\n'
        '        </div>\n' % (valeur, flat(texte))
    )


def build_faq_html(faq):
    blocks = []
    for q, a in faq:
        blocks.append(
            '          <div class="bg-white border border-stone-100 p-6 md:p-8 rounded-sm">\n'
            '            <h3 class="font-serif text-xl text-[#2C6E68] mb-3">%s</h3>\n'
            '            <p class="text-stone-600 leading-relaxed text-[0.95rem] m-0">%s</p>\n'
            '          </div>' % (q, flat(a))
        )
    return (
        '    <section class="px-6 pb-20 bg-stone-50">\n'
        '      <div class="max-w-3xl mx-auto">\n'
        '        <h2 class="text-3xl font-serif text-[#2C6E68] tracking-tight mb-8">Questions fréquentes</h2>\n'
        '        <div class="flex flex-col gap-4">\n'
        + "\n".join(blocks) + "\n"
        '        </div>\n'
        '      </div>\n'
        '    </section>\n'
    )


def build_schema(p):
    url = BASE + "/" + p["slug"]
    faq_items = ",\n".join(
        '        {\n'
        '          "@type": "Question",\n'
        '          "name": "%s",\n'
        '          "acceptedAnswer": { "@type": "Answer", "text": "%s" }\n'
        '        }' % (json_esc(q), json_esc(flat(a)))
        for q, a in p["faq"]
    )
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "name": "%(h1)s",
      "description": "%(desc)s",
      "serviceType": "%(about)s",
      "inLanguage": "fr-FR",
      "url": "%(url)s",
      "areaServed": { "@type": "Country", "name": "France" },
      "provider": {
        "@type": "LegalService",
        "name": "Cabinet Maître Pierre HAMOUMOU",
        "url": "%(base)s/",
        "telephone": "+33770282546",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "90 rue Servient",
          "postalCode": "69003",
          "addressLocality": "Lyon",
          "addressCountry": "FR"
        },
        "logo": {
          "@type": "ImageObject",
          "url": "%(base)s/logo-header.png"
        }
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Accueil",
          "item": "%(base)s/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Droit de la sécurité sociale",
          "item": "%(base)s%(hub)s"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "%(fil)s",
          "item": "%(url)s"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
%(faq)s
      ]
    }
  ]
}
</script>""" % {
        "h1": json_esc(p["h1"]),
        "desc": json_esc(p["desc"]),
        "about": json_esc(p["about"]),
        "url": url,
        "base": BASE,
        "hub": HUB,
        "fil": json_esc(p["fil"]),
        "faq": faq_items,
    }


def build_page(p):
    url = BASE + "/" + p["slug"]
    liens = "\n".join(
        '          <a href="%s" class="text-sm text-[#2C6E68] hover:underline underline-offset-4">\n'
        '            %s\n'
        '          </a>' % (href, label)
        for href, label in p["liens"]
    )

    parts = []
    parts.append("""<!DOCTYPE html>
<html lang="fr" class="scroll-smooth"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="%(desc)s">
<title>%(title)s</title>
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="%(url)s">
<meta property="og:type" content="website">
<meta property="og:url" content="%(url)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(og_desc)s">
<meta property="og:image" content="%(base)s/logo-header.png">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Cabinet Maître Pierre HAMOUMOU">
<link rel="stylesheet" href="/tailwind.css?v=%(css)s">
<link rel="preload" as="font" type="font/woff2" href="/fonts/dm-sans.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/fonts/cormorant-garamond.woff2" crossorigin>
<link rel="stylesheet" href="/fonts/fonts.css">
%(style)s
%(schema)s
</head>
  <body class="bg-stone-50 text-slate-800 antialiased selection:bg-[#AED18E] selection:text-[#2C6E68]">
""" % {
        "desc": esc(p["desc"]),
        "title": esc(p["title"]),
        "og_desc": esc(p["og_desc"]),
        "url": url,
        "base": BASE,
        "css": CSS_VERSION,
        "style": STYLE,
        "schema": build_schema(p),
    })

    parts.append("    <!-- Navigation -->\n" + NAV + "\n\n")

    # Hero
    parts.append("""    <!-- Hero -->
    <header class="relative pt-32 pb-12 md:pt-44 md:pb-16 px-6 bg-white overflow-hidden">
      <div class="absolute top-0 right-0 w-1/3 h-full bg-[#AED18E]/10 -skew-x-12 translate-x-1/4 pointer-events-none"></div>

      <div class="max-w-3xl mx-auto relative z-10 fade-in-up">
        <nav aria-label="Fil d'ariane" class="text-xs text-stone-400 mb-8 flex items-center gap-2 flex-wrap">
          <a href="/" class="hover:text-[#2C6E68] transition-colors">Accueil</a>
          <span>/</span>
          <a href="%(hub)s" class="hover:text-[#2C6E68] transition-colors">Droit de la sécurité sociale</a>
          <span>/</span>
          <span class="text-stone-500">%(fil)s</span>
        </nav>

        <span class="inline-block py-1 px-3 border border-[#AED18E] text-[#2C6E68] text-xs uppercase tracking-widest rounded-full mb-6 bg-[#AED18E]/10">
          %(badge)s
        </span>

        <h1 class="text-4xl md:text-5xl font-serif text-[#2C6E68] tracking-tight leading-[1.15] mb-6">
          %(h1)s
        </h1>

        <div class="flex items-center gap-4 text-sm text-stone-500 border-t border-stone-100 pt-6">
          <span>Cabinet Maître Pierre Hamoumou</span>
          <span class="text-stone-300">|</span>
          <span>Avocat au Barreau de Lyon</span>
        </div>
      </div>
    </header>

""" % {"hub": HUB, "fil": p["fil"], "badge": p["badge"], "h1": p["h1"]})

    if p.get("etape"):
        parts.append(build_parcours(p["etape"]) + "\n")

    # Corps
    parts.append("""    <main class="px-6 pb-16">
      <div class="max-w-3xl mx-auto">

        <div class="bg-white border-l-4 border-[#AED18E] p-6 md:p-8 mb-12 shadow-sm">
          <p class="text-stone-600 leading-relaxed text-base md:text-lg font-light">
            %(chapo)s
          </p>
        </div>

%(delai)s        <div class="prose-cabinet text-stone-600 text-base md:text-[1.0625rem]">
%(body)s
        </div>

      </div>
    </main>

""" % {
        "chapo": flat(p["chapo"]),
        "delai": build_delai(p.get("delai")),
        "body": p["body"].strip("\n"),
    })

    parts.append(build_faq_html(p["faq"]) + "\n")

    # CTA
    parts.append("""    <section class="py-20 px-6 bg-[#AED18E]/20 border-t border-stone-100">
      <div class="max-w-3xl mx-auto">
        <div class="bg-white p-8 md:p-12 shadow-sm border-t-4 border-[#AED18E] text-center">
          <div class="inline-flex items-center justify-center p-3 rounded-full bg-[#AED18E]/20 text-[#2C6E68] mb-6">
            %(icon)s
          </div>
          <h2 class="text-3xl font-serif text-[#2C6E68] mb-4 tracking-tight">
            %(cta_h2)s
          </h2>
          <p class="text-stone-500 font-light max-w-xl mx-auto mb-8 leading-relaxed">
            %(cta_p)s
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="/contact-2.html" class="w-full sm:w-auto px-8 py-4 bg-[#2C6E68] text-white font-medium rounded-sm hover:bg-[#1a4541] transition-colors duration-300">
              Contacter le Cabinet
            </a>
            <a href="tel:+33770282546" class="w-full sm:w-auto px-8 py-4 border border-[#2C6E68] text-[#2C6E68] font-medium rounded-sm hover:bg-[#2C6E68] hover:text-white transition-colors duration-300">
              07 70 28 25 46
            </a>
          </div>
          <p class="text-xs text-stone-400 mt-6 tracking-wider">
            Réponse sous 24 à 48 heures ouvrées
          </p>
        </div>

        <div class="text-center mt-10 flex flex-col gap-3">
%(liens)s
          <a href="%(hub)s" class="text-sm text-[#2C6E68] hover:underline underline-offset-4">
            Toutes les interventions en droit de la sécurité sociale
          </a>
        </div>
      </div>
    </section>

""" % {
        "icon": CTA_ICON,
        "cta_h2": p["cta_h2"],
        "cta_p": flat(p["cta_p"]),
        "liens": liens,
        "hub": HUB,
    })

    parts.append("    <!-- Footer -->\n" + FOOTER + "\n</body></html>\n")

    return "".join(parts)


def main():
    erreurs = []
    for p in PAGES:
        html = build_page(p)

        # Garde-fou : aucun tiret cadratin ni demi-cadratin dans le contenu produit.
        for mauvais, nom in (("\u2014", "cadratin"), ("\u2013", "demi-cadratin")):
            if mauvais in html:
                erreurs.append("%s : %s present" % (p["slug"], nom))

        chemin = os.path.join(ROOT, p["slug"])
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(html)
        print("ecrit  %-52s %6d octets" % (p["slug"], len(html.encode("utf-8"))))

    if erreurs:
        print("\nERREURS :")
        for e in erreurs:
            print("  " + e)
        return 1

    print("\n%d pages generees." % len(PAGES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
