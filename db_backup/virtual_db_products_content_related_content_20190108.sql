-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: memaker
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products_content_related_content`
--

DROP TABLE IF EXISTS `products_content_related_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_content_related_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_content_id` int(11) NOT NULL,
  `to_content_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `products_content_related_from_content_id_to_conte_96a765c3_uniq` (`from_content_id`,`to_content_id`),
  KEY `products_content_rel_to_content_id_80960158_fk_products_` (`to_content_id`),
  CONSTRAINT `products_content_rel_from_content_id_b5f8d3d9_fk_products_` FOREIGN KEY (`from_content_id`) REFERENCES `products_content` (`id`),
  CONSTRAINT `products_content_rel_to_content_id_80960158_fk_products_` FOREIGN KEY (`to_content_id`) REFERENCES `products_content` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_content_related_content`
--

LOCK TABLES `products_content_related_content` WRITE;
/*!40000 ALTER TABLE `products_content_related_content` DISABLE KEYS */;
INSERT INTO `products_content_related_content` VALUES (1,3,1);
/*!40000 ALTER TABLE `products_content_related_content` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-08 15:03:02
