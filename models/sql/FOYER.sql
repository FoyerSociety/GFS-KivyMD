-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : lun. 16 nov. 2020 à 19:11
-- Version du serveur :  10.3.25-MariaDB-0ubuntu0.20.04.1
-- Version de PHP : 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `FOYER`
--

-- --------------------------------------------------------

--
-- Structure de la table `Cotisation`
--

CREATE TABLE `Cotisation` (
  `id` int(11) NOT NULL,
  `amount` float DEFAULT NULL,
  `mounth` varchar(10) DEFAULT NULL,
  `year` int(4) DEFAULT NULL,
  `reason` varchar(50) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `Date_begin`
--

CREATE TABLE `Date_begin` (
  `id` int(11) NOT NULL,
  `mp` date DEFAULT NULL,
  `ma` date DEFAULT NULL,
  `ck` date DEFAULT NULL,
  `fk` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `Dept`
--

CREATE TABLE `Dept` (
  `id` int(11) NOT NULL,
  `amount` float DEFAULT NULL,
  `reason` varchar(50) DEFAULT NULL,
  `user_set` int(11) DEFAULT NULL,
  `user_get` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `Food`
--

CREATE TABLE `Food` (
  `id` int(11) NOT NULL,
  `plate` varchar(50) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `day` varchar(10) DEFAULT NULL,
  `week` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `Transaction`
--

CREATE TABLE `Transaction` (
  `id` int(11) NOT NULL,
  `date_insert` datetime DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `reason` varchar(50) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  `date_trans` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `User`
--

CREATE TABLE `User` (
  `id` int(11) NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `prom` char(3) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `priv` char(2) DEFAULT NULL,
  `ind_uni_mp` int(11) DEFAULT NULL,
  `ind_uni_ma` int(11) DEFAULT NULL,
  `ind_uni_ck` int(11) DEFAULT NULL,
  `ind_fk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour la table 'User'
--
  ALTER TABLE `User` 
    ADD UNIQUE(`username`); 
--
-- Index pour la table `Cotisation`
--
ALTER TABLE `Cotisation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_user` (`id_user`);

--
-- Index pour la table `Date_begin`
--
ALTER TABLE `Date_begin`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `Dept`
--
ALTER TABLE `Dept`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_set` (`user_set`),
  ADD KEY `fk_get` (`user_get`);

--
-- Index pour la table `Food`
--
ALTER TABLE `Food`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `Transaction`
--
ALTER TABLE `Transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_user1` (`id_user`);

--
-- Index pour la table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`id`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Cotisation`
--
ALTER TABLE `Cotisation`
  ADD CONSTRAINT `FK_user` FOREIGN KEY (`id_user`) REFERENCES `User` (`id`);

--
-- Contraintes pour la table `Dept`
--
ALTER TABLE `Dept`
  ADD CONSTRAINT `fk_get` FOREIGN KEY (`user_get`) REFERENCES `User` (`id`),
  ADD CONSTRAINT `fk_set` FOREIGN KEY (`user_set`) REFERENCES `User` (`id`);

--
-- Contraintes pour la table `Transaction`
--
ALTER TABLE `Transaction`
  ADD CONSTRAINT `FK_user1` FOREIGN KEY (`id_user`) REFERENCES `User` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
