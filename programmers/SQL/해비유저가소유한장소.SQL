/**
* 프로그래머스 - 해비 유저가 소유한 장소
* URL : https://programmers.co.kr/learn/courses/30/lessons/77487
*/

SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(1) > 1
    );
