#Ubuntu 16.04 LTS - Apache, PHP, Mysql 설치

1. 패키지 설치

mysql은 설치중 비밀번호를 물어본다

```
sudo apt-get install mysql-server mysql-client
sudo apt-get install apache2
sudo apt-get install php libapache2-mod-php php-xml php-gd php-mysql
```

2. 서비스 재시작

```
/etc/init.d/apache2 restart
/etc/init.d/mysql restart
```

3. 설치 확인
```
netstat -nlp

dpkg -l | grep apache2
dpkg -l |grep php
```
