-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: ems_db
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
-- Table structure for table `EMS_REST_API_attendancelog`
--

DROP TABLE IF EXISTS `EMS_REST_API_attendancelog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMS_REST_API_attendancelog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_in` datetime(6) DEFAULT NULL,
  `time_out` datetime(6) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `EMS_REST_API_attenda_user_id_9e6910f6_fk_EMS_REST_` (`user_id`),
  CONSTRAINT `EMS_REST_API_attenda_user_id_9e6910f6_fk_EMS_REST_` FOREIGN KEY (`user_id`) REFERENCES `EMS_REST_API_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMS_REST_API_attendancelog`
--

LOCK TABLES `EMS_REST_API_attendancelog` WRITE;
/*!40000 ALTER TABLE `EMS_REST_API_attendancelog` DISABLE KEYS */;
INSERT INTO `EMS_REST_API_attendancelog` VALUES (1,'2018-08-05 23:00:16.897330','2018-08-06 07:00:17.830004',1),(2,'2018-08-05 23:00:17.432250','2018-08-06 07:00:18.325637',2),(3,'2018-08-06 23:00:00.841323','2018-08-07 07:00:01.824860',1),(4,'2018-08-06 23:00:01.254817','2018-08-07 07:00:02.283042',2),(5,'2018-08-07 23:00:00.888043','2018-08-08 07:00:01.849324',1),(6,'2018-08-07 23:00:01.322909','2018-08-08 07:00:02.326546',2),(7,'2018-08-08 23:00:00.826197','2018-08-09 07:00:01.828479',1),(8,'2018-08-08 23:00:01.245732','2018-08-09 07:00:02.319667',2),(9,'2018-08-09 23:00:00.823203','2018-08-10 07:00:01.832055',1),(10,'2018-08-09 23:00:01.234294','2018-08-10 07:00:02.299715',2),(11,'2018-08-12 23:00:00.826973','2018-08-13 07:00:01.845809',1),(12,'2018-08-12 23:00:01.296571','2018-08-13 07:00:02.298303',2),(13,'2018-08-13 23:00:00.839029','2018-08-14 07:00:01.827596',1),(14,'2018-08-13 23:00:01.261676','2018-08-14 07:00:02.277732',2),(15,'2018-08-14 23:00:00.826800','2018-08-15 07:00:01.844119',1),(16,'2018-08-14 23:00:01.270885','2018-08-15 07:00:02.302313',2),(17,'2018-08-15 23:00:00.825315','2018-08-16 07:00:01.824358',1),(18,'2018-08-15 23:00:01.296567','2018-08-16 07:00:02.293272',2),(19,'2018-08-16 23:00:00.754910','2018-08-17 07:00:01.757404',1),(20,'2018-08-16 23:00:01.105660','2018-08-17 07:00:02.348451',2),(21,'2018-08-19 23:00:00.760967','2018-08-20 07:00:01.756990',1),(22,'2018-08-19 23:00:01.165617','2018-08-20 07:00:02.138424',2),(23,'2018-08-20 23:00:00.756767','2018-08-21 07:00:01.752488',1),(24,'2018-08-20 23:00:01.095794','2018-08-21 07:00:02.137415',2),(25,'2018-08-21 23:00:00.758777','2018-08-22 07:00:01.756655',1),(26,'2018-08-21 23:00:01.133761','2018-08-22 07:00:02.135224',2),(27,'2018-08-22 23:00:00.757846','2018-08-23 07:00:01.762572',1),(28,'2018-08-22 23:00:01.102921','2018-08-23 07:00:02.145289',2),(29,'2018-08-23 23:00:00.754762','2018-08-24 07:00:01.754574',1),(30,'2018-08-23 23:00:01.157270','2018-08-24 07:00:02.139691',2),(31,'2018-08-26 23:00:00.752736','2018-08-27 07:00:01.751764',1),(32,'2018-08-26 23:00:01.101183','2018-08-27 07:00:02.165113',2),(33,'2018-08-27 23:00:00.749680','2018-08-28 07:00:01.754905',1),(34,'2018-08-27 23:00:01.100532','2018-08-28 07:00:02.158014',2),(35,'2018-08-28 23:00:00.752219','2018-08-29 07:00:01.755830',1),(36,'2018-08-28 23:00:01.104916','2018-08-29 07:00:02.144791',2),(37,'2018-08-29 23:00:00.758317','2018-08-30 07:00:01.754629',1),(38,'2018-08-29 23:00:01.112000','2018-08-30 07:00:02.160424',2),(39,'2018-08-30 23:00:00.811132','2018-08-31 07:00:01.757324',1),(40,'2018-08-30 23:00:01.214134','2018-08-31 07:00:02.138600',2),(41,'2018-09-02 23:00:00.950284','2018-09-03 07:00:06.752823',1),(42,'2018-09-02 23:00:01.615074','2018-09-03 07:00:07.533660',2),(43,'2018-09-03 23:00:00.767599','2018-09-04 07:00:01.750873',1),(44,'2018-09-03 23:00:01.109445','2018-09-04 07:00:02.163053',2),(45,'2018-09-04 23:00:00.817003','2018-09-05 07:00:05.822252',1),(46,'2018-09-04 23:00:05.273389','2018-09-05 07:00:06.310713',2),(47,'2018-09-05 23:00:00.759488','2018-09-06 07:00:01.752536',1),(48,'2018-09-05 23:00:01.125247','2018-09-06 07:00:02.148464',2),(49,'2018-09-06 23:00:02.009320','2018-09-07 07:00:09.823783',1),(50,'2018-09-06 23:00:02.743732','2018-09-07 07:00:10.295580',2),(51,'2018-09-09 23:00:00.828705','2018-09-10 07:00:01.807265',1),(52,'2018-09-09 23:00:01.246973','2018-09-10 07:00:03.838650',2),(53,'2018-09-10 23:00:02.136200','2018-09-11 07:00:04.917712',1),(54,'2018-09-10 23:00:04.135230','2018-09-11 07:00:06.806302',2),(55,'2018-09-11 23:00:00.952692','2018-09-12 07:00:01.823547',1),(56,'2018-09-11 23:00:01.375996','2018-09-12 07:00:02.295522',2),(57,'2018-09-12 23:00:02.161070','2018-09-13 07:00:04.863548',1),(58,'2018-09-12 23:00:03.183511','2018-09-13 07:00:05.938375',2),(59,'2018-09-13 23:00:01.102830','2018-09-14 07:00:02.833820',1),(60,'2018-09-13 23:00:02.886596','2018-09-14 07:00:03.295814',2),(61,'2018-09-16 23:00:01.171694','2018-09-17 07:00:03.147265',1),(62,'2018-09-16 23:00:01.985906','2018-09-17 07:00:06.917730',2),(63,'2018-09-17 23:00:00.983855','2018-09-18 07:00:03.823755',1),(64,'2018-09-17 23:00:01.672637','2018-09-18 07:00:04.286402',2),(65,'2018-09-18 23:00:03.000569','2018-09-19 07:00:05.967585',1),(66,'2018-09-18 23:00:03.894686','2018-09-19 07:00:06.532279',2),(67,'2018-09-19 23:00:01.217329','2018-09-20 07:00:01.834247',1),(68,'2018-09-19 23:00:01.690170','2018-09-20 07:00:02.299831',2),(69,'2018-09-20 23:00:01.145342','2018-09-21 07:00:05.103707',1),(70,'2018-09-20 23:00:03.428487','2018-09-21 07:00:06.995715',2),(71,'2018-09-23 23:00:00.917462','2018-09-24 07:00:03.829059',1),(72,'2018-09-23 23:00:01.613488','2018-09-24 07:00:04.309926',2),(73,'2018-09-24 23:00:01.031437','2018-09-25 07:00:05.103616',1),(74,'2018-09-24 23:00:03.057510','2018-09-25 07:00:07.740205',2),(75,'2018-09-25 23:00:01.830519','2018-09-26 07:00:02.825444',1),(76,'2018-09-25 23:00:02.247650','2018-09-26 07:00:03.302858',2),(77,'2018-09-26 23:00:00.828706','2018-09-27 07:00:01.830463',1),(78,'2018-09-26 23:00:01.240436','2018-09-27 07:00:02.316193',2),(79,'2018-09-27 23:00:00.830445','2018-09-28 07:00:01.830776',1),(80,'2018-09-27 23:00:01.302631','2018-09-28 07:00:02.311949',2),(81,'2018-09-30 23:00:01.159724','2018-10-01 07:00:08.072463',1),(82,'2018-09-30 23:00:05.556006','2018-10-01 07:00:08.727716',2),(83,'2018-10-01 23:00:00.824527','2018-10-02 07:00:01.830755',1),(84,'2018-10-01 23:00:01.238646','2018-10-02 07:00:02.323703',2),(85,'2018-10-02 23:00:00.846412','2018-10-03 07:00:01.823919',1),(86,'2018-10-02 23:00:01.323011','2018-10-03 07:00:02.296420',2),(87,'2018-10-03 23:00:00.830326','2018-10-04 07:00:01.877360',1),(88,'2018-10-03 23:00:01.248617','2018-10-04 07:00:02.551330',2),(89,'2018-10-04 23:00:00.994660','2018-10-05 07:00:03.135385',1),(90,'2018-10-04 23:00:01.679075','2018-10-05 07:00:03.841510',2),(91,'2018-10-07 23:00:00.753050','2018-10-08 07:00:01.826674',1),(92,'2018-10-07 23:00:01.092284','2018-10-08 07:00:02.432339',2),(93,'2018-10-08 23:00:00.832914','2018-10-09 07:00:01.759341',1),(94,'2018-10-08 23:00:01.252091','2018-10-09 07:00:02.147766',2),(95,'2018-10-09 23:00:00.757255','2018-10-10 07:00:01.757958',1),(96,'2018-10-09 23:00:01.110722','2018-10-10 07:00:02.135522',2),(97,'2018-10-10 23:00:00.766339','2018-10-11 07:00:02.753615',1),(98,'2018-10-10 23:00:02.883808','2018-10-11 07:00:03.131419',2),(99,'2018-10-11 23:00:00.758292','2018-10-12 07:00:01.761174',1),(100,'2018-10-11 23:00:01.100174','2018-10-12 07:00:02.145320',2),(101,'2018-10-14 23:00:00.756740','2018-10-15 07:00:01.756313',1),(102,'2018-10-14 23:00:01.094674','2018-10-15 07:00:02.259774',2),(103,'2018-10-15 23:00:00.848800','2018-10-16 07:00:01.806228',1),(104,'2018-10-15 23:00:01.274356','2018-10-16 07:00:02.288746',2),(105,'2018-10-16 23:00:01.928926','2018-10-17 07:00:02.756603',1),(106,'2018-10-16 23:00:02.289312','2018-10-17 07:00:03.159726',2),(107,'2018-10-17 23:00:00.758985','2018-10-18 07:00:01.758900',1),(108,'2018-10-17 23:00:01.117897','2018-10-18 07:00:02.196521',2),(109,'2018-10-18 23:00:00.758533','2018-10-19 07:00:01.754165',1),(110,'2018-10-18 23:00:01.194677','2018-10-19 07:00:02.161456',2),(111,'2018-10-21 23:00:00.760569','2018-10-22 07:00:01.879692',1),(112,'2018-10-21 23:00:01.148763','2018-10-22 07:00:02.401247',2),(113,'2018-10-22 23:00:01.148527','2018-10-23 07:00:02.774896',1),(114,'2018-10-22 23:00:02.798260','2018-10-23 07:00:03.181100',2),(115,'2018-10-23 23:00:00.803102','2018-10-24 07:00:01.835709',1),(116,'2018-10-23 23:00:01.237784','2018-10-24 07:00:02.337310',2),(117,'2018-10-24 23:00:00.763261','2018-10-25 07:00:01.758197',1),(118,'2018-10-24 23:00:01.136358','2018-10-25 07:00:02.238006',2),(119,'2018-10-25 23:00:00.807742','2018-10-26 07:00:05.755445',1),(120,'2018-10-25 23:00:05.781651','2018-10-26 07:00:06.129071',2),(121,'2018-10-28 23:00:00.812693','2018-10-29 07:00:01.759442',1),(122,'2018-10-28 23:00:01.251825','2018-10-29 07:00:02.135704',2),(123,'2018-10-29 23:00:00.756995','2018-10-30 07:00:01.786201',1),(124,'2018-10-29 23:00:01.160260','2018-10-30 07:00:02.212581',2),(125,'2018-10-30 23:00:01.139268','2018-10-31 07:00:03.754510',1),(126,'2018-10-30 23:00:03.617866','2018-10-31 07:00:04.157726',2),(127,'2018-10-31 23:00:00.756288','2018-11-01 07:00:01.756788',1),(128,'2018-10-31 23:00:01.119194','2018-11-01 07:00:02.134596',2),(129,'2018-11-01 23:00:00.756615','2018-11-02 07:00:01.759992',1),(130,'2018-11-01 23:00:01.100596','2018-11-02 07:00:02.171279',2);
/*!40000 ALTER TABLE `EMS_REST_API_attendancelog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMS_REST_API_employee`
--

DROP TABLE IF EXISTS `EMS_REST_API_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMS_REST_API_employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `is_clocked_in` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `EMS_REST_API_employee_user_id_0a16aef7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMS_REST_API_employee`
--

LOCK TABLES `EMS_REST_API_employee` WRITE;
/*!40000 ALTER TABLE `EMS_REST_API_employee` DISABLE KEYS */;
INSERT INTO `EMS_REST_API_employee` VALUES (1,'cedrick','cuizon','Domingo','administrator',1,1,'2018-11-02',NULL,0,2),(2,'dudeson','versus','betsafe','instructor',0,1,'2018-11-02',NULL,0,3);
/*!40000 ALTER TABLE `EMS_REST_API_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMS_REST_API_employeeconfig`
--

DROP TABLE IF EXISTS `EMS_REST_API_employeeconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMS_REST_API_employeeconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sss_number` varchar(40) NOT NULL,
  `pagibig_number` varchar(40) NOT NULL,
  `philhealth_number` varchar(40) NOT NULL,
  `tin_number` varchar(40) NOT NULL,
  `rate_per_hour` double NOT NULL,
  `non_working_days` varchar(70) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `EMS_REST_API_employe_user_id_37d6024e_fk_EMS_REST_` (`user_id`),
  CONSTRAINT `EMS_REST_API_employe_user_id_37d6024e_fk_EMS_REST_` FOREIGN KEY (`user_id`) REFERENCES `EMS_REST_API_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMS_REST_API_employeeconfig`
--

LOCK TABLES `EMS_REST_API_employeeconfig` WRITE;
/*!40000 ALTER TABLE `EMS_REST_API_employeeconfig` DISABLE KEYS */;
INSERT INTO `EMS_REST_API_employeeconfig` VALUES (1,'3453-3453453-4353','3453-5345-4534','53-345345345-3','345-534-345-34543',200,'sunday, saturday',1),(2,'2342-2342342-3423','2342-3242-2342','23-234234234-2','234-234-234-23423',100,'sunday, saturday',2);
/*!40000 ALTER TABLE `EMS_REST_API_employeeconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMS_REST_API_employeeprofile`
--

DROP TABLE IF EXISTS `EMS_REST_API_employeeprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMS_REST_API_employeeprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(128) NOT NULL,
  `birthday` date NOT NULL,
  `gender` varchar(15) NOT NULL,
  `height` int(11) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `absences_count` int(11) NOT NULL,
  `presences_count` int(11) NOT NULL,
  `profile_photo` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `EMS_REST_API_employe_user_id_fdc397d5_fk_EMS_REST_` (`user_id`),
  CONSTRAINT `EMS_REST_API_employe_user_id_fdc397d5_fk_EMS_REST_` FOREIGN KEY (`user_id`) REFERENCES `EMS_REST_API_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMS_REST_API_employeeprofile`
--

LOCK TABLES `EMS_REST_API_employeeprofile` WRITE;
/*!40000 ALTER TABLE `EMS_REST_API_employeeprofile` DISABLE KEYS */;
INSERT INTO `EMS_REST_API_employeeprofile` VALUES (1,'gapan','2000-01-01','male',178,'9509340590',1,65,'',1),(2,'gapan','2000-01-01','male',178,'9402930492',1,65,'',2);
/*!40000 ALTER TABLE `EMS_REST_API_employeeprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMS_REST_API_globalconfig`
--

DROP TABLE IF EXISTS `EMS_REST_API_globalconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMS_REST_API_globalconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_cutoff` int(11) NOT NULL,
  `second_cutoff` int(11) NOT NULL,
  `level_1_rate` double NOT NULL,
  `level_2_rate` double NOT NULL,
  `level_3_rate` double NOT NULL,
  `overtime_rate` double NOT NULL,
  `regular_holiday_rate` double NOT NULL,
  `special_holiday_rate` double NOT NULL,
  `pagibig_contrib_rate` double NOT NULL,
  `philhealth_contrib_rate` double NOT NULL,
  `sss_contrib_rate` double NOT NULL,
  `tax_contrib_rate` double NOT NULL,
  `tax_income_candidate` double NOT NULL,
  `pagibig_pay_day` int(11) NOT NULL,
  `philhealth_pay_day` int(11) NOT NULL,
  `sss_pay_day` int(11) NOT NULL,
  `tax_pay_day` int(11) NOT NULL,
  `is_operating` tinyint(1) NOT NULL,
  `fb_page_id` varchar(50) NOT NULL,
  `fb_user_token` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMS_REST_API_globalconfig`
--

LOCK TABLES `EMS_REST_API_globalconfig` WRITE;
/*!40000 ALTER TABLE `EMS_REST_API_globalconfig` DISABLE KEYS */;
INSERT INTO `EMS_REST_API_globalconfig` VALUES (1,5,20,100,200,250,1.25,1,0.3,0.02,0.01375,0.0363,0.0333,20833,20,20,20,20,1,'1104237039735655','EAAZAUX1v4ACUBAEBVObGa91JTBH4QIXStTCqiZBGD8lF20DTydG9RffOIQ9pAG47dOfIsCNbwMbPeLpNbso4K8dh4QVJyC4jG4KXddlCSgM9zE6ZCo9ZAfLXD4nmOZCNvWFNoEvZCvM3efGhZAraFuBZAZA630ZCzBdekzs68WTQ4NOAZDZD');
/*!40000 ALTER TABLE `EMS_REST_API_globalconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMS_REST_API_salaryreport`
--

DROP TABLE IF EXISTS `EMS_REST_API_salaryreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMS_REST_API_salaryreport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `total_time` double NOT NULL,
  `total_over_time` double NOT NULL,
  `days_present` int(11) NOT NULL,
  `days_absent` int(11) NOT NULL,
  `sss_contrib` double NOT NULL,
  `philhealth_contrib` double NOT NULL,
  `pagibig_contrib` double NOT NULL,
  `tax` double NOT NULL,
  `special_pay` double NOT NULL,
  `gross_pay` double NOT NULL,
  `net_pay` double NOT NULL,
  `period` varchar(60) DEFAULT NULL,
  `is_released` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `EMS_REST_API_salaryr_user_id_8b555b09_fk_EMS_REST_` (`user_id`),
  CONSTRAINT `EMS_REST_API_salaryr_user_id_8b555b09_fk_EMS_REST_` FOREIGN KEY (`user_id`) REFERENCES `EMS_REST_API_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMS_REST_API_salaryreport`
--

LOCK TABLES `EMS_REST_API_salaryreport` WRITE;
/*!40000 ALTER TABLE `EMS_REST_API_salaryreport` DISABLE KEYS */;
INSERT INTO `EMS_REST_API_salaryreport` VALUES (1,0,0,0,1,0,0,0,0,0,0,0,'2018/08/6 - 2018/08/06',1,1),(2,0,0,0,1,0,0,0,0,0,0,0,'2018/08/6 - 2018/08/06',1,2),(3,88,0,11,0,638.88,242,352,0,0,17600,16367.12,'2018/08/6 - 2018/08/20',1,1),(4,88,0,11,0,319.44,121,176,0,0,8800,8183.56,'2018/08/6 - 2018/08/20',1,2),(5,96,0,12,0,0,0,0,0,480,19680,19680,'2018/8/21 - 2018/09/05',1,1),(6,96,0,12,0,0,0,0,0,240,9840,9840,'2018/8/21 - 2018/09/05',1,2),(7,88,0,11,0,1353.264,512.6,745.6,1241.424,0,17600,13747.112,'2018/09/6 - 2018/09/20',1,1),(8,88,0,11,0,676.632,256.3,372.8,0,0,8800,7494.268,'2018/09/6 - 2018/09/20',1,2),(9,88,0,11,0,0,0,0,0,0,17600,17600,'2018/9/21 - 2018/10/05',1,1),(10,88,0,11,0,0,0,0,0,0,8800,8800,'2018/9/21 - 2018/10/05',1,2),(11,80,0,10,0,1219.68,462,672,1118.88,0,16000,12527.44,'2018/10/6 - 2018/10/20',1,1),(12,80,0,10,0,609.84,231,336,0,0,8000,6823.16,'2018/10/6 - 2018/10/20',1,2),(13,80,0,10,0,0,0,0,0,480,16480,0,NULL,0,1),(14,80,0,10,0,0,0,0,0,240,8240,0,NULL,0,2);
/*!40000 ALTER TABLE `EMS_REST_API_salaryreport` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add global config',7,'add_globalconfig'),(26,'Can change global config',7,'change_globalconfig'),(27,'Can delete global config',7,'delete_globalconfig'),(28,'Can view global config',7,'view_globalconfig'),(29,'Can add employee profile',8,'add_employeeprofile'),(30,'Can change employee profile',8,'change_employeeprofile'),(31,'Can delete employee profile',8,'delete_employeeprofile'),(32,'Can view employee profile',8,'view_employeeprofile'),(33,'Can add employee config',9,'add_employeeconfig'),(34,'Can change employee config',9,'change_employeeconfig'),(35,'Can delete employee config',9,'delete_employeeconfig'),(36,'Can view employee config',9,'view_employeeconfig'),(37,'Can add salary report',10,'add_salaryreport'),(38,'Can change salary report',10,'change_salaryreport'),(39,'Can delete salary report',10,'delete_salaryreport'),(40,'Can view salary report',10,'view_salaryreport'),(41,'Can add attendance log',11,'add_attendancelog'),(42,'Can change attendance log',11,'change_attendancelog'),(43,'Can delete attendance log',11,'delete_attendancelog'),(44,'Can view attendance log',11,'view_attendancelog'),(45,'Can add employee',12,'add_employee'),(46,'Can change employee',12,'change_employee'),(47,'Can delete employee',12,'delete_employee'),(48,'Can view employee',12,'view_employee');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$cgcChnqpYZye$SzVuffXX8k4J1TB6gh2vgPZ3XF6mtFfAaHqEBc+IahM=','2018-08-04 22:05:24.015235',1,'cedrick','','','cedrickdomingo048@gmail.com',1,1,'2018-08-04 22:01:19.301642'),(2,'pbkdf2_sha256$120000$iCg9zeISq1oG$vaQD+ofU9QixOgD3A/3dpYhNWXR+Zd6URzHWtznRU5k=',NULL,0,'cedie','','','cedrickdomingo57@gmail.com',0,1,'2018-08-04 22:07:20.202554'),(3,'pbkdf2_sha256$120000$uFr3pzk7ccIZ$ivKK/5ht6PEdsv7Krts+L1gEYZ4pSyS+KtP5A+itzzw=',NULL,0,'dudeson','','','dudes@gmail.com',0,1,'2018-08-04 22:08:53.337221');
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'EMS_REST_API','attendancelog'),(12,'EMS_REST_API','employee'),(9,'EMS_REST_API','employeeconfig'),(8,'EMS_REST_API','employeeprofile'),(7,'EMS_REST_API','globalconfig'),(10,'EMS_REST_API','salaryreport'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-08-04 22:00:11.275095'),(2,'auth','0001_initial','2018-08-04 22:00:19.473159'),(3,'admin','0001_initial','2018-08-04 22:00:21.233305'),(4,'admin','0002_logentry_remove_auto_add','2018-08-04 22:00:21.286824'),(5,'admin','0003_logentry_add_action_flag_choices','2018-08-04 22:00:21.336134'),(6,'contenttypes','0002_remove_content_type_name','2018-08-04 22:00:22.354406'),(7,'auth','0002_alter_permission_name_max_length','2018-08-04 22:00:22.455996'),(8,'auth','0003_alter_user_email_max_length','2018-08-04 22:00:22.582673'),(9,'auth','0004_alter_user_username_opts','2018-08-04 22:00:22.635028'),(10,'auth','0005_alter_user_last_login_null','2018-08-04 22:00:23.147973'),(11,'auth','0006_require_contenttypes_0002','2018-08-04 22:00:23.191258'),(12,'auth','0007_alter_validators_add_error_messages','2018-08-04 22:00:23.247478'),(13,'auth','0008_alter_user_username_max_length','2018-08-04 22:00:23.383178'),(14,'auth','0009_alter_user_last_name_max_length','2018-08-04 22:00:23.509709'),(15,'sessions','0001_initial','2018-08-04 22:00:24.040763'),(16,'EMS_REST_API','0001_initial','2018-08-04 22:00:45.385495');
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('jnbluhg40crkvrobxs7oqkzqqijsfxhc','MDkwYzNhNzdlNmI3MTk2M2VhNDUxY2U4YmQyNjE1YjlhNGU2NjQwYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MmE5MzU5NjU4MjM4NzAxNmQyYWM5M2MzZmMyNmNjMTVlYTE0MWE5In0=','2018-08-18 22:05:24.057126');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-30 14:29:38
