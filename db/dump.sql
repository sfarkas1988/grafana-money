CREATE DATABASE IF NOT EXISTS grafana_money;
use grafana_money;
create table IF NOT EXISTS sales
(
  id int unsigned auto_increment primary key,
  date date not null,
  floatDate date not null,
  category varchar(255) null,
  name varchar(255) null,
  purposeOfPayment varchar(255) null,
  account varchar(255) not null,
  bank varchar(255) null,
  amount decimal(12,2) not null,
  currency varchar(255) null
)
  collate=utf8_unicode_ci;
