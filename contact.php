<?php
// Reception du formulaire de contact du site, sans service tiers.
// Remplace Formspree : envoi par le serveur Hostinger du site (domaine couvert par
// le SPF _spf.mail.hostinger.com). Repond en JSON, lu par contact-form.js.

const DESTINATAIRE = 'pierre.hamoumou.avocat@gmail.com';
const EXPEDITEUR   = 'formulaire@pierrehamoumou-avocat.fr';
const DOMAINE      = 'pierrehamoumou-avocat.fr';
const MAX_PAR_HEURE = 5;

// Copie cachee temporaire pour les tests de Mathieu Bila (prestataire du site) : seuls les
// messages envoyes avec son adresse lui sont copies, jamais ceux des visiteurs. Expire seule
// a la fin du 03/11/2026 (heure de Paris). Bloc a retirer ensuite.
const COPIE_TEST = 'matbila63@gmail.com';
const COPIE_TEST_JUSQUA = '2026-11-04 00:00:00';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Robots-Tag: noindex');

function repondre(int $code, array $corps): void {
    http_response_code($code);
    echo json_encode($corps, JSON_UNESCAPED_UNICODE);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    repondre(405, ['error' => 'Methode non autorisee']);
}

// Refuse les envois declenches depuis un autre site.
$origine = $_SERVER['HTTP_ORIGIN'] ?? ($_SERVER['HTTP_REFERER'] ?? '');
$hote = parse_url($origine, PHP_URL_HOST) ?: '';
if ($hote !== DOMAINE && $hote !== 'www.' . DOMAINE) {
    repondre(403, ['error' => 'Origine refusee']);
}

// Piege a robots : champ invisible pour un humain. Rempli, on feint le succes sans envoyer.
if (!empty($_POST['website'])) {
    repondre(200, ['ok' => true]);
}

// Limite par adresse IP : MAX_PAR_HEURE envois par heure.
// REMOTE_ADDR est reecrit par Hostinger avec la vraie adresse du visiteur. Ne jamais lire
// X-Forwarded-For : son premier element est fourni par le visiteur et falsifiable
// (verifie le 02/11/2026), ce qui permettait de contourner la limite.
$ip = $_SERVER['REMOTE_ADDR'] ?? 'inconnue';
// En IPv6, un abonne dispose d'un bloc /64 entier : on limite par bloc, pas par adresse.
if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6)) {
    $ip = substr(bin2hex(inet_pton($ip)), 0, 16) . '/64';
}
$journal = sys_get_temp_dir() . '/contact-' . hash('sha256', $ip . DOMAINE);
$recents = [];
if (is_file($journal)) {
    $recents = array_filter(array_map('intval', explode("\n", (string) file_get_contents($journal))), fn($t) => $t > time() - 3600);
}
if (count($recents) >= MAX_PAR_HEURE) {
    repondre(429, ['error' => 'Trop de messages, reessayez plus tard']);
}

// Nettoyage et validation.
$ligne = fn($v) => trim(str_replace(["\r", "\n", "\0"], ' ', (string) $v));
$nom     = mb_substr($ligne($_POST['nom'] ?? ''), 0, 120);
$email   = mb_substr($ligne($_POST['email'] ?? ''), 0, 200);
$sujet   = mb_substr($ligne($_POST['sujet'] ?? ''), 0, 200);
$profil  = mb_substr($ligne($_POST['profile'] ?? ''), 0, 40);
$origineForm = mb_substr($ligne($_POST['subject'] ?? 'Nouveau message - Cabinet Hamoumou'), 0, 120);
$message = mb_substr(trim(str_replace("\0", '', (string) ($_POST['message'] ?? ''))), 0, 5000);

$erreurs = [];
if ($nom === '')     $erreurs[] = ['field' => 'nom'];
if ($sujet === '')   $erreurs[] = ['field' => 'sujet'];
if ($message === '') $erreurs[] = ['field' => 'message'];
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $erreurs[] = ['field' => 'email'];
if ($erreurs) {
    repondre(422, ['error' => 'Champs invalides', 'errors' => $erreurs]);
}

// Envoi.
$objet = $origineForm . ' : ' . $sujet;
$corps = "Nouveau message recu depuis le site pierrehamoumou-avocat.fr\n\n"
       . "Nom : $nom\n"
       . "Email : $email\n"
       . "Profil : " . ($profil ?: 'non precise') . "\n"
       . "Sujet : $sujet\n\n"
       . "Message :\n$message\n\n"
       . "Pour repondre, utilisez simplement le bouton Repondre : la reponse partira vers $email.\n";

$entetes = [
    'From: ' . mb_encode_mimeheader('Site Cabinet Hamoumou', 'UTF-8') . ' <' . EXPEDITEUR . '>',
    'Reply-To: ' . mb_encode_mimeheader($nom, 'UTF-8') . ' <' . $email . '>',
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
];

$paris = new DateTimeZone('Europe/Paris');
if (strcasecmp($email, COPIE_TEST) === 0 && new DateTime('now', $paris) < new DateTime(COPIE_TEST_JUSQUA, $paris)) {
    $entetes[] = 'Bcc: ' . COPIE_TEST;
}

$envoye = mail(DESTINATAIRE, mb_encode_mimeheader($objet, 'UTF-8'), $corps, implode("\r\n", $entetes), '-f' . EXPEDITEUR);
if (!$envoye) {
    repondre(500, ['error' => 'Envoi impossible']);
}

$recents[] = time();
@file_put_contents($journal, implode("\n", $recents));
repondre(200, ['ok' => true]);
