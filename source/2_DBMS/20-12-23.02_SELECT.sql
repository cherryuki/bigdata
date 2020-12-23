-- 2020-12-23 DBMS_SELECT   ⓒcherryuki(ji)
-- [II] SELECT문
-- 01. SQL문장 작성법
SELECT * FROM TAB; -- 현 계정(SCOTT)이 가지고 있는 모든 테이블
SELECT * FROM DEPT; -- DEPT 테이블의 모든 열, 모든 행
SELECT * FROM EMP; -- EMP 테이블의 모든 열, 모든 행
-- DEPT 테이블의 구조(ORACLE 전용)
DESC DEPT;
-- 02. SQL문장 실행(특정 열만 출력)
SELECT EMPNO, ENAME, SAL, JOB FROM EMP;
SELECT EMPNO AS "사번", ENAME AS "이름", SAL AS "급여", JOB AS "직업" FROM EMP; -- 열에 별명(별칭) 사용(타이틀 조정)
SELECT EMPNO AS 사번, ENAME AS 이름, SAL AS 급여, JOB AS 직업 FROM EMP; --SPACE 없을 경우 " " 생략 가능
SELECT EMPNO 사번, ENAME 이름, SAL 급여, JOB 직업 FROM EMP; -- AS 생략 가능
SELECT EMPNO NO, ENAME NAME, SAL SALARY, JOB FROM EMP; -- 별칭은 한국어, 영어 모두 가능(일부만 바꾸는 것도 가능, 영어 추천)
-- 03. WHERE절(조건) 비교 연산자 이용(같다, 다르다, 작거나 같다, 크거나 같다 등)
SELECT EMPNO "사번", ENAME 이름, SAL AS 급여 FROM EMP
    WHERE SAL=3000; --SAL이 3000인 행만 출력(사번, 이름, 급여)
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL!=3000; --다르다
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL^=3000; --다르다
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL<>3000; --다르다
SELECT EMPNO, ENAME, SAL FROM EMP WHERE NOT SAL=3000; --다르다
-- 10번 부서인 사원의 모든 필드를 출력
SELECT * FROM EMP WHERE DEPTNO=10;
-- ENAME이 'FORD'인 직원의 모든 필드를 출력
SELECT * FROM EMP WHERE ENAME='FORD'; --데이터('DATA')는 대소문자 구분, 별칭은 " ", 데이터는 ' '안에 기재
-- 04. 논리연산자(AND, OR, NOT) + 비교 연산자
-- 급여가 2000이상 3000미만인 직원의 모든 필드를 출력
SELECT * FROM EMP WHERE SAL>=2000 AND SAL<3000;
-- 비교 연산은 숫자, 문자, DATE형 모두 가능
SELECT * FROM EMP WHERE ENAME<'F'; --A,B,C,D,E로 시작하는 이름
SELECT * FROM EMP WHERE HIREDATE < '81/01/01'; --81년 1월 1일 전 입사자
SELECT * FROM EMP WHERE HIREDATE >= '82/01/01' AND HIREDATE <= '82/12/31'; --82년도 입사자
-- 날짜 표기법 셋팅(RR/MM/DD)
ALTER SESSION SET NLS_DATE_FORMAT='RR/MM/DD';
-- 연봉이 24000이상인 직원의 ENAME, SAL, 연봉 출력(연봉=SAL*12)
SELECT ENAME, SAL, SAL*12 연봉 FROM EMP 
    WHERE SAL*12>=24000 --WHERE절에는 별칭 사용 불가(실제 컬럼명으로만 가능)
    ORDER BY 연봉; --ORDER BY절에는 별칭 사용 가능
-- 05. 산술 표현식
SELECT ENAME, SAL, SAL+300 UPGRADESAL FROM EMP;
-- 모든 사원의 사원명, 월급, 상여금, 연봉(SAL*12+COMM)
SELECT ENAME 사원명, SAL 월급, COMM 상여금, SAL*12+NVL(COMM,0) 연봉 FROM EMP; -- NVL(COMM,0) COMM에 NULL이 있을 경우 0으로 계산
-- 산술 연산의 결과는 NULL을 포함하면 결과가 NULL로 나옴 -> NVL(NULL일 수 있는 필드명, 대치값), 단 둘의 타입이 같아야 함
DESC EMP; -- 필드의 타입 확인하는 방법 (NUMBER:숫자 VARCHAR:문자 DATE:날짜)
-- 모든 사원의 사원명, 월급, 상여금, 연봉(SAL*12+COMM) -- COMM이 NULL이면 0으로 출력
SELECT ENAME, SAL, NVL(COMM,0), SAL*12+NVL(COMM,0) FROM EMP;
-- 모든 사원의 사원명, 상사의 사번 -- 상사가 없으면 0출력
SELECT ENAME, NVL(MGR,0) FROM EMP;
-- 06. 연결 연산자(||); 열이나 문자를 연결
SELECT ENAME||'은 '||JOB||'이다' FROM EMP;
-- "SMITH IS CLERK"로 출력되고 TITLE은 EMPLOYEES로 모든 직원 출력
SELECT ENAME||' IS '||JOB EMPLOYEES FROM EMP;
-- 07. 중복 제거(DISTINCT)
SELECT DISTINCT JOB FROM EMP;
SELECT DISTINCT MGR FROM EMP;

-- 중간 연습문제
--1. emp 테이블의 구조 출력
DESC EMP;
--2. emp 테이블의 모든 내용을 출력 
SELECT * FROM EMP;
--3. 현 scott 계정에서 사용가능한 테이블 출력
SELECT * FROM TAB;
--4. emp 테이블에서 사번, 이름, 급여, 업무, 입사일 출력
SELECT EMPNO 사번, ENAME 이름, SAL 급여, JOB 업무, HIREDATE 입사일 FROM EMP;
--5. emp 테이블에서 급여가 2000미만인 사람의 사번, 이름, 급여 출력
SELECT EMPNO 사번, ENAME 이름, SAL 급여 FROM EMP WHERE SAL<2000;
--6. 입사일이 81/02이후에 입사한 사람의 사번, 이름, 업무, 입사일 출력
SELECT EMPNO 사번, ENAME 이름, JOB 업무, HIREDATE 입사일 FROM EMP WHERE HIREDATE>='81/02/01';
--7. 업무가 SALESMAN인 사람들 모든 자료 출력
SELECT * FROM EMP WHERE JOB='SALESMAN';
--8. 업무가 CLERK이 아닌 사람들 모든 자료 출력
SELECT * FROM EMP WHERE NOT JOB='CLERK';
SELECT * FROM EMP WHERE JOB<>'CLERK';
--9. 급여가 1500이상이고 3000이하인 사람의 사번, 이름, 급여 출력
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL>=1500 AND SAL<=3000;
--10. 부서코드가 10번이거나 30인 사람의 사번, 이름, 업무, 부서코드 출력
SELECT EMPNO, ENAME, JOB, DEPTNO FROM EMP WHERE DEPTNO=10 OR DEPTNO=30;
--11. 업무가 SALESMAN이거나 급여가 3000이상인 사람의 사번, 이름, 업무, 부서코드 출력
SELECT EMPNO, ENAME, JOB, DEPTNO FROM EMP WHERE JOB='SALESMAN' OR SAL>=3000;
--12. 급여가 2500이상이고 업무가 MANAGER인 사람의 사번, 이름, 업무, 급여 출력
SELECT EMPNO, ENAME, JOB, SAL FROM EMP WHERE SAL>=2500 AND JOB='MANAGER';
--13.“ename은 XXX 업무이고 연봉은 XX다” 스타일로 모두 출력
SELECT ENAME||'은 '||JOB||' 업무이고 연봉은 '||(SAL*12+NVL(COMM,0))||'다' FROM EMP;


-- 08. SQL연산자(BETWEEN, IN, LIKE, IS NULL)
-- SAL이 1500이상이고 3000이하인 사번, 이름, 급여
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL>=1500 AND SAL<=3000;
-- 필드명 BETWEEN A AND B (A~B까지, A와 B포함 A<B)
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL BETWEEN 1500 AND 3000;
-- 82년도 입사한 직원의 모든 필드를 출력
SELECT * FROM EMP WHERE HIREDATE BETWEEN '82/01/01' AND '82/12/31';
-- 이름이 A~C로 시작하는 사람
SELECT * FROM EMP WHERE ENAME BETWEEN 'A' AND 'D' AND ENAME!='D';
-- 부서번호(DEPTNO)가 10, 20인 사원의 모든 필드
SELECT * FROM EMP WHERE DEPTNO=10 OR DEPTNO=20;
SELECT * FROM EMP WHERE DEPTNO IN (10,20);
SELECT * FROM EMP WHERE DEPTNO NOT IN (10,20); 
-- EMPNO가 7902, 7788, 7566인 사원의 모든 필드
SELECT * FROM EMP WHERE EMPNO IN (7902,7788,7566);
-- 이름이 M으로 시작하는 사원의 모든 필드
SELECT * FROM EMP WHERE ENAME LIKE 'M%'; --%:0글자 이상 / _:한글자 (숫자나 날짜형도 가능)
-- 이름에 N이 들어가는 사원의 모든 필드
SELECT * FROM EMP WHERE ENAME LIKE '%N%';
-- 이름이 S로 끝나는 사원의 모든 필드
SELECT * FROM EMP WHERE ENAME LIKE '%S';
-- 이름에 %가 들어가는 사원의 모든 필드
INSERT INTO EMP VALUES (9999, 'A%', NULL, NULL, NULL, 1000, 1000, 40); --이름에 %가 들어있는 사람 강제 입력
SELECT * FROM EMP WHERE ENAME LIKE '%\%%' ESCAPE '\';
ROLLBACK; --DML(데이터 조작어)를 취소(이름에 %가 들어가 있는 사람 삭제)
SELECT * FROM EMP;
-- SAL이 5로 끝나는 사원의 모든 필드
SELECT * FROM EMP WHERE SAL LIKE '%5'; --숫자에서도 사용 가능
DESC EMP; -- 타입 확인
-- 입사년도가 82년인 사원의 모든 필드
SELECT * FROM EMP WHERE HIREDATE LIKE '82%'; --날짜에서도 사용 가능
SELECT * FROM EMP WHERE HIREDATE 
    BETWEEN TO_DATE('1982/01/01', 'YYYY/MM/DD') AND TO_DATE('1982/12/31', 'YYYY/MM/DD'); --타임존이 한국이 아닐 경우에도 사용하기 위함
-- 1월에 입사한 사원의 모든 필드
SELECT * FROM EMP WHERE HIREDATE LIKE '__/01/__';
-- 상여금이 없는 사원의 모든 필드 -- NULL은 IS NULL, IS NOT NULL로만 가능 (=NULL 불가능)
SELECT * FROM EMP WHERE COMM IS NULL OR COMM=0;
-- 상여금이 있는 사원의 모든 필드
SELECT * FROM EMP WHERE COMM IS NOT NULL AND NOT COMM=0;
SELECT * FROM EMP WHERE COMM IS NOT NULL AND COMM!=0;
-- 09. 정렬(오름차순, 내림차순)
SELECT ENAME, SAL FROM EMP ORDER BY SAL ASC; --급여 오름차순(기본값) 정렬
SELECT ENAME, SAL FROM EMP ORDER BY SAL; --급여 오름차순 정렬
SELECT ENAME, SAL FROM EMP ORDER BY SAL DESC; -- 급여 내림차순 정렬
-- SAL이 높은 순으로 출력(단, 같은 SAL일 경우 입사일 최신순으로 정렬, 입사일이 같을 경우 이름순으로 정렬)
SELECT * FROM EMP ORDER BY SAL DESC, HIREDATE DESC, ENAME;
-- 이름, 연봉(SAL*12+COMM)을 출력(연봉이 높은 순으로)
SELECT ENAME, SAL*12+NVL(COMM,0) 연봉 FROM EMP ORDER BY 연봉 DESC;
SELECT ENAME, SAL*12+NVL(COMM,0) 연봉 FROM EMP ORDER BY SAL*12+NVL(COMM,0) DESC;
-- 연봉이 20000이상인 직원의 이름, 연봉을 출력(연봉이 높은 순)
    -- ORDER BY 절에서는 필드별명 사용 가능, WHERE 절에서는 필드별명 사용 불가
    -- WHERE -> ALIAS -> ORDER BY -> SELECT 순으로 실행
SELECT ENAME, SAL*12+NVL(COMM,0) 연봉 FROM EMP 
    WHERE SAL*12+NVL(COMM,0)>=20000 
    ORDER BY 연봉 DESC;

--총 연습문제
--1.	EMP 테이블에서 sal이 3000이상인 사원의 empno, ename, job, sal을 출력
SELECT EMPNO, ENAME, JOB, SAL FROM EMP WHERE SAL>=3000;
--2.	EMP 테이블에서 empno가 7788인 사원의 ename과 deptno를 출력
SELECT ENAME, DEPTNO FROM EMP WHERE EMPNO=7788;
--3.	연봉이 24000이상인 사번, 이름, 급여 출력 (급여순정렬)
SELECT EMPNO, ENAME, SAL FROM EMP WHERE (SAL*12+NVL(COMM,0))>=24000 ORDER BY SAL;
--4.	EMP 테이블에서 hiredate가 1981년 2월 20과 1981년 5월 1일 사이에 입사한 사원의 
--ename,job,hiredate을 출력하는 SELECT 문장을 작성 (단 hiredate 순으로 출력)
SELECT ENAME, JOB, HIREDATE FROM EMP 
    WHERE HIREDATE BETWEEN '1981/02/20' AND '1981/05/01' 
    ORDER BY HIREDATE;
--5.	EMP 테이블에서 deptno가 10,20인 사원의 모든 정보를 출력 (단 ename순으로 정렬)
SELECT * FROM EMP WHERE DEPTNO IN (10,20) ORDER BY ENAME;
--6.	EMP 테이블에서 sal이 1500이상이고 deptno가 10,30인 사원의 ename과 sal를 출력
-- (단 HEADING을 employee과 Monthly Salary로 출력)
SELECT ENAME "employee", SAL "Monthly Salary" FROM EMP WHERE SAL>=1500 AND DEPTNO IN (10,30);
--7.	EMP 테이블에서 hiredate가 1982년인 사원의 모든 정보를 출력
SELECT * FROM EMP WHERE HIREDATE LIKE '82%';
--8.	이름의 첫자가 C부터  P로 시작하는 사람의 이름, 급여 이름순 정렬
SELECT ENAME, SAL FROM EMP WHERE ENAME BETWEEN 'C' AND 'Q' AND ENAME!='Q' ORDER BY ENAME;
SELECT ENAME FROM EMP WHERE ENAME BETWEEN 'C' AND 'Q' AND ENAME!='Q' ORDER BY SAL, ENAME;
--9.	EMP 테이블에서 comm이 sal보다 10%가 많은 모든 사원에 대하여 이름, 급여, 상여금을 
--출력하는 SELECT 문을 작성
SELECT ENAME, SAL, COMM FROM EMP WHERE COMM>SAL*1.1;
--10.	EMP 테이블에서 job이 CLERK이거나 ANALYST이고 sal이 1000,3000,5000이 아닌 모든 사원의 정보를 출력
SELECT * FROM EMP WHERE JOB IN ('CLERK', 'ANALYST') AND SAL NOT IN (1000,3000,5000);
--11.	EMP 테이블에서 ename에 L이 두 자가 있고 deptno가 30이거나 또는 mgr이 7782인 사원의 
--모든 정보를 출력하는 SELECT 문을 작성하여라.
SELECT * FROM EMP WHERE ENAME LIKE '%L%L%' AND DEPTNO=30 OR MGR=7782;
--12.	사원 테이블에서 입사일이 81년도인 직원의 사번,사원명, 입사일, 업무, 급여를 출력
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP WHERE HIREDATE LIKE '81%';
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP 
    WHERE TO_CHAR(HIREDATE, 'YY') = '81';
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP 
    WHERE HIREDATE BETWEEN TO_DATE('1981/01/01', 'YYYY/MM/DD/') 
                        AND TO_DATE('1981/12/31', 'YYYY/MM/DD');
--13.	사원 테이블에서 입사일이81년이고 업무가 'SALESMAN'이 아닌 직원의 사번, 사원명, 입사일, 
-- 업무, 급여를 검색하시오.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP 
    WHERE HIREDATE LIKE '81%' AND JOB<>'SALESMAN';
--14.	사원 테이블의 사번, 사원명, 입사일, 업무, 급여를 급여가 높은 순으로 정렬하고, 
-- 급여가 같으면 입사일이 빠른 사원으로 정렬하시오.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP ORDER BY SAL DESC, HIREDATE;
--15.	사원 테이블에서 사원명의 세 번째 알파벳이 'N'인 사원의 사번, 사원명을 검색하시오
SELECT EMPNO, ENAME FROM EMP WHERE ENAME LIKE '__N%';
--16.	사원 테이블에서연봉(SAL*12)이 35000 이상인 사번, 사원명, 연봉을 검색 하시오.
SELECT EMPNO, ENAME, SAL*12 연봉 FROM EMP WHERE SAL*12>=35000;
