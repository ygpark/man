
# Docker 치트시트


이미지 검색

	sudo docker search ubuntu

이미지 받기

	docker pull ubuntu:latest

이미지 목록 출력하기

	docker images

컨테이너 생성하기

	docker run -i -t --name hello ubuntu /bin/bash

컨테이너 목록 확인하기

	docker ps -a

컨테이너 시작하기

	docker start hello

컨테이너 재시작하기

	docker restart hello

컨테이너에 접속하기

	docker attach hello

컨테이너 정지하기

	docker stop hello

컨테이너 삭제하기

	docker rm hello

이미지 삭제하기

	docker rmi ubuntu:latest

모든 컨테이너 삭제하기

	docker rm `docker ps -aq`


