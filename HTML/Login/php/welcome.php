<?php
session_start();
if (!isset($_SESSION["user_id"])) {
    header("Location: login.html");
    exit();
}

$nom = $_SESSION["nom"];
$prenom = $_SESSION["prenom"];
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenue</title>
</head>
<body>
<h2>Bienvenue</h2>
<p>Bonjour <?php echo htmlspecialchars($nom . " " . $prenom); ?> !</p>
</body>
</html>