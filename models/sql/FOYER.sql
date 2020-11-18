CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `username` varchar(20) DEFAULT NULL UNIQUE,
  `prom` char(3) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `priv` char(2) DEFAULT NULL,
  `ind_uni_mp` int(11) DEFAULT NULL,
  `ind_uni_ma` int(11) DEFAULT NULL,
  `ind_uni_ck` int(11) DEFAULT NULL,
  `ind_fk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `Cotisation` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `amount` float DEFAULT NULL,
  `mounth` varchar(10) DEFAULT NULL,
  `year` int(4) DEFAULT NULL,
  `reason` varchar(50) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  FOREIGN KEY (id_user) REFERENCES User(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE `Date_begin` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `mp` date DEFAULT NULL,
  `ma` date DEFAULT NULL,
  `ck` date DEFAULT NULL,
  `fk` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE `Dept` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `amount` float DEFAULT NULL,
  `reason` varchar(50) DEFAULT NULL,
  `user_set` int(11) ,
  `user_get` int(11),
  FOREIGN KEY (user_set) REFERENCES User(id),
  FOREIGN KEY (user_get) REFERENCES User(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE `Food` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `plate` varchar(50) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `day` varchar(10) DEFAULT NULL,
  `week` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE `Transaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `date_insert` datetime DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `reason` varchar(50) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  `date_trans` date DEFAULT curdate(),
  FOREIGN KEY (id_user) REFERENCES User(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
