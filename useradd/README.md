# useradd

## 일반 계정 만들기

레드햇 계열에서는 아무 옵션을 주지 않아도 홈 디렉토리 생성되고 쉘 설정됨

```bash
useradd 계정명 -m -s /bin/bash -G ftpuser
# -m : 홈 디렉토리 생성
# -s : 쉘 지정
# -G : 그룹 지정
```

## 홈디렉토리 변경

```bash
usermod -d 폴더위치 아이디

# 예시
usermod -d /var/www/ testuser

```

## ftp 전용 사용자 계정 만들기

```bash
#sudo addgroup ftpuser
sudo useradd -d /var/ftp -s /sbin/nologin test1 -G ftpuser
#sudo usermod -a -G test1 ftpuser
sudo passwd test1
암호입력:


```


# vsftpd 설정 (업로드 전용)

`/etc/vsftpd.conf` 수정

	anonymous_enable=NO		#익명 로그인 막기
	local_enable=YES
	write_enable=YES
	local_umask=022
	dirmessage_enable=YES
	use_localtime=YES
	xferlog_enable=YES
	connect_from_port_20=YES
	chroot_local_user=YES
	allow_writeable_chroot=YES
	chroot_local_user=YES
	chroot_list_enable=YES
	chroot_list_file=/etc/vsftpd.chroot_list
	#pam_service_name=vsftpd
	pam_service_name=ftp	# 쉘 로그인 막으려고 설정을 /bin/false 로 바꾸면 ftp로그인이 안되므로 바꿔준다.
	secure_chroot_dir=/var/run/vsftpd/empty
	pam_service_name=ftp
	rsa_cert_file=/etc/ssl/private/vsftpd.pem
	user_config_dir=/etc/vsftpd/vsftpd_user_conf # 개인 설정하려면 필요함


`/etc/vsftpd_user_conf/` 폴더에 사용자 이름으로 파일을 만들어 주고 아래와 같이 권한을 준다.


	local_root=/var/ftp
	cmds_allowed=LIST,CWD,STOR,QUIT,PASS,PASV,PWD,ACCT,USER,STAT,NOOP,PORT,NLIST,SITE,ABOR,SYST,TYPE,STRU


# 재시작

sudo service vsftpd restart