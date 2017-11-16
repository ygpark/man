# Ubuntu16.04 - Samba 설치

1. 패키지 설치.

```
sudo apt-get install samba cifs-utils
```

2. 설정

```
$ sudo vi /etc/samba/smb.conf

# 맨 아래쪽에 추가한다.

[www]
path = /var/www/html
valid users = user
public = no
writable = yes
```

삼바 로그인용 비밀번호 설정

```
$ sudo smbpasswd -a [유저명]

New SMB password:
Retype new SMB password:
Added user user.
```

3. 서비스 재시작

```
sudo service smbd restart
```
