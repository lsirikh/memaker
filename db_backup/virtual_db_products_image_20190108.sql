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
-- Table structure for table `products_image`
--

DROP TABLE IF EXISTS `products_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_image`
--

LOCK TABLES `products_image` WRITE;
/*!40000 ALTER TABLE `products_image` DISABLE KEYS */;
INSERT INTO `products_image` VALUES (2,'content_image/2019/01/02/조이스틱_대문_WmkJU5g.png','조이스틱 대문 사진'),(3,'content_image/2019/01/02/조이스틱01_배경x.png','조이스틱 대문사진 2'),(4,'content_image/2019/01/02/main_image01.png','엔트리 이론 메인 이미지01'),(5,'content_image/2019/01/02/main_image02.png','엔트리 이론 메인 이미지02'),(6,'content_image/2019/01/02/main_image03.png','엔트리 이론 메인 이미지03'),(7,'content_image/2019/01/02/엔트리를_활용한_SW_코딩의_이해.png','엔트리를 활용한 SW 코딩의 이해 메인이미지01'),(8,'content_image/2019/01/02/엔트리를_활용한_SW_코딩의_이해_양쪽.png','엔트리를 활용한 SW 코딩의 이해 메인이미지02'),(9,'content_image/2019/01/02/엔트리를_활용한_SW_코딩의_특징2.png','엔트리를 활용한 SW 코딩의 이해 메인이미지03'),(10,'content_image/2019/01/02/미메이커코딩보드_하늘_diy버전_제품대문이미지.png','미메이커 코딩보드 메인 이미지01'),(11,'content_image/2019/01/02/Cap_2018-11-10_15-36-45-337.jpg','미메이커 코딩보드 메인 이미지02'),(12,'content_image/2019/01/03/초시계_대문.png','초시계 대문'),(13,'content_image/2019/01/03/초시계01_배경o.png','초시계이미지01_배경있음'),(14,'content_image/2019/01/03/초시계02_배경o.png','초시계이미지02_배경있음'),(15,'content_image/2019/01/03/초시계03_배경o.png','초시계이미지03_배경있음'),(16,'content_image/2019/01/03/초시계04_배경o.png','초시계이미지04_배경있음'),(17,'','-----------------------------'),(18,'content_image/2019/01/03/거리측정기_대문.png','거리측정기_대문'),(19,'content_image/2019/01/03/거리측정기01_배경o.png','거리측정기_이미지01_배경있음'),(20,'content_image/2019/01/03/거리측정기02_배경o.png','거리측정기_이미지02_배경있음'),(21,'content_image/2019/01/03/거리측정기03_배경o.png','거리측정기_이미지03_배경있음'),(22,'content_image/2019/01/03/거리측정기04_배경o.png','거리측정기_이미지04_배경있음'),(23,'content_image/2019/01/03/조이스틱_대문.png','조이스틱_대문'),(24,'content_image/2019/01/03/조이스틱01_배경o.png','조이스틱_이미지01_배경있음'),(25,'content_image/2019/01/03/조이스틱02_배경o.png','조이스틱_이미지02_배경있음'),(26,'content_image/2019/01/03/조이스틱03_배경o.png','조이스틱_이미지03_배경있음'),(27,'content_image/2019/01/03/꽃무드등_대문.png','꽃무드등_대문'),(28,'content_image/2019/01/03/꽃무드등_01_배경o.png','꽃무드등_이미지01_배경있음'),(29,'content_image/2019/01/03/꽃무드등_02_배경o.png','꽃무드등_이미지02_배경있음'),(30,'content_image/2019/01/03/꽃무드등_03_배경o.png','꽃무드등_이미지03_배경있음'),(31,'content_image/2019/01/03/꽃무드등_04_배경o.png','꽃무드등_이미지04_배경있음'),(32,'content_image/2019/01/03/악어복불복_00_소형.png','악어복불복_대문'),(33,'content_image/2019/01/03/악어복불복01_배경x_대형.png','악어복불복_이미지01_배경있음'),(34,'content_image/2019/01/03/악어복불복02_소형_배경o.png','악어복불복_이미지02_배경있음'),(35,'content_image/2019/01/03/악어복불복03_소형_배경o.png','악어복불복_이미지03_배경있음'),(36,'content_image/2019/01/03/악어복불복04_소형_배경o.png','악어복불복_이미지04_배경있음'),(37,'content_image/2019/01/03/악어복불복05_배경o.png','악어복불복_이미지05_배경있음'),(38,'content_image/2019/01/03/스마트주차장_대문.png','스마트주차장_대문'),(39,'content_image/2019/01/03/스마트주차장01_배경o.png','스마트주차장_이미지01_배경있음'),(40,'content_image/2019/01/03/스마트주차장02_배경o.png','스마트주차장_이미지02_배경있음'),(41,'content_image/2019/01/03/스마트주차장03_배경o.png','스마트주차장_이미지03_배경있음'),(42,'content_image/2019/01/03/스마트주차장_04.jpg','스마트주차장_이미지04_스틸컷'),(43,'content_image/2019/01/03/스마트주차장_05.jpg','스마트주차장_이미지05_스틸컷'),(44,'content_image/2019/01/03/스마트주차장_06.jpg','스마트주차장_이미지06_스틸컷'),(45,'content_image/2019/01/03/스마트스탠드_00_소형.png','스마트스탠드_대문'),(46,'content_image/2019/01/03/스마트스탠드_01_배경o.png','스마트스탠드_이미지01_배경있음'),(47,'content_image/2019/01/03/스마트스탠드_02_배경o.png','스마트스탠드_이미지02_배경있음'),(48,'content_image/2019/01/03/스마트스탠드_03_배경o.png','스마트스탠드_이미지03_배경있음'),(49,'content_image/2019/01/03/스마트스탠드_04_배경o.png','스마트스탠드_이미지04_배경있음'),(50,'content_image/2019/01/03/주차장차단기_대문.png','주차장차단기_대문'),(51,'content_image/2019/01/03/주차장차단기_01_배경o.png','주차장차단기_이미지01_배경있음'),(52,'content_image/2019/01/03/주차장차단기_02_배경o.png','주차장차단기_이미지02_배경있음'),(53,'content_image/2019/01/03/주차장차단기_03_배경o.png','주차장차단기_이미지03_배경있음'),(54,'content_image/2019/01/03/주차장차단기_04_배경o.png','주차장차단기_이미지04_배경있음');
/*!40000 ALTER TABLE `products_image` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-08 15:50:37
