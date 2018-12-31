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
-- Table structure for table `accounts_userprofile`
--

DROP TABLE IF EXISTS `accounts_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(200) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `birth` date DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `email_confirmed` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `route` varchar(5) DEFAULT NULL,
  `agree` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `accounts_userprofile_user_id_92240672_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile`
--

LOCK TABLES `accounts_userprofile` WRITE;
/*!40000 ALTER TABLE `accounts_userprofile` DISABLE KEYS */;
INSERT INTO `accounts_userprofile` VALUES (12,'이기호 소개 내용 적는 곳afdasdfaf마ㅓㅇㄹ;ㅁ넝ㄹ;ㅣㅁ넝;리ㅓㅁㄴ;ㅇ리ㅓㅁ;ㅐ','경기도 안양시 석수동 석수아이파크',1041340786,1,'1984-03-22','남',1,'account_image/1_lsirikh/insung_Kap.jpg','',0),(43,NULL,NULL,NULL,42,NULL,NULL,0,'account_image/account_pic_default.png','FBK',0);
/*!40000 ALTER TABLE `accounts_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_userprofile_favorite_lecture`
--

DROP TABLE IF EXISTS `accounts_userprofile_favorite_lecture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile_favorite_lecture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `lecture_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_userprofile_fav_userprofile_id_lecture_i_3a2d0a65_uniq` (`userprofile_id`,`lecture_id`),
  KEY `accounts_userprofile_lecture_id_1305ecf6_fk_lectures_` (`lecture_id`),
  CONSTRAINT `accounts_userprofile_lecture_id_1305ecf6_fk_lectures_` FOREIGN KEY (`lecture_id`) REFERENCES `lectures_lecture` (`id`),
  CONSTRAINT `accounts_userprofile_userprofile_id_7d06d70c_fk_accounts_` FOREIGN KEY (`userprofile_id`) REFERENCES `accounts_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile_favorite_lecture`
--

LOCK TABLES `accounts_userprofile_favorite_lecture` WRITE;
/*!40000 ALTER TABLE `accounts_userprofile_favorite_lecture` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_userprofile_favorite_lecture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_userprofile_favorite_product`
--

DROP TABLE IF EXISTS `accounts_userprofile_favorite_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile_favorite_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_userprofile_fav_userprofile_id_product_i_9367cda5_uniq` (`userprofile_id`,`product_id`),
  KEY `accounts_userprofile_product_id_07f3c2db_fk_products_` (`product_id`),
  CONSTRAINT `accounts_userprofile_product_id_07f3c2db_fk_products_` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `accounts_userprofile_userprofile_id_d9b70a51_fk_accounts_` FOREIGN KEY (`userprofile_id`) REFERENCES `accounts_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile_favorite_product`
--

LOCK TABLES `accounts_userprofile_favorite_product` WRITE;
/*!40000 ALTER TABLE `accounts_userprofile_favorite_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_userprofile_favorite_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add source',7,'add_source'),(26,'Can change source',7,'change_source'),(27,'Can delete source',7,'delete_source'),(28,'Can view source',7,'view_source'),(29,'Can add thumbnail',8,'add_thumbnail'),(30,'Can change thumbnail',8,'change_thumbnail'),(31,'Can delete thumbnail',8,'delete_thumbnail'),(32,'Can view thumbnail',8,'view_thumbnail'),(33,'Can add thumbnail dimensions',9,'add_thumbnaildimensions'),(34,'Can change thumbnail dimensions',9,'change_thumbnaildimensions'),(35,'Can delete thumbnail dimensions',9,'delete_thumbnaildimensions'),(36,'Can view thumbnail dimensions',9,'view_thumbnaildimensions'),(37,'Can add choice',10,'add_choice'),(38,'Can change choice',10,'change_choice'),(39,'Can delete choice',10,'delete_choice'),(40,'Can view choice',10,'view_choice'),(41,'Can add question',11,'add_question'),(42,'Can change question',11,'change_question'),(43,'Can delete question',11,'delete_question'),(44,'Can view question',11,'view_question'),(45,'Can add intro',12,'add_intro'),(46,'Can change intro',12,'change_intro'),(47,'Can delete intro',12,'delete_intro'),(48,'Can view intro',12,'view_intro'),(49,'Can add category',13,'add_category'),(50,'Can change category',13,'change_category'),(51,'Can delete category',13,'delete_category'),(52,'Can view category',13,'view_category'),(53,'Can add detail',14,'add_detail'),(54,'Can change detail',14,'change_detail'),(55,'Can delete detail',14,'delete_detail'),(56,'Can view detail',14,'view_detail'),(57,'Can add product',15,'add_product'),(58,'Can change product',15,'change_product'),(59,'Can delete product',15,'delete_product'),(60,'Can view product',15,'view_product'),(61,'Can add category',16,'add_category'),(62,'Can change category',16,'change_category'),(63,'Can delete category',16,'delete_category'),(64,'Can view category',16,'view_category'),(65,'Can add lecture',17,'add_lecture'),(66,'Can change lecture',17,'change_lecture'),(67,'Can delete lecture',17,'delete_lecture'),(68,'Can view lecture',17,'view_lecture'),(69,'Can add section',18,'add_section'),(70,'Can change section',18,'change_section'),(71,'Can delete section',18,'delete_section'),(72,'Can view section',18,'view_section'),(73,'Can add video',19,'add_video'),(74,'Can change video',19,'change_video'),(75,'Can delete video',19,'delete_video'),(76,'Can view video',19,'view_video'),(77,'Can add user profile',20,'add_userprofile'),(78,'Can change user profile',20,'change_userprofile'),(79,'Can delete user profile',20,'delete_userprofile'),(80,'Can view user profile',20,'view_userprofile'),(81,'Can add board',21,'add_board'),(82,'Can change board',21,'change_board'),(83,'Can delete board',21,'delete_board'),(84,'Can view board',21,'view_board'),(85,'Can add topic',22,'add_topic'),(86,'Can change topic',22,'change_topic'),(87,'Can delete topic',22,'delete_topic'),(88,'Can view topic',22,'view_topic'),(89,'Can add post',23,'add_post'),(90,'Can change post',23,'change_post'),(91,'Can delete post',23,'delete_post'),(92,'Can view post',23,'view_post');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$yc9TvpFFN2Mv$F7/VVxcbtpwAHMqMI5UvG86e5wR6dU9Uo1SvA11S+dY=','2018-12-31 08:16:16.760503',1,'memaker','정기호','이','lsirikh@gmail.com',1,1,'2018-11-12 07:00:33.000000'),(42,'pbkdf2_sha256$120000$kOLkvVN7JQjd$KF/kjRDZlG1UMPWWAJxNhceuitreMQh5PPsVTkrNuMs=','2018-12-31 08:33:45.514784',0,'testuser01','테스트유저','','lsirikh@naver.com',0,1,'2018-12-31 08:20:06.623046');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boards_board`
--

DROP TABLE IF EXISTS `boards_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boards_board` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boards_board`
--

LOCK TABLES `boards_board` WRITE;
/*!40000 ALTER TABLE `boards_board` DISABLE KEYS */;
INSERT INTO `boards_board` VALUES (1,'코딩 강의 게시판','코딩 강의에 관련된 질문을 올려주세요.'),(2,'미메이커 코딩보드 게시판','미메이커 코딩 보드 및 키트를 사용하면서 문의사항을 올려주세요.'),(3,'3D모델링 및 출력 게시판','3D모델링 및 출력에 관련된 질문을 올려주세요.');
/*!40000 ALTER TABLE `boards_board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boards_post`
--

DROP TABLE IF EXISTS `boards_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boards_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `topic_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `order` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `boards_post_topic_id_f477c024_fk_boards_topic_id` (`topic_id`),
  KEY `boards_post_user_id_4f28d7d6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `boards_post_topic_id_f477c024_fk_boards_topic_id` FOREIGN KEY (`topic_id`) REFERENCES `boards_topic` (`id`),
  CONSTRAINT `boards_post_user_id_4f28d7d6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=273 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boards_post`
--

LOCK TABLES `boards_post` WRITE;
/*!40000 ALTER TABLE `boards_post` DISABLE KEYS */;
/*!40000 ALTER TABLE `boards_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boards_topic`
--

DROP TABLE IF EXISTS `boards_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boards_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `views` int(10) unsigned NOT NULL,
  `board_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `boards_topic_board_id_4462fe82_fk_boards_board_id` (`board_id`),
  KEY `boards_topic_user_id_599505cb_fk_auth_user_id` (`user_id`),
  CONSTRAINT `boards_topic_board_id_4462fe82_fk_boards_board_id` FOREIGN KEY (`board_id`) REFERENCES `boards_board` (`id`),
  CONSTRAINT `boards_topic_user_id_599505cb_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boards_topic`
--

LOCK TABLES `boards_topic` WRITE;
/*!40000 ALTER TABLE `boards_topic` DISABLE KEYS */;
INSERT INTO `boards_topic` VALUES (113,'안녕하세요. 코딩 강의 게시판에 오신것을 환영합니다.','<p><span style=\"font-size:16px\">안녕하세요.</span></p>\r\n\r\n<p><span style=\"font-size:16px\">미메이커의 <span style=\"color:#8e44ad\"><strong>코딩선장</strong></span>입니다!</span></p>\r\n\r\n<p><span style=\"font-size:16px\">우리가 배우면서 생기는 다양한 궁금증을 게시판에 올리고 해결해보세요.</span></p>\r\n\r\n<p><span style=\"font-size:16px\">저 뿐만 아니라 다양한 유저들이 함께 고민하고 문제를 해결하는 공간으로 활용해봅시다!</span></p>\r\n\r\n<div style=\"background:#eeeeee; border:1px solid #cccccc; padding:5px 10px\"><img alt=\"\" height=\"108\" src=\"/uploads/files/memaker/2018/12/31/feature03.png\" width=\"108\" />&nbsp;&nbsp;<span style=\"font-size:14px\"><em><q>만들면서 배우는 코딩 교육 서비스 미메이커</q></em></span></div>','2018-12-31 03:29:59.555895','2018-12-31 03:30:43.547894',1,1,1),(114,'미메이커 코딩 보드 게시판을 통해 더 많은 도전과 고민을 공유해봅시다!','<p><span style=\"font-size:18px\">안녕하세요.</span></p>\r\n\r\n<p><span style=\"font-size:18px\"><span style=\"color:#8e44ad\"><strong>코딩선장</strong></span>입니다!</span></p>\r\n\r\n<p><span style=\"font-size:18px\">미메이커 코딩 보드 게시판에서는 여러분이 만들어본 미메이커 키트, 미메이커 코딩 프로젝트의 다양한 궁금증과 노하우를 공유하고 해결하는 자리입니다.</span></p>\r\n\r\n<p><span style=\"font-size:18px\">코딩선장도 여러분의 프로젝트에 함께 동참하여 만들면서 배우는 코딩교육서비스를 완성하는데 성실한 길잡이가 되어드리겠습니다.</span></p>\r\n\r\n<p><span style=\"font-size:18px\">감사합니다!</span></p>\r\n\r\n<p><img alt=\"yes\" height=\"23\" src=\"http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/thumbs_up.png\" title=\"yes\" width=\"23\" /></p>\r\n\r\n<figure class=\"image\"><img alt=\"\" height=\"534\" src=\"/uploads/files/memaker/2018/12/31/shutterstock_323893160.jpg\" width=\"800\" />\r\n<figcaption>미메이커는 만들면서 배우는 코딩교육 서비스 입니다.</figcaption>\r\n</figure>','2018-12-31 03:36:07.713093','2018-12-31 03:36:07.712322',1,2,1),(115,'3D모델링 및 출력 게시판에서 다양한 지식과 노하우를 공유해보세요!','<p><span style=\"font-size:18px\">안녕하세요.</span></p>\r\n\r\n<p><span style=\"font-size:18px\"><span style=\"color:#8e44ad\"><strong>코딩선장</strong></span>입니다.</span></p>\r\n\r\n<p><span style=\"font-size:18px\">미메이커는 3D 모델링과 3D 프린팅에 관한 다양한 지식과 노하우를 활용하여 여러분의 궁금증을 해결해드리기 위해 노력하고 있습니다.</span></p>\r\n\r\n<p><span style=\"font-size:18px\">미메이커의 3D 모델링 프로젝트를 활용하면 여러분의 나만의 제품을 만들어서 활용할 수 있습니다.</span></p>\r\n\r\n<p><span style=\"font-size:18px\">코딩은 단순한 논리 지식이 아니라 실생활에 활용할 수 있고, 우리 삶의 문제를 해결할 수 있는 나의 삶이라는 것을 경험해보세요!</span></p>\r\n\r\n<p><span style=\"font-size:18px\">3D 모델링 메이커 프로젝트를 이용하여 수준있는 프로젝트를 만들어 보세요.</span></p>\r\n\r\n<p><span style=\"font-size:18px\">감사합니다!</span></p>\r\n\r\n<figure class=\"image\"><img alt=\"\" height=\"400\" src=\"/uploads/files/memaker/2018/12/31/3d.png\" width=\"800\" />\r\n<figcaption>미메이커 코딩보드를 활용한 3D 모델링 메이커 프로젝트</figcaption>\r\n</figure>','2018-12-31 03:56:23.498160','2018-12-31 03:57:13.224927',1,3,1);
/*!40000 ALTER TABLE `boards_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=337 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-12 08:53:56.396187','1','미메이커 코딩보드',1,'[{\"added\": {}}]',12,1),(2,'2018-11-12 08:54:37.593560','2','교육 영상 콘텐츠',1,'[{\"added\": {}}]',12,1),(3,'2018-11-12 08:55:16.184030','3','코딩 교육 교재',1,'[{\"added\": {}}]',12,1),(4,'2018-11-12 08:56:08.335419','1','교재',1,'[{\"added\": {}}]',13,1),(5,'2018-11-12 08:56:14.416603','2','언플러그드',1,'[{\"added\": {}}]',13,1),(6,'2018-11-12 08:56:19.351440','3','조립키트',1,'[{\"added\": {}}]',13,1),(7,'2018-11-12 08:56:25.065066','4','코딩보드',1,'[{\"added\": {}}]',13,1),(8,'2018-11-12 09:02:32.958208','1','[교재] 엔트리로 S/W 코딩의 이해(강의 영상 제공)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"1\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"2\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"3\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"4\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"5\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"6\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"7\"}}]',15,1),(9,'2018-11-12 09:05:25.076460','1','[교재] 엔트리로 S/W 코딩의 이해(강의 영상 제공)',2,'[{\"added\": {\"name\": \"detail\", \"object\": \"8\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"9\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"10\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"11\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"12\"}}]',15,1),(10,'2018-11-12 09:11:49.069690','2','[교재] 로봇 코딩의 이해(무료 영상 준비중)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"13\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"14\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"15\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"16\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"17\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"18\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"19\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"20\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"21\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"22\"}}]',15,1),(11,'2018-11-12 09:26:55.389151','3','[보드]미메이커 코딩보드 DIY',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"23\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"24\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"25\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"26\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"27\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"28\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"29\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"30\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"31\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"32\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"33\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"34\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"35\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"36\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"37\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"38\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"39\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"40\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"41\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"42\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"43\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"44\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"45\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"46\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"47\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"48\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"49\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"50\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"51\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"52\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"53\"}}]',15,1),(12,'2018-11-12 09:35:12.197679','4','[키트] 악어복불복 게임 만들기 키트(미메이커보드)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"54\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"55\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"56\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"57\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"58\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"59\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"60\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"61\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"62\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"63\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"64\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"65\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"66\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"67\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"68\"}}]',15,1),(13,'2018-11-12 09:40:19.470004','5','[키트] 스마트스탠드 만들기 키트(미메이커보드)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"69\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"70\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"71\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"72\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"73\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"74\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"75\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"76\"}}]',15,1),(14,'2018-11-12 09:44:54.470735','6','[키트] 꽃 무드등 만들기 키트(미메이커보드)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"77\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"78\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"79\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"80\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"81\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"82\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"83\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"84\"}}]',15,1),(15,'2018-11-12 09:45:13.216341','6','[키트] 꽃 무드등 만들기 키트(미메이커보드)',2,'[{\"changed\": {\"fields\": [\"product_image\"]}}]',15,1),(16,'2018-11-12 09:45:22.910544','5','[키트] 스마트스탠드 만들기 키트(미메이커보드)',2,'[{\"changed\": {\"name\": \"detail\", \"object\": \"76\", \"fields\": [\"lower_line\"]}}]',15,1),(17,'2018-11-12 09:45:28.995069','4','[키트] 악어복불복 게임 만들기 키트(미메이커보드)',2,'[{\"changed\": {\"name\": \"detail\", \"object\": \"68\", \"fields\": [\"lower_line\"]}}]',15,1),(18,'2018-11-12 09:50:14.592289','7','[키트] 주차장 차단기 만들기 키트(미메이커보드)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"85\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"86\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"87\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"88\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"89\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"90\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"91\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"92\"}}]',15,1),(19,'2018-11-12 09:51:23.625650','7','[키트] 주차장 차단기 만들기 키트(미메이커보드)',2,'[{\"changed\": {\"fields\": [\"isSale\"]}}]',15,1),(20,'2018-11-12 09:55:41.276736','8','[키트] 스탑워치 만들기 키트(미메이커보드)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"93\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"94\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"95\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"96\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"97\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"98\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"99\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"100\"}}]',15,1),(21,'2018-11-12 10:31:27.871296','9','[키트] 조이스틱 만들기 키트(미메이커보드)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"101\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"102\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"103\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"104\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"105\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"106\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"107\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"108\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"109\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"110\"}}]',15,1),(22,'2018-11-12 10:31:36.917307','9','[키트] 조이스틱 만들기 키트(미메이커보드)',2,'[{\"changed\": {\"name\": \"detail\", \"object\": \"110\", \"fields\": [\"lower_line\"]}}]',15,1),(23,'2018-11-12 10:35:50.801016','10','[키트] 스마트 주차장 만들기 키트(미메이커보드)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"111\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"112\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"113\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"114\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"115\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"116\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"117\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"118\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"119\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"120\"}}]',15,1),(24,'2018-11-12 10:40:43.814499','11','[키트] 거리측정기 만들기 키트(미메이커보드)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"detail\", \"object\": \"121\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"122\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"123\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"124\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"125\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"126\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"127\"}}, {\"added\": {\"name\": \"detail\", \"object\": \"128\"}}]',15,1),(25,'2018-11-12 10:43:50.457595','1','온라인',1,'[{\"added\": {}}]',18,1),(26,'2018-11-12 10:43:55.025637','2','오프라인',1,'[{\"added\": {}}]',18,1),(27,'2018-11-12 10:44:03.119307','3','온/오프라인 혼합',1,'[{\"added\": {}}]',18,1),(28,'2018-11-12 10:44:12.664553','1','엔트리',1,'[{\"added\": {}}]',16,1),(29,'2018-11-12 10:44:18.113722','2','스크래치',1,'[{\"added\": {}}]',16,1),(30,'2018-11-12 10:44:23.056991','3','메이커',1,'[{\"added\": {}}]',16,1),(31,'2018-11-12 10:48:03.722681','1','[초등학교 완벽대비] 엔트리를 활용한 SW 코딩의 이해',1,'[{\"added\": {}}]',17,1),(32,'2018-11-12 10:48:12.557854','1','[초등학교 완벽대비] 엔트리를 활용한 SW 코딩의 이해',2,'[{\"changed\": {\"fields\": [\"section\", \"category\"]}}]',17,1),(33,'2018-11-12 11:03:57.192249','2','Tinkeracd로 배우는 3D 프린터 기초와 모델링',1,'[{\"added\": {}}, {\"added\": {\"name\": \"video\", \"object\": \"Video object (1)\"}}, {\"added\": {\"name\": \"video\", \"object\": \"Video object (2)\"}}, {\"added\": {\"name\": \"video\", \"object\": \"Video object (3)\"}}, {\"added\": {\"name\": \"video\", \"object\": \"Video object (4)\"}}, {\"added\": {\"name\": \"video\", \"object\": \"Video object (5)\"}}, {\"added\": {\"name\": \"video\", \"object\": \"Video object (6)\"}}, {\"added\": {\"name\": \"video\", \"object\": \"Video object (7)\"}}, {\"added\": {\"name\": \"video\", \"object\": \"Video object (8)\"}}]',17,1),(34,'2018-11-12 11:06:15.187707','3','[무료][5분 영상] 엔트리(이론)',1,'[{\"added\": {}}]',17,1),(35,'2018-11-12 11:07:21.091328','4','[무료][5분 영상] 엔트리(기초, 예제)',1,'[{\"added\": {}}]',17,1),(36,'2018-11-12 11:09:36.398432','11','[키트] 거리측정기 만들기 키트(미메이커보드)',2,'[{\"changed\": {\"fields\": [\"product_image\"]}}]',15,1),(37,'2018-11-12 12:10:52.298112','2','Tinkeracd로 배우는 3D 프린터 기초와 모델링',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',17,1),(38,'2018-11-17 10:41:44.744179','1','[초등학교 완벽대비] 엔트리를 활용한 SW 코딩의 이해',2,'[{\"changed\": {\"fields\": [\"material\"]}}]',17,1),(39,'2018-11-17 13:44:15.620854','3','[보드]미메이커 코딩보드 DIY',2,'[{\"changed\": {\"fields\": [\"related_lec\"]}}]',15,1),(40,'2018-11-17 13:48:43.893511','2','[교재] 로봇 코딩의 이해(무료 영상 준비중)',2,'[{\"changed\": {\"fields\": [\"related_lec\"]}}]',15,1),(41,'2018-11-18 03:55:29.167330','1','이름은?',1,'[{\"added\": {}}, {\"added\": {\"name\": \"choice\", \"object\": \"\\uc774\\uae30\\ud638\"}}, {\"added\": {\"name\": \"choice\", \"object\": \"\\uc800\\uae30\\ud638\"}}, {\"added\": {\"name\": \"choice\", \"object\": \"\\ubc15\\uae30\\ud638\"}}]',11,1),(42,'2018-11-18 06:19:28.242962','2','testuser1',1,'[{\"added\": {}}]',4,1),(43,'2018-11-18 06:19:31.276329','1','UserProfile object (1)',1,'[{\"added\": {}}]',20,1),(44,'2018-11-19 07:03:58.081793','1','lsirikh',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',4,1),(45,'2018-11-19 07:04:16.762151','1','lsirikh',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',4,1),(46,'2018-11-23 03:21:06.696542','10','testuser8',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(47,'2018-11-23 03:31:13.282343','7','testuser5',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(48,'2018-11-27 02:30:28.937048','17','testuser15',3,'',4,1),(49,'2018-11-27 02:31:27.598394','2','testuser1',3,'',4,1),(50,'2018-11-27 02:31:27.602502','12','testuser10',3,'',4,1),(51,'2018-11-27 02:31:27.605894','13','testuser11',3,'',4,1),(52,'2018-11-27 02:31:27.608763','14','testuser12',3,'',4,1),(53,'2018-11-27 02:31:27.611777','15','testuser13',3,'',4,1),(54,'2018-11-27 02:31:27.617318','16','testuser14',3,'',4,1),(55,'2018-11-27 02:31:27.619944','7','testuser5',3,'',4,1),(56,'2018-11-27 02:31:27.621662','8','testuser6',3,'',4,1),(57,'2018-11-27 02:31:27.623772','9','testuser7',3,'',4,1),(58,'2018-11-27 02:31:27.625987','10','testuser8',3,'',4,1),(59,'2018-11-27 02:31:27.628753','11','testuser9',3,'',4,1),(60,'2018-11-27 02:31:27.634763','3','usertest2',3,'',4,1),(61,'2018-11-27 02:31:27.636979','4','usertest3',3,'',4,1),(62,'2018-11-27 02:31:27.639264','5','usertest4',3,'',4,1),(63,'2018-11-27 02:31:27.641069','6','usertest5',3,'',4,1),(64,'2018-11-27 07:47:36.632782','20','testuser02',2,'[{\"changed\": {\"fields\": [\"birth\", \"gender\"]}}]',20,1),(65,'2018-11-28 06:56:41.738306','20','testuser02',2,'[{\"changed\": {\"fields\": [\"favorite_lecture\"]}}]',20,1),(66,'2018-12-05 07:12:45.757893','12','lsirikh',2,'[{\"changed\": {\"fields\": [\"email_confirmed\"]}}]',20,1),(67,'2018-12-05 07:12:54.071325','19','testuser01',2,'[{\"changed\": {\"fields\": [\"email_confirmed\"]}}]',20,1),(68,'2018-12-05 07:12:59.601316','20','testuser02',2,'[{\"changed\": {\"fields\": [\"email_confirmed\"]}}]',20,1),(69,'2018-12-05 07:13:06.607837','21','testuser03',2,'[{\"changed\": {\"fields\": [\"email_confirmed\"]}}]',20,1),(70,'2018-12-05 07:14:20.056797','21','testuser04',3,'',4,1),(71,'2018-12-05 07:36:46.810648','22','testuser04',3,'',4,1),(72,'2018-12-05 07:36:46.813567','23','testuser05',3,'',4,1),(73,'2018-12-05 07:43:22.083913','24','testuser04',3,'',4,1),(74,'2018-12-05 07:47:24.931353','25','testuser04',3,'',4,1),(75,'2018-12-05 07:47:24.935493','26','testuser05',3,'',4,1),(76,'2018-12-05 07:47:24.938435','27','testuser06',3,'',4,1),(77,'2018-12-05 07:53:54.638044','28','testuser04',3,'',4,1),(78,'2018-12-09 08:30:30.050349','20','testuser03',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(79,'2018-12-12 15:09:36.375523','12','lsirikh',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',20,1),(80,'2018-12-15 16:39:33.286167','1','코딩 강의 게시판',1,'[{\"added\": {}}]',21,1),(81,'2018-12-15 16:40:02.026930','2','미메이커 코딩보드 게시판',1,'[{\"added\": {}}]',21,1),(82,'2018-12-15 16:40:41.182920','3','3D모델링 및 출력 게시판',1,'[{\"added\": {}}]',21,1),(83,'2018-12-15 16:49:19.708700','3','3D모델링 및 출력',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',21,1),(84,'2018-12-15 16:49:29.129852','2','미메이커 코딩보드',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',21,1),(85,'2018-12-15 16:49:38.141653','1','코딩 강의',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',21,1),(86,'2018-12-16 10:27:19.516562','1','테스트입니다.',1,'[{\"added\": {}}]',22,1),(87,'2018-12-16 10:28:46.451689','1','Post object (1)',1,'[{\"added\": {}}]',23,1),(88,'2018-12-19 04:04:52.886056','2','두 번째 테스트 입니다.',1,'[{\"added\": {}}]',22,1),(89,'2018-12-19 05:51:18.831776','4','아두이노',1,'[{\"added\": {}}]',21,1),(90,'2018-12-19 05:53:49.566251','3','세 번째 테스트 입니다.',1,'[{\"added\": {}}]',22,1),(91,'2018-12-19 05:59:26.977514','4','네 번째 테스트입니다.',1,'[{\"added\": {}}]',22,1),(92,'2018-12-19 06:00:14.498419','4','네 번째 테스트입니다.',3,'',22,1),(93,'2018-12-19 06:05:02.523885','4','아두이노',3,'',21,1),(94,'2018-12-20 08:54:07.038971','9','Post object (9)',2,'[{\"changed\": {\"fields\": [\"message\", \"updated_at\", \"updated_by\"]}}]',23,1),(95,'2018-12-21 04:06:13.180647','2','두 번째 테스트 입니다.',3,'',22,1),(96,'2018-12-21 07:45:17.771927','13','Post object (13)',3,'',23,1),(97,'2018-12-21 07:45:17.774500','12','Post object (12)',3,'',23,1),(98,'2018-12-21 07:45:17.776718','11','Post object (11)',3,'',23,1),(99,'2018-12-21 07:45:17.779121','10','Post object (10)',3,'',23,1),(100,'2018-12-21 07:45:17.780848','9','Post object (9)',3,'',23,1),(101,'2018-12-21 07:45:17.783087','8','Post object (8)',3,'',23,1),(102,'2018-12-21 07:45:17.786655','7','Post object (7)',3,'',23,1),(103,'2018-12-21 07:45:17.791130','6','Post object (6)',3,'',23,1),(104,'2018-12-21 07:45:17.794286','5','Post object (5)',3,'',23,1),(105,'2018-12-21 07:45:17.796700','4','Post object (4)',3,'',23,1),(106,'2018-12-21 07:45:17.801948','3','Post object (3)',3,'',23,1),(107,'2018-12-21 07:45:17.804655','2','Post object (2)',3,'',23,1),(108,'2018-12-21 07:45:17.807408','1','Post object (1)',3,'',23,1),(109,'2018-12-21 08:27:37.021934','1','코딩 강의 게시판',1,'[{\"added\": {}}]',21,1),(110,'2018-12-21 08:27:44.251987','2','미메이커 코딩보드 게시판',1,'[{\"added\": {}}]',21,1),(111,'2018-12-21 08:27:51.706938','3','3D모델링 및 출력 게시판',1,'[{\"added\": {}}]',21,1),(112,'2018-12-21 08:28:12.516183','1','테스트 입니다.',1,'[{\"added\": {}}]',22,1),(113,'2018-12-21 14:29:43.010975','7','Post object (7)',3,'',23,1),(114,'2018-12-23 12:10:19.324712','116','Post object (116)',3,'',23,1),(115,'2018-12-23 12:10:19.329149','115','Post object (115)',3,'',23,1),(116,'2018-12-23 12:10:19.332216','114','Post object (114)',3,'',23,1),(117,'2018-12-23 12:10:19.335698','113','Post object (113)',3,'',23,1),(118,'2018-12-23 12:10:19.339227','112','Post object (112)',3,'',23,1),(119,'2018-12-23 12:10:19.342171','111','Post object (111)',3,'',23,1),(120,'2018-12-23 12:10:19.357266','110','Post object (110)',3,'',23,1),(121,'2018-12-23 12:10:19.360507','109','Post object (109)',3,'',23,1),(122,'2018-12-23 12:10:19.363018','108','Post object (108)',3,'',23,1),(123,'2018-12-23 12:10:19.364374','107','Post object (107)',3,'',23,1),(124,'2018-12-23 12:10:19.366143','106','Post object (106)',3,'',23,1),(125,'2018-12-23 12:10:19.367456','105','Post object (105)',3,'',23,1),(126,'2018-12-23 12:10:19.370238','104','Post object (104)',3,'',23,1),(127,'2018-12-23 12:10:19.371563','103','Post object (103)',3,'',23,1),(128,'2018-12-23 12:10:19.373705','102','Post object (102)',3,'',23,1),(129,'2018-12-23 12:10:19.376420','101','Post object (101)',3,'',23,1),(130,'2018-12-23 12:10:19.379768','100','Post object (100)',3,'',23,1),(131,'2018-12-23 12:10:19.383376','99','Post object (99)',3,'',23,1),(132,'2018-12-23 12:10:19.385893','98','Post object (98)',3,'',23,1),(133,'2018-12-23 12:10:19.389471','97','Post object (97)',3,'',23,1),(134,'2018-12-23 12:10:19.393076','96','Post object (96)',3,'',23,1),(135,'2018-12-23 12:10:19.395334','95','Post object (95)',3,'',23,1),(136,'2018-12-23 12:10:19.397525','94','Post object (94)',3,'',23,1),(137,'2018-12-23 12:10:19.402667','93','Post object (93)',3,'',23,1),(138,'2018-12-23 12:10:19.405869','92','Post object (92)',3,'',23,1),(139,'2018-12-23 12:10:19.408001','91','Post object (91)',3,'',23,1),(140,'2018-12-23 12:10:19.411724','90','Post object (90)',3,'',23,1),(141,'2018-12-23 12:10:19.414185','89','Post object (89)',3,'',23,1),(142,'2018-12-23 12:10:19.415826','88','Post object (88)',3,'',23,1),(143,'2018-12-23 12:10:19.418051','87','Post object (87)',3,'',23,1),(144,'2018-12-23 12:10:19.421104','86','Post object (86)',3,'',23,1),(145,'2018-12-23 12:10:19.422579','85','Post object (85)',3,'',23,1),(146,'2018-12-23 12:10:19.424137','84','Post object (84)',3,'',23,1),(147,'2018-12-23 12:10:19.429824','83','Post object (83)',3,'',23,1),(148,'2018-12-23 12:10:19.431462','82','Post object (82)',3,'',23,1),(149,'2018-12-23 12:10:19.433244','81','Post object (81)',3,'',23,1),(150,'2018-12-23 12:10:19.435179','80','Post object (80)',3,'',23,1),(151,'2018-12-23 12:10:19.437054','79','Post object (79)',3,'',23,1),(152,'2018-12-23 12:10:19.438471','78','Post object (78)',3,'',23,1),(153,'2018-12-23 12:10:19.439901','77','Post object (77)',3,'',23,1),(154,'2018-12-23 12:10:19.443247','76','Post object (76)',3,'',23,1),(155,'2018-12-23 12:10:19.445804','75','Post object (75)',3,'',23,1),(156,'2018-12-23 12:10:19.448659','74','Post object (74)',3,'',23,1),(157,'2018-12-23 12:10:19.454931','73','Post object (73)',3,'',23,1),(158,'2018-12-23 12:10:19.456765','72','Post object (72)',3,'',23,1),(159,'2018-12-23 12:10:19.458338','71','Post object (71)',3,'',23,1),(160,'2018-12-23 12:10:19.459880','70','Post object (70)',3,'',23,1),(161,'2018-12-23 12:10:19.461710','69','Post object (69)',3,'',23,1),(162,'2018-12-23 12:10:19.463217','68','Post object (68)',3,'',23,1),(163,'2018-12-23 12:10:19.469198','67','Post object (67)',3,'',23,1),(164,'2018-12-23 12:10:19.471744','66','Post object (66)',3,'',23,1),(165,'2018-12-23 12:10:19.474450','65','Post object (65)',3,'',23,1),(166,'2018-12-23 12:10:19.486705','64','Post object (64)',3,'',23,1),(167,'2018-12-23 12:10:19.488587','63','Post object (63)',3,'',23,1),(168,'2018-12-23 12:10:19.490159','62','Post object (62)',3,'',23,1),(169,'2018-12-23 12:10:19.491648','61','Post object (61)',3,'',23,1),(170,'2018-12-23 12:10:19.497202','60','Post object (60)',3,'',23,1),(171,'2018-12-23 12:10:19.498682','59','Post object (59)',3,'',23,1),(172,'2018-12-23 12:10:19.500066','58','Post object (58)',3,'',23,1),(173,'2018-12-23 12:10:19.502281','57','Post object (57)',3,'',23,1),(174,'2018-12-23 12:10:19.503785','56','Post object (56)',3,'',23,1),(175,'2018-12-23 12:10:19.505540','55','Post object (55)',3,'',23,1),(176,'2018-12-23 12:10:19.506983','54','Post object (54)',3,'',23,1),(177,'2018-12-23 12:10:19.510133','53','Post object (53)',3,'',23,1),(178,'2018-12-23 12:10:19.517009','52','Post object (52)',3,'',23,1),(179,'2018-12-23 12:10:19.518627','51','Post object (51)',3,'',23,1),(180,'2018-12-23 12:10:19.520740','50','Post object (50)',3,'',23,1),(181,'2018-12-23 12:10:19.522131','49','Post object (49)',3,'',23,1),(182,'2018-12-23 12:10:19.523720','48','Post object (48)',3,'',23,1),(183,'2018-12-23 12:10:19.526933','47','Post object (47)',3,'',23,1),(184,'2018-12-23 12:10:19.529377','46','Post object (46)',3,'',23,1),(185,'2018-12-23 12:10:19.531684','45','Post object (45)',3,'',23,1),(186,'2018-12-23 12:10:19.535823','44','Post object (44)',3,'',23,1),(187,'2018-12-23 12:10:19.537768','43','Post object (43)',3,'',23,1),(188,'2018-12-23 12:10:19.539196','42','Post object (42)',3,'',23,1),(189,'2018-12-23 12:10:19.540956','41','Post object (41)',3,'',23,1),(190,'2018-12-23 12:10:19.548153','40','Post object (40)',3,'',23,1),(191,'2018-12-23 12:10:19.551547','39','Post object (39)',3,'',23,1),(192,'2018-12-23 12:10:19.555460','38','Post object (38)',3,'',23,1),(193,'2018-12-23 12:10:19.557820','37','Post object (37)',3,'',23,1),(194,'2018-12-23 12:10:19.559336','36','Post object (36)',3,'',23,1),(195,'2018-12-23 12:10:19.561081','35','Post object (35)',3,'',23,1),(196,'2018-12-23 12:10:19.562712','34','Post object (34)',3,'',23,1),(197,'2018-12-23 12:10:19.565110','33','Post object (33)',3,'',23,1),(198,'2018-12-23 12:10:19.566677','32','Post object (32)',3,'',23,1),(199,'2018-12-23 12:10:19.568903','31','Post object (31)',3,'',23,1),(200,'2018-12-23 12:10:19.570369','30','Post object (30)',3,'',23,1),(201,'2018-12-23 12:10:19.571741','29','Post object (29)',3,'',23,1),(202,'2018-12-23 12:10:19.578562','28','Post object (28)',3,'',23,1),(203,'2018-12-23 12:10:19.580179','27','Post object (27)',3,'',23,1),(204,'2018-12-23 12:10:19.582044','26','Post object (26)',3,'',23,1),(205,'2018-12-23 12:10:19.583640','25','Post object (25)',3,'',23,1),(206,'2018-12-23 12:10:19.586582','24','Post object (24)',3,'',23,1),(207,'2018-12-23 12:10:19.588136','23','Post object (23)',3,'',23,1),(208,'2018-12-23 12:10:19.590379','22','Post object (22)',3,'',23,1),(209,'2018-12-23 12:10:19.594005','21','Post object (21)',3,'',23,1),(210,'2018-12-23 12:10:19.597447','20','Post object (20)',3,'',23,1),(211,'2018-12-23 12:10:19.598987','19','Post object (19)',3,'',23,1),(212,'2018-12-28 13:37:03.812264','20','testuser03',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(213,'2018-12-30 08:48:26.923092','3','[보드]미메이커 코딩보드 DIY',2,'[{\"changed\": {\"fields\": [\"link\"]}}]',15,1),(214,'2018-12-31 02:35:14.745976','39','testuser21',3,'',4,1),(215,'2018-12-31 02:35:28.547289','38','testuser20',3,'',4,1),(216,'2018-12-31 02:36:15.576272','38','testuser12',2,'[{\"changed\": {\"fields\": [\"email_confirmed\"]}}]',20,1),(217,'2018-12-31 02:38:05.465320','37','testuser12',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(218,'2018-12-31 02:52:56.192187','38','testuser12',3,'',20,1),(219,'2018-12-31 03:13:54.865707','37','testuser12',3,'',4,1),(220,'2018-12-31 03:14:02.987531','35','testuser10',3,'',4,1),(221,'2018-12-31 03:14:02.990261','36','testuser11',3,'',4,1),(222,'2018-12-31 03:14:15.348930','30','testuser05',3,'',4,1),(223,'2018-12-31 03:14:15.351084','31','testuser06',3,'',4,1),(224,'2018-12-31 03:14:15.352590','32','testuser07',3,'',4,1),(225,'2018-12-31 03:14:15.353894','33','testuser08',3,'',4,1),(226,'2018-12-31 03:14:15.358044','34','testuser09',3,'',4,1),(227,'2018-12-31 03:14:36.451381','18','testuser01',3,'',4,1),(228,'2018-12-31 03:14:36.453813','19','testuser02',3,'',4,1),(229,'2018-12-31 03:14:36.455931','20','testuser03',3,'',4,1),(230,'2018-12-31 03:14:36.457584','29','testuser04',3,'',4,1),(231,'2018-12-31 03:22:17.818716','112','이미지 테스트 글입니다.',3,'',22,1),(232,'2018-12-31 03:22:17.821840','103','Topic test #99',3,'',22,1),(233,'2018-12-31 03:22:17.824312','102','Topic test #98',3,'',22,1),(234,'2018-12-31 03:22:17.826078','101','Topic test #97',3,'',22,1),(235,'2018-12-31 03:22:17.828569','100','Topic test #96',3,'',22,1),(236,'2018-12-31 03:22:17.832814','99','Topic test #95',3,'',22,1),(237,'2018-12-31 03:22:17.835675','98','Topic test #94',3,'',22,1),(238,'2018-12-31 03:22:17.837582','97','Topic test #93',3,'',22,1),(239,'2018-12-31 03:22:17.840485','96','Topic test #92',3,'',22,1),(240,'2018-12-31 03:22:17.842736','95','Topic test #91',3,'',22,1),(241,'2018-12-31 03:22:17.844681','94','Topic test #90',3,'',22,1),(242,'2018-12-31 03:22:17.850670','93','Topic test #89',3,'',22,1),(243,'2018-12-31 03:22:17.853867','92','Topic test #88',3,'',22,1),(244,'2018-12-31 03:22:17.855785','91','Topic test #87',3,'',22,1),(245,'2018-12-31 03:22:17.858225','90','Topic test #86',3,'',22,1),(246,'2018-12-31 03:22:17.861722','89','Topic test #85',3,'',22,1),(247,'2018-12-31 03:22:17.863830','88','Topic test #84',3,'',22,1),(248,'2018-12-31 03:22:17.865504','87','Topic test #83',3,'',22,1),(249,'2018-12-31 03:22:17.870706','86','Topic test #82',3,'',22,1),(250,'2018-12-31 03:22:17.873032','85','Topic test #81',3,'',22,1),(251,'2018-12-31 03:22:17.875229','84','Topic test #80',3,'',22,1),(252,'2018-12-31 03:22:17.876716','83','Topic test #79',3,'',22,1),(253,'2018-12-31 03:22:17.881761','82','Topic test #78',3,'',22,1),(254,'2018-12-31 03:22:17.884904','81','Topic test #77',3,'',22,1),(255,'2018-12-31 03:22:17.887900','80','Topic test #76',3,'',22,1),(256,'2018-12-31 03:22:17.891100','79','Topic test #75',3,'',22,1),(257,'2018-12-31 03:22:17.894340','78','Topic test #74',3,'',22,1),(258,'2018-12-31 03:22:17.896633','77','Topic test #73',3,'',22,1),(259,'2018-12-31 03:22:17.899911','76','Topic test #72',3,'',22,1),(260,'2018-12-31 03:22:17.901865','75','Topic test #71',3,'',22,1),(261,'2018-12-31 03:22:17.903952','74','Topic test #70',3,'',22,1),(262,'2018-12-31 03:22:17.905642','73','Topic test #69',3,'',22,1),(263,'2018-12-31 03:22:17.907724','72','Topic test #68',3,'',22,1),(264,'2018-12-31 03:22:17.909365','71','Topic test #67',3,'',22,1),(265,'2018-12-31 03:22:17.911374','70','Topic test #66',3,'',22,1),(266,'2018-12-31 03:22:17.915555','69','Topic test #65',3,'',22,1),(267,'2018-12-31 03:22:17.918449','68','Topic test #64',3,'',22,1),(268,'2018-12-31 03:22:17.920405','67','Topic test #63',3,'',22,1),(269,'2018-12-31 03:22:17.923880','66','Topic test #62',3,'',22,1),(270,'2018-12-31 03:22:17.926109','65','Topic test #61',3,'',22,1),(271,'2018-12-31 03:22:17.929187','64','Topic test #60',3,'',22,1),(272,'2018-12-31 03:22:17.934601','63','Topic test #59',3,'',22,1),(273,'2018-12-31 03:22:17.936998','62','Topic test #58',3,'',22,1),(274,'2018-12-31 03:22:17.939057','61','Topic test #57',3,'',22,1),(275,'2018-12-31 03:22:17.940689','60','Topic test #56',3,'',22,1),(276,'2018-12-31 03:22:17.942724','59','Topic test #55',3,'',22,1),(277,'2018-12-31 03:22:17.944655','58','Topic test #54',3,'',22,1),(278,'2018-12-31 03:22:17.951372','57','Topic test #53',3,'',22,1),(279,'2018-12-31 03:22:17.953034','56','Topic test #52',3,'',22,1),(280,'2018-12-31 03:22:17.961261','55','Topic test #51',3,'',22,1),(281,'2018-12-31 03:22:17.964088','54','Topic test #50',3,'',22,1),(282,'2018-12-31 03:22:17.966589','53','Topic test #49',3,'',22,1),(283,'2018-12-31 03:22:17.968972','52','Topic test #48',3,'',22,1),(284,'2018-12-31 03:22:17.971179','51','Topic test #47',3,'',22,1),(285,'2018-12-31 03:22:17.974966','50','Topic test #46',3,'',22,1),(286,'2018-12-31 03:22:17.976813','49','Topic test #45',3,'',22,1),(287,'2018-12-31 03:22:17.979993','48','Topic test #44',3,'',22,1),(288,'2018-12-31 03:22:17.982290','47','Topic test #43',3,'',22,1),(289,'2018-12-31 03:22:17.984294','46','Topic test #42',3,'',22,1),(290,'2018-12-31 03:22:17.985864','45','Topic test #41',3,'',22,1),(291,'2018-12-31 03:22:17.987860','44','Topic test #40',3,'',22,1),(292,'2018-12-31 03:22:17.989472','43','Topic test #39',3,'',22,1),(293,'2018-12-31 03:22:17.991536','42','Topic test #38',3,'',22,1),(294,'2018-12-31 03:22:17.993307','41','Topic test #37',3,'',22,1),(295,'2018-12-31 03:22:17.995371','40','Topic test #36',3,'',22,1),(296,'2018-12-31 03:22:18.002032','39','Topic test #35',3,'',22,1),(297,'2018-12-31 03:22:18.004190','38','Topic test #34',3,'',22,1),(298,'2018-12-31 03:22:18.005813','37','Topic test #33',3,'',22,1),(299,'2018-12-31 03:22:18.007828','36','Topic test #32',3,'',22,1),(300,'2018-12-31 03:22:18.009402','35','Topic test #31',3,'',22,1),(301,'2018-12-31 03:22:18.011414','34','Topic test #30',3,'',22,1),(302,'2018-12-31 03:22:18.014381','33','Topic test #29',3,'',22,1),(303,'2018-12-31 03:22:18.017939','32','Topic test #28',3,'',22,1),(304,'2018-12-31 03:22:18.024365','31','Topic test #27',3,'',22,1),(305,'2018-12-31 03:22:18.026556','30','Topic test #26',3,'',22,1),(306,'2018-12-31 03:22:18.028519','29','Topic test #25',3,'',22,1),(307,'2018-12-31 03:22:18.030776','28','Topic test #24',3,'',22,1),(308,'2018-12-31 03:22:18.032473','27','Topic test #23',3,'',22,1),(309,'2018-12-31 03:22:18.034515','26','Topic test #22',3,'',22,1),(310,'2018-12-31 03:22:18.036579','25','Topic test #21',3,'',22,1),(311,'2018-12-31 03:22:18.041649','24','Topic test #20',3,'',22,1),(312,'2018-12-31 03:22:18.044644','23','Topic test #19',3,'',22,1),(313,'2018-12-31 03:22:18.047172','22','Topic test #18',3,'',22,1),(314,'2018-12-31 03:22:18.051761','21','Topic test #17',3,'',22,1),(315,'2018-12-31 03:22:18.053400','20','Topic test #16',3,'',22,1),(316,'2018-12-31 03:22:18.055421','19','Topic test #15',3,'',22,1),(317,'2018-12-31 03:22:18.057031','18','Topic test #14',3,'',22,1),(318,'2018-12-31 03:22:18.059224','17','Topic test #13',3,'',22,1),(319,'2018-12-31 03:22:18.060830','16','Topic test #12',3,'',22,1),(320,'2018-12-31 03:22:18.065957','15','Topic test #11',3,'',22,1),(321,'2018-12-31 03:22:18.068954','14','Topic test #10',3,'',22,1),(322,'2018-12-31 03:22:18.070695','13','Topic test #9',3,'',22,1),(323,'2018-12-31 03:22:18.072034','12','Topic test #8',3,'',22,1),(324,'2018-12-31 03:22:18.073375','11','Topic test #7',3,'',22,1),(325,'2018-12-31 03:22:18.075092','10','Topic test #6',3,'',22,1),(326,'2018-12-31 03:22:18.076447','9','Topic test #5',3,'',22,1),(327,'2018-12-31 03:22:18.079242','8','Topic test #4',3,'',22,1),(328,'2018-12-31 03:22:18.085316','7','Topic test #3',3,'',22,1),(329,'2018-12-31 03:22:18.087590','6','Topic test #2',3,'',22,1),(330,'2018-12-31 03:22:18.088966','5','Topic test #1',3,'',22,1),(331,'2018-12-31 03:22:34.043983','4','Topic test #0',3,'',22,1),(332,'2018-12-31 03:22:34.049372','3','두 번째 테스트 글',3,'',22,1),(333,'2018-12-31 03:22:34.052800','1','테스트 입니다.  수정했습니다.',3,'',22,1),(334,'2018-12-31 03:23:26.971720','1','memaker',2,'[{\"changed\": {\"fields\": [\"username\"]}}]',4,1),(335,'2018-12-31 04:41:39.396043','40','testuser01',3,'',4,1),(336,'2018-12-31 08:16:26.453745','41','testuser01',3,'',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (20,'accounts','userprofile'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(21,'boards','board'),(23,'boards','post'),(22,'boards','topic'),(5,'contenttypes','contenttype'),(7,'easy_thumbnails','source'),(8,'easy_thumbnails','thumbnail'),(9,'easy_thumbnails','thumbnaildimensions'),(12,'intro','intro'),(16,'lectures','category'),(17,'lectures','lecture'),(18,'lectures','section'),(19,'lectures','video'),(10,'polls','choice'),(11,'polls','question'),(13,'products','category'),(14,'products','detail'),(15,'products','product'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-12 06:59:20.182348'),(2,'auth','0001_initial','2018-11-12 06:59:20.553856'),(3,'admin','0001_initial','2018-11-12 06:59:20.637659'),(4,'admin','0002_logentry_remove_auto_add','2018-11-12 06:59:20.646597'),(5,'admin','0003_logentry_add_action_flag_choices','2018-11-12 06:59:20.656516'),(6,'contenttypes','0002_remove_content_type_name','2018-11-12 06:59:20.714150'),(7,'auth','0002_alter_permission_name_max_length','2018-11-12 06:59:20.746559'),(8,'auth','0003_alter_user_email_max_length','2018-11-12 06:59:20.784235'),(9,'auth','0004_alter_user_username_opts','2018-11-12 06:59:20.794145'),(10,'auth','0005_alter_user_last_login_null','2018-11-12 06:59:20.823899'),(11,'auth','0006_require_contenttypes_0002','2018-11-12 06:59:20.826953'),(12,'auth','0007_alter_validators_add_error_messages','2018-11-12 06:59:20.836663'),(13,'auth','0008_alter_user_username_max_length','2018-11-12 06:59:20.875856'),(14,'auth','0009_alter_user_last_name_max_length','2018-11-12 06:59:20.915737'),(15,'easy_thumbnails','0001_initial','2018-11-12 06:59:21.046683'),(16,'easy_thumbnails','0002_thumbnaildimensions','2018-11-12 06:59:21.099250'),(17,'intro','0001_initial','2018-11-12 06:59:21.119225'),(18,'intro','0002_auto_20181025_2011','2018-11-12 06:59:21.123911'),(19,'intro','0003_intro_character','2018-11-12 06:59:21.152716'),(20,'products','0001_initial','2018-11-12 06:59:21.294799'),(21,'products','0002_auto_20181026_1826','2018-11-12 06:59:21.306401'),(22,'products','0003_auto_20181026_1829','2018-11-12 06:59:21.312821'),(23,'products','0004_auto_20181026_2111','2018-11-12 06:59:21.324294'),(24,'products','0005_auto_20181026_2119','2018-11-12 06:59:21.330923'),(25,'products','0006_product_product_thumbnail','2018-11-12 06:59:21.366426'),(26,'products','0007_remove_product_product_thumbnail','2018-11-12 06:59:21.394559'),(27,'products','0008_auto_20181029_0212','2018-11-12 06:59:21.400603'),(28,'products','0009_auto_20181107_1255','2018-11-12 06:59:21.569339'),(29,'lectures','0001_initial','2018-11-12 06:59:21.751017'),(30,'lectures','0002_auto_20181101_1241','2018-11-12 06:59:21.759360'),(31,'lectures','0003_auto_20181106_1437','2018-11-12 06:59:22.080030'),(32,'lectures','0004_auto_20181106_1443','2018-11-12 06:59:22.111083'),(33,'lectures','0005_auto_20181106_1452','2018-11-12 06:59:22.356867'),(34,'lectures','0006_auto_20181106_1457','2018-11-12 06:59:22.398600'),(35,'lectures','0007_lecture_description','2018-11-12 06:59:22.433552'),(36,'lectures','0008_lecture_material','2018-11-12 06:59:22.498932'),(37,'lectures','0009_auto_20181112_0023','2018-11-12 06:59:22.575224'),(38,'lectures','0010_lecture_content','2018-11-12 06:59:22.612748'),(39,'polls','0001_initial','2018-11-12 06:59:22.697846'),(40,'products','0010_auto_20181111_2346','2018-11-12 06:59:22.754765'),(41,'products','0011_detail_title','2018-11-12 06:59:22.786841'),(42,'products','0012_auto_20181112_1434','2018-11-12 06:59:22.849644'),(43,'products','0013_auto_20181112_1523','2018-11-12 06:59:22.858630'),(44,'sessions','0001_initial','2018-11-12 06:59:22.886479'),(45,'lectures','0011_auto_20181117_1940','2018-11-17 10:40:32.447115'),(46,'lectures','0012_auto_20181117_2206','2018-11-17 13:07:02.472982'),(47,'products','0014_product_related_lec','2018-11-17 13:42:25.514643'),(48,'products','0015_remove_product_related_lec','2018-11-17 13:42:25.552176'),(49,'products','0016_product_related_lec','2018-11-17 13:42:25.671137'),(50,'accounts','0001_initial','2018-11-18 06:15:28.988951'),(51,'accounts','0002_auto_20181127_1642','2018-11-27 07:42:14.546230'),(52,'accounts','0003_auto_20181127_1646','2018-11-27 07:46:55.313120'),(53,'accounts','0004_auto_20181127_1646','2018-11-27 07:46:55.468292'),(54,'accounts','0005_userprofile_email_confirmed','2018-12-05 07:12:06.386212'),(55,'accounts','0006_userprofile_image','2018-12-12 15:05:42.731158'),(56,'accounts','0007_auto_20181213_0008','2018-12-12 15:08:22.751665'),(57,'accounts','0008_remove_userprofile_image','2018-12-12 15:10:26.839752'),(58,'accounts','0009_userprofile_image','2018-12-12 15:10:50.151347'),(59,'accounts','0010_remove_userprofile_image','2018-12-12 15:13:17.831662'),(60,'accounts','0011_userprofile_image','2018-12-12 15:13:28.271055'),(61,'accounts','0012_auto_20181213_0024','2018-12-12 15:24:33.293187'),(62,'accounts','0013_auto_20181213_0025','2018-12-12 15:25:40.709528'),(63,'accounts','0014_auto_20181213_0058','2018-12-12 15:58:43.953923'),(64,'accounts','0015_auto_20181213_0100','2018-12-12 16:00:48.328977'),(65,'accounts','0016_userprofile_route','2018-12-13 03:29:39.593545'),(67,'boards','0002_topic_views','2018-12-20 06:44:47.879984'),(68,'boards','0003_auto_20181220_1733','2018-12-20 08:33:39.954129'),(69,'boards','0004_auto_20181221_1241','2018-12-21 07:34:50.006733'),(70,'boards','0005_auto_20181221_1631','2018-12-21 07:34:50.235893'),(71,'boards','0001_initial','2018-12-21 08:15:21.855208'),(72,'boards','0002_remove_post_created_by','2018-12-21 09:10:27.841227'),(73,'boards','0003_auto_20181221_1812','2018-12-21 09:12:14.931287'),(74,'boards','0004_auto_20181221_1812','2018-12-21 09:12:59.736277'),(75,'boards','0005_auto_20181221_1813','2018-12-21 09:13:17.190676'),(76,'boards','0006_auto_20181221_1824','2018-12-21 09:24:49.967423'),(77,'boards','0007_post_order','2018-12-21 10:15:48.948904'),(78,'accounts','0017_userprofile_agree','2018-12-27 01:59:14.659653'),(79,'products','0017_product_link','2018-12-30 08:41:44.208298'),(80,'boards','0008_auto_20181231_1213','2018-12-31 03:13:34.766708');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('127b8hgpsxf22nlyxjuiijtic7jod6nl','NGIzYTE4YTRlNmJmZDRiZjkxYTY0YmYyMTU5NmMwMTI1OWM3ODE5Yzp7fQ==','2018-12-05 17:02:13.883609'),('1lpumlttwfqhwdw613lz5u1b645al77n','NGIzYTE4YTRlNmJmZDRiZjkxYTY0YmYyMTU5NmMwMTI1OWM3ODE5Yzp7fQ==','2018-12-05 17:05:28.937142'),('68hfg8qri7046g55yxfj8ayyglss1bt1','MzhhZTc3NzBhNzBjNjMwNzBlZDhlMTlhNjRhZTAyMzVjODg4MWE5Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4NGU1MDIwNGZlNWYxYTE2MTUwN2VlYjBjZmNiMzY2ZWVhNTM2YTNkIn0=','2018-12-04 03:08:16.075682'),('82x63crugv4dul79gqwqzpgntnr0hcaa','Y2MwNmQ3YWRiNmJhYzlmY2M0NWRhMzBhOWIxYTYyMzhmOTk2MGRkNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNWE0NGJiMDNlNWI0MzkyNGQyM2I4YjRjMTlkMWJiMjAwYjEzMzZlIn0=','2018-12-04 03:45:52.472424'),('a7zbl9wn96r38bifo3wcz4unz71yabx8','NWJmMjlmOWI5Njg4MTZlZDdjZmYxOGUzN2Y5ZTJiMmVkMmI0YzYyMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZWY2YjQ1NjdhOGFkMWU0OGNjOGMzZGEwNzMzYmRmZjQyZDkwNGYzIn0=','2018-12-04 06:03:27.391780'),('azpnbgdyp7s3qskz4q7de7dxvwt6vftu','ZDYxZDM4YmRkNmZlMTdmZmQ3MTExZDk2ZmQ0YzZlYTU2NzA3N2MxMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3ZDBkZGE3NjIwMjdhZjA2MzIwNzQ3NGZmNzZhNWNhNjM0NWFiZTNlIn0=','2018-12-04 03:49:38.788997'),('ba925wv5y8e26foee462zbuo3juyznua','NjNmZTBjNWEyNDAyNmU5YjZhNWUzNDQyMDUzNGI1MGFhNDQxYzg2YTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YzVhNjU5MjY1MDE1YjJhMmUwOTFmNzk2NzYxNjczNDU3YzQxZTUzIn0=','2018-12-04 06:09:17.837710'),('bklboh6nrwih75swq17d0spzd8mrw7oh','NGIzYTE4YTRlNmJmZDRiZjkxYTY0YmYyMTU5NmMwMTI1OWM3ODE5Yzp7fQ==','2018-12-05 17:15:52.542212'),('ctw6wba04ybimr58iexc276xd1jbdyva','Y2E5MTZiODQ3M2IwNjgxNzM5NWM0NjQ2NjNkN2M5ZDhiMDNhMzk5Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiN2JhZjQzMTk3OWRkMGNlZWU5YTM1N2JjZjE2N2RmMWZmNDk1OGU5In0=','2018-12-04 03:13:38.199050'),('d6ienzleb7nykekpot5tmq9ioo9q53rh','NDRjNjQ2NjQxMWU1MTI1ZDAxODJkYzg5YzJjMTc2ZjBjYTQ5ODhmYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjOGRlYTQzYmFhMDc2ZjExYjE2MDZiMjgxNmQ0OWNlNGYwYTJhNDA4In0=','2018-12-04 03:12:36.293440'),('de40e7nyac51yriyn41b3r3rnc308arw','MTA2ZGI5ODYzYWU4YmNmOTAyNGQ4NjM4OGNlYzQyNGFjNjdiMzg3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNzRlYWI4OTczOTU5NzljYjQ3OThhYzk3ZjgzNjU1NjIxMmU0NjBjIn0=','2018-11-26 07:01:02.882194'),('drzn4h1kxxusr8twubdlltag5wbwizr9','Njg2MDFhYmMxZTI2NzBjMjRiNjRkY2E2MDc4YzM2NzNkMTM0Y2Q1Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZjY4ODg4ODc0MjNhNjBlN2E0Y2NmNDdhY2QzY2MyODVkZmViNDk5In0=','2018-12-04 06:26:15.054962'),('jdl3d3wilc480dhiomzwjz5179uznxgr','NGIzYTE4YTRlNmJmZDRiZjkxYTY0YmYyMTU5NmMwMTI1OWM3ODE5Yzp7fQ==','2018-12-02 12:16:00.040472'),('mdkt1o2gdbobbgf3uhr2uq8f276b9m00','ZjcyMGU2ZjI2MmRmMDJiOTQzYjkwZGJiY2QwMmNhMDNhOTg2Y2QxMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NDhiMWNhYzU4MDVjMDZjZWNmMDQzYjQzZjdmYjQ0MjU5Y2I4OWY3In0=','2018-12-04 03:34:35.455486'),('mv1z5qspj20yaox3apzrr1p6pr39e9jp','MTA2ZGI5ODYzYWU4YmNmOTAyNGQ4NjM4OGNlYzQyNGFjNjdiMzg3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNzRlYWI4OTczOTU5NzljYjQ3OThhYzk3ZjgzNjU1NjIxMmU0NjBjIn0=','2018-11-26 12:10:07.882936'),('okpn4skai6wfibr4ismc3onuaw191p2d','ZjllZWE1YzRmNTFiZTgxNThlZTY4OWI4YjU4N2NiYzVhYzk4NTVmOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNzlmNmQ4MDg3ZjExOTc3NmIzZDNmOTJjZjllMGM4ZTdjYzRkODNiIn0=','2018-12-04 03:41:58.349575'),('p2e36bws0u1std8ob6ecjdba83i2lkqi','NGIzYTE4YTRlNmJmZDRiZjkxYTY0YmYyMTU5NmMwMTI1OWM3ODE5Yzp7fQ==','2018-12-02 12:16:26.946073'),('rcrbg12aqtfh1t3ffwji05ghxbxhkqzv','MTA2ZGI5ODYzYWU4YmNmOTAyNGQ4NjM4OGNlYzQyNGFjNjdiMzg3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNzRlYWI4OTczOTU5NzljYjQ3OThhYzk3ZjgzNjU1NjIxMmU0NjBjIn0=','2018-11-26 08:52:12.061368'),('s85h9ee6isrkqisk5mlfk4qcezjs1z19','NGIzYTE4YTRlNmJmZDRiZjkxYTY0YmYyMTU5NmMwMTI1OWM3ODE5Yzp7fQ==','2018-12-05 17:07:13.259539'),('slm26qrcy1du08zmulkmji4a6tdoibgj','MzVmZTkzYzI3MmQ1OWE2MjNlNjBjNmZkNGQxOTg5MDRmNDA3OWJjYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNmUyN2I0N2NkMzJlMTBhYTNlNmU2YTkzZGZlZTlkYTY1NzE2MTk1In0=','2018-12-04 06:22:54.079696'),('u09bd618aq7yev13b3zlsii9np4ekfl3','ZmViYTlmZDg3NDNkYWRlNzNmMmFjNDYxZjI5ZTZhNGE4MDQ2YjI5Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzOTcxM2U5OGY5ZDczODQwMzAxZTg2NzFmZWU0Nzc4ZDI0ZjMzYTY4In0=','2018-12-04 03:37:48.126522'),('ul11xn7fbff9g2o9bth6vie6imn758eu','NTFmNmEwMjk5NzlhYmQxNzU5ODNlYTIxYzZmZmQwZGZjYTBlNjY2Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDE4NzllOWRhMWNkNjkwYzkwNTQ0NTc5ZmI2N2NhZGNiOWY2MTQ2In0=','2018-12-07 11:28:38.331615'),('xecz1y7ja76y1x9evfoan240v4jh3fh0','MTA2ZGI5ODYzYWU4YmNmOTAyNGQ4NjM4OGNlYzQyNGFjNjdiMzg3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNzRlYWI4OTczOTU5NzljYjQ3OThhYzk3ZjgzNjU1NjIxMmU0NjBjIn0=','2018-12-01 10:40:55.291791'),('yk3txpqsmc4smtsy43izgxe2km8pef8x','NGIzYTE4YTRlNmJmZDRiZjkxYTY0YmYyMTU5NmMwMTI1OWM3ODE5Yzp7fQ==','2018-12-02 12:17:08.770924'),('zoyqdcrwtvjgslqjskyodirw6ntwrcjo','NGIzYTE4YTRlNmJmZDRiZjkxYTY0YmYyMTU5NmMwMTI1OWM3ODE5Yzp7fQ==','2018-12-05 16:24:37.931600');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `easy_thumbnails_source`
--

DROP TABLE IF EXISTS `easy_thumbnails_source`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `easy_thumbnails_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_source_storage_hash_name_481ce32d_uniq` (`storage_hash`,`name`),
  KEY `easy_thumbnails_source_storage_hash_946cbcc9` (`storage_hash`),
  KEY `easy_thumbnails_source_name_5fe0edc6` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `easy_thumbnails_source`
--

LOCK TABLES `easy_thumbnails_source` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_source` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_source` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `easy_thumbnails_thumbnail`
--

DROP TABLE IF EXISTS `easy_thumbnails_thumbnail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `easy_thumbnails_thumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `source_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_thumbnai_storage_hash_name_source_fb375270_uniq` (`storage_hash`,`name`,`source_id`),
  KEY `easy_thumbnails_thum_source_id_5b57bc77_fk_easy_thum` (`source_id`),
  KEY `easy_thumbnails_thumbnail_storage_hash_f1435f49` (`storage_hash`),
  KEY `easy_thumbnails_thumbnail_name_b5882c31` (`name`),
  CONSTRAINT `easy_thumbnails_thum_source_id_5b57bc77_fk_easy_thum` FOREIGN KEY (`source_id`) REFERENCES `easy_thumbnails_source` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `easy_thumbnails_thumbnail`
--

LOCK TABLES `easy_thumbnails_thumbnail` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `easy_thumbnails_thumbnaildimensions`
--

DROP TABLE IF EXISTS `easy_thumbnails_thumbnaildimensions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `easy_thumbnails_thumbnaildimensions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thumbnail_id` int(11) NOT NULL,
  `width` int(10) unsigned DEFAULT NULL,
  `height` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `thumbnail_id` (`thumbnail_id`),
  CONSTRAINT `easy_thumbnails_thum_thumbnail_id_c3a0c549_fk_easy_thum` FOREIGN KEY (`thumbnail_id`) REFERENCES `easy_thumbnails_thumbnail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `easy_thumbnails_thumbnaildimensions`
--

LOCK TABLES `easy_thumbnails_thumbnaildimensions` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `intro_intro`
--

DROP TABLE IF EXISTS `intro_intro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `intro_intro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `character` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `intro_intro`
--

LOCK TABLES `intro_intro` WRITE;
/*!40000 ALTER TABLE `intro_intro` DISABLE KEYS */;
INSERT INTO `intro_intro` VALUES (1,'미메이커 코딩보드','content_image/창의제작_grUMlry.png','· 직관적인 디자인\r\n· 간편한 모듈연결 및 조립\r\n· 오픈소스 기반의 뛰어난 확장성\r\n· 자신만의 제품을 완성할 수 있는 다양한 프로젝트 키트 상품','character_image/케릭터_곰_FOZvEyi.png'),(2,'교육 영상 콘텐츠','content_image/영상강의_YQW0V9e.png','· 애니메이션을 비롯한 다양한 교육 영상 콘텐츠로 쉽고, 재미있는 코딩 교육\r\n· 코딩 제작 과정과 만들기 제작 과정을 상세히 묘사한 영상 콘텐츠\r\n· 현직 교사 및 전문가의 검토를 완료한 검증된 교육 콘텐츠','character_image/케릭터_토끼_Qwf4lLb.png'),(3,'코딩 교육 교재','content_image/교재및교안_UY8yqH0.png','· 교육부 지침을 반영한 코딩 교재\r\n· 현직 교사의 검증을 받은 학습 구성 및 내용\r\n· 다양한 예제를 통학 학습내용 확인\r\n· 국내 최대 코딩 교육 플랫폼 엔트리 적용 교재 \r\n· 교사를 위한 교육 지도서 제공(별도문의)','character_image/케릭터_돼지_ce5NT4u.png');
/*!40000 ALTER TABLE `intro_intro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lectures_category`
--

DROP TABLE IF EXISTS `lectures_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lectures_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lectures_category`
--

LOCK TABLES `lectures_category` WRITE;
/*!40000 ALTER TABLE `lectures_category` DISABLE KEYS */;
INSERT INTO `lectures_category` VALUES (1,'엔트리'),(2,'스크래치'),(3,'메이커');
/*!40000 ALTER TABLE `lectures_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lectures_lecture`
--

DROP TABLE IF EXISTS `lectures_lecture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lectures_lecture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `lecture_image` varchar(100) NOT NULL,
  `register_from` date DEFAULT NULL,
  `register_to` date DEFAULT NULL,
  `period_from` date DEFAULT NULL,
  `period_to` date DEFAULT NULL,
  `fee` int(11) NOT NULL,
  `discount` int(11) NOT NULL,
  `isDiscount` tinyint(1) NOT NULL,
  `sample` varchar(200) NOT NULL,
  `book` varchar(200) NOT NULL,
  `teacher` varchar(200) NOT NULL,
  `location` varchar(300) NOT NULL,
  `isSale` tinyint(1) NOT NULL,
  `isShow` tinyint(1) NOT NULL,
  `category_id` int(11) NOT NULL,
  `section_id` int(11) NOT NULL,
  `description` varchar(500) NOT NULL,
  `added` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lectures_lecture_category_id_7322d0d4_fk_lectures_category_id` (`category_id`),
  KEY `lectures_lecture_section_id_5cc4fbfe_fk_lectures_section_id` (`section_id`),
  CONSTRAINT `lectures_lecture_category_id_7322d0d4_fk_lectures_category_id` FOREIGN KEY (`category_id`) REFERENCES `lectures_category` (`id`),
  CONSTRAINT `lectures_lecture_section_id_5cc4fbfe_fk_lectures_section_id` FOREIGN KEY (`section_id`) REFERENCES `lectures_section` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lectures_lecture`
--

LOCK TABLES `lectures_lecture` WRITE;
/*!40000 ALTER TABLE `lectures_lecture` DISABLE KEYS */;
INSERT INTO `lectures_lecture` VALUES (1,'[초등학교 완벽대비] 엔트리를 활용한 SW 코딩의 이해','lecture_image/2c99b9c71cc57318afc05eef1b8558d6.jpg','2018-11-12','2018-11-12','2018-11-12','2018-11-12',0,0,0,'','','','',1,1,1,1,'우리는 그 동안 국영수 위주의 재미없는 주입식 교육에 빠져살았습니다. 미메이커가 여러분에게 재미있고, 다양한 참여의 기회가 있는  코딩교육의 세계로 초대합니다.','2018-11-12 10:48:03.719595','2018-11-17 10:41:44.688184','4차 산업혁명시대로 빠르게 변하면서, 이제 초등학생도 코딩을 배우지 못하면 생존할 수 없는 시대가 되고 있습니다.\r\n \r\n\r\n우리는 그동안 국영수 위주의 재미없는 주입식 교육에 빠져살았습니다. 미메이커가 여러분에게 재미있고, 다양한 참여의 기회가 있는\r\n\r\n코딩교육의 세계로 초대합니다.\r\n\r\n초등학교 완벽대비 코딩교육을 통해 학생과 선생님 모두 코딩 소양을 갖추실 수 있습니다.\r\n\r\n코딩의 이해시간에 여러분이 배우게 될 내용은 다음과 같습니다.\r\n\r\n \r\n\r\n \r\n\r\n1, 정보화 시대에 필요한 기본적인 지식을 배우실 수 있습니다.\r\n\r\n2. 코딩을 배우기위해 필요한 사전지식을 충분히 익히실 수 있습니다.\r\n\r\n3. 엔트리 블록코딩에 기본적인 지식을 배울 수 있습니다.\r\n\r\n4. 엔트리를 이용하여 순차, 반복, 선택 논리를 배우고 다양한 알고리즘을 구성할 수 있습니다.\r\n\r\n5. 엔트리를 이용하여 게임과 애니메이션을 만들 수 있습니다.\r\n\r\n\r\n\r\n초등학교 학생에게는 과목을 대비할수 있는 좋은 교육의 기회이며, 선생님에게는 새로운 교육을 준비할 수 있는\r\n\r\n시간이 될 것이라고 확신합니다.\r\n\r\n \r\n\r\n코딩의 이해 두 번째 시간에는 미메이커 코딩 보드와 블록코딩 엔트리를 활용한 다양한 프로젝트 및 알고리즘 교육을 \r\n\r\n받으실 수 있습니다.\r\n\r\n \r\n\r\n자 그럼 코딩의 세계로 출발~!\r\n\r\n학습목표\r\n1. 정보화 시대에 필요한 기본적인 소양을 익힐 수 있다.\r\n2. 코딩의 의미와 알고리즘의 의미를 익힐 수 있다.\r\n3. 코딩과 연관된 다양한 배경지식을 익힐 수 있다.\r\n4. 블록코딩 프로그램 엔트리를 익힐 수 있다.\r\n5. 블록코딩 프로그램 엔트리로 게임과 애니메이션을 만들 수 있다.'),(2,'Tinkeracd로 배우는 3D 프린터 기초와 모델링','lecture_image/Cap_2018-09-09_16-26-06-693.jpg','2018-11-12','2018-11-12','2018-11-12','2018-11-12',0,0,0,'','','','',1,1,3,1,'3D 프린터 활용과 Tinkercad를 활용한 기초 모델링으로 3D 프린팅의 세계로 초대합니다. 학생, 선생님, 일반인 등 최근 3D 모델링에 관심이 많아지면서 모델링을 배우고자 하는 분들에게 적절한 강의가 됩니다.','2018-11-12 11:03:57.182234','2018-11-12 12:10:52.284643','만들면서 배우는 코딩교육 서비스 미메이커의 서비스 채널입니다.\r\n\r\n틴커캐드를 활용하여 3D 모델링을 배우 기초 콘텐츠 입니다.\r\n\r\n본 내용은 tinkercad로 배우는 3d 모델링 기초와 3D 프린팅 활용 교재에 수록된 내용을 포함 합니다.'),(3,'[무료][5분 영상] 엔트리(이론)','lecture_image/f4ad437b60e267a7a0a0df23469c6864.jpg','2018-11-12','2018-11-12','2018-11-12','2018-11-12',0,0,0,'','','','',1,1,1,1,'선생님, 학생, 학부모 모두 코딩을 배워야 한다고 생각을 하지만, 어디서부터 어떻게 배워야 할지 모르는 경우가 많습니다.      그래도 이곳에 찾아와 강의를 찾아보는 여러분은 블록코딩 엔트리에 대해서 들어보셨을 겁니다.','2018-11-12 11:06:15.183556','2018-11-12 11:06:15.183588','선생님, 학생, 학부모 모두 코딩을 배워야 한다고 생각을 하지만, 어디서부터 어떻게 배워야 할지 모르는 경우가 많습니다. \r\n\r\n \r\n\r\n그래도 이곳에 찾아와 강의를 찾아보는 여러분은 블록코딩 엔트리에 대해서 들어보셨을 겁니다. \r\n\r\n \r\n\r\n엔트리는 국내에서 교육용 소프트웨어 언어(EPL : Education Programing Language)로 가장 많이 활용되는 블록코딩 프로그램입니다.\r\n\r\n \r\n\r\n‘다른 강사들과 똑같은 강의를 하려는 구나’ 하는 생각은 잠시 넣어두시기 바랍니다.\r\n\r\n \r\n\r\n시중에 수많은 엔트리 코딩 관련 교재와 영상이 나와 있습니다. \r\n\r\n \r\n\r\n하지만, 그 어디에서도 엔트리에 대해 자세히 다루지 않더군요.\r\n\r\n \r\n\r\n다음은 김경훈 선생님의 한마디입니다.\r\n\r\n“엔트리도 잘 모르면서 엔트리로 코딩을 배우고 프로그램을 만들겠다? 알파벳을 배우지 않고 영어 공부를 시작하는 것과 같습니다.”\r\n\r\n \r\n\r\n어느 공부를 하더라도 기본이 가장 중요합니다. 기본기가 강해야 꾸준히 발전할 수 있습니다.\r\n\r\n \r\n\r\n코딩을 잘하고 싶은 여러분은 김경훈 선생님의 엔트리 가입부터 작품공유까지의 ‘5분강좌 이론편’을 듣는 것을 강력 추천합니다. \r\n\r\n\r\n\r\n\r\n\r\n강의목적 : 엔트리 회원 가입하기부터 작품공유하기까지 엔트리를 파헤쳐보고 엔트리와 친해진다.		\r\n\r\n강의구성 : 총 9강								\r\n\r\n대상학년 : 초등 4,5,6 학년 / 엔트리 입문자								\r\n\r\n강의범위 : 엔트리 입문이론 /기초 	\r\n\r\n \r\n\r\n※ 수강신청 대상\r\n\r\n1. 코딩을 처음 배우는 학생\r\n\r\n2. 코딩을 교육해야하는데 어떻게 해야할지 막막한 선생님\r\n\r\n3. 우리아이에게 코딩을 지도하고 싶은 학부모님\r\n\r\n4. 코딩교육 분야로 진출하고 싶으신 코딩 강사님\r\n\r\n\r\n\r\n---------------------------------------학습내용---------------------------------------\r\n\r\n\r\n\r\n엔트리 이론	\r\n\r\n                1	코딩이란?\r\n\r\n                2	블록코딩과 엔트리\r\n\r\n                3	엔트리 회원가입\r\n\r\n                4	엔트리로 할 수 있는 것들\r\n\r\n                5	작품만들기 화면\r\n\r\n                6	오브젝트 의미와 요소\r\n\r\n                7	오브젝트창 살펴보기\r\n\r\n                8	블록꾸러미 살펴보기\r\n\r\n                9	오브젝트 추가 및 삭제\r\n\r\n                10	실행화면 세부기능\r\n\r\n                11	실행화면의 좌표\r\n\r\n                12	블록 조립소\r\n\r\n                13	엔트리 상단메뉴\r\n\r\n                14	간단한코드로 통해 오브젝트 제어하기\r\n\r\n                15	코드 분리하기, 삭제하기\r\n\r\n                16	오브젝트 움직이기 예제\r\n\r\n                17	작품저장\r\n\r\n                18	작품공유\r\n\r\n \r\n\r\n----------------------------------------------------------------------------------------\r\n\r\n\r\n\r\n \r\n\r\n학습목표\r\n1. 엔트리를 사용하는 이유를 배운다. \r\n2. 엔트리의 메뉴와 기능을 하나하나 살펴본다.\r\n3. 간단한 코드로 작품을 만들어 본다.\r\n4. 작품을 저장하고 공유할 수 있다.'),(4,'[무료][5분 영상] 엔트리(기초, 예제)','lecture_image/8e7c14d4301f5d197bfa30f444a4de07.jpg','2018-11-12','2018-11-12','2018-11-12','2018-11-12',0,0,0,'','','','',1,1,1,1,'다른 컴퓨터 프로그래밍 언어와 마찬가지로 엔트리(블록코딩) 역시 다양한 예제를 연습해야 알고리즘을 만들어내는 능력과 코딩 실력을 향상 시킬 수 있습니다.','2018-11-12 11:07:21.089567','2018-11-12 11:07:21.089598','다른 컴퓨터 프로그래밍 언어와 마찬가지로 엔트리(블록코딩) 역시 다양한 예제를 연습해야 알고리즘을 만들어내는 능력과 코딩 실력을 향상 시킬 수 있습니다. \r\n\r\n엔티리 학습하기에 수록된 엔트리 예제는 순차, 반복문, 선택문, 함수, 비교연산 문 등을 익힐 수 있는 예제들로 구성이 되어있습니다.\r\n\r\n처음부터 코딩을 잘 할 수는 없습니다. 코딩을 잘하기 위해선 수 많은 예제를 경험하고 완성된 코딩을 수정 해보며 조금씩 더 나은 방법을 찾아야 합니다. \r\n\r\n이 강의는 여러분이 앞으로 코딩을 하며 가장 많이 사용하게될 순차, 반복선택, 비교연산, 함수에 대해 다룰 것입니다. 이 강의를 통해 코딩에 기본이 되는 문법을 익히시길 바랍니다.\r\n\r\n \r\n\r\n \r\n\r\n강의목적 : 엔트리 블록코딩의 기초부터 고급피지컬 컴퓨팅까지 쉽고 명쾌한 진행을 통해 배워 나가고, 코딩실력을 키우며 컴퓨팅 사고력을 키울 수 있다.	\r\n\r\n강의구성 : 총 8강 								\r\n\r\n대상학년 : 초등 4,5,6 학년 / 엔트리 이론, 기초를 학습한 입문자								\r\n\r\n강의범위 : 엔트리 입문 /기초  예제 를 통한 초등 컴퓨팅 사고력 완벽 대비								\r\n\r\n수강대상: \r\n\r\n★기본기를 닦은 후 다양한 예제풀이로 실전코딩 능력을 키우고 싶은 친구들\r\n\r\n★코딩공부를 따로 해왔지만 실력의 향상이 없고 어렵게만 느껴지는 친구들\r\n\r\n★지루한 수업은 못견디는 친구들\r\n\r\n★중급 수준의 엔트리 실력을 쌓고 싶은 분들\r\n\r\n \r\n\r\n \r\n\r\n---------------------------------------학습내용---------------------------------------\r\n\r\n		\r\n\r\n1	엔트리 첫 걸음 스텝 1\r\n\r\n2	엔트리 첫 걸음 스텝 2\r\n\r\n3	마을탐험  	예제를 통해 순차, 함수를 익힌다.\r\n\r\n4	우주여행  	예제를 통해 순차, 반복, 선택, 비교연산문을 익힌다.\r\n\r\n----------------------------------------------------------------------------------------\r\n\r\n학습목표\r\n1. 엔트리에서 제공하는 예제 미션을 완료할 수 있다.\r\n2. 예제 미션을 통해 순차, 반복, 선택 논리를 학습 할 수 있다.\r\n3. 코딩 논리를 이용하여 알고리즘을 만들 수 있다.');
/*!40000 ALTER TABLE `lectures_lecture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lectures_lecture_material`
--

DROP TABLE IF EXISTS `lectures_lecture_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lectures_lecture_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lecture_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lectures_lecture_material_lecture_id_product_id_0119586b_uniq` (`lecture_id`,`product_id`),
  KEY `lectures_lecture_mat_product_id_5b787604_fk_products_` (`product_id`),
  CONSTRAINT `lectures_lecture_mat_lecture_id_07386efa_fk_lectures_` FOREIGN KEY (`lecture_id`) REFERENCES `lectures_lecture` (`id`),
  CONSTRAINT `lectures_lecture_mat_product_id_5b787604_fk_products_` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lectures_lecture_material`
--

LOCK TABLES `lectures_lecture_material` WRITE;
/*!40000 ALTER TABLE `lectures_lecture_material` DISABLE KEYS */;
INSERT INTO `lectures_lecture_material` VALUES (1,1,3),(2,1,4),(3,1,5),(4,1,6);
/*!40000 ALTER TABLE `lectures_lecture_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lectures_section`
--

DROP TABLE IF EXISTS `lectures_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lectures_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lectures_section`
--

LOCK TABLES `lectures_section` WRITE;
/*!40000 ALTER TABLE `lectures_section` DISABLE KEYS */;
INSERT INTO `lectures_section` VALUES (1,'온라인'),(2,'오프라인'),(3,'온/오프라인 혼합');
/*!40000 ALTER TABLE `lectures_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lectures_video`
--

DROP TABLE IF EXISTS `lectures_video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lectures_video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `movie` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `file` varchar(100) NOT NULL,
  `lecture_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lectures_video_lecture_id_37e3be95_fk_lectures_lecture_id` (`lecture_id`),
  CONSTRAINT `lectures_video_lecture_id_37e3be95_fk_lectures_lecture_id` FOREIGN KEY (`lecture_id`) REFERENCES `lectures_lecture` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lectures_video`
--

LOCK TABLES `lectures_video` WRITE;
/*!40000 ALTER TABLE `lectures_video` DISABLE KEYS */;
INSERT INTO `lectures_video` VALUES (1,'[3D 프린팅 기초] 01.CURA 다운로드 및 기본세팅 M508 3D 프린터용','https://www.youtube.com/embed/bNJy4afpkUw?list=PLjOE0xVFFMJymHm9qfkXCX04_Ys7rf9wv','만들면서 배우는 코딩교육 서비스 미메이커의 서비스 채널입니다.\r\n\r\nM508 3D 프린터 및 유사한 종류의 3D 프린터로 활용이 가능한 Cura를 다운로드부터 설치 세팅까지 배우는 영상입니다.\r\n\r\n본 내용은 tinkercad로 배우는 3d 모델링 기초와 3D 프린팅 활용 교재에 수록된 내용을 포함 합니다.','',2),(2,'[3D 프린팅 기초] 02. Tinkcad 기초 배우기','https://www.youtube.com/embed/LW3thIvpZEM?list=PLjOE0xVFFMJymHm9qfkXCX04_Ys7rf9wv','만들면서 배우는 코딩교육 서비스 미메이커의 서비스 채널입니다.\r\n\r\n틴커캐드를 활용하여 3D 모델링을 배우는 기초적인 내용의 콘텐츠입니다.\r\n\r\n본 내용은 tinkercad로 배우는 3d 모델링 기초와 3D 프린팅 활용 교재에 수록된 내용을 포함 합니다.','',2),(3,'[3D 프린팅 기초] 03. Tinkcad 기초 배우기 조립구조물 만들기','https://www.youtube.com/embed/VmXu_BQGdF0?list=PLjOE0xVFFMJymHm9qfkXCX04_Ys7rf9wv','만들면서 배우는 코딩교육 서비스 미메이커의 서비스 채널입니다.\r\n\r\n틴커캐드를 활용하여 3D 모델링을 배우는조립 구조만들기 기초 콘텐츠 입니다.\r\n\r\n본 내용은 tinkercad로 배우는 3d 모델링 기초와 3D 프린팅 활용 교재에 수록된 내용을 포함 합니다.','',2),(4,'[3D 프린팅 기초] 04. Tinkcad 기초 배우기 의자 만들기','https://www.youtube.com/embed/dORS9xevhYI?list=PLjOE0xVFFMJymHm9qfkXCX04_Ys7rf9wv','만들면서 배우는 코딩교육 서비스 미메이커의 서비스 채널입니다.\r\n\r\n틴커캐드를 활용하여 3D 모델링을 배우는 의자 만들기 기초 콘텐츠 입니다.\r\n\r\n본 내용은 tinkercad로 배우는 3d 모델링 기초와 3D 프린팅 활용 교재에 수록된 내용을 포함 합니다.','',2),(5,'[3D 프린팅 기초] 05. Tinkcad 기초 배우기 의자 만들기 후반부 정렬활용(수정)','https://www.youtube.com/embed/rzntfzuiYY8?list=PLjOE0xVFFMJymHm9qfkXCX04_Ys7rf9wv','만들면서 배우는 코딩교육 서비스 미메이커의 서비스 채널입니다.\r\n\r\n틴커캐드를 활용하여 3D 모델링을 배우는 의자만들기 기초 콘텐츠 입니다.\r\n\r\n본 내용은 tinkercad로 배우는 3d 모델링 기초와 3D 프린팅 활용 교재에 수록된 내용을 포함 합니다.','',2),(6,'[3D 프린팅 기초] 06. Tinkcad 기초 배우기 집만들기 기초','https://www.youtube.com/embed/R1vaEhE3diw?list=PLjOE0xVFFMJymHm9qfkXCX04_Ys7rf9wv','만들면서 배우는 코딩교육 서비스 미메이커의 서비스 채널입니다.\r\n\r\n틴커캐드를 활용하여 3D 모델링을 배우는 3D 모델링 집 만들기 콘텐츠 입니다.\r\n\r\n본 내용은 tinkercad로 배우는 3d 모델링 기초와 3D 프린팅 활용 교재에 수록된 내용을 포함 합니다.','',2),(7,'[3D 프린팅 기초] 07. Tinkcad 기초 배우기 집만들기 심화','https://www.youtube.com/embed/OncyefEvvGU?list=PLjOE0xVFFMJymHm9qfkXCX04_Ys7rf9wv','만들면서 배우는 코딩교육 서비스 미메이커의 서비스 채널입니다.\r\n\r\n틴커캐드를 활용하여 3D 모델링을 배우는 3D 모델링 집 만들기 심화 콘텐츠 입니다.\r\n\r\n본 내용은 tinkercad로 배우는 3d 모델링 기초와 3D 프린팅 활용 교재에 수록된 내용을 포함 합니다.','',2),(8,'[3D 프린팅 기초] 08. Tinkcad 기초 배우기 나로호 로켓 모델링 배우기','https://www.youtube.com/embed/HS1UWUpLslc?list=PLjOE0xVFFMJymHm9qfkXCX04_Ys7rf9wv','만들면서 배우는 코딩교육 서비스 미메이커의 서비스 채널입니다.\r\n\r\n틴커캐드를 활용하여 3D 모델링을 배우는 로켓 모델링 기초 콘텐츠 입니다.\r\n\r\n본 내용은 tinkercad로 배우는 3d 모델링 기초와 3D 프린팅 활용 교재에 수록된 내용을 포함 합니다.','',2);
/*!40000 ALTER TABLE `lectures_video` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_choice`
--

DROP TABLE IF EXISTS `polls_choice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `choice_text` varchar(200) NOT NULL,
  `votes` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_choice_question_id_c5b4b260_fk_polls_question_id` (`question_id`),
  CONSTRAINT `polls_choice_question_id_c5b4b260_fk_polls_question_id` FOREIGN KEY (`question_id`) REFERENCES `polls_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_choice`
--

LOCK TABLES `polls_choice` WRITE;
/*!40000 ALTER TABLE `polls_choice` DISABLE KEYS */;
INSERT INTO `polls_choice` VALUES (1,'이기호',0,1),(2,'저기호',0,1),(3,'박기호',0,1);
/*!40000 ALTER TABLE `polls_choice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_question`
--

DROP TABLE IF EXISTS `polls_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_text` varchar(200) NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_question`
--

LOCK TABLES `polls_question` WRITE;
/*!40000 ALTER TABLE `polls_question` DISABLE KEYS */;
INSERT INTO `polls_question` VALUES (1,'이름은?','2018-11-18 03:55:27.000000');
/*!40000 ALTER TABLE `polls_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_category`
--

DROP TABLE IF EXISTS `products_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_category`
--

LOCK TABLES `products_category` WRITE;
/*!40000 ALTER TABLE `products_category` DISABLE KEYS */;
INSERT INTO `products_category` VALUES (1,'교재'),(2,'언플러그드'),(3,'조립키트'),(4,'코딩보드');
/*!40000 ALTER TABLE `products_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_detail`
--

DROP TABLE IF EXISTS `products_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `product_id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `lower_line` tinyint(1) NOT NULL,
  `upper_line` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_detail_product_id_e9775435_fk_products_product_id` (`product_id`),
  CONSTRAINT `products_detail_product_id_e9775435_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_detail`
--

LOCK TABLES `products_detail` WRITE;
/*!40000 ALTER TABLE `products_detail` DISABLE KEYS */;
INSERT INTO `products_detail` VALUES (1,'본 도서는 초등학교 실과시간에 도입되는 코딩교육에 완벽한 대비를 할 수 있도록 다양한 전문가와 교사의 검토를 마친 \r\n\r\n교육 도서로서 학생들에게 코딩에 대한 배경지식과 기초적인 코딩에 이해를 도울 수 있는 다양한 내용을 수록하고 있습니다.\r\n\r\n또한, 국내에서 가장 활성화되어 있는 블록코딩 엔트리를 활용한 알고리즘 교육과 애니메이션, 게임 등을 제작하며 코딩에 세계를 완벽하게 체험할 수 있습니다.\r\n\r\n본 도서는 \'미메이커 코딩보드\'를 이용한 피지컬 컴퓨팅 교육과정을 체계적으로 다루고 있기 때문에 학생들의 알고리즘 능력 배양 뿐만 아니라\r\n\r\n창의 제작 체험을 통해 다양한 역량을 배양하여 4차 산업시대에 꼭 필요한 인재를 양성하는 데 필수적인 지식과 활동을 정리하였습니다.\r\n\r\n본 도서를 통해 학생들은 창의력과 컴퓨팅적 사고력을 키우고, 선생님은 전문성을 향상 시킬 수 있도록 안내하고 있습니다.','',1,'',0,1),(2,'','product_image/3e2b1f4b5f2ab8baa5d409478b104768.png',1,'교재 미리보기',0,0),(3,'본 교재가 제공하는 다양한 특징들을 통해서 학습자분들의 코딩 학습 뿐만 아니라, 교육자분들도 쉽고 재미있는 수업이 될 수 있습니다.','',1,'',0,0),(4,'','product_image/e33367c2a3625f8f6e4f5e08e63e0b60.png',1,'',0,0),(5,'','product_image/be22a989114ce78ec1186737bf7731bc.png',1,'',0,0),(6,'','product_image/56637a2bd91e7d34c0b0dd48e75b70ec.png',1,'목차 구성',0,0),(7,'','product_image/2ba841049f096e263cccf6f81ff960bb.png',1,'',0,0),(8,'※교재 내용의 다양한 특징과 내용 살펴보기\r\n\r\n>6컷 애니메이션의 재미있는 이야기를 통해 앞으로 배우게 될 내용을 알 수 있습니다.\r\n>학습목표에 따라 학생들은 무엇을 배울지, 선생님을 무엇을 지도해야 할 것인지 서로 알기 쉽습니다.\r\n>체계적인 구성을 통해 코딩을 정복할 수 있습니다.\r\n>좀 더 알아보기를 통해 깊이있는 학습이 가능합니다.','',1,'교재 내용 살펴보기',0,0),(9,'','product_image/882d082ce140d6ab6bd67d6db4e07667.png',1,'',0,0),(10,'','product_image/73d4d4a9c79ba85453235cd8094e04b5.png',1,'',0,0),(11,'','product_image/33f7fa0ed0ad69a9ce8aa12e540cf603.png',1,'',0,0),(12,'','product_image/5c33a53fa7fc0d392e8db7c0a55aaff5.png',1,'',1,0),(13,'복잡하고 어려운 \"로봇 코딩\" 이제는 엔트리와 미메이커보드를 활용한 로봇 코딩의 이해로 쉽고 재미있게 배울 수 있습니다. \r\n\r\n시중에 나와있는 복잡하고 어려운 로봇 코딩 책들 로봇 코딩은 수단일 뿐, 정말 중요한 코딩의 논리와 체계를 배우는 것에\r\n\r\n너무 대수롭게 생각하지 않는 경우가 많습니다.\r\n\r\n이제 아이들이 생각하고 학습할 수 있는 로봇 코딩 교재가 필요합니다.\r\n\r\n무료 강의로 함께 배울 수 있는 쉬운 로봇 코딩 교재 바로  엔트리와 미메이커보드를 활용한 로봇 코딩의 이해로 지금 당장\r\n\r\n코딩을 시작하세요!','',2,'',0,1),(14,'','product_image/Cap_2018-08-01_14-34-31-378.png',2,'교재 미리보기',0,0),(15,'본 교재가 제공하는 다양한 특징들을 통해서 학습자분들의 코딩 학습 뿐만 아니라, 교육자분들도 쉽고 재미있는 수업이 될 수 있습니다.','',2,'이 책의 특징',0,0),(16,'','product_image/Cap_2018-08-01_14-31-35-345.png',2,'',0,0),(17,'','product_image/Cap_2018-08-01_14-31-51-411.png',2,'',0,0),(18,'','product_image/Cap_2018-08-01_14-32-16-515.png',2,'목차 구성',0,0),(19,'','product_image/Cap_2018-08-01_14-32-32-815.png',2,'',0,0),(20,'','product_image/Cap_2018-08-01_14-33-11-521.png',2,'교재 내용 살펴보기',0,0),(21,'','product_image/Cap_2018-08-01_14-33-29-655.jpg',2,'',0,0),(22,'','product_image/Cap_2018-08-01_14-33-35-072.png',2,'',1,0),(23,'코딩을 쉽게 배울 수 있는 코딩 보드 \"미메이커 코딩보드\"\r\n\r\n피지컬 컴퓨팅, 로봇 코딩 등 다양한 만들기 기반의 코딩 교육용 보드로 \r\n\r\n코딩 교육과 창의력 두 마리의 토끼를 모두 잡으세요!\r\n\r\n미메이커에서 체계적인 온라인 강의와 함께 활용할 수 있는 코딩 교육용 보드를 출시 했습니다.\r\n\r\n초기 프리미엄 형태로 깔끔한 외형을 구현하고자 하였으나, \r\n\r\n가격이 높아져 보편적인 교육을 할 수 없는 단점을 보완하고자\r\n\r\n단순하고 경제적인 형태의 외형으로 고객에게 좀 더 낮은 가격으로 제공하였습니다.','',3,'',0,1),(24,'','product_image/f7145fde23fd12a4f0c927d4bdc6616e.png',3,'수상 내역',0,0),(25,'','product_image/Cap_2018-11-10_15-35-45-495.jpg',3,'',0,0),(26,'','product_image/Cap_2018-11-10_15-35-59-358.jpg',3,'',0,0),(27,'','product_image/Cap_2018-11-10_15-36-08-891.jpg',3,'',0,0),(28,'','product_image/Cap_2018-11-10_15-36-16-108.jpg',3,'',0,0),(29,'','product_image/Cap_2018-11-10_15-36-22-038.jpg',3,'',0,0),(30,'','product_image/Cap_2018-11-10_15-36-28-342.jpg',3,'',0,0),(31,'','product_image/Cap_2018-11-10_15-36-45-337.jpg',3,'',0,0),(32,'','product_image/Cap_2018-11-10_15-36-57-520.jpg',3,'미메이커 코딩보드 장점',0,0),(33,'','product_image/Cap_2018-11-10_15-37-08-142.jpg',3,'',0,0),(34,'','product_image/Cap_2018-11-10_15-37-23-979.jpg',3,'',0,0),(35,'','product_image/Cap_2018-11-10_15-37-35-712.jpg',3,'',0,0),(36,'','product_image/Cap_2018-11-10_15-37-46-413.jpg',3,'',0,0),(37,'','product_image/Cap_2018-11-10_15-37-58-329.jpg',3,'',0,0),(38,'','product_image/Cap_2018-11-10_15-38-15-146.jpg',3,'',0,0),(39,'','product_image/Cap_2018-11-10_15-38-20-492.jpg',3,'',0,0),(40,'','product_image/Cap_2018-11-10_15-38-33-424.jpg',3,'',0,0),(41,'','product_image/Cap_2018-11-10_15-39-13-356.jpg',3,'제품 구성',0,0),(42,'','product_image/Cap_2018-11-10_15-39-19-989.jpg',3,'',0,0),(43,'','product_image/Cap_2018-11-10_15-39-33-072.jpg',3,'',0,0),(44,'','product_image/Cap_2018-11-10_15-39-41-855.jpg',3,'',0,0),(45,'','product_image/Cap_2018-11-10_15-39-51-690.jpg',3,'',0,0),(46,'','product_image/Cap_2018-11-10_15-39-57-872.jpg',3,'',0,0),(47,'','product_image/Cap_2018-11-10_15-40-05-672.jpg',3,'',0,0),(48,'','product_image/Cap_2018-11-10_15-40-14-173.jpg',3,'',0,0),(49,'','product_image/Cap_2018-11-10_15-40-21-990.jpg',3,'',0,0),(50,'','product_image/Cap_2018-11-10_15-40-29-674.jpg',3,'',0,0),(51,'','product_image/Cap_2018-11-10_15-40-36-357.jpg',3,'',0,0),(52,'','product_image/Cap_2018-11-10_15-40-42-807.jpg',3,'',0,0),(53,'','product_image/Cap_2018-11-10_15-40-53-173.jpg',3,'',0,0),(54,'미메이커 코딩 보드와 연결하여 조립하고 코딩 할 수 있는 악어 복불복 게임 만들기 키트 입니다.\r\n\r\n미메이커 보드를 활용하여, 만들면서 배우는 코딩을 학습해보시기 바랍니다!!\r\n\r\nLED 만 켜보는 단순한 로봇 코딩에 대한 생각은 이제 그만!\r\n\r\n미메이커 보드를 이용하여 다양한 로봇코딩 키트가 지금도 계속 업데이트 되고 있습니다.\r\n\r\n우리가 만들게 될 악어 복불복 게임은 어떻게 만들까요?','',4,'',0,1),(55,'','product_image/823a7974dbbbdef15ebc9b8ccf3695a5.png',4,'키트 이미지',0,0),(56,'','product_image/f230b0c1532678c2f032404bfc6fe16d.png',4,'',0,0),(57,'','product_image/ac9cc05bd8a4c135fedb16efc7fa92c2.png',4,'',0,0),(58,'완성하게 되면 다음과 같은 형태의 악어가 만들어집니다!!(현재 플라스틱 조립체를 활용하여 더 쉽게 더 재미있게 조립할 수 있습니다.)','',4,'',0,0),(59,'','product_image/6d72e6e0895ec8b7d84f51e02aac5643.jpg',4,'조립 메뉴얼',0,0),(60,'','product_image/07b70c5d4debc2fc265b888b2ad97c6b.jpg',4,'',0,0),(61,'','product_image/ef119124f1427f676f567faa30cd4a2c.gif',4,'조립 과정',0,0),(62,'','product_image/90c632d964aeb8bcaf9ebd8676ed95b3.gif',4,'',0,0),(63,'','product_image/d6c17ed7ba46dc8127d9d9a8790fa417.gif',4,'',0,0),(64,'1. 악어복불복 구조체 (MDF)\r\n\r\n2. 연결 결합체 구조물 (플라스틱 ABS)\r\n\r\n3. 조립 설명서','',4,'제품 구성',0,0),(65,'너무 강한 힘으로 조립하면 조립키트가 부러질 수 있습니다.','',4,'주의 사항',0,0),(66,'','product_image/10274170f51fb63c0326a635dcff7cee.png',4,'엔트리 프로그램 활용',0,0),(67,'','product_image/fd90a139883dad28869629202a9a6963.png',4,'',0,0),(68,'악어를 만들고 재미있는 게임도 즐기는 행복한 코딩의 세계로 여러분을 초대합니다!','',4,'',1,0),(69,'미메이커 코딩보드로 제작할 수 있는 프로젝트 키트 입니다.\r\n\r\n스마트 스탠드는 조도센서와 LED모듈을 활용하여 조도센서 값에 따라 LED 빛이 켜지고 꺼지는 기능을 코딩을 통해\r\n\r\n작동시키는 프로젝트 키트입니다. \r\n\r\n코딩으로 만든 제품을 실생활에 활용할 수 있습니다. \r\n\r\n미메이커는 지속적으로 다양한 프로젝트가 추가될 예정입니다.','',5,'',0,1),(70,'','product_image/930a6464f49dea7cbea4a85bcc48ec63.png',5,'키트 이미지',0,0),(71,'','product_image/64db327cca63fa412ad916e85f616eb7.png',5,'',0,0),(72,'','product_image/7db9166f0fe5f57e47394da27d69b5d6.png',5,'',0,0),(73,'','product_image/a166e22464825a2d93b5c5909b859e23.png',5,'',0,0),(74,'','product_image/5486d578d16ab9e233caff8305d4cd7a.png',5,'조립 메뉴얼',0,0),(75,'','product_image/9d268babaaf14956c1a6078c0868347e.gif',5,'조립 과정',0,0),(76,'※ 엔트리, 스크래치 코드가 올라올 예정입니다.','',5,'',1,0),(77,'미메이커 코딩보드를 활용하여 꽃 무드등을 만들 수 있는 키트입니다.\r\n\r\n조립법에 대한 설명서는 함께 동봉 되어있습니다.\r\n\r\n엔트리, 스크래치를 활용하여 무드등 프로젝트를 완성해 봅시다!!','',6,'',0,1),(78,'','product_image/8a1869e2edc3bd1eb9bdb90c95494237.png',6,'키트 이미지',0,0),(79,'','product_image/20cb392505f80b2876bfa0cb6a3dd488.png',6,'',0,0),(80,'','product_image/d493edd5310220076a6458983a798e85.png',6,'',0,0),(81,'','product_image/f8be98cf4205d9df7d107352540ca7d1.png',6,'',0,0),(82,'','product_image/a46450162ac8a7d4d4fec8c46514afc8.png',6,'조립 메뉴얼',0,0),(83,'','product_image/2f6e234da424fd097e933ddc24f0ab0c.gif',6,'조립 과정',0,0),(84,'※엔트리, 스크래치 프로젝트 추가예정','',6,'',1,0),(85,'미메이커 코딩보드로 제작 가능한 프로젝트 키트 시리즈 입니다.\r\n\r\n프로젝트 키트를 이용하여 주차장 차단기를 만들고 그 원리를 코딩으로 이해해 봅시다.\r\n\r\n만드는 재미와 주차장 차단기의 원리를 함께 배우고 자동차를 갖고 놀면서 활용해봅시다~!','',7,'',0,1),(86,'','product_image/87fd559e8488c065726f15d47f71d7d6.png',7,'키트 이미지',0,0),(87,'','product_image/232ff5515129079df049da47b45f46f3.png',7,'',0,0),(88,'','product_image/572f8527ece3fd2db04f1cebf8d68534.png',7,'',0,0),(89,'','product_image/d667022b56cfb8d8e0e22f7be2c5f998.png',7,'',0,0),(90,'','product_image/55c42513214212e5df538d8833a31ab9.png',7,'조립 메뉴얼',0,0),(91,'','product_image/b94144d4a70153aedcaee66cffa60f37.gif',7,'조립 과정',0,0),(92,'※ 엔트리, 스크래치 코딩이 업로드 될 예정입니다.','',7,'',1,0),(93,'​미메이커 코딩보드를 활용한 스탑워치(초시계) 만들기 프로젝트 키트입니다.\r\n\r\n엔트리 및 스크래치 등을 활용하여 경주 게임에 Lap 타임을 측정하는 알고리즘을 만들 수 있습니다.\r\n\r\n직접 만든 스탑워치를 이용하여 친구, 가족들과 운동회에서 활용해보는 건 어떨까요??\r\n\r\n본 키트에 활용되는 LCD와 택트스위치(버튼) 모듈은 미메이커 DIY 보드에 포함된 모듈입니다.(키트에 포함 x)','',8,'',0,1),(94,'','product_image/9379b61e3f217b1bbef213701c7d2c59.png',8,'키트 이미지',0,0),(95,'','product_image/c061713616a0778621e5257f91ba1858.png',8,'',0,0),(96,'','product_image/e0f9538d9519f4522fb2ab34b534adb1.png',8,'',0,0),(97,'','product_image/ea8b1872b9d0d18cb637d59a3c5a9072.png',8,'',0,0),(98,'','product_image/aa0921c2b043b87832a65cff0782f908.png',8,'조립 메뉴얼',0,0),(99,'','product_image/37e5440bfb823b517ddcc163b298c673.gif',8,'조립 과정',0,0),(100,'미메이커 코딩보드를 활용한 로봇코딩의 이해 참고\r\n\r\n지속적으로 추가 업데이트 중입니다.','',8,'엔트리 프로그램',1,0),(101,'미메이커 코딩보드를 활용한 조이스틱 만들기 프로젝트 키트입니다.\r\n\r\n엔트리 및 스크래치 등을 활용하여 미로탈출 및 비행기 게임을 조종하는 조이스틱 게임을 만들 수 있습니다.\r\n\r\n직접 만든 조이스틱을 이용하여 친구, 가족들과 게임을 하고 점수를 비교해보는 건 어떨까요??\r\n\r\n본 키트에 활용되는 조이스틱와 택트스위치(버튼) 모듈은 미메이커 DIY 보드에 포함된 모듈입니다.(키트에 포함 x)','',9,'',0,1),(102,'','product_image/7cdfb89003bcfc85f5c8b52a329bb852.png',9,'키트 이미지',0,0),(103,'','product_image/05772adbc9b2796bf5e958184af276cb.png',9,'',0,0),(104,'','product_image/5284865bf6a8a8ab1b8e97195dbaa23c.png',9,'',0,0),(105,'조이스틱을 만들고 엔트리/스크래치를 활용하여 다양한 게임과 콘텐츠를 만들고 즐겨보세요!','',9,'',0,0),(106,'','product_image/09ddb447ca6ad6edc2edd2fc422d72ed.png',9,'조립 메뉴얼',0,0),(107,'','product_image/fadca726181d8958503ab3bb5b14e59c.gif',9,'조립 과정',0,0),(108,'','product_image/f1d4242ad4a9d55a8af77f37b8aecc60.png',9,'엔트리 프로그램',0,0),(109,'','product_image/cedff12d44f0f76b4802c8f2e8bd7c07.png',9,'',0,0),(110,'미메이커 코딩보드를 활용한 로봇코딩의 이해 참고\r\n\r\n지속적으로 추가 업데이트 중입니다.','',9,'',1,0),(111,'미메이커 코딩보드를 활용한 스마트 주차장 만들기 프로젝트 키트입니다.\r\n\r\n엔트리 및 스크래치 등을 활용하여 스마트 주차장 만들기 게임과 함께 활용하는 스마트 주차장을 만들 수 있습니다.\r\n\r\n직접 만든 스마트 주차장을 이용하여 친구, 가족들과 즐겨보는 건 어떨까요??\r\n\r\n본 키트에 활용되는 RGB(3색) LED, 장애물 회피센서 모듈은 미메이커 DIY 보드에 포함된 모듈입니다.\r\n\r\n(키트에 포함 x)','',10,'',0,1),(112,'','product_image/0fb44f90ceaac77a95108002f9203be0.png',10,'키트 이미지',0,0),(113,'','product_image/8fdca034ff57c0306c86017668c129a9.png',10,'',0,0),(114,'','product_image/39f3c2948dca9543116f7a02922c483f.png',10,'',0,0),(115,'','product_image/506f9ed5fb8557514bae90f61ad19e0a.jpg',10,'',0,0),(116,'','product_image/2490b815985be3f6826e0c7042bbe188.jpg',10,'',0,0),(117,'','product_image/ff49a18eef25281ec4ac4363eb3c3c7e.jpg',10,'',0,0),(118,'','product_image/b27cce0504a6541e3579c7a98891836f.jpg',10,'조립 메뉴얼',0,0),(119,'','product_image/0e1557876c3ba16ff23fe94195396f31.gif',10,'조립 과정',0,0),(120,'미메이커 코딩보드를 활용한 로봇코딩의 이해 참고\r\n\r\n지속적으로 추가 업데이트 중입니다.','',10,'엔트리 프로그램',1,0),(121,'미메이커 코딩보드를 활용한 거리 측정기 만들기 프로젝트 키트입니다.\r\n\r\n엔트리 및 스크래치 등을 활용하여 스마트 거리측정기 게임과 함께 활용하는 거리 측정기 실물을 만들 수 있습니다.\r\n\r\n직접 만든 스마트 주차장을 이용하여 치수를 재는 데 직접 활용해보는 건 어떨까요? 줄자나 자로 재던 것과는 색다른 재미가 있을 겁니다!^^\r\n\r\n본 키트에 활용되는 초음파센서, LCD 모듈은 미메이커 DIY 보드에 포함된 모듈입니다.\r\n\r\n(키트에 포함 x)','',11,'',0,1),(122,'','product_image/09b24c14885fc57cae98c52b55aeb3d3.png',11,'키트 이미지',0,0),(123,'','product_image/270faa01444ade658d458a7c7f06f5a2.png',11,'',0,0),(124,'','product_image/2575dba11175b4fdc5eb552e21ad5cbe.png',11,'',0,0),(125,'','product_image/d8a3270471618368ab44095b92282c47.png',11,'',0,0),(126,'','product_image/38a59cff09310cdea980e32ebfd54d71.png',11,'조립 메뉴얼',0,0),(127,'','product_image/aedb91c715da2b33bd0d4da9c4257313.gif',11,'조립 과정',0,0),(128,'미메이커 코딩보드를 활용한 로봇코딩의 이해 참고\r\n\r\n지속적으로 추가 업데이트 중입니다.','',11,'엔트리 프로그램',1,0);
/*!40000 ALTER TABLE `products_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product`
--

DROP TABLE IF EXISTS `products_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cost` int(11) NOT NULL,
  `discount` int(11) NOT NULL,
  `isSale` tinyint(1) NOT NULL,
  `description` varchar(300) NOT NULL,
  `file` varchar(100) NOT NULL,
  `product_image` varchar(100) NOT NULL,
  `movie` varchar(200) NOT NULL,
  `category_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `added` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `link` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_product_category_id_9b594869_fk_products_category_id` (`category_id`),
  CONSTRAINT `products_product_category_id_9b594869_fk_products_category_id` FOREIGN KEY (`category_id`) REFERENCES `products_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product`
--

LOCK TABLES `products_product` WRITE;
/*!40000 ALTER TABLE `products_product` DISABLE KEYS */;
INSERT INTO `products_product` VALUES (1,11000,0,1,'본 도서는 초등학교 실과시간에 도입되는 코딩교육에 완벽한 대비를 할 수 있도록 다양한 전문가와 교사의 검토를 마친 교육 도서로서 학생들에게 코딩에 대한 배경지식과 기초적인 코딩에 이해를 도울 수 있는 다양한 내용을 수록하고 있습니다.','','product_image/01249f71da2bf8e3d800a751124ab702.png','',1,'[교재] 엔트리로 S/W 코딩의 이해(강의 영상 제공)','2018-11-12 09:02:32.941044','2018-11-12 09:05:25.062208',''),(2,11000,0,1,'​복잡하고 어려운 \"로봇 코딩\" 이제는 엔트리와 미메이커보드를 활용한 로봇 코딩의 이해로 쉽고 재미있게 배울 수 있습니다.','','product_image/로봇코딩의_의해_대문.png','',1,'[교재] 로봇 코딩의 이해(무료 영상 준비중)','2018-11-12 09:11:49.053439','2018-11-17 13:48:43.872467',''),(3,110000,0,1,'코딩을 쉽게 배울 수 있는 코딩 보드 \"미메이커 코딩보드\"  피지컬 컴퓨팅, 로봇 코딩 등 다양한 만들기 기반의 코딩 교육용 보드로   코딩 교육과 창의력 두 마리의 토끼를 모두 잡으세요!','','product_image/미메이커코딩보드_하늘_diy버전_제품대문이미지_.png','',4,'[보드]미메이커 코딩보드 DIY','2018-11-12 09:26:55.359882','2018-12-30 08:48:26.899679','https://smartstore.naver.com/memaker_shop/products/3901746800#dts'),(4,9000,0,1,'미메이커 코딩 보드와 연결하여 조립하고 코딩 할 수 있는 악어 복불복 게임 만들기 키트 입니다.     미메이커 보드를 활용하여, 만들면서 배우는 코딩을 학습해보시기 바랍니다!!','','product_image/da43d8262dc2c2f349994afa3bc7a3d3.png','',3,'[키트] 악어복불복 게임 만들기 키트(미메이커보드)','2018-11-12 09:35:12.179441','2018-11-12 09:45:28.992557',''),(5,8000,0,1,'미메이커 코딩보드로 제작할 수 있는 프로젝트 키트 입니다.     스마트 스탠드는 조도센서와 LED모듈을 활용하여 조도센서 값에 따라 LED 빛이 켜지고 꺼지는 기능을 코딩을 통해     작동시키는 프로젝트 키트입니다.','','product_image/c92e5b679754fdba6597b01d606a151a.png','',3,'[키트] 스마트스탠드 만들기 키트(미메이커보드)','2018-11-12 09:40:19.458783','2018-11-12 09:45:22.908040',''),(6,6000,0,1,'미메이커 코딩보드를 활용하여 꽃 무드등을 만들 수 있는 키트입니다.     조립법에 대한 설명서는 함께 동봉 되어있습니다.','','product_image/7d37ea58df532b78a005cce4926ef1f6.png','',3,'[키트] 꽃 무드등 만들기 키트(미메이커보드)','2018-11-12 09:44:54.459162','2018-11-12 09:45:13.213276',''),(7,8000,0,1,'미메이커 코딩보드로 제작 가능한 프로젝트 키트 시리즈 입니다.    프로젝트 키트를 이용하여 주차장 차단기를 만들고 그 원리를 코딩으로 이해해 봅시다.','','product_image/038be483c6de196fbffa5313d6a035b5.png','',3,'[키트] 주차장 차단기 만들기 키트(미메이커보드)','2018-11-12 09:50:14.581574','2018-11-12 09:51:23.623982',''),(8,8000,0,1,'미메이커 코딩보드를 활용한 스탑워치(초시계) 만들기 프로젝트 키트입니다.     엔트리 및 스크래치 등을 활용하여 경주 게임에 Lap 타임을 측정하는 알고리즘을 만들 수 있습니다.','','product_image/af92d49721da7670d9c2acc4adae88e1.png','',3,'[키트] 스탑워치 만들기 키트(미메이커보드)','2018-11-12 09:55:41.265384','2018-11-12 09:55:41.265416',''),(9,8000,0,1,'​미메이커 코딩보드를 활용한 조이스틱 만들기 프로젝트 키트입니다.     엔트리 및 스크래치 등을 활용하여 미로탈출 및 비행기 게임을 조종하는 조이스틱 게임을 만들 수 있습니다.','','product_image/a6f9874a8976bd8ba26ed2ac0e5d45a5.png','',3,'[키트] 조이스틱 만들기 키트(미메이커보드)','2018-11-12 10:31:27.844409','2018-11-12 10:31:36.914807',''),(10,8000,0,1,'미메이커 코딩보드를 활용한 스마트 주차장 만들기 프로젝트 키트입니다.     엔트리 및 스크래치 등을 활용하여 스마트 주차장 만들기 게임과 함께 활용하는 스마트 주차장을 만들 수 있습니다.','','product_image/d12d77a488459d7ad567cd35d6ae69f9.png','',3,'[키트] 스마트 주차장 만들기 키트(미메이커보드)','2018-11-12 10:35:50.788782','2018-11-12 10:35:50.788818',''),(11,8000,0,1,'미메이커 코딩보드를 활용한 거리 측정기 만들기 프로젝트 키트입니다.     엔트리 및 스크래치 등을 활용하여 스마트 거리측정기 게임과 함께 활용하는 거리 측정기 실물을 만들 수 있습니다.','','product_image/30a2c29253ec8429a4efe412838df3b3.png','',3,'[키트] 거리측정기 만들기 키트(미메이커보드)','2018-11-12 10:40:43.799408','2018-11-12 11:09:36.395997','');
/*!40000 ALTER TABLE `products_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product_related_lec`
--

DROP TABLE IF EXISTS `products_product_related_lec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_product_related_lec` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `lecture_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `products_product_related_lec_product_id_lecture_id_73488562_uniq` (`product_id`,`lecture_id`),
  KEY `products_product_rel_lecture_id_1c1d025f_fk_lectures_` (`lecture_id`),
  CONSTRAINT `products_product_rel_lecture_id_1c1d025f_fk_lectures_` FOREIGN KEY (`lecture_id`) REFERENCES `lectures_lecture` (`id`),
  CONSTRAINT `products_product_rel_product_id_f5d3f139_fk_products_` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product_related_lec`
--

LOCK TABLES `products_product_related_lec` WRITE;
/*!40000 ALTER TABLE `products_product_related_lec` DISABLE KEYS */;
INSERT INTO `products_product_related_lec` VALUES (2,2,4),(1,3,4);
/*!40000 ALTER TABLE `products_product_related_lec` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-31 17:53:08
