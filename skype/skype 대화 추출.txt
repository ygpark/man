
-- 그룹채팅
SELECT DISTINCT datetime(m.timestamp, 'unixepoch', 'localtime') as 'Date Time', m.author as 'User Name', m.from_dispname as 'Display Name', m.body_xml as 'Chat Message'
FROM messages m
JOIN conversations c ON c.id = m.convo_id
WHERE c.type = 2 AND
m.body_xml NOT NULL
and m.author = 'live:intelskype12'
ORDER BY m.timestamp ASC

-- 개인 채팅
SELECT DISTINCT datetime(m.timestamp, 'unixepoch', 'localtime') as 'Date Time', m.author as 'User Name', m.from_dispname as 'Display Name', m.body_xml as 'Chat Message'
FROM messages m
JOIN conversations c ON c.id = m.convo_id
WHERE m.body_xml NOT NULL AND
c.identity LIKE '%YOUR.BUDDY.NAME.HERE%' --case insensitive
ORDER BY m.timestamp ASC


-- 대화 검색
SELECT DISTINCT datetime(m.timestamp, 'unixepoch', 'localtime') as 'Date Time', m.author as 'User Name', m.from_dispname as 'Display Name', m.body_xml as 'Chat Message'
FROM messages m
JOIN conversations c ON c.id = m.convo_id
WHERE c.identity = 'YOUR.BUDDY.NAME.HERE' AND
m.body_xml NOT NULL AND
m.body_xml LIKE '%YOUR.SEARCHED.WORD.HERE%' --case insensitive
ORDER BY m.timestamp ASC



-- 둘 명의 대화내역 보기
SELECT DISTINCT datetime(m.timestamp, 'unixepoch', 'localtime') as 'Date Time', m.author as 'User Name', m.from_dispname as 'Display Name', m.body_xml as 'Chat Message' FROM
messages m
JOIN conversations c ON c.id = m.convo_id
WHERE m.body_xml NOT NULL
and c.identity = 'live:intelskype12'
ORDER BY m.timestamp ASC
