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
-- Table structure for table `products_content`
--

DROP TABLE IF EXISTS `products_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `added` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `description` varchar(300) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  `discount` int(11) DEFAULT NULL,
  `isSale` tinyint(1) DEFAULT NULL,
  `sample` varchar(200) DEFAULT NULL,
  `isShow` tinyint(1) DEFAULT NULL,
  `isDiscount` tinyint(1) DEFAULT NULL,
  `recommend` int(11) DEFAULT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_content_category_id_d2f6e625_fk_products_category_id` (`category_id`),
  CONSTRAINT `products_content_category_id_d2f6e625_fk_products_category_id` FOREIGN KEY (`category_id`) REFERENCES `products_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_content`
--

LOCK TABLES `products_content` WRITE;
/*!40000 ALTER TABLE `products_content` DISABLE KEYS */;
INSERT INTO `products_content` VALUES (1,'엔트리 이론','2019-01-01 17:02:22.090999','2019-01-06 03:27:52.011057','엔트리를 활용하기 위한 가장 기본적인 내용을 설명하고 있습니다. 오브젝트, 블록조립소 등 생소한 개념을 익혀보세요.',0,0,1,'https://www.youtube.com/embed/MgdWk7EWRL4?list=PLjOE0xVFFMJwGa6VejoBOj21MuxyM_Rft',1,0,1,5),(2,'엔트리를 활용한 SW코딩의 이해','2019-01-01 19:05:39.413047','2019-01-04 05:33:12.657417','본 도서는 초등학교 실과시간에 도입되는 코딩교육에 완벽한 대비를 할 수 있도록 다양한 전문가와 교사의 검토를 마친 교육 도서로서 학생들에게 코딩에 대한 배경지식과 기초적인 코딩에 이해를 도울 수 있는 다양한 내용을 수록하고 있습니다.',12000,11000,1,NULL,1,1,NULL,1),(3,'미메이커 코딩보드','2019-01-02 08:43:48.075311','2019-01-08 02:00:17.832835','코딩을 쉽게 배울 수 있는 코딩 보드 \"미메이커 코딩보드\" 피지컬 컴퓨팅, 로봇 코딩 등 다양한 만들기 기반의 코딩 교육용 보드로 코딩 교육과 창의력 두 마리의 토끼를 모두 잡으세요!',120000,110000,1,'https://www.youtube.com/embed/cB3VoyYMTFI',1,1,2,4),(4,'거리측정기 만들기 키트','2019-01-02 16:41:00.134651','2019-01-08 01:52:22.747939','미메이커 코딩보드를 활용한 거리 측정기 만들기 프로젝트 키트입니다. 엔트리 및 스크래치 등을 활용하여 스마트 거리측정기 게임과 함께 활용하는 거리 측정기 실물을 만들 수 있습니다.',8000,0,1,'https://www.youtube.com/embed/eETOmATyLXE',1,0,NULL,3);
/*!40000 ALTER TABLE `products_content` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-08 15:01:41
