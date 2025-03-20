<?php
$servername = "localhost";
$username = "root"; // À adapter selon votre configuration
$password = ""; // À changer si nécessaire
$database = "site5tt";

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Échec de la connexion : " . $conn->connect_error);
}
?>