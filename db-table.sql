CREATE DATABASE  IF NOT EXISTS `spider-cnblog`
USE `spider-cnblog`;


DROP TABLE IF EXISTS `cnblog_blogs`;

CREATE TABLE `cnblog_blogs` (
  `cnblog_blog_id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `title` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `article` text COLLATE utf8_bin,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `creation_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cnblog_blog_id`),
  UNIQUE KEY `idcnblog_blogs_UNIQUE` (`cnblog_blog_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3464 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;



DROP TABLE IF EXISTS `urls`;

CREATE TABLE `urls` (
  `url_id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(64) COLLATE utf8_bin NOT NULL,
  `title` varchar(16) COLLATE utf8_bin NOT NULL DEFAULT '',
  `visited` tinyint(1) NOT NULL DEFAULT '0',
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `creation_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`url_id`),
  UNIQUE KEY `idurls_UNIQUE` (`url_id`)
) ENGINE=InnoDB AUTO_INCREMENT=846 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

