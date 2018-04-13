-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: bbg_server
-- ------------------------------------------------------
-- Server version	5.5.48-log

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
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account` (
  `account_id` int(10) unsigned NOT NULL COMMENT 'Identifier',
  `uuid` varchar(256) NOT NULL DEFAULT '',
  `cid` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'channel id',
  `user_name` varchar(128) NOT NULL DEFAULT '',
  `password` varchar(128) NOT NULL DEFAULT '',
  `token_key` varchar(128) NOT NULL DEFAULT '',
  `locked` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `locked_expire` int(3) unsigned NOT NULL DEFAULT '0',
  `create_time` int(10) unsigned NOT NULL DEFAULT '0',
  `last_login` int(10) unsigned NOT NULL DEFAULT '0',
  `last_logout` int(10) unsigned NOT NULL DEFAULT '0',
  `name` varchar(512) NOT NULL DEFAULT '' COMMENT '角色名称',
  `head_frame` longtext NOT NULL COMMENT '头像框',
  `head_icon` longtext NOT NULL COMMENT '头像',
  `sex` tinyint(1) DEFAULT '1' COMMENT '性别 默认男',
  `room_id` int(3) unsigned NOT NULL DEFAULT '0' COMMENT '当前进入的房间',
  `room_type` int(3) unsigned NOT NULL DEFAULT '0' COMMENT '当前进入的游戏类型',
  `gold` int(10) DEFAULT '0' COMMENT '元宝',
  `proxy_id` int(10) DEFAULT '0' COMMENT '上级ID',
  `proxy_count` int(10) DEFAULT '0' COMMENT '下级数量',
  `level` int(10) NOT NULL DEFAULT '4' COMMENT '代理等级(0-N) 0位管理员',
  `month` int(10) DEFAULT '0' COMMENT '本月月份',
  `month_recharge` int(10) DEFAULT '0' COMMENT '当月充值',
  `all_recharge` int(10) DEFAULT '0' COMMENT '总充值',
  `month_proxy_recharge` int(10) DEFAULT '0' COMMENT '代理当月充值',
  `all_proxy_recharge` int(10) DEFAULT '0' COMMENT '代理总充值',
  `poker_point` int(10) DEFAULT '0' COMMENT '扑克总积分',
  `mahjong_point` int(10) DEFAULT '0' COMMENT '麻将总积分',
  `gold_point` int(10) DEFAULT '0' COMMENT '金币总积分',
  PRIMARY KEY (`account_id`),
  UNIQUE KEY `idx_username` (`user_name`),
  KEY `uuid` (`uuid`(255))
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Account';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `history` (
  `account_id` int(10) unsigned NOT NULL,
  `data` longtext NOT NULL,
  `room_ids` varchar(10240) NOT NULL,
  PRIMARY KEY (`account_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `infomation`
--

DROP TABLE IF EXISTS `infomation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `infomation` (
  `id` int(10) unsigned NOT NULL,
  `content` longtext NOT NULL,
  `desc` varchar(128) NOT NULL DEFAULT '' COMMENT '描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `log_gold`
--

DROP TABLE IF EXISTS `log_gold`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_gold` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '管理ID',
  `account_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '帐号ID',
  `count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '消费数量',
  `remain` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '剩余数量',
  `origin_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '消费处ID',
  `time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '使用时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=537674 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `log_s_gold_use`
--

DROP TABLE IF EXISTS `log_s_gold_use`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_s_gold_use` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `day` varchar(32) NOT NULL,
  `room_use_total` int(11) NOT NULL,
  `time` int(11) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `day` (`day`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `proxy`
--

DROP TABLE IF EXISTS `proxy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proxy` (
  `proxy_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '代理人ID',
  `account` varchar(32) NOT NULL DEFAULT '' COMMENT '账号',
  `password` varchar(32) NOT NULL DEFAULT '' COMMENT '密码',
  `level` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '级别',
  `name` varchar(32) NOT NULL DEFAULT '' COMMENT '代理人名字',
  `phone` int(10) unsigned NOT NULL DEFAULT '0',
  `address` varchar(128) NOT NULL DEFAULT '',
  `join_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '加入时间',
  `before_proxy_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '上一级代理人ID',
  `state` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '状态',
  PRIMARY KEY (`proxy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `recharge`
--

DROP TABLE IF EXISTS `recharge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recharge` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '管理ID',
  `account_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '帐号ID',
  `proxy_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '代理人ID',
  `op_id` varchar(128) NOT NULL COMMENT '订单号',
  `transaction_id` varchar(128) NOT NULL,
  `money` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '充值金额',
  `ingot` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '转化的代币',
  `origin` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '充值来源',
  `time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '充值时间',
  `level` tinyint(3) NOT NULL DEFAULT '4' COMMENT '代理等级',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_op_id` (`op_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4486 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `room` (
  `room_id` int(10) unsigned NOT NULL COMMENT 'Identifier',
  `room_type` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `room_help` int(10) unsigned NOT NULL DEFAULT '0',
  `rounds` int(10) unsigned NOT NULL DEFAULT '0',
  `create_time` int(10) unsigned NOT NULL DEFAULT '0',
  `account_id` int(10) unsigned NOT NULL DEFAULT '0',
  `data` longtext NOT NULL,
  PRIMARY KEY (`room_id`,`room_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT,
  `account_id` varchar(256) NOT NULL,
  `user_name` varchar(256) NOT NULL COMMENT '用户名',
  `password` varchar(128) NOT NULL,
  `locked` tinyint(3) NOT NULL COMMENT '代理开启状态',
  `create_time` int(10) NOT NULL,
  `last_login` int(10) NOT NULL,
  `name` varchar(128) NOT NULL COMMENT '昵称',
  `head_icon` longtext NOT NULL,
  `sex` tinyint(3) NOT NULL,
  `month` int(10) DEFAULT '0' COMMENT '本月月份',
  `month_recharge` int(10) DEFAULT '0' COMMENT '当月充值',
  `all_recharge` int(10) DEFAULT '0' COMMENT '总充值',
  `month_proxy_recharge` int(10) DEFAULT '0' COMMENT '代理当月充值',
  `all_proxy_recharge` int(10) DEFAULT '0' COMMENT '代理总充值',
  `level` tinyint(3) NOT NULL COMMENT '代理等级(0-N) 0位管理员',
  `superiorId` varchar(32) NOT NULL COMMENT '上级ID',
  `insertingCoil` int(10) NOT NULL COMMENT '下线数量',
  `address` varchar(256) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `card` int(32) NOT NULL,
  `city` varchar(128) NOT NULL,
  `remark` varchar(256) NOT NULL,
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=268 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-02 14:50:33
