<?php
// Sonde temporaire (a supprimer) : en-tetes d'IP vus par le serveur pour l'appelant.
header('Content-Type: application/json'); header('Cache-Control: no-store');
$k = ['REMOTE_ADDR','HTTP_X_FORWARDED_FOR','HTTP_X_REAL_IP','HTTP_CF_CONNECTING_IP','HTTP_TRUE_CLIENT_IP','HTTP_X_CLIENT_IP','HTTP_FORWARDED'];
$o = []; foreach ($k as $h) { if (isset($_SERVER[$h])) $o[$h] = $_SERVER[$h]; }
echo json_encode($o);
