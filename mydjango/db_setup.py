drop database if exists mydjango_db;
create database mydjango_db CHARACTER SET utf8 COLLATE utf8_general_ci;
grant all on mydjango_db.* to 'mydjango'@'localhost' identified by 'mydjango@123#';
