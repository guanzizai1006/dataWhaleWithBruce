# Task 1 的2个MySQL的小任务
> 上一节，我们完成了环境的搭建，这里，我们完成第一节的内容。


## 第一个任务，搜索邮箱内容

- 首先，进入MySQL；
'''
(base) bruce@zhengdz-PowerEdge-T310:/usr/bin$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 5.7.27-0ubuntu0.16.04.1 (Ubuntu)
Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
'''

- 然后，创建名字为 TASK1 的数据库；
'''
mysql> CREATE DATABASE TASK1;
Query OK, 1 row affected (0.00 sec)
'''

- 进入该数据库；
'''
mysql> use TASK1;
Database changed
'''

- 此数据库下，创建名为 Person 的表, 并添加内容；
'''
mysql> CREATE TABLE IF NOT EXISTS Person (Id int, Email varchar(255));
Query OK, 0 rows affected (0.25 sec)
mysql> insert into Person (Id, Email) values ('1', 'a@b.com');
Query OK, 1 row affected (0.05 sec)
mysql> insert into Person (Id, Email) values ('2', 'c@d.com');
Query OK, 1 row affected (0.08 sec)
mysql> insert into Person (Id, Email) values ('3', 'a@b.com');
Query OK, 1 row affected (0.04 sec)
'''


- 数据库中，‘group by’来完成数据的选择；
'''
mysql> select Email from Person group by Emain having count(Email)>1;
ERROR 1054 (42S22): Unknown column 'Emain' in 'group statement'

mysql> select Email from Person group by Email having count(Email)>1;
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
1 row in set (0.00 sec)
'''



## 第二个任务，搜索国家信息

- 首先，进入MySQL；
'''
(base) bruce@zhengdz-PowerEdge-T310:/usr/bin$ mysql -u root -p;
'''

- 创建名为 world_demo 的数据库；
'''
mysql> create database world_demo charset utf8;
Query OK, 1 row affected (0.02 sec)
'''

- 显示所有的数据库；
'''
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| TASK1              |
| mysql              |
| performance_schema |
| sys                |
| world_demo         |
+--------------------+
6 rows in set (0.00 sec)
'''

- 选定名为 world_demo 的数据库；
'''
mysql> use world_demo
Database changed
'''

- 该数据库下，创建一个表，命名为 world；
'''
mysql> create table world(
    -> cntinent varchar(100) not null,
    -> area int not null,
    -> population int not null,
    -> gdp int not null
    -> );
Query OK, 0 rows affected (0.52 sec)
'''


- 显示所有的表的名称；
'''
mysql> show tables;
mysql> alter table world add name varchar(100) not null primary key; 
'''

- Bruce插入数据
'''
mysql> insert into world values('Afghanistan',652230,25500100,20343000,'Asia');
Query OK, 1 row affected (0.06 sec)
'''
- 显示这个名为 world 的表的内容；
'''
mysql> select * from world;
+-------------+--------+------------+----------+------+
| cntinent    | area   | population | gdp      | name |
+-------------+--------+------------+----------+------+
| Afghanistan | 652230 |   25500100 | 20343000 | Asia |
+-------------+--------+------------+----------+------+
1 row in set (0.00 sec)
'''

- 选择符合该条件下的内容；
'''
mysql> select cntinent, area, population
    -> from world
    -> group by cntinent, area, population
    -> having population > 12960000;
+-------------+---------+------------+
| cntinent    | area    | population |
+-------------+---------+------------+
| Afghanistan |  652230 |   25500100 |
| Algeria     | 2381741 |   37100000 |
| bruce       | 2345235 |  123413421 |
+-------------+---------+------------+
3 rows in set (0.10 sec)
'''

#### 总结：至此，完成Task 1 的内容，请多多熟悉基本语句和方法，这样 操作就更加熟练啦~加油~~











