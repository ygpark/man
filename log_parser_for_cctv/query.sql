/*
--몇 군데 카메라에 접속했나
select external_ip, cam_ip, MIN(date) as first, MAX(date) as last, count(*) as cnt, log
      from log 
      where external_ip='222.102.170.2'
      group by external_ip, cam_ip
      order by external_ip asc, cnt desc;
*/

/*
--몇 군데 카메라에 접속했나, 모든 카메라
SELECT external_ip, COUNT(cam_ip) as cam_num
FROM (select external_ip, cam_ip, MIN(date) as first, MAX(date) as last, count(*) as cnt, log
      from log 
      --where external_ip='222.102.170.2'
      group by external_ip, cam_ip
      order by external_ip asc, cnt desc)
--where external_ip='222.102.170.2'
GROUP by external_ip
ORDER by cam_num desc
--*/











--log_korea.csv 만들기
/*
select cam_ip, date, external_ip, log, device_name, isp from log as a
left join whois as b on a.external_ip= b.ip
where b.country='KR' and a.date > '2017-05-20 00:00:00';
*/

-- 후이즈 만들기
/*
create table whois_external (id integer primary key autoincrement, ip, country, isp, user);

.separator ','
drop table tmp;
create table tmp (ip, country, isp, user);
.import whois.csv tmp

insert into whois_external (ip, country, isp, user) select ip, country, isp, user from tmp;
*/

-- 후이즈 만들기
/*
create table whois_owner (id integer primary key autoincrement, ip, country, isp, user);
.separator ','
drop table tmp;
create table tmp (ip, country, isp, user);
--UTF-8 으로 변경
.import whois_cam_ip.csv tmp
select * from tmp limit 100;
insert into whois_owner (ip, country, isp, user) select ip, country, isp, user from tmp;
*/
---------------------------------------------------------------------------------------


-- 통합 후이즈 만들기 (주인집 중복 제거)
/*
insert into whois (ip, country, isp, user) 
select ip, country, isp, user from whois_owner 
where ip is not '112.163.11.89' 
and ip is not '119.204.167.7'
and ip is not '121.156.172.73'
and ip is not '121.173.13.42'
and ip is not '106.245.43.173'
and ip is not '211.198.199.213'
and ip is not '220.82.129.177'
---------------------------------------------------------------------------------------





--drop table whois;

--insert into whois (ip, country, isp, user) select ip, country, isp, user from whois_tmp;

--create table whois (id integer primary key autoincrement, ip, country, isp, user);

--select * from whois;

--select * from whois; 

--select * from whois where ip='223.62.215.82'


/* log 외부 IP 주소 추출 */

--select distinct external_ip from log;
--select external_ip from log

--select * from whois where country='KR';


-- q1 테이블 -- 침입자 통신자료 올릴 것
/*
create table q1 as
select external_ip, date, isp, user 
from log 
left join whois_external on log.external_ip = whois_external.ip
where whois_external.country='KR' and log.date > "2017-05-22 00:00:00"
group by log.external_ip
order by log.date desc;
*/


-- q2 테이블
/*
create table q2 as
select ip, '2017-08-18 17:00:00', '2017-08-18 17:00:00', isp, user
from whois_owner;
*/

-- q3 테이블 -- 외부 IP에서 주인집이랑 같은거
/*
create table q3 as
select * from whois_external as a
left join whois_owner as b on a.ip=b.ip
where b.ip not null; 
*/

/*
select external_ip, date, isp, user
from whois 
left join log on whois.ip = log.external_ip
where whois.country='KR'
group by whois.ip
*/