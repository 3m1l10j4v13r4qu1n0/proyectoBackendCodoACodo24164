-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para jacarandaclienteuser
CREATE DATABASE IF NOT EXISTS `jacarandaclienteuser` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `jacarandaclienteuser`;

-- Volcando estructura para tabla jacarandaclienteuser.acumcarrito
CREATE TABLE IF NOT EXISTS `acumcarrito` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `precio` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `acumcarrito_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla jacarandaclienteuser.acumcarrito: ~0 rows (aproximadamente)
DELETE FROM `acumcarrito`;

-- Volcando estructura para tabla jacarandaclienteuser.datalogin
CREATE TABLE IF NOT EXISTS `datalogin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `userName` varchar(25) DEFAULT NULL,
  `userPassword` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `datalogin_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla jacarandaclienteuser.datalogin: ~0 rows (aproximadamente)
DELETE FROM `datalogin`;

-- Volcando estructura para tabla jacarandaclienteuser.producto
CREATE TABLE IF NOT EXISTS `producto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(50) DEFAULT NULL,
  `imagen` varchar(250) DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `precio` varchar(50) DEFAULT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla jacarandaclienteuser.producto: ~5 rows (aproximadamente)
DELETE FROM `producto`;
INSERT INTO `producto` (`id`, `titulo`, `imagen`, `descripcion`, `precio`) VALUES
	(1, 'Florales', '../img/products/florales.jpg', 'Un toque de color y fragancia para tu hogar con estas hermosas flores. Rosas, orquídeas, lirios, tulipanes, ¡las opciones son infinitas! Decoración vivaz y alegre para cualquier espacio. Cuidados sencillos para disfrutar de ', '1200'),
	(2, 'Interiores', '../img/products/Interior.jpg', 'Belleza natural para tu hogar. Decora con estas plantas resistentes y fáciles de cuidar. Desde cactus y suculentas hasta helechos y flores, hay una opción para cada estilo. Purifica el aire y crea un ambiente tranquilo y relajante. <br /> ¡Empieza tu propio jardín interior hoy mismo!', '1400'),
	(3, 'Cactus', '../img/products/Cactus.jpg', 'Supervivientes del desierto: belleza resistente y adaptable. Formas y colores únicos que decoran tu hogar. Cuidados mínimos para disfrutar de su presencia durante años. Aliados perfectos para principiantes en jardinería. <br /> ¡Descubre el fascinante mundo de los cactus!', '1600'),
	(4, 'Exteriores', '../img/products/Exterior.jpg', 'Color y vida para tu jardín o terraza con estas resistentes especies. Desde aromáticas y trepadoras hasta árboles y arbustos, hay una opción para cada espacio. Atraen polinizadores y crean un ambiente natural. Cuidados variados según las especies, pero generalmente adaptables. <br /> ¡Disfruta de la belleza y frescura de las plantas de exterior!', '1800'),
	(5, 'Macetas', '../img/products/Macetas.jpg', 'Hogar ideal para tus plantas: estilo, funcionalidad y variedad. Materiales, formas y tamaños para todos los gustos y necesidades. Complemento perfecto para la decoración de tu hogar o jardín. Cuida las raíces de tus plantas y aporta un toque estético. <br /> ¡Elige la maceta perfecta para cada una de tus plantas!', '2000');

-- Volcando estructura para tabla jacarandaclienteuser.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla jacarandaclienteuser.usuario: ~0 rows (aproximadamente)
DELETE FROM `usuario`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
