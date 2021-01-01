-- 2020-12-31 DBMS_07.DCL   ⓒcherryuki(ji)
SHOW USER; -- KIM계정으로 접속 중
SELECT * FROM TAB;
SELECT * FROM DBA_TABLES; --DBA권한이 아니므로 접근 불가
SELECT * FROM USER_TABLES; -- 현 계정이 소유한 테이블 정보
SELECT * FROM ALL_TABLES; --현 계정에서 접근 가능한 테이블 정보
SELECT * FROM ALL_TABLES WHERE TABLE_NAME='EMP';
SELECT * FROM SCOTT.EMP; --현 계정이 소유한 테이블이 아니므로 '소유자명.테이블명'으로 입력해야 함
EXIT; --접속 해제

SHOW USER;
SELECT * FROM SCOTT.EMP; --권한 박탈 후 접근 불가
EXIT;