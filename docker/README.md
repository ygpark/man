
# Docker ġƮ��Ʈ


�̹��� �˻�

	sudo docker search ubuntu

�̹��� �ޱ�

	docker pull ubuntu:latest

�̹��� ��� ����ϱ�

	docker images

�����̳� �����ϱ�

	docker run -i -t --name hello ubuntu /bin/bash

�����̳� ��� Ȯ���ϱ�

	docker ps -a

�����̳� �����ϱ�

	docker start hello

�����̳� ������ϱ�

	docker restart hello

�����̳ʿ� �����ϱ�

	docker attach hello

�����̳� �����ϱ�

	docker stop hello

�����̳� �����ϱ�

	docker rm hello

�̹��� �����ϱ�

	docker rmi ubuntu:latest

��� �����̳� �����ϱ�

	docker rm `docker ps -aq`


