CREATE DATABASE IF NOT EXISTS moneymoney;
use moneymoney;
create table IF NOT EXISTS cms
(
  id int unsigned auto_increment
    primary key,
  path varchar(255) not null,
  createdAt datetime not null,
  updatedAt datetime not null,
  status varchar(255) not null
)
  collate=utf8_unicode_ci;

