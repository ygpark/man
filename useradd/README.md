# useradd

## �Ϲ� ���� �����

������ �迭������ �ƹ� �ɼ��� ���� �ʾƵ� Ȩ ���丮 �����ǰ� �� ������

```bash
useradd ������ -m -s /bin/bash -G ftpuser
# -m : Ȩ ���丮 ����
# -s : �� ����
# -G : �׷� ����
```

## Ȩ���丮 ����

```bash
usermod -d ������ġ ���̵�

# ����
usermod -d /var/www/ testuser

```

## ftp ���� ����� ���� �����

```bash
#sudo addgroup ftpuser
sudo useradd -d /var/ftp -s /sbin/nologin test1 -G ftpuser
#sudo usermod -a -G test1 ftpuser
sudo passwd test1
��ȣ�Է�:


```


# vsftpd ���� (���ε� ����)

`/etc/vsftpd.conf` ����

	anonymous_enable=NO		#�͸� �α��� ����
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
	pam_service_name=ftp	# �� �α��� �������� ������ /bin/false �� �ٲٸ� ftp�α����� �ȵǹǷ� �ٲ��ش�.
	secure_chroot_dir=/var/run/vsftpd/empty
	pam_service_name=ftp
	rsa_cert_file=/etc/ssl/private/vsftpd.pem
	user_config_dir=/etc/vsftpd/vsftpd_user_conf # ���� �����Ϸ��� �ʿ���


`/etc/vsftpd_user_conf/` ������ ����� �̸����� ������ ����� �ְ� �Ʒ��� ���� ������ �ش�.


	local_root=/var/ftp
	cmds_allowed=LIST,CWD,STOR,QUIT,PASS,PASV,PWD,ACCT,USER,STAT,NOOP,PORT,NLIST,SITE,ABOR,SYST,TYPE,STRU


# �����

sudo service vsftpd restart