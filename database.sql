-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: curiosityskills
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

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
-- Table structure for table `age_range_list`
--

DROP TABLE IF EXISTS `age_range_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `age_range_list` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `age_range_listings` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `age_range_list`
--

LOCK TABLES `age_range_list` WRITE;
/*!40000 ALTER TABLE `age_range_list` DISABLE KEYS */;
INSERT INTO `age_range_list` VALUES (1,'0-4'),(2,'5-9'),(3,'10-14'),(4,'15-19'),(5,'20-24'),(6,'25-29'),(7,'30-34'),(8,'35-39'),(9,'40-44'),(10,'45-49'),(11,'50-54'),(12,'55-59'),(13,'60-64'),(14,'65-69'),(15,'70-74'),(16,'75-79'),(17,'80-84'),(18,'85-89'),(19,'90 and over');
/*!40000 ALTER TABLE `age_range_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_age`
--

DROP TABLE IF EXISTS `client_age`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_age` (
  `client_age` int(10) unsigned NOT NULL,
  `age_age` int(10) unsigned NOT NULL,
  KEY `client_age` (`client_age`),
  KEY `client_age_ibfk_2` (`age_age`),
  CONSTRAINT `client_age_ibfk_1` FOREIGN KEY (`client_age`) REFERENCES `client_exp` (`id`),
  CONSTRAINT `client_age_ibfk_2` FOREIGN KEY (`age_age`) REFERENCES `age_range_list` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_age`
--

LOCK TABLES `client_age` WRITE;
/*!40000 ALTER TABLE `client_age` DISABLE KEYS */;
INSERT INTO `client_age` VALUES (23,8),(24,12),(25,11),(26,9);
/*!40000 ALTER TABLE `client_age` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_exp`
--

DROP TABLE IF EXISTS `client_exp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_exp` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(64) NOT NULL,
  `details` text NOT NULL,
  `date` date NOT NULL,
  `work_fk` int(11) unsigned NOT NULL,
  `gender_fk` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `work_fk` (`work_fk`),
  KEY `client_exp_ibfk_2` (`gender_fk`),
  CONSTRAINT `client_exp_ibfk_1` FOREIGN KEY (`work_fk`) REFERENCES `work_exp` (`id`),
  CONSTRAINT `client_exp_ibfk_2` FOREIGN KEY (`gender_fk`) REFERENCES `gender_list` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_exp`
--

LOCK TABLES `client_exp` WRITE;
/*!40000 ALTER TABLE `client_exp` DISABLE KEYS */;
INSERT INTO `client_exp` VALUES (23,'Converting a bank client to sign up for credit card','Had a walk in client who wanted to open up an account. She is a single mum who was worried about committing to a credit card. I informed her that there was a low risk plan available for people in her situation. Had a chat with my manager and he offered to give her an attractive interest rate for a credit card sign up for an additional 3months. ','2019-10-02',42,3),(24,'Shipment discussions for all branches','We discussed shipment packages for our buses, lorry and train parts.','2019-10-21',44,2),(25,'Had important things to discuss but sidetracking kept happening','Couldn\'t get a word in with my client who kept going off about his company. It was extremely unprofessional considering the urgency of the matter at hand. Eventually, I pretended to say that my granny was sick and that I had to go and was willing to cut a \'good\' deal with him. He agreed and days later, the contract was signed. ','2019-10-07',50,2),(26,'General Health Lecture','An obese lady came into my clinic for prescription due to her intense pain on her back. I suggested exercise and healthier food for her, but she ended lecturing me on what was healthy. Its a tough situation... ','2019-10-28',51,3);
/*!40000 ALTER TABLE `client_exp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_exp_comment`
--

DROP TABLE IF EXISTS `client_exp_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_exp_comment` (
  `comments_fk` int(10) unsigned NOT NULL,
  `client_exp_fk` int(10) unsigned NOT NULL,
  KEY `comments_fk` (`comments_fk`),
  KEY `client_exp_fk` (`client_exp_fk`),
  CONSTRAINT `client_exp_comment_ibfk_1` FOREIGN KEY (`comments_fk`) REFERENCES `comments` (`id`),
  CONSTRAINT `client_exp_comment_ibfk_2` FOREIGN KEY (`client_exp_fk`) REFERENCES `client_exp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_exp_comment`
--

LOCK TABLES `client_exp_comment` WRITE;
/*!40000 ALTER TABLE `client_exp_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `client_exp_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type_exp` varchar(64) NOT NULL,
  `comment` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,'Client','She\'s seems like a very nice person.');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edu_age`
--

DROP TABLE IF EXISTS `edu_age`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `edu_age` (
  `edu_age` int(10) unsigned NOT NULL,
  `age_age` int(10) unsigned NOT NULL,
  KEY `edu_age` (`edu_age`),
  KEY `edu_age_ibfk_2` (`age_age`),
  CONSTRAINT `edu_age_ibfk_1` FOREIGN KEY (`edu_age`) REFERENCES `edu_exp` (`id`),
  CONSTRAINT `edu_age_ibfk_2` FOREIGN KEY (`age_age`) REFERENCES `age_range_list` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_age`
--

LOCK TABLES `edu_age` WRITE;
/*!40000 ALTER TABLE `edu_age` DISABLE KEYS */;
INSERT INTO `edu_age` VALUES (4,15),(5,11);
/*!40000 ALTER TABLE `edu_age` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edu_exp`
--

DROP TABLE IF EXISTS `edu_exp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `edu_exp` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `details` text NOT NULL,
  `date` date NOT NULL,
  `work_fk` int(10) unsigned NOT NULL,
  `role_fk` int(10) unsigned NOT NULL,
  `level_fk` int(10) unsigned NOT NULL,
  `topic_fk` int(10) unsigned NOT NULL,
  `institute_fk` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `edu_exp_ibfk_1` (`work_fk`),
  KEY `role_fk` (`role_fk`),
  KEY `level_fk` (`level_fk`),
  KEY `topic_fk` (`topic_fk`),
  KEY `institute_fk` (`institute_fk`),
  CONSTRAINT `edu_exp_ibfk_1` FOREIGN KEY (`work_fk`) REFERENCES `work_exp` (`id`),
  CONSTRAINT `edu_exp_ibfk_2` FOREIGN KEY (`role_fk`) REFERENCES `edu_role_list` (`id`),
  CONSTRAINT `edu_exp_ibfk_3` FOREIGN KEY (`level_fk`) REFERENCES `edu_level_list` (`id`),
  CONSTRAINT `edu_exp_ibfk_4` FOREIGN KEY (`topic_fk`) REFERENCES `topic_list` (`id`),
  CONSTRAINT `edu_exp_ibfk_5` FOREIGN KEY (`institute_fk`) REFERENCES `edu_institute_list` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_exp`
--

LOCK TABLES `edu_exp` WRITE;
/*!40000 ALTER TABLE `edu_exp` DISABLE KEYS */;
INSERT INTO `edu_exp` VALUES (4,'Teaching international students singapore security measures','Educating overseas students on the importance of security in singapore and to make sure to report anything suspicious they might notice around them in school or in public settings.','2019-10-29',43,1,4,30,3),(5,'Presentation for other subsidiaries on the new tax laws','New tax laws were implemented last month and our company organised a presentation to discuss the new business strategies and financial reportings. There were freebies given out throughout the session. ','2019-10-22',45,2,7,25,4);
/*!40000 ALTER TABLE `edu_exp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edu_exp_comment`
--

DROP TABLE IF EXISTS `edu_exp_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `edu_exp_comment` (
  `edu_exp_fk` int(10) unsigned NOT NULL,
  `comment_fk` int(10) unsigned NOT NULL,
  KEY `edu_exp_fk` (`edu_exp_fk`),
  KEY `comment_fk` (`comment_fk`),
  CONSTRAINT `edu_exp_comment_ibfk_1` FOREIGN KEY (`edu_exp_fk`) REFERENCES `edu_exp` (`id`),
  CONSTRAINT `edu_exp_comment_ibfk_2` FOREIGN KEY (`comment_fk`) REFERENCES `comments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_exp_comment`
--

LOCK TABLES `edu_exp_comment` WRITE;
/*!40000 ALTER TABLE `edu_exp_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `edu_exp_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edu_institute_list`
--

DROP TABLE IF EXISTS `edu_institute_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `edu_institute_list` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `institute` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_institute_list`
--

LOCK TABLES `edu_institute_list` WRITE;
/*!40000 ALTER TABLE `edu_institute_list` DISABLE KEYS */;
INSERT INTO `edu_institute_list` VALUES (1,'Public'),(2,'Private'),(3,'Personal Tutor'),(4,'Others');
/*!40000 ALTER TABLE `edu_institute_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edu_level_list`
--

DROP TABLE IF EXISTS `edu_level_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `edu_level_list` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `edu_level` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_level_list`
--

LOCK TABLES `edu_level_list` WRITE;
/*!40000 ALTER TABLE `edu_level_list` DISABLE KEYS */;
INSERT INTO `edu_level_list` VALUES (1,'Pre-School'),(2,'Primary School'),(3,'High School'),(4,'Tertiary'),(5,'Postgraduate'),(6,'Work Environment'),(7,'Others');
/*!40000 ALTER TABLE `edu_level_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edu_role_list`
--

DROP TABLE IF EXISTS `edu_role_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `edu_role_list` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `role` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edu_role_list`
--

LOCK TABLES `edu_role_list` WRITE;
/*!40000 ALTER TABLE `edu_role_list` DISABLE KEYS */;
INSERT INTO `edu_role_list` VALUES (1,'Student'),(2,'Teacher'),(3,'Private Tutor');
/*!40000 ALTER TABLE `edu_role_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gender_list`
--

DROP TABLE IF EXISTS `gender_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gender_list` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `gender` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gender_list`
--

LOCK TABLES `gender_list` WRITE;
/*!40000 ALTER TABLE `gender_list` DISABLE KEYS */;
INSERT INTO `gender_list` VALUES (1,'N/A'),(2,'Male'),(3,'Female');
/*!40000 ALTER TABLE `gender_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_category_list`
--

DROP TABLE IF EXISTS `job_category_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_category_list` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `category` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_category_list`
--

LOCK TABLES `job_category_list` WRITE;
/*!40000 ALTER TABLE `job_category_list` DISABLE KEYS */;
INSERT INTO `job_category_list` VALUES (1,'Agriculture, Food and Natural Resources'),(2,'Architecture and Construction'),(3,'Arts, Audio/Video Technology and Communications'),(4,'Business Management and Administration'),(5,'Education and Training'),(6,'Finance'),(7,'Government and Public Administration'),(8,'Health Science'),(9,'Hospitality and Tourism'),(10,'Human Services'),(11,'Information Technology'),(12,'Law, Public Safety, Corrections and Security'),(13,'Manufacturing'),(14,'Marketing, Sales and Service'),(15,'Science, Technology, Engineering and Mathematics'),(16,'Transportation, Distribution and Logistics');
/*!40000 ALTER TABLE `job_category_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_level_list`
--

DROP TABLE IF EXISTS `job_level_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_level_list` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `level` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_level_list`
--

LOCK TABLES `job_level_list` WRITE;
/*!40000 ALTER TABLE `job_level_list` DISABLE KEYS */;
INSERT INTO `job_level_list` VALUES (1,'Intern'),(2,'Junior-Level'),(3,'Entry-Level'),(4,'Intermediate'),(5,'First-level Management'),(6,'Upper-Management'),(7,'Top-Level Management');
/*!40000 ALTER TABLE `job_level_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topic_list`
--

DROP TABLE IF EXISTS `topic_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_list` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `topic` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_list`
--

LOCK TABLES `topic_list` WRITE;
/*!40000 ALTER TABLE `topic_list` DISABLE KEYS */;
INSERT INTO `topic_list` VALUES (1,'N/A'),(2,'English Language'),(3,'Mother Tongue Languages'),(4,'Mathematics'),(5,'Science (General)'),(6,'Character and Citizenship Education'),(7,'Geography'),(8,'English Literature'),(9,'History'),(10,'Design and Technology'),(11,'Food and Consumer Education'),(12,'Physical Education'),(13,'Art'),(14,'Music'),(15,'Co-curriculum Activities'),(16,'General Paper'),(17,'Project Work'),(18,'Economics'),(19,'Biology'),(20,'Physics'),(21,'Engineering '),(22,'Life Sciences'),(23,'Psychology'),(24,'Law'),(25,'Business'),(26,'Finance'),(27,'Computer Science'),(28,'Health Sciences'),(29,'Clinical Health'),(30,'Physical Sciences'),(31,'Education'),(32,'Social Sciences'),(33,'Others');
/*!40000 ALTER TABLE `topic_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_exp`
--

DROP TABLE IF EXISTS `work_exp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `work_exp` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `job_category` int(10) unsigned NOT NULL,
  `job_level` int(10) unsigned NOT NULL,
  `salary` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `job category` (`job_category`),
  KEY `job_level` (`job_level`),
  CONSTRAINT `work_exp_ibfk_1` FOREIGN KEY (`job_category`) REFERENCES `job_category_list` (`id`),
  CONSTRAINT `work_exp_ibfk_2` FOREIGN KEY (`job_level`) REFERENCES `job_level_list` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_exp`
--

LOCK TABLES `work_exp` WRITE;
/*!40000 ALTER TABLE `work_exp` DISABLE KEYS */;
INSERT INTO `work_exp` VALUES (42,4,3,2800),(43,15,4,3700),(44,15,5,7600),(45,14,6,12500),(50,12,7,30000),(51,8,3,3000);
/*!40000 ALTER TABLE `work_exp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_exp_comment`
--

DROP TABLE IF EXISTS `work_exp_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `work_exp_comment` (
  `work_exp_fk` int(10) unsigned NOT NULL,
  `comments_fk` int(10) unsigned NOT NULL,
  KEY `work_exp_fk` (`work_exp_fk`),
  KEY `comments_fk` (`comments_fk`),
  CONSTRAINT `work_exp_comment_ibfk_1` FOREIGN KEY (`work_exp_fk`) REFERENCES `work_exp` (`id`),
  CONSTRAINT `work_exp_comment_ibfk_2` FOREIGN KEY (`comments_fk`) REFERENCES `comments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_exp_comment`
--

LOCK TABLES `work_exp_comment` WRITE;
/*!40000 ALTER TABLE `work_exp_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `work_exp_comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-29  7:17:41
