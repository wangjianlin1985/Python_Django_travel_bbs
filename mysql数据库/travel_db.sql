/*
Navicat MySQL Data Transfer

Source Server         : mysql5.6
Source Server Version : 50620
Source Host           : localhost:3306
Source Database       : travel_db

Target Server Type    : MYSQL
Target Server Version : 50620
File Encoding         : 65001

Date: 2020-07-01 17:47:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
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

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add user', '7', 'add_newuser');
INSERT INTO `auth_permission` VALUES ('26', 'Can change user', '7', 'change_newuser');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete user', '7', 'delete_newuser');
INSERT INTO `auth_permission` VALUES ('28', 'Can view user', '7', 'view_newuser');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 系统素材表', '8', 'add_sysmaterial');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 系统素材表', '8', 'change_sysmaterial');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 系统素材表', '8', 'delete_sysmaterial');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 系统素材表', '8', 'view_sysmaterial');
INSERT INTO `auth_permission` VALUES ('33', 'Can add 临时手机号验证码表', '9', 'add_temptelcode');
INSERT INTO `auth_permission` VALUES ('34', 'Can change 临时手机号验证码表', '9', 'change_temptelcode');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete 临时手机号验证码表', '9', 'delete_temptelcode');
INSERT INTO `auth_permission` VALUES ('36', 'Can view 临时手机号验证码表', '9', 'view_temptelcode');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 评论表', '10', 'add_comment');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 评论表', '10', 'change_comment');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 评论表', '10', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('40', 'Can view 评论表', '10', 'view_comment');
INSERT INTO `auth_permission` VALUES ('41', 'Can add 论坛分类', '11', 'add_forumsort');
INSERT INTO `auth_permission` VALUES ('42', 'Can change 论坛分类', '11', 'change_forumsort');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete 论坛分类', '11', 'delete_forumsort');
INSERT INTO `auth_permission` VALUES ('44', 'Can view 论坛分类', '11', 'view_forumsort');
INSERT INTO `auth_permission` VALUES ('45', 'Can add 评论表', '12', 'add_topicreview');
INSERT INTO `auth_permission` VALUES ('46', 'Can change 评论表', '12', 'change_topicreview');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete 评论表', '12', 'delete_topicreview');
INSERT INTO `auth_permission` VALUES ('48', 'Can view 评论表', '12', 'view_topicreview');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 论坛分类', '13', 'add_topictext');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 论坛分类', '13', 'change_topictext');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 论坛分类', '13', 'delete_topictext');
INSERT INTO `auth_permission` VALUES ('52', 'Can view 论坛分类', '13', 'view_topictext');
INSERT INTO `auth_permission` VALUES ('53', 'Can add 文章关注表', '14', 'add_guan_zhu');
INSERT INTO `auth_permission` VALUES ('54', 'Can change 文章关注表', '14', 'change_guan_zhu');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete 文章关注表', '14', 'delete_guan_zhu');
INSERT INTO `auth_permission` VALUES ('56', 'Can view 文章关注表', '14', 'view_guan_zhu');
INSERT INTO `auth_permission` VALUES ('57', 'Can add 评论表', '15', 'add_collectcomment');
INSERT INTO `auth_permission` VALUES ('58', 'Can change 评论表', '15', 'change_collectcomment');
INSERT INTO `auth_permission` VALUES ('59', 'Can delete 评论表', '15', 'delete_collectcomment');
INSERT INTO `auth_permission` VALUES ('60', 'Can view 评论表', '15', 'view_collectcomment');
INSERT INTO `auth_permission` VALUES ('61', 'Can add 文档内容', '16', 'add_guidebody');
INSERT INTO `auth_permission` VALUES ('62', 'Can change 文档内容', '16', 'change_guidebody');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete 文档内容', '16', 'delete_guidebody');
INSERT INTO `auth_permission` VALUES ('64', 'Can view 文档内容', '16', 'view_guidebody');
INSERT INTO `auth_permission` VALUES ('65', 'Can add 文档标题', '17', 'add_guidetitle');
INSERT INTO `auth_permission` VALUES ('66', 'Can change 文档标题', '17', 'change_guidetitle');
INSERT INTO `auth_permission` VALUES ('67', 'Can delete 文档标题', '17', 'delete_guidetitle');
INSERT INTO `auth_permission` VALUES ('68', 'Can view 文档标题', '17', 'view_guidetitle');
INSERT INTO `auth_permission` VALUES ('69', 'Can add 图片记录', '18', 'add_imgmaterial');
INSERT INTO `auth_permission` VALUES ('70', 'Can change 图片记录', '18', 'change_imgmaterial');
INSERT INTO `auth_permission` VALUES ('71', 'Can delete 图片记录', '18', 'delete_imgmaterial');
INSERT INTO `auth_permission` VALUES ('72', 'Can view 图片记录', '18', 'view_imgmaterial');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$180000$nad5uqnVKRVj$CabQcQhHukgCurl1c5Yxtxxkbl8aN+2UyN+OspdGQ14=', '2020-07-01 06:43:57.810136', '0', 'user1', '汪', '大哥', '254540457@qq.com', '0', '1', '2020-06-30 18:24:03.671035');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$180000$NqWme47DqOPu$jOvD0V+icTLQVwbSTiQwzDYhnoexckBlu2/6v0ZjNUo=', '2020-07-01 09:27:32.307044', '1', 'admin', '', '', 'test@126.com', '1', '1', '2020-07-01 07:51:23.234131');
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$180000$EDjVMUgNoDod$yE6XTswbaJyaN0wHE+ZLFHpgvYqC16LTUN2Z95hnhKM=', '2020-07-01 09:12:54.905037', '0', 'user2', '', '', '344245001@qq.com', '0', '1', '2020-07-01 09:22:21.120705');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
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

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
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

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `base_comment`
-- ----------------------------
DROP TABLE IF EXISTS `base_comment`;
CREATE TABLE `base_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext,
  `like_count` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `parent_type` varchar(256) DEFAULT NULL,
  `parent_comment` int(11) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `target_user_id` int(11) DEFAULT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_comment_parent_id_244e8170` (`parent_id`),
  KEY `base_comment_parent_type_20723f37` (`parent_type`(255)),
  KEY `base_comment_parent_comment_84ad8d1e` (`parent_comment`),
  KEY `base_comment_create_user_id_320e75cd_fk_auth_user_id` (`create_user_id`),
  KEY `base_comment_target_user_id_95960f82_fk_auth_user_id` (`target_user_id`),
  KEY `base_comment_write_user_id_42c1b47b_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `base_comment_create_user_id_320e75cd_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `base_comment_target_user_id_95960f82_fk_auth_user_id` FOREIGN KEY (`target_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `base_comment_write_user_id_42c1b47b_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of base_comment
-- ----------------------------
INSERT INTO `base_comment` VALUES ('1', '<p>谁要去的话，联系我电话136****1341</p>', '0', '3', 'TopicText', null, '1', '2020-07-01 05:29:49.944036', '2020-07-01 05:29:49.944036', '1', '1', '1');
INSERT INTO `base_comment` VALUES ('2', '<p>怎么样，大家觉得漂亮吗？</p>', '0', '5', 'TopicText', null, '1', '2020-07-01 09:11:51.550456', '2020-07-01 09:11:51.550957', '3', '3', '3');

-- ----------------------------
-- Table structure for `base_newuser`
-- ----------------------------
DROP TABLE IF EXISTS `base_newuser`;
CREATE TABLE `base_newuser` (
  `user_ptr_id` int(11) NOT NULL,
  `show_name` varchar(255) DEFAULT NULL,
  `avatar_path` varchar(255) DEFAULT NULL,
  `telephone` varchar(255) DEFAULT NULL,
  `auth_code` varchar(255) DEFAULT NULL,
  `signatrue` varchar(255) DEFAULT NULL,
  `send_date` datetime(6) DEFAULT NULL,
  `avatar_id` int(11) DEFAULT NULL,
  `home_img_id` int(11) DEFAULT NULL,
  `home_path` varchar(255) DEFAULT NULL,
  `abstract` longtext,
  `sex` tinyint(1) NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  KEY `base_newuser_avatar_id_3ab5c934_fk_img_material_id` (`avatar_id`),
  KEY `base_newuser_home_img_id_950719a6_fk_img_material_id` (`home_img_id`),
  CONSTRAINT `base_newuser_avatar_id_3ab5c934_fk_img_material_id` FOREIGN KEY (`avatar_id`) REFERENCES `img_material` (`id`),
  CONSTRAINT `base_newuser_home_img_id_950719a6_fk_img_material_id` FOREIGN KEY (`home_img_id`) REFERENCES `img_material` (`id`),
  CONSTRAINT `base_newuser_user_ptr_id_121b7531_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of base_newuser
-- ----------------------------
INSERT INTO `base_newuser` VALUES ('1', null, null, '13594122934', '4103', '我是一个大神', '2020-07-01 07:39:15.334274', null, null, null, '健康快乐每一天', '0');
INSERT INTO `base_newuser` VALUES ('3', null, null, '13508233082', '6642', '我是一个旅游爱好者', '2020-07-01 09:26:52.399260', null, null, null, '喜欢旅游的朋友，大家来一起交朋友吧', '1');

-- ----------------------------
-- Table structure for `base_sys_material`
-- ----------------------------
DROP TABLE IF EXISTS `base_sys_material`;
CREATE TABLE `base_sys_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) DEFAULT NULL,
  `value` longtext,
  `note` longtext,
  `group` varchar(256) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `base_sys_material_create_user_id_5bdd902c_fk_auth_user_id` (`create_user_id`),
  KEY `base_sys_material_write_user_id_a5352118_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `base_sys_material_create_user_id_5bdd902c_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `base_sys_material_write_user_id_a5352118_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of base_sys_material
-- ----------------------------
INSERT INTO `base_sys_material` VALUES ('1', 'user_default_icon_path', '/static/media/icon/sysicon/yangwangtiankong.jpg', '默认的用户头像', null, '2020-06-30 17:52:26.436001', '2020-06-30 17:52:26.440512', null, null);
INSERT INTO `base_sys_material` VALUES ('2', 'user_images_default', '/static/media/icon/sysicon/user_images_ default_160x160.jpg', '评论页的默认用户头像', null, '2020-06-30 17:52:26.446027', '2020-06-30 17:52:26.450539', null, null);
INSERT INTO `base_sys_material` VALUES ('3', 'user_home_img', '/static/media/images/sysimg/default_user_home_images.jpg', '用户主页默认头像', null, '2020-06-30 17:52:26.462071', '2020-06-30 17:52:26.465078', null, null);
INSERT INTO `base_sys_material` VALUES ('4', 'comm_page_size', '10', '社区首页展示的帖子的条数', null, '2020-06-30 17:52:26.470092', '2020-06-30 17:52:26.473100', null, null);
INSERT INTO `base_sys_material` VALUES ('5', 'sort_page_size', '10', '分类展示帖子的页数', null, '2020-06-30 17:52:26.477613', '2020-06-30 17:52:26.480619', null, null);
INSERT INTO `base_sys_material` VALUES ('6', 'image_path', 'static', '文件默认上传的路径', null, '2020-06-30 17:52:26.486134', '2020-06-30 17:52:26.489142', null, null);
INSERT INTO `base_sys_material` VALUES ('7', 'TopicText', '{\"app_label\": \"community\", \"model\": \"topictext\"}', 'TopicText的app_label和model', null, '2020-06-30 17:52:26.493655', '2020-06-30 17:52:26.496662', null, null);
INSERT INTO `base_sys_material` VALUES ('8', 'GuideTitle', '{\"app_label\": \"guides\", \"model\": \"guidetitle\"}', 'GuideTitle的app_label和model', null, '2020-06-30 17:52:26.502678', '2020-06-30 17:52:26.505686', null, null);

-- ----------------------------
-- Table structure for `community_guan_zhu`
-- ----------------------------
DROP TABLE IF EXISTS `community_guan_zhu`;
CREATE TABLE `community_guan_zhu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `gz_user_id` int(11) DEFAULT NULL,
  `topic_id` int(11) DEFAULT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `community_guan_zhu_create_user_id_1aec3b31_fk_auth_user_id` (`create_user_id`),
  KEY `community_guan_zhu_gz_user_id_012079ab_fk_auth_user_id` (`gz_user_id`),
  KEY `community_guan_zhu_topic_id_9a3dc971_fk_comm_topic_text_id` (`topic_id`),
  KEY `community_guan_zhu_write_user_id_f2397426_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `community_guan_zhu_create_user_id_1aec3b31_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `community_guan_zhu_gz_user_id_012079ab_fk_auth_user_id` FOREIGN KEY (`gz_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `community_guan_zhu_topic_id_9a3dc971_fk_comm_topic_text_id` FOREIGN KEY (`topic_id`) REFERENCES `comm_topic_text` (`id`),
  CONSTRAINT `community_guan_zhu_write_user_id_f2397426_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of community_guan_zhu
-- ----------------------------
INSERT INTO `community_guan_zhu` VALUES ('1', '2020-07-01 09:10:37.079486', '2020-07-01 09:10:37.079988', '3', '3', '3', '3');

-- ----------------------------
-- Table structure for `comm_collect_comment`
-- ----------------------------
DROP TABLE IF EXISTS `comm_collect_comment`;
CREATE TABLE `comm_collect_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `topic_id` int(11) DEFAULT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `comm_collect_comment_create_user_id_ce8f8df0_fk_auth_user_id` (`create_user_id`),
  KEY `comm_collect_comment_topic_id_9289c0ba_fk_base_comment_id` (`topic_id`),
  KEY `comm_collect_comment_user_id_b5291deb_fk_auth_user_id` (`user_id`),
  KEY `comm_collect_comment_write_user_id_b4778c9b_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `comm_collect_comment_create_user_id_ce8f8df0_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `comm_collect_comment_topic_id_9289c0ba_fk_base_comment_id` FOREIGN KEY (`topic_id`) REFERENCES `base_comment` (`id`),
  CONSTRAINT `comm_collect_comment_user_id_b5291deb_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `comm_collect_comment_write_user_id_b4778c9b_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comm_collect_comment
-- ----------------------------

-- ----------------------------
-- Table structure for `comm_forum_sort`
-- ----------------------------
DROP TABLE IF EXISTS `comm_forum_sort`;
CREATE TABLE `comm_forum_sort` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `describe` longtext,
  `source` varchar(256) DEFAULT NULL,
  `url` varchar(256) DEFAULT NULL,
  `icon` varchar(256) DEFAULT NULL,
  `a_public` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `comm_forum_sort_create_user_id_61146905_fk_auth_user_id` (`create_user_id`),
  KEY `comm_forum_sort_write_user_id_95a68fac_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `comm_forum_sort_create_user_id_61146905_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `comm_forum_sort_write_user_id_95a68fac_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comm_forum_sort
-- ----------------------------
INSERT INTO `comm_forum_sort` VALUES ('1', '综合交流', '自从出了冰神，死神就有些堕落了。后来兽神又来了，死神几乎无用武之地。现在天神降临，死神....还有人记得这杆枪吗？我的死神该何去何从？死神是否需要再进化？', null, 'exchange', null, '1', '2020-06-30 17:52:26.523233', '2020-06-30 17:52:26.526241', null, null);
INSERT INTO `comm_forum_sort` VALUES ('2', '旅行心得', '自从出了冰神，死神就有些堕落了。后来兽神又来了，死神几乎无用武之地。现在天神降临，死神....还有人记得这杆枪吗？我的死神该何去何从？死神是否需要再进化？', null, 'taste', null, '1', '2020-06-30 17:52:26.531755', '2020-06-30 17:52:26.535266', null, null);
INSERT INTO `comm_forum_sort` VALUES ('3', '杂谈', '自从出了冰神，死神就有些堕落了。后来兽神又来了，死神几乎无用武之地。现在天神降临，死神....还有人记得这杆枪吗？我的死神该何去何从？死神是否需要再进化？', null, 'gossip', null, '1', '2020-06-30 17:52:26.540278', '2020-06-30 17:52:26.543287', null, null);

-- ----------------------------
-- Table structure for `comm_topic_review`
-- ----------------------------
DROP TABLE IF EXISTS `comm_topic_review`;
CREATE TABLE `comm_topic_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `review_text` longtext,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `forum_sort_id` int(11) DEFAULT NULL,
  `topic_text_id` int(11) DEFAULT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `comm_topic_review_create_user_id_8e3336a0_fk_auth_user_id` (`create_user_id`),
  KEY `comm_topic_review_forum_sort_id_0a290783_fk_comm_forum_sort_id` (`forum_sort_id`),
  KEY `comm_topic_review_topic_text_id_439d8629_fk_comm_topic_text_id` (`topic_text_id`),
  KEY `comm_topic_review_write_user_id_252b9252_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `comm_topic_review_create_user_id_8e3336a0_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `comm_topic_review_forum_sort_id_0a290783_fk_comm_forum_sort_id` FOREIGN KEY (`forum_sort_id`) REFERENCES `comm_forum_sort` (`id`),
  CONSTRAINT `comm_topic_review_topic_text_id_439d8629_fk_comm_topic_text_id` FOREIGN KEY (`topic_text_id`) REFERENCES `comm_topic_text` (`id`),
  CONSTRAINT `comm_topic_review_write_user_id_252b9252_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comm_topic_review
-- ----------------------------

-- ----------------------------
-- Table structure for `comm_topic_text`
-- ----------------------------
DROP TABLE IF EXISTS `comm_topic_text`;
CREATE TABLE `comm_topic_text` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `text_txt` longtext,
  `text_htm` longtext,
  `u_public` tinyint(1) NOT NULL,
  `a_public` tinyint(1) NOT NULL,
  `priority` int(11) DEFAULT NULL,
  `pviews` int(11) DEFAULT NULL,
  `collection` int(11) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `forum_sort_id` int(11) DEFAULT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `comm_topic_text_create_user_id_a35a455d_fk_auth_user_id` (`create_user_id`),
  KEY `comm_topic_text_forum_sort_id_0640ef9d_fk_comm_forum_sort_id` (`forum_sort_id`),
  KEY `comm_topic_text_write_user_id_31893722_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `comm_topic_text_create_user_id_a35a455d_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `comm_topic_text_forum_sort_id_0640ef9d_fk_comm_forum_sort_id` FOREIGN KEY (`forum_sort_id`) REFERENCES `comm_forum_sort` (`id`),
  CONSTRAINT `comm_topic_text_write_user_id_31893722_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comm_topic_text
-- ----------------------------
INSERT INTO `comm_topic_text` VALUES ('3', '有一起去西藏旅游的吗？', '最近我打算去西藏旅游，有人一起去吗？', '<p>最近我打算去西藏旅游，有人一起去吗？</p>', '1', '1', '0', '0', '0', '2020-07-01 05:29:17.077388', '2020-07-01 05:29:17.077889', '1', '1', '1');
INSERT INTO `comm_topic_text` VALUES ('4', '其实旅游也可以不用耗费多少钱', '我喜欢自驾游，其实花不了多少钱，有的时候在野外搭个帐篷就可以过一夜，和大自然亲密接触呢！', '<p>我喜欢自驾游，其实花不了多少钱，有的时候在野外搭个帐篷就可以过一夜，和大自然亲密接触呢！</p>', '1', '1', '0', '0', '0', '2020-07-01 09:07:50.060555', '2020-07-01 09:07:50.061558', '3', '2', '3');
INSERT INTO `comm_topic_text` VALUES ('5', '分享我旅游认识的美女朋友！', '来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！', '<p>来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！来一张上次旅游认识拍的美女！！</p><p><img src=\"/static/media/editor/84143a90-bb7a-11ea-b3e2-e4029b8604f6_user2.jpg\" alt=\"23\" style=\"max-width: 100%;\"></p><p><br></p>', '1', '1', '0', '0', '0', '2020-07-01 09:09:55.978950', '2020-07-01 09:09:55.979451', '3', '3', '3');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('7', 'base', 'newuser');
INSERT INTO `django_content_type` VALUES ('8', 'base', 'sysmaterial');
INSERT INTO `django_content_type` VALUES ('9', 'base', 'temptelcode');
INSERT INTO `django_content_type` VALUES ('15', 'community', 'collectcomment');
INSERT INTO `django_content_type` VALUES ('10', 'community', 'comment');
INSERT INTO `django_content_type` VALUES ('11', 'community', 'forumsort');
INSERT INTO `django_content_type` VALUES ('14', 'community', 'guan_zhu');
INSERT INTO `django_content_type` VALUES ('12', 'community', 'topicreview');
INSERT INTO `django_content_type` VALUES ('13', 'community', 'topictext');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('16', 'guides', 'guidebody');
INSERT INTO `django_content_type` VALUES ('17', 'guides', 'guidetitle');
INSERT INTO `django_content_type` VALUES ('18', 'mycenter', 'imgmaterial');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2020-06-30 17:44:38.176164');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2020-06-30 17:44:38.439382');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2020-06-30 17:44:39.101329');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2020-06-30 17:44:39.383580');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2020-06-30 17:44:39.409148');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2020-06-30 17:44:39.573084');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2020-06-30 17:44:39.640263');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2020-06-30 17:44:39.740530');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2020-06-30 17:44:39.758578');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2020-06-30 17:44:39.831272');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2020-06-30 17:44:39.838793');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2020-06-30 17:44:39.853330');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2020-06-30 17:44:39.928862');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2020-06-30 17:44:40.016617');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0010_alter_group_name_max_length', '2020-06-30 17:44:40.097135');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0011_update_proxy_permissions', '2020-06-30 17:44:40.118691');
INSERT INTO `django_migrations` VALUES ('17', 'mycenter', '0001_initial', '2020-06-30 17:44:40.213945');
INSERT INTO `django_migrations` VALUES ('18', 'base', '0001_initial', '2020-06-30 17:44:40.499162');
INSERT INTO `django_migrations` VALUES ('19', 'base', '0002_temptelcode', '2020-06-30 17:44:40.790929');
INSERT INTO `django_migrations` VALUES ('20', 'base', '0003_auto_20170503_2012', '2020-06-30 17:44:40.936716');
INSERT INTO `django_migrations` VALUES ('21', 'base', '0004_auto_20170513_1047', '2020-06-30 17:44:41.114689');
INSERT INTO `django_migrations` VALUES ('22', 'base', '0005_auto_20170514_1145', '2020-06-30 17:44:41.310711');
INSERT INTO `django_migrations` VALUES ('23', 'base', '0006_auto_20200701_0144', '2020-06-30 17:44:41.612514');
INSERT INTO `django_migrations` VALUES ('24', 'community', '0001_initial', '2020-06-30 17:44:42.245055');
INSERT INTO `django_migrations` VALUES ('25', 'community', '0002_guan_zhu', '2020-06-30 17:44:43.061788');
INSERT INTO `django_migrations` VALUES ('26', 'community', '0003_auto_20170423_1806', '2020-06-30 17:44:43.550522');
INSERT INTO `django_migrations` VALUES ('27', 'community', '0004_collectcomment', '2020-06-30 17:44:43.646777');
INSERT INTO `django_migrations` VALUES ('28', 'community', '0005_auto_20170510_0922', '2020-06-30 17:44:44.312047');
INSERT INTO `django_migrations` VALUES ('29', 'community', '0006_auto_20200701_0144', '2020-06-30 17:44:48.411876');
INSERT INTO `django_migrations` VALUES ('30', 'guides', '0001_initial', '2020-06-30 17:44:49.160366');
INSERT INTO `django_migrations` VALUES ('31', 'guides', '0002_auto_20200701_0144', '2020-06-30 17:44:50.227204');
INSERT INTO `django_migrations` VALUES ('32', 'mycenter', '0002_auto_20200701_0144', '2020-06-30 17:44:50.451802');
INSERT INTO `django_migrations` VALUES ('33', 'sessions', '0001_initial', '2020-06-30 17:44:50.496921');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('idvmg69nd1yixh20ky6wdyje8wiuxqk7', 'MWM4MjdhNjIwZTlmMGQ5MmNiOWM3YmI3YmI0Mjk5NWJhYjI3OGQwZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MThkMzY4YWU2YTE4NGMzYTZlZTk2ODUzOTk5Mzc0M2RmODBmZDI0In0=', '2020-07-14 18:26:57.182263');
INSERT INTO `django_session` VALUES ('oa199re8k7k2isifs7tbm5wvj9lyib77', 'MTk0Njc0MzdhZmRhNWJhNWFiZTI0ZWM1YmRlZGJlNDY4ZDQ4ODEzNTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDQ4NDdkNWNkNWFmNTMwYTI4NjVhNjRmYWIzNjI1ODM4YmY2YTk2In0=', '2020-07-15 09:27:32.317071');

-- ----------------------------
-- Table structure for `guide_document_body`
-- ----------------------------
DROP TABLE IF EXISTS `guide_document_body`;
CREATE TABLE `guide_document_body` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(256) NOT NULL,
  `s_title` varchar(256) DEFAULT NULL,
  `s_body` longtext,
  `image_path` varchar(256) DEFAULT NULL,
  `image_name` varchar(256) DEFAULT NULL,
  `image_msg` varchar(256) DEFAULT NULL,
  `image_location` varchar(256) DEFAULT NULL,
  `image_explain` longtext,
  `numbers` int(11) DEFAULT NULL,
  `parent` int(11) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `title_id` int(11) NOT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `guide_document_body_title_id_3d33caab_fk_guide_document_title_id` (`title_id`),
  KEY `guide_document_body_create_user_id_e4e146ad_fk_auth_user_id` (`create_user_id`),
  KEY `guide_document_body_write_user_id_e0f2b1e6_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `guide_document_body_create_user_id_e4e146ad_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `guide_document_body_title_id_3d33caab_fk_guide_document_title_id` FOREIGN KEY (`title_id`) REFERENCES `guide_document_title` (`id`),
  CONSTRAINT `guide_document_body_write_user_id_e0f2b1e6_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of guide_document_body
-- ----------------------------
INSERT INTO `guide_document_body` VALUES ('8', 'mo9fUcyQg4CrFtCDygM9ZC', null, null, 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\images\\32417902-3701-5921-affa-f76bc6dceb0d.jpg', '2.jpg', null, 'all', null, '1', null, '2020-07-01 06:25:32.699984', '2020-07-01 06:25:51.557243', null, '8', null);
INSERT INTO `guide_document_body` VALUES ('9', 'QPcgNWAeD4CxZ5d9riiDfY', null, '  之前考虑过自己玩，网上的攻略更是一头的雾水，又因特殊疫情及当地政策时效性等相关问题，景区酒店等都需提前预约，再说去西双版纳各个景点分散路程较远，尤其交通安全、安排路线是很麻烦的，同时吸取多方旅行经验，本着不花冤枉钱省心的原则！同事就推荐给我她上次去版纳的傣族导游--小艾，联系了她根据我们的想法，设计了行程旅游方案。 这次真心感谢小艾的热情服务及周到安排，想要玩得省心省钱的朋友，可以联系小艾，亲测告诉你，绝对不会让你失望的！', null, null, null, null, null, '0', null, '2020-07-01 06:25:37.895270', '2020-07-01 06:25:51.571280', null, '8', null);
INSERT INTO `guide_document_body` VALUES ('10', 'mdFnxutp8egP7GbxuE53Kf', null, '辞职纯浪的两个月里，终于进行了计划了两年的【青海甘肃大环线】7日自由行享这条大环线自由行细节，希望给大家一些参考！\n\n我和马哥拼车去玩的。西北旅行拼车的方式比较常见，网上也能找到很多拼车信息。拼车师傅可以帮你们搞定食宿，路线也不用操心。划算方便又省心，很适合这样的长途旅行！想去青甘环线游玩的朋友可以找他，人非常好，真的很推荐！\n先附上路线图：\n\n给大家详细介绍我的7日行程：\nDay1：\n西宁—塔尔寺—青海湖—茶卡（夜宿）\nDay2：\n茶卡盐湖—翡翠湖—大柴旦（夜宿）\nDay3：\n青海雅丹—石油小镇—西千佛洞—敦煌沙漠（夜宿）\nDay4：\n又见敦煌（莫高窟的票没买到）—沙洲夜市—敦煌（夜宿）\nDay5：\n瓜州——张掖七彩丹霞公园—张掖（夜宿）\nDay6：\n祁连山草原—\n阿柔大寺—卓尔山—祁连（夜宿）\nDay7：\n扁都口—岗什卡雪峰—西宁', null, null, null, null, null, '2', null, '2020-07-01 09:00:19.981284', '2020-07-01 09:02:30.837116', null, '9', null);
INSERT INTO `guide_document_body` VALUES ('11', '2HVsyJuDmbgfUBdZAfCbFn', null, null, 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\images\\bbfe2836-bfab-564f-9968-ba78618d12e8.jpg', '4.jpg', null, 'all', null, '1', null, '2020-07-01 09:01:49.554277', '2020-07-01 09:02:30.848683', null, '9', null);
INSERT INTO `guide_document_body` VALUES ('12', 'iQwRwKDcYk4DiLjQuLbiEV', null, null, 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\images\\d5d002ab-bfd0-5f08-8c00-885b5409d2c1.jpg', '5.jpg', null, 'all', null, '0', null, '2020-07-01 09:02:00.866221', '2020-07-01 09:02:30.861682', null, '9', null);

-- ----------------------------
-- Table structure for `guide_document_title`
-- ----------------------------
DROP TABLE IF EXISTS `guide_document_title`;
CREATE TABLE `guide_document_title` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(256) NOT NULL,
  `title` varchar(256) DEFAULT NULL,
  `abstract` longtext,
  `type` varchar(256) DEFAULT NULL,
  `source` varchar(256) DEFAULT NULL,
  `pviews` int(11) DEFAULT NULL,
  `collection` int(11) DEFAULT NULL,
  `u_public` tinyint(1) NOT NULL,
  `a_public` tinyint(1) NOT NULL,
  `priority` int(11) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `title_ico_id` int(11) DEFAULT NULL,
  `title_img_id` int(11) DEFAULT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `guide_document_title_title_ico_id_86bbf2b3_fk_img_material_id` (`title_ico_id`),
  KEY `guide_document_title_title_img_id_04db21db_fk_img_material_id` (`title_img_id`),
  KEY `guide_document_title_create_user_id_432888cf_fk_auth_user_id` (`create_user_id`),
  KEY `guide_document_title_write_user_id_0ecd4435_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `guide_document_title_create_user_id_432888cf_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `guide_document_title_title_ico_id_86bbf2b3_fk_img_material_id` FOREIGN KEY (`title_ico_id`) REFERENCES `img_material` (`id`),
  CONSTRAINT `guide_document_title_title_img_id_04db21db_fk_img_material_id` FOREIGN KEY (`title_img_id`) REFERENCES `img_material` (`id`),
  CONSTRAINT `guide_document_title_write_user_id_0ecd4435_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of guide_document_title
-- ----------------------------
INSERT INTO `guide_document_title` VALUES ('8', '8cCfiVNveVTkuAd2HkXRFk', '2020西双版纳新攻略', '测告诉你，绝对不会让你失望的！', null, 'user create', '0', '0', '1', '1', '0', '2020-07-01 06:25:05.972369', '2020-07-01 06:25:51.612389', '1', null, '10', '1');
INSERT INTO `guide_document_title` VALUES ('9', 'krxnqKNrRuNmVm8BxUtC93', '青海甘肃大环线', '寺—青海湖—茶卡（夜宿）\nDay2：\n茶卡盐湖—翡翠湖—大柴旦（夜宿）\nDay3：\n青海雅丹—石油小镇—西千佛洞—敦煌沙漠（夜宿）\nDay4：\n又见敦煌（莫高窟的票没买到）—沙洲夜市—敦煌（夜宿）\nDay5：\n瓜州——张掖七彩丹霞公园—张掖（夜宿）\nDay6：\n祁连山草原—\n阿柔大寺—卓尔山—祁连（夜宿）\nDay7：\n扁都口—岗什卡雪峰—西宁', null, 'user create', '0', '0', '1', '1', '0', '2020-07-01 08:57:25.450676', '2020-07-01 09:02:30.996039', '3', null, '12', '3');

-- ----------------------------
-- Table structure for `img_material`
-- ----------------------------
DROP TABLE IF EXISTS `img_material`;
CREATE TABLE `img_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `alias` varchar(255) NOT NULL,
  `describe` longtext,
  `old_path` varchar(256) DEFAULT NULL,
  `new_path` varchar(256) DEFAULT NULL,
  `file_size` varchar(256) DEFAULT NULL,
  `downs` int(11) NOT NULL,
  `source` varchar(256) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `write_date` datetime(6) NOT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `write_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alias` (`alias`),
  KEY `img_material_create_user_id_1b027e4b_fk_auth_user_id` (`create_user_id`),
  KEY `img_material_write_user_id_810acf92_fk_auth_user_id` (`write_user_id`),
  CONSTRAINT `img_material_create_user_id_1b027e4b_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `img_material_write_user_id_810acf92_fk_auth_user_id` FOREIGN KEY (`write_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of img_material
-- ----------------------------
INSERT INTO `img_material` VALUES ('10', '1.jpg', 'def1a94b-1046-56e0-97b8-8b83939fbc47.jpg', null, 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\media\\OldImgFile', 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\images', '350234', '0', null, '2020-07-01 06:25:05.888145', '2020-07-01 06:25:06.051078', null, null);
INSERT INTO `img_material` VALUES ('11', '2.jpg', '32417902-3701-5921-affa-f76bc6dceb0d.jpg', null, 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\media\\OldImgFile', 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\images', '291426', '0', null, '2020-07-01 06:25:32.595200', '2020-07-01 06:25:32.617265', null, null);
INSERT INTO `img_material` VALUES ('12', '3.jpg', 'e016dc93-0772-5bd2-99b1-831688deff0e.jpg', null, 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\media\\OldImgFile', 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\images', '58933', '0', null, '2020-07-01 08:59:03.771060', '2020-07-01 08:59:03.892884', null, null);
INSERT INTO `img_material` VALUES ('13', '4.jpg', 'bbfe2836-bfab-564f-9968-ba78618d12e8.jpg', null, 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\media\\OldImgFile', 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\images', '65475', '0', null, '2020-07-01 09:01:49.464537', '2020-07-01 09:01:49.479077', null, null);
INSERT INTO `img_material` VALUES ('14', '5.jpg', 'd5d002ab-bfd0-5f08-8c00-885b5409d2c1.jpg', null, 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\media\\OldImgFile', 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\images', '34115', '0', null, '2020-07-01 09:02:00.776482', '2020-07-01 09:02:00.791522', null, null);
INSERT INTO `img_material` VALUES ('15', '08522119983545573.jpg', '84143a90-bb7a-11ea-b3e2-e4029b8604f6_user2.jpg', null, 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\editor\\b64\\84143a90-bb7a-11ea-b3e2-e4029b8604f6_user2.jpg', 'D:\\定做区\\2019-2020年定做\\1216Python基于Django旅游攻略论坛交流系统设计\\travel-master\\static\\media\\editor\\84143a90-bb7a-11ea-b3e2-e4029b8604f6_user2.jpg', '17653', '0', 'user_upload', '2020-07-01 09:09:06.472937', '2020-07-01 09:09:06.473940', '3', '3');

-- ----------------------------
-- Table structure for `temp_tel_code`
-- ----------------------------
DROP TABLE IF EXISTS `temp_tel_code`;
CREATE TABLE `temp_tel_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telphone` bigint(20) DEFAULT NULL,
  `code` int(11) DEFAULT NULL,
  `write_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `temp_tel_code_telphone_a048204c` (`telphone`),
  KEY `temp_tel_code_code_98e26398` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of temp_tel_code
-- ----------------------------
