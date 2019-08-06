# ubuntu16.04安装MySQL
### @time: 20190806  
### @author: Bruce
### @Email: guanzizai1006@gmail.com

## 1. 查看是否已经安装了MySQL

'''
(base) bruce@zhengdz-PowerEdge-T310:~/Downloads/git/dataWhaleWithBruce/mysql$ rpm -qa | grep -i mysql
'''
如果没有输出MySQL-server-5.6 和 MySQL-client-5.6 类似的内容，则表明没有安装。

## 2. 安装MySQL
>官网教程：https://dev.mysql.com/doc/refman/8.0/en/linux-installation-apt-repo.html
>进入官网教程后，可按此步骤进行安装：[点击此处查看步骤](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/)

这里我粘贴一下 Bruce 的操作：
'''
(base) bruce@zhengdz-PowerEdge-T310:/usr/bin$ sudo apt-get update
(base) bruce@zhengdz-PowerEdge-T310:/usr/bin$ dpkg -l | grep mysql | grep ii
(base) bruce@zhengdz-PowerEdge-T310:/usr/bin$ sudo apt-get install mysql-server
'''

然后按下键盘的”下“方向键，输入”root“作为MySQL的密码。坐等安装完成。

## 3. 安装完成
正常安装完毕，会输出安装的内容：
'''
libevent-core-2.0-5 libhtml-template-perl mysql-client-5.7
  mysql-client-core-5.7 mysql-common mysql-server mysql-server-5.7
  mysql-server-core-5.7
'''

再次验证是否安装成功：
'''
(base) bruce@zhengdz-PowerEdge-T310:/usr/bin$ dpkg -l | grep mysql | grep ii
'''
输出内容：
'''
ii  mysql-client-5.7                           5.7.27-0ubuntu0.16.04.1                      amd64        MySQL database client binaries
ii  mysql-client-core-5.7                      5.7.27-0ubuntu0.16.04.1                      amd64        MySQL database core client binaries
ii  mysql-common                               5.7.27-0ubuntu0.16.04.1                      all          MySQL database common files, e.g. /etc/mysql/my.cnf
ii  mysql-server                               5.7.27-0ubuntu0.16.04.1                      all          MySQL database server (metapackage depending on the latest version)
ii  mysql-server-5.7                           5.7.27-0ubuntu0.16.04.1                      amd64        MySQL database server binaries and system database setup
ii  mysql-server-core-5.7                      5.7.27-0ubuntu0.16.04.1                      amd64        MySQL database server binaries
'''

当然，也可以直接查看安装版本，同样可以验证是否成功安装：
'''
(base) bruce@zhengdz-PowerEdge-T310:/usr/bin$ mysqladmin --version
mysqladmin  Ver 8.42 Distrib 5.7.27, for Linux on x86_64
'''

## 4. 测试数据库

>开启数据库
>(base) bruce@zhengdz-PowerEdge-T310:/usr/bin$ mysql -u root -p
>然后输入密码：root（默认为空，但是我安装的过程中就设置了为root这4个字母）
>退出数据库：
>输入exit


ok, 这样就完成了ubuntu16.04下的安装步骤了，可以开始下一个旅程咯~

总结：
参照官网安装步骤，是很方便的做法。大家加油哦~










