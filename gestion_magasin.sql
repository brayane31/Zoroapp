-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 07 nov. 2023 à 17:51
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `gestion_magasin`
--

-- --------------------------------------------------------

--
-- Structure de la table `magasin`
--

DROP TABLE IF EXISTS `magasin`;
CREATE TABLE IF NOT EXISTS `magasin` (
  `MagasinID` int NOT NULL AUTO_INCREMENT,
  `NomMagasin` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Adresse` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Telephone` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`MagasinID`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `magasin`
--

INSERT INTO `magasin` (`MagasinID`, `NomMagasin`, `Adresse`, `Telephone`, `Email`) VALUES
(1, 'anicette magasins', 'bingerville', '01790867', 'anicettegohilouo@gmail.com'),
(10, 'Magasin brayane', 'Adresse6', '07887453', 'admin@gmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

DROP TABLE IF EXISTS `produit`;
CREATE TABLE IF NOT EXISTS `produit` (
  `ProduitID` int NOT NULL AUTO_INCREMENT,
  `NomProduit` varchar(255) DEFAULT NULL,
  `Description` text,
  `PrixUnitaire` decimal(10,2) DEFAULT NULL,
  `Categorie` varchar(100) NOT NULL,
  PRIMARY KEY (`ProduitID`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`ProduitID`, `NomProduit`, `Description`, `PrixUnitaire`, `Categorie`) VALUES
(1, 'Produit 1', 'Description du Produit 1', '10.99', 'Catégorie 1'),
(2, 'Produit 2', 'Description du Produit 2', '19.99', 'Catégorie 2'),
(3, 'Produit 3', 'Description du Produit 3', '5.99', 'Catégorie 1'),
(4, 'Produit 4', 'Description du Produit 4', '15.49', 'Catégorie 3'),
(5, 'Produit 5', 'Description du Produit 5', '8.99', 'Catégorie 2');

-- --------------------------------------------------------

--
-- Structure de la table `stock`
--

DROP TABLE IF EXISTS `stock`;
CREATE TABLE IF NOT EXISTS `stock` (
  `StockID` int NOT NULL AUTO_INCREMENT,
  `MagasinID` int DEFAULT NULL,
  `ProduitID` int DEFAULT NULL,
  `QuantiteEnStock` int DEFAULT NULL,
  PRIMARY KEY (`StockID`),
  KEY `MagasinID` (`MagasinID`),
  KEY `ProduitID` (`ProduitID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `UtilisateurID` int NOT NULL AUTO_INCREMENT,
  `MotDePasse` varchar(100) DEFAULT NULL,
  `Nom` varchar(255) DEFAULT NULL,
  `Prenom` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`UtilisateurID`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`UtilisateurID`, `MotDePasse`, `Nom`, `Prenom`, `Email`, `Role`) VALUES
(1, '12345', 'Doe', 'John', 'john.doe@email.com', 'Utilisateur'),
(2, '98765', 'Smith', 'Alice', 'alice.smith@email.com', 'Administrateur'),
(3, '45678', 'Johnson', 'Bob', 'bob.johnson@email.com', 'Utilisateur'),
(4, '54321', 'Williams', 'Emily', 'emily.williams@email.com', 'Utilisateur'),
(5, '78901', 'Brown', 'Chris', 'chris.brown@email.com', 'Administrateur');

-- --------------------------------------------------------

--
-- Structure de la table `vente`
--

DROP TABLE IF EXISTS `vente`;
CREATE TABLE IF NOT EXISTS `vente` (
  `VenteID` int NOT NULL AUTO_INCREMENT,
  `MagasinID` int DEFAULT NULL,
  `ProduitID` int DEFAULT NULL,
  `QuantiteVendue` int DEFAULT NULL,
  `MontantTotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`VenteID`),
  KEY `MagasinID` (`MagasinID`),
  KEY `ProduitID` (`ProduitID`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `vente`
--

INSERT INTO `vente` (`VenteID`, `MagasinID`, `ProduitID`, `QuantiteVendue`, `MontantTotal`) VALUES
(1, 10, 2, 13, '12300.00'),
(2, 6, 2, 4, '1200.00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
