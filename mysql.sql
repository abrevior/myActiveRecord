DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
     `id`       INTEGER(11) auto_increment,
     `name`     VARCHAR(50) NOT NULL,
     `surname`  VARCHAR(50) NOT NULL,
     `password` VARCHAR(20) NOT NULL,
     PRIMARY KEY(`id`));

INSERT INTO `user`(`name`, `surname`, `password`) VALUES ('serega','kolesnk','lololo');