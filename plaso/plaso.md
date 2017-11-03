# 플라소(plaso) 사용법

# osfmount 프로그램으로 이미지를 f:에 마운트시킨 다음 아래 명령 실행

log2timeline.exe -z Asia/Seoul timeline.dump f:

# 프리프로세서
log2timeline.exe -z Asia/Seoul -p timeline.dump z:

psort.exe -z Asia/Seoul -o 4n6time_sqlite -w result.db timeline.dump



------------------------------------------------------------------------------------------


select datetime, filename, description 
from log2timeline 
where filename like "%pdf_enc" order by datetime limit 0,1;

------------------------------------------------------------------------------------------

select datetime, filename, description 
from log2timeline 
where datetime < "2015-09-25 15:22:48" order by datetime desc;


------------------------------------------------------------------------------------------
select datetime, filename, description 
from log2timeline 
where datetime > "2015-09-25 15:25:08" order by datetime asc
------------------------------------------------------------------------------------------
--select datetime, filename, description 
from log2timeline 
where datetime > "2015-09-25 15:25:08" order by datetime asc
--where filename like "%pdf_enc" order by datetime desc limit 0,1;
--where datetime < "2015-09-25 15:22:48"
--where datetime < "2015-09-25 15:22:48" and description like "%jandi.com%" order by datetime desc
--where description like "%jandi.com%" order by datetime desc

where datetime > "2015-09-25 15:25:08" order by datetime asc