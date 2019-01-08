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
-- Table structure for table `products_lecture`
--

DROP TABLE IF EXISTS `products_lecture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_lecture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `introduce` longtext NOT NULL,
  `register_from` date DEFAULT NULL,
  `period_from` date DEFAULT NULL,
  `period_to` date DEFAULT NULL,
  `duration` bigint(20) DEFAULT NULL,
  `location` varchar(300) NOT NULL,
  `content_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_lecture_content_id_1d8fc010_fk_products_content_id` (`content_id`),
  CONSTRAINT `products_lecture_content_id_1d8fc010_fk_products_content_id` FOREIGN KEY (`content_id`) REFERENCES `products_content` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_lecture`
--

LOCK TABLES `products_lecture` WRITE;
/*!40000 ALTER TABLE `products_lecture` DISABLE KEYS */;
INSERT INTO `products_lecture` VALUES (1,'<p>미메이커 코딩 교육(www.memaker.co.kr)</p>\r\n\r\n<p>선생님, 학생, 학부모 모두 코딩을 배워야 한다고 생각을 하지만, 어디서부터 어떻게 배워야 할지 모르는 경우가 많습니다.&nbsp;</p>\r\n\r\n<p>그래도 이곳에 찾아와 강의를 찾아보는 여러분은 블록코딩 엔트리에 대해서 들어보셨을 겁니다.&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>엔트리는 국내에서 교육용 소프트웨어 언어(EPL : Education Programing Language)로 가장 많이 활용되는 블록코딩 프로그램입니다.</p>\r\n\r\n<p>&lsquo;다른 강사들과 똑같은 강의를 하려는 구나&rsquo; 하는 생각은 잠시 넣어두시기 바랍니다.</p>\r\n\r\n<p>시중에 수많은 엔트리 코딩 관련 교재와 영상이 나와 있습니다.&nbsp;</p>\r\n\r\n<p>하지만, 그 어디에서도 엔트리에 대해 자세히 다루지 않더군요.</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>다음은 김경훈 선생님의 한마디입니다.</p>\r\n\r\n<p><span style=\"color:#c0392b\"><strong><q>엔트리도 잘 모르면서 엔트리로 코딩을 배우고 프로그램을 만들겠다? 알파벳을 배우지 않고 영어 공부를 시작하는 것과 같습니다.</q></strong></span></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>어느 공부를 하더라도 기본이 가장 중요합니다. 기본기가 강해야 꾸준히 발전할 수 있습니다.</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>코딩을 잘하고 싶은 여러분은 김경훈 선생님의 엔트리 가입부터 작품공유까지의 &lsquo;5분강좌 이론편&rsquo;을 듣는 것을 강력 추천합니다.&nbsp;</p>\r\n\r\n<p>강의목적 : 엔트리 회원 가입하기부터 작품공유하기까지 엔트리를 파헤쳐보고 엔트리와 친해진다. &nbsp;</p>\r\n\r\n<p>강의구성 : 총 9강 &nbsp; &nbsp; &nbsp; &nbsp;</p>\r\n\r\n<p>대상학년 : 초등 4,5,6 학년 / 엔트리 입문자 &nbsp; &nbsp; &nbsp; &nbsp;</p>\r\n\r\n<p>강의범위 : 엔트리 입문이론 /기초 &nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>※ 수강신청 대상</p>\r\n\r\n<p>1. 코딩을 처음 배우는 학생</p>\r\n\r\n<p>2. 코딩을 교육해야하는데 어떻게 해야할지 막막한 선생님</p>\r\n\r\n<p>3. 우리아이에게 코딩을 지도하고 싶은 학부모님</p>\r\n\r\n<p>4. 코딩교육 분야로 진출하고 싶으신 코딩 강사님</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><span style=\"font-size:18px\"><strong><img alt=\"enlightened\" height=\"23\" src=\"http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/lightbulb.png\" title=\"enlightened\" width=\"23\" />학습 목차</strong></span></p>\r\n\r\n<hr />\r\n<p><span style=\"font-size:18px\"><strong>엔트리 이론&nbsp;</strong></span></p>\r\n\r\n<p><span style=\"font-size:18px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span style=\"font-size:16px\"> &nbsp; 1 코딩이란?</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2 블록코딩과 엔트리</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 3 엔트리 회원가입</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 4 엔트리로 할 수 있는 것들</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 5 작품만들기 화면</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 오브젝트 의미와 요소</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 7 오브젝트창 살펴보기</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 8 블록꾸러미 살펴보기</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 9 오브젝트 추가 및 삭제</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 10 실행화면 세부기능</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 11 실행화면의 좌표</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 12 블록 조립소</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 13 엔트리 상단메뉴</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 14 간단한코드로 통해 오브젝트 제어하기</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 15 코드 분리하기, 삭제하기</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 16 오브젝트 움직이기 예제</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 17 작품저장</span></p>\r\n\r\n<p><span style=\"font-size:16px\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 18 작품공유</span></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><span style=\"font-size:18px\"><img alt=\"enlightened\" height=\"23\" src=\"http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/lightbulb.png\" title=\"enlightened\" width=\"23\" />학습목표</span></p>\r\n\r\n<p><span style=\"font-size:16px\">1. 엔트리를 사용하는 이유를 배운다.&nbsp;</span></p>\r\n\r\n<p><span style=\"font-size:16px\">2. 엔트리의 메뉴와 기능을 하나하나 살펴본다.</span></p>\r\n\r\n<p><span style=\"font-size:16px\">3. 간단한 코드로 작품을 만들어 본다.</span></p>\r\n\r\n<p><span style=\"font-size:16px\">4. 작품을 저장하고 공유할 수 있다.</span></p>','2019-01-02','2019-01-02','2019-01-02',NULL,'',1);
/*!40000 ALTER TABLE `products_lecture` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-08 15:06:32
