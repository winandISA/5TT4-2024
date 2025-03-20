<?php
session_start();
require 'connection.php'; // Connexion à la base de données

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $identifiant = $_POST["identifiant"]; // Peut être un mail ou un pseudo
    $password = $_POST["password"];

    if (!empty($identifiant) && !empty($password)) {
        // Requête pour récupérer l'utilisateur via email OU pseudo
        $sql = "SELECT id, pseudo, nom, prenom, password FROM login WHERE mail = ? OR pseudo = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ss", $identifiant, $identifiant);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows === 1) {
            $user = $result->fetch_assoc();
            if ($password === $user["password"]) { // Comparaison simple du mot de passe
                // Stockage des infos en session
                $_SESSION["user_id"] = $user["id"];
                $_SESSION["pseudo"] = $user["pseudo"];
                $_SESSION["nom"] = $user["nom"];
                $_SESSION["prenom"] = $user["prenom"];
                header("Location: welcome.php");
                exit();
            } else {
                echo "Mot de passe incorrect.";
            }
        } else {
            echo "Utilisateur non trouvé.";
        }
    } else {
        echo "Tous les champs sont obligatoires.";
    }
}
?>