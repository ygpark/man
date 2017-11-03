--SELECT * FROM log WHERE ip='218.53.216.47' ORDER BY date desc;


SELECT log.ip, MIN(log.date) as first, MAX(log.date) as last, COUNT(*) as no, log.status, log.log, whois.country, whois.isp, whois.user 
FROM log
LEFT JOIN whois ON log.ip=whois.ip
WHERE country='KR' and (log.log like '%����%' or log.log like '%����%')
GROUP BY log.ip
ORDER BY last desc;

/*
SELECT log.date, log.ip, log.status, log.log, whois.country, whois.isp, whois.user 
FROM log
LEFT JOIN whois ON log.ip=whois.ip
WHERE country='KR' and (log.log like '%����%' or log.log like '%����%')
ORDER BY date desc;
*/