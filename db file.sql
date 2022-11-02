/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - collegeproduct
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`collegeproduct` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `collegeproduct`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admin` */

insert  into `admin`(`username`,`password`) values ('admin','admin');

/*Table structure for table `lostproduct` */

DROP TABLE IF EXISTS `lostproduct`;

CREATE TABLE `lostproduct` (
  `username` varchar(50) NOT NULL,
  `rollno` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `product` varchar(45) DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT 'lost',
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `lostproduct` */

insert  into `lostproduct`(`username`,`rollno`,`phone`,`product`,`department`,`status`) values ('munna','1234567','8639966858','bottle','CSE','lost');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `rollno` varchar(45) DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`username`,`password`,`email`,`rollno`,`department`) values ('munna','munna','munna@gmail.com','1234567','CSE');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
