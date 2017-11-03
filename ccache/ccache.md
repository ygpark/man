# ccache

빌드 시간을 짧게 줄여주는 프로그램

# 설치

	if [ "$PATH_ORI" == "" ] ; then
		export PATH_ORI=$PATH
	fi

	export PATH=/usr/lib/ccache:$PATH_ORI

