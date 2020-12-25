-- 2020-12-24 DBMS_단일행 함수(1)   ⓒcherryuki(ji)
-- [IV] 단일행 함수
-- 함수: 단일행 함수, 그룹함수([V] 참고)
SELECT HIREDATE, TO_CHAR(HIREDATE, 'YY"년"MM"월"DD"일"') 입사년월일 FROM EMP;
SELECT ENAME, INITCAP(ENAME) FROM EMP; -- 단일행 함수
SELECT SUM(SAL) FROM EMP; --그룹 함수(다중 행의 결과를 하나의 행으로 나타냄) --[V] 그룹함수 참고
SELECT DEPTNO, SUM(SAL) FROM EMP GROUP BY DEPTNO; --그룹 함수(다중 행의 결과를 그룹으로 묶어서 나타냄)
-- EX) 숫자 함수, 문자 함수, 날짜 함수, 형변환 함수, NVL(), ETC

-- 1) 숫자 함수
DESC DUAL; --오라클에서 제공하는 1행 1열짜리 DEUMMY TABLE(∵테이블 입력必)
-- 절대값
SELECT ABS(-9) FROM DUAL; 
-- 내림, 올림, 반올림 -- ROUND(데이터, -e^n); 데이터를 -e(1/10)의 n자리까지 나타냄  
SELECT FLOOR(1234.567) FROM DUAL; --소수점 첫째자리에서 내림(일의 자리까지 나타냄)
SELECT FLOOR(1234.567*10)/10 FROM DUAL; --소수점 둘째자리에서 내림
SELECT TRUNC(1234.567) FROM DUAL; --소수점 첫째자리에서 내림(일의 자리까지 나타냄)
SELECT TRUNC(1234.567, 0) FROM DUAL; --0은 기본값으로 생략 가능(1/10(-e)의 0승(1의 자리)까지 나타냄)
SELECT TRUNC(1234.567, 1) FROM DUAL; -- 소수점 둘째자리 버림(1/10의 1승(소수점 첫째자리)까지 나타냄)
SELECT TRUNC(1234.567, -1) FROM DUAL; -- 일의 자리 버림(1/10의 -1승=10의 자리까지 나타냄)
-- EMP 테이블에서 이름, 급여(십의 자리에서 내림=백의 자리까지 나타냄)
SELECT ENAME, TRUNC(SAL, -2) FROM EMP; 
SELECT CEIL(1234.567) FROM DUAL; -- 소수점 첫째자리에서 올림(일의 자리까지 나타냄)
SELECT ROUND(1234.567) FROM DUAL; -- 소수점 첫째자리에서 반올림(일의 자리까지 나타냄)
SELECT ROUND(1234.567, 1) FROM DUAL; -- 소수점 둘째자리에서 반올림(소수점 첫째자리까지 나타냄)
SELECT ROUND(1234.567, -1) FROM DUAL; --일의 자리에서 반올림(10의자리까지 나타냄)

SELECT FLOOR(10/4) FROM DUAL;
SELECT MOD(9,2) FROM DUAL; -- 나머지 연산
SELECT MOD('9', 2) FROM DUAL; -- 9/2의 나머지
-- 홀수달에 입사한 직원들의 모든 필드
SELECT * FROM EMP WHERE MOD(TO_CHAR(HIREDATE, 'MM'),2)=1;

-- 2) 문자 처리 함수
SELECT UPPER('abcABC') FROM DUAL; --전부 대문자로
SELECT LOWER('abcABC') FROM DUAL; --전부 소문자로
SELECT INITCAP('abcABC') FROM DUAL; --첫글자만 대문자(이니셜 캡), 뒤에는 소문자로
-- JOB이 MANAGER인 직원의 모든 필드
SELECT * FROM EMP WHERE UPPER(JOB)='MANAGER';
SELECT EMPNO, INITCAP(ENAME) FROM EMP;
-- 문자 연결
SELECT 'AB'||'CD'||'EF'||'GH' FROM DUAL;
SELECT CONCAT(CONCAT('AB','CD'),CONCAT('EF','GH')) FROM DUAL;
--- XXX는 XX다(ENAME은 JOB이다)
SELECT ENAME||'는 '||JOB||'이다' FROM EMP;
SELECT CONCAT(CONCAT(ENAME, '는 '), CONCAT(JOB, '이다')) FROM EMP;
-- SUBSTR(STR, 시작위치, 문자 수) --첫 위치가 1부터(JAVA는 0부터)
-- SUBSTRB(STR, 시작위치, 문자 바이트 수)
SELECT SUBSTR('WELCOME TO ORACLE', 3, 2) FROM DUAL; --LC(3번째 부터 2글자)
SELECT SUBSTRB('WELCOME TO ORACLE', 3, 2) FROM DUAL; --LC(3번째BYTE부터 2BYTE) --영어일 경우 1글자=1BYTE여서 동일
SELECT SUBSTR('메리크리스마스', 4, 3) FROM DUAL; --리스마(4번째 글자부터 3글자)
SELECT SUBSTRB('메리크리스마스', 4, 3) FROM DUAL; --리(4번째BYTE부터 3BYTE)
-- 영어는 한 글자(문자)=1BYTE, 한글은 한 글자(문자)=3BYTE 
-- 9월에 입사한 사원의 모든 필드 81/01/01
SELECT * FROM EMP WHERE SUBSTR(HIREDATE, 4, 2)='09';
SELECT SUBSTR('02-123-0000', -4, 4) FROM DUAL; --전화번호 뒷 4자리
-- 글자 수 세는 방법
--  1  2  3  4  5  6  (앞에서부터 셀 때)
-- -6 -5 -4 -3 -2 -1  (뒤에서부터 셀 때)

-- 9일에 입사한 사원의 모든 필드 
SELECT * FROM EMP WHERE SUBSTR(HIREDATE, -2, 2)='09';
SELECT LENGTH('ORACLE') FROM DUAL; --문자 수:4
SELECT LENGTHB('ORACLE') FROM DUAL; --BYTE수: 4 (영어는 1문자=1BYTE)
SELECT LENGTH('오라클') FROM DUAL; --문자 수:3
SELECT LENGTHB('오라클') FROM DUAL; --BYTE수: 9 (한글은 1문자=3BYTE)
DESC DEPT;
-- INSTR(STR, 찾을 글자); STR에서 찾을 글자의 첫 위치(1부터 카운트), 없으면 0출력
-- INSTR(STR, 찾을 글자, 시작 위치); STR에서 시작위치부터 찾아서 찾을 글자의 위치(1부터 카운트), 없으면 0
SELECT INSTR('ABCABC', 'B') FROM DUAL; --2
SELECT INSTR('ABCABC', 'B', 3) FROM DUAL; --5
-- 9월에 입사한 사원 정보(INSTR 이용)
SELECT * FROM EMP WHERE INSTR(HIREDATE, '09')=4;
-- 9일에 입사한 사원 정보(INSTR 이용)
SELECT * FROM EMP WHERE INSTR(HIREDATE, '09')=7;
-- LPADE(문자, 자리수, '*'); 문자와 *를 자리수 만큼 확보(*은 문자 왼쪽(L)으로 채움)
SELECT LPAD('ORACLE', 10, '#') FROM DUAL; --####ORACLE
SELECT RPAD('ORACLE', 10, '*') FROM DUAL; --ORACLE**** --오른쪽(R) 빈자리를 *로 채움
SELECT ENAME, LPAD(SAL, 6, '*') FROM EMP;
-- 사번, 이름은 첫문자만 출력하고 나머지는 *로 출력(S****)
SELECT EMPNO, RPAD(SUBSTR(ENAME, 1, 1), LENGTH(ENAME), '*') NAME FROM EMP;
-- 사번, 이름(S*****), 입사일(80/12/**) 출력
SELECT EMPNO 사번, RPAD(SUBSTR(ENAME, 1, 1), LENGTH(ENAME), '*') 이름, 
    RPAD(SUBSTR(HIREDATE, 1, 6), LENGTH(HIREDATE), '*') 입사년월일 FROM EMP;
-- 사번, 이름(****H), 입사일(80/12/**) 출력
SELECT EMPNO, LPAD(SUBSTR(ENAME, -1, 1), LENGTH(ENAME), '*') 이름, 
    RPAD(SUBSTR(HIREDATE, 1, 6), LENGTH(HIREDATE), '*') 입사년월일 FROM EMP;
-- 이름의 세번째 자리가 R인 사원 출력(INSTR, SUBSTR, LIKE)
SELECT * FROM EMP WHERE INSTR(ENAME, 'R')=3;
SELECT * FROM EMP WHERE SUBSTR(ENAME, 3, 1)='R';
SELECT * FROM EMP WHERE ENAME LIKE '__R%';
SELECT TRIM('        ORACLE DB    ') FROM DUAL; --앞 뒤의 SPACE 없앰(문자 사이 SPACE는 그대로)
SELECT LTRIM('       ORACLE DB    ') FROM DUAL;  --왼쪽(앞) SPACE 없앰
SELECT RTRIM('       ORACLE DB    ') FROM DUAL;  --오른쪽(뒤) SPACE 없앰
SELECT REPLACE(ENAME, 'A', 'XX') FROM EMP;

-- 3) 날짜 관련 예약어, 함수
SELECT SYSDATE FROM DUAL; --현재(날짜 및 시간)
SELECT TO_CHAR(SYSDATE, 'YY-MM-DD HH24:MI:SS') "현재 날짜 및 시각" FROM DUAL;
SELECT SYSDATE-1 어제, SYSDATE 오늘, SYSDATE+1 내일 FROM DUAL; --날짜형도 연산 가능
-- 14일 후
SELECT SYSDATE+14 FROM DUAL;

-- 이름, 입사일, 근무일자 출력
SELECT ENAME, HIREDATE, TRUNC(SYSDATE-HIREDATE) 근속일수 FROM EMP;
SELECT ENAME, HIREDATE, FLOOR(SYSDATE-HIREDATE) 근속일수 FROM EMP;
-- 이름, 입사일, 근무주수, 근무년수 출력
SELECT ENAME, HIREDATE, TRUNC((SYSDATE-HIREDATE)/7) 근무주수, 
    FLOOR((SYSDATE-HIREDATE)/365) 근무년수 FROM EMP;
-- MONTHS_BETWEEN(): 특정한 두 시점 사이의 개월 수
-- 이름, 입사일, 근무월수(MONTHS_BETWEEN 함수 사용)
SELECT ENAME, HIREDATE, TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE)) 근무월수 FROM EMP;
-- ADD_MONTHS(특정날짜, 개월 수): 특정한 날짜로부터 몇 개월 후의 시점
-- 이름, 입사일, 수습기간 만료일(수습기간은 6개월)
SELECT ENAME, HIREDATE, ADD_MONTHS(HIREDATE, 6) "수습기간 만료일" FROM EMP;
-- NEXT_DAY(특정날짜, 'E요일'): 특정날짜로부터 처음 도래하는 E요일
SELECT NEXT_DAY(SYSDATE, '토') FROM DUAL; 
SELECT NEXT_DAY(SYSDATE, '일요일') FROM DUAL;
-- LAST_DAY(특정날짜): 특정날짜가 속한 달의 말일
SELECT LAST_DAY(SYSDATE) FROM DUAL;
-- 이름, 입사일, 월급날(월급은 말일)
SELECT ENAME, HIREDATE, LAST_DAY(HIREDATE) "첫 월급날" FROM EMP;
-- ROUND: 날짜 반올림
SELECT ROUND(SYSDATE-30, 'YEAR') FROM DUAL; --결과: 가까운 년도 1월 1일
SELECT ROUND(SYSDATE-30, 'MONTH') FROM DUAL; --결과: 가까운 월 1일 --EX: 15일까지 당월, 16일부터 익월
SELECT ROUND(SYSDATE, 'DAY') FROM DUAL; --결과: 가까운 일요일
SELECT TO_CHAR(ROUND(SYSDATE), 'YY-MM-DD HH24:MI:SS') FROM DUAL; -- 결과: 가까운 일 0시
SELECT ROUND(SYSDATE) FROM DUAL; --결과: 가까운 일(0시) EX) 오전일 경우 당일(0시), 오후일 경우 익일(0시)
-- TRUNC: 날짜 버림
SELECT TRUNC(SYSDATE-30, 'YEAR') FROM DUAL; --결과: 당해년도 1월 1일(지난 1월 1일)
SELECT TRUNC(SYSDATE-30, 'MONTH') FROM DUAL; --결과: 당월 1일(지난 1일)
SELECT TRUNC(SYSDATE, 'DAY') FROM DUAL; --결과: 지난 일요일(해당일자가 일요일일 경우 해당일자 출력)
SELECT TO_CHAR(TRUNC(SYSDATE), 'YY-MM-DD HH24:MI:SS') FROM DUAL; --결과: 지난 0시(당일 0시)
SELECT TRUNC(SYSDATE) FROM DUAL; --결과: 당일(0시)

-- 연습문제
-- EX1. 이름, 입사일, 입사일이 속한 달의 1일
SELECT ENAME, HIREDATE, TRUNC(HIREDATE, 'MONTH') FROM EMP;
-- EX2. 이름, 입사일, 월급날(25일) - 25일 전 입사면 입사한 달 25일, 25일 이후면 다음 달 25일
SELECT ENAME, HIREDATE, ROUND(HIREDATE-9, 'MONTH')+24 "첫 월급날" FROM EMP;
-- ROUND(해당날짜, 'MONTH')의 경우 15일까지는 당월 1일, 16일부터는 익월 1일로 출력됨 
-- 24일까지 입사하면 당월로 표시되게 입사일-9일(24-9=15), 급여일은 +24일(1+24=25)로 계산(24일이 월급날일 경우 -8, +23)
-- EX3. 이름, 입사일, SAL(월급), 이때까지 받은 월급 합
SELECT ENAME, HIREDATE, SAL, TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE))*SAL "월급의 합" FROM EMP;
-- EX4. 이름, 입사일, SAL, COMM, 이때까지 받은 연봉(SAL*12+COMM)
SELECT ENAME, HIREDATE, SAL, COMM, TRUNC((SYSDATE-HIREDATE)/365)*(SAL*12+NVL(COMM,0)) "연봉의 합" FROM EMP;