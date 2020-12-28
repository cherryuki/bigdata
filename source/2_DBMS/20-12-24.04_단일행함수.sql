-- 2020-12-24 DBMS_05.단일행 함수   ⓒcherryuki(ji)
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

-- 2020-12-28 DBMS_단일행 함수   ⓒcherryuki(ji)
-- 4) 형변환 함수
-- TO_CHAR(날짜, 패턴); 날짜값을 패턴에 맞게 문자형으로 변환
    -- YY(년도) MM(월) MON(N월 ex:12월) DD(일) DY(요일)
    -- HH24(0~23시) AM(오전/오후) HH(0~11시) MI(분) SS(초)
SELECT ENAME, TO_CHAR(HIREDATE, 'YYYY-MM-DD') FROM EMP;
SELECT ENAME, TO_CHAR(HIREDATE, 'YYYY"년"MM"월"DD"일" DY"요일"') FROM EMP;
SELECT ENAME, TO_CHAR(SYSDATE, 'YY"년"MONDD"일" AMHH"시"MI"분"SS"초"') FROM EMP;

-- TO_CHAR(숫자, 패턴); 숫자값을 패턴에 맞게 문자로 형변환
    -- 패턴 내 0: 자릿수, 자릿수가 맞지 않으면 0으로 채움
    -- 패턴 내 9: 자릿수, 자릿수가 맞지 않으면 채우지 않음(자바에서는 #)
    -- 패턴 내 $: 통화 단위, $가 숫자 앞에 붙음
    -- 패턴 내 L: 지역통화 단위가 숫자 앞에 붙음
SELECT ENAME, TO_CHAR(SAL, 'L999,999') SAL FROM EMP;
SELECT ENAME, TO_CHAR(SAL, '$9,999') SAL FROM EMP;
SELECT ENAME, TO_CHAR(SAL, '$000,000') SAL FROM EMP;

-- TO_DATE(문자, 패턴); '81/01/01' 문자를 패턴에 맞게 날짜형으로 형변환
-- 81/05/01~83/05/01 사이에 입사한 직원 출력
SELECT * FROM EMP
    WHERE HIREDATE BETWEEN '81/05/01' AND '83/05/01';
SELECT * FROM EMP 
    WHERE HIREDATE BETWEEN TO_DATE('19810501', 'YY/MM/DD') AND TO_DATE('19830501', 'YY/MM/DD'); --연도 4자리로
-- 2020년 11월 30일부터 현재까지 날짜수를 출력(시스템의 날짜형 포맷 모름)
SELECT TRUNC(SYSDATE-TO_DATE('2020/11/30', 'YYYY/MM/DD')) 경과일 FROM DUAL; --28일(내림)
SELECT CEIL(SYSDATE-TO_DATE('2020-11-30', 'YYYY-MM-DD')) 경과일 FROM DUAL; --29일(올림)
SELECT * FROM EMP WHERE TO_CHAR(HIREDATE, 'YY/MM/DD') BETWEEN '81/05/01' AND '83/05/01';

-- TO_NUMBER(문자, 패턴); 문자를 패턴에 맞게 숫자형으로 변환
SELECT TO_NUMBER('1,000', '9,999') FROM DUAL;
SELECT TO_NUMBER('1,000', '9,999')*1.1 FROM DUAL;

-- 5) NULL 관련 함수: NVL(NULL일 수도 있는 데이터, NULL이면 대신할 값) --매개변수 2개는 타입이 일치해야 함
-- 사원 이름, 직속 상사의 이름(직속 상사가 없으면 CEO 출력)
SELECT W.ENAME "사원명", NVL(M.ENAME, 'CEO') "직속 상사명" 
    FROM EMP W, EMP M
    WHERE W.MGR=M.EMPNO(+);
-- 사원 이름, 직속 상사의 사번(직속 상사가 없으면 CEO 출력)
SELECT ENAME, NVL(TO_CHAR(MGR), 'CEO') MGR FROM EMP; --CEO를 숫자로 바꿀 수 없으므로 MGR(숫자)를 문자로 형변환

-- 6) DECODE(데이터, 값1, 결과1, 값2, 결과2, ..., 값N, 결과N, 그 외 결과)
-- 이름, 부서번호, 부서이름
SELECT ENAME, EMPNO, DNAME 
    FROM EMP E, DEPT D
    WHERE E.DEPTNO=D.DEPTNO; --EQUI JOIN
SELECT ENAME, DEPTNO, 
    DECODE(DEPTNO, 10, 'ACCOUNTING', 20, 'RESEARCH', 30, 'SALES', 40, 'OPERATIONS', 'ETC') DNAME 
    FROM EMP;
-- DECODE와 유사하게 사용할 수 있는 CASE
SELECT ENAME, DEPTNO,
    CASE WHEN DEPTNO=10 THEN 'ACCOUNTING'
         WHEN DEPTNO=20 THEN 'RESEARCH'
         WHEN DEPTNO=30 THEN 'SALES'
         WHEN DEPTNO=40 THEN 'OPERATIONS'
         ELSE 'ETC'
    END AS "DNAME" FROM EMP;
SELECT ENAME, DEPTNO,
    CASE DEPTNO WHEN 10 THEN 'ACCOUNTING'
                WHEN 20 THEN 'RESEARCH'
                WHEN 30 THEN 'SALES'
                WHEN 40 THEN 'OPERATIONS'
        ELSE 'ETC'
    END AS "DNAME" FROM EMP;

-- 이름, 급여, 인상 예정 급여 출력(DECODE, CASE)
  -- JOB에 따른 인상율: 'ANALYST' 10% 인상, 'MANAGER' 20% 인상, 'PRESIDENT' 30% 인상, 'SALESMAN' 40% 인상, 'CLERK' 인상X
SELECT ENAME, SAL "현재 급여", 
    DECODE(JOB, 'ANALYST', SAL*1.1, 'MANAGER', SAL*1.2, 
                'PRESIDENT', SAL*1.3, 'SALESMAN', SAL*1.4, 'CLERK', SAL) "인상 예정 급여" 
    FROM EMP;
SELECT ENAME, SAL "현재 급여", 
    DECODE(JOB, 'ANALYST', SAL*1.1, 'MANAGER', SAL*1.2, 
                'PRESIDENT', SAL*1.3, 'SALESMAN', SAL*1.4, SAL) "인상 예정 급여" 
    FROM EMP;
SELECT ENAME, SAL "현재 급여", 
    CASE JOB WHEN 'ANALYST' THEN SAL*1.1
             WHEN 'MANAGER' THEN SAL*1.2
             WHEN 'PRESIDENT' THEN SAL*1.3
             WHEN 'SALESMAN' THEN SAL*1.4
             WHEN 'CLERK' THEN SAL
    END AS "인상 예정 급여" FROM EMP;

-- 7) 그 외: EXTRACT, LEVEL별 출력
SELECT EXTRACT(YEAR FROM HIREDATE) YEAR FROM EMP;
SELECT TO_CHAR(HIREDATE, 'YYYY') YEAR FROM EMP;
SELECT EXTRACT(MONTH FROM HIREDATE) MONTH FROM EMP;
SELECT TO_CHAR(HIREDATE, 'MM') MONTH FROM EMP;
-- LEVEL, START WITH(최상위 레벨의 조건), CONNECT BY PRIOR(상하레벨 연결 조건)
SELECT LEVEL, LPAD(' ', LEVEL*2)||ENAME, MGR FROM EMP
    START WITH MGR IS NULL
    CONNECT BY PRIOR EMPNO=MGR;
    
-- <총 연습문제>
-- 1. 현재 날짜를 출력하고 TITLE에 “Current Date”로 출력하는 SELECT 문장을 기술하시오.
SELECT SYSDATE "Current Date" FROM DUAL;
-- 2. EMP 테이블에서 현재 급여에 15%가 증가된 급여를 계산하여,
-- 사원번호,이름,업무,급여,증가된 급여(New Salary),증가액(Increase)를 출력하는 SELECT 문장
SELECT EMPNO, ENAME, JOB, SAL, SAL*1.15 "New Salary", SAL*0.15 "Increase" FROM EMP;
--3. 이름, 입사일, 입사일로부터 6개월 후 돌아오는 월요일 구하여 출력하는 SELECT 문장을 기술하시오.
SELECT ENAME, HIREDATE, NEXT_DAY(ADD_MONTHS(HIREDATE, 6), '월') "6개월 후 월요일" FROM EMP;
--4. 이름, 입사일, 입사일로부터 현재까지의 개월수, 급여, 입사일부터 현재까지의 받은 급여의 총계를 출력
SELECT ENAME, HIREDATE, TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE)) 근속월수, 
    SAL, SAL*TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE)) "급여 총계" FROM EMP;
--5. 모든 사원의 이름과 급여(15자리로 출력 좌측의 빈 곳은 “*”로 대치)를 출력
SELECT ENAME, LPAD(SAL, 15, '*') 급여 FROM EMP;
--6. 모든 사원의 정보를 이름,업무,입사일,입사한 요일을 출력하는 SELECT 문장을 기술하시오.
SELECT ENAME, JOB, HIREDATE, TO_CHAR(HIREDATE, 'DY"요일"') "입사한 요일" FROM EMP;
--7. 이름의 길이가 6자 이상인 사원의 정보를 이름,이름의 글자수,업무를 출력
SELECT ENAME, LENGTH(ENAME), JOB
    FROM EMP
    WHERE LENGTH(ENAME)>=6;
--8. 모든 사원의 정보를 이름, 업무, 급여, 보너스, 급여+보너스를 출력
SELECT ENAME, JOB, SAL, COMM, SAL+NVL(COMM,0) "급여+보너스" FROM EMP;
-- 9.사원 테이블의 사원명에서 2번째 문자부터 3개의 문자를 추출하시오. 
SELECT SUBSTR(ENAME, 2, 3) FROM EMP;
--10. 사원 테이블에서 입사일이 12월인 사원의 사번, 사원명, 입사일을 검색하시오. 
SELECT EMPNO, ENAME, HIREDATE FROM EMP
    WHERE TO_CHAR(HIREDATE, 'MM')=12;
SELECT EMPNO, ENAME, HIREDATE FROM EMP
    WHERE EXTRACT(MONTH FROM HIREDATE)=12;
--11. 다음과 같은 결과를 검색할 수 있는 SQL 문장을 작성하시오
--EMPNO		ENAME		급여
--7369		SMITH		*******800
--7499		ALLEN		******1600
--7521		WARD		******1250
SELECT EMPNO, ENAME, LPAD(SAL, 10, '*') 급여 FROM EMP;
-- 12. 다음과 같은 결과를 검색할 수 있는 SQL 문장을 작성하시오
-- EMPNO	 ENAME 	입사일
-- 7369	  SMITH		1980-12-17
-- ….
SELECT EMPNO, ENAME, TO_CHAR(HIREDATE, 'YYYY-MM-DD') 입사일 FROM EMP;
--13. 사원 테이블에서 부서 번호가 20인 사원의 사번, 이름, 직무, 급여를 출력하시오.
    --(급여는 앞에 $를 삽입하고3자리마다 ,를 출력한다)
SELECT EMPNO, ENAME, JOB, TO_CHAR(SAL, '$9,999') 급여 
    FROM EMP 
    WHERE DEPTNO=20;
-- 14. 사원 테이블에서 급여에 따라 사번, 이름, 급여, 등급을 검색하는 SQL 문장을 작성 하시 오.
-- 급여가 0~1000 E / 1001~2000 D / 2001~3000 C / 3001~4000 B / 4001~5000 A
SELECT EMPNO, ENAME, SAL, 
    DECODE(TRUNC((SAL-1)/1000), 0, 'E', 1, 'D', 2, 'C', 3, 'B', 4, 'A') 등급
    FROM EMP;
SELECT EMPNO, ENAME, SAL,
    CASE TRUNC((SAL-1)/1000) WHEN 0 THEN 'E'
                             WHEN 1 THEN 'D'
                             WHEN 2 THEN 'C'
                             WHEN 3 THEN 'B'
                             WHEN 4 THEN 'A'
    END AS "등급"
    FROM EMP;
SELECT EMPNO, ENAME, SAL,
    CASE WHEN SAL BETWEEN 0 AND 1000 THEN 'E'
         WHEN SAL BETWEEN 1001 AND 2000 THEN 'D'
         WHEN SAL BETWEEN 2001 AND 3000 THEN 'C'
         WHEN SAL BETWEEN 3001 AND 4000 THEN 'B'
         WHEN SAL BETWEEN 4001 AND 5000 THEN 'A'
    END "등급"
    FROM EMP;