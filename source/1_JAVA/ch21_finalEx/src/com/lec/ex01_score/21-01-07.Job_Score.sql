-- 21-01-07 JDBC_Final EX	(c)cherryuki(ji)
SELECT * FROM TAB; -- 테이블 확인(SCORE, JOB 테이블 없음)
CREATE TABLE JOB(
    JNO     NUMBER(3)   PRIMARY KEY,
    JNAME   VARCHAR2(30)
    );
DESC JOB;
INSERT INTO JOB VALUES (10, '배우');
INSERT INTO JOB VALUES (20, '가수');
INSERT INTO JOB VALUES (90, '기타');
SELECT * FROM JOB;
CREATE TABLE SCORE(
    NO      NUMBER(5)    PRIMARY KEY, --S_SEQ
    NAME    VARCHAR2(30) NOT NULL,
    JNO     NUMBER(3)    REFERENCES JOB(JNO),
    KOR     NUMBER(3),
    ENG     NUMBER(3),
    MAT     NUMBER(3)
    );
DESC SCORE;
CREATE SEQUENCE S_SEQ
    MAXVALUE 99999
    NOCYCLE
    NOCACHE;
-- 1) 1을 누르면 데이터 입력(이름, 직업, 국어, 영어, 수학점수 입력받아 데이터 베이스 번호를 포함하여 입력)
--  (1) 번호는 시퀀스 이용하여 순차적으로 입력 
--  (2) 직업은 JNAME입력시 JNO로 자동 변환해서 저장
INSERT INTO SCORE VALUES(S_SEQ.NEXTVAL, '정우성', (SELECT JNO FROM JOB WHERE JNAME='배우'), 90, 80, 81);
INSERT INTO SCORE VALUES(S_SEQ.NEXTVAL, '고현정', (SELECT JNO FROM JOB WHERE JNAME='배우'), 80, 90, 80);
INSERT INTO SCORE VALUES(S_SEQ.NEXTVAL, '배수지', (SELECT JNO FROM JOB WHERE JNAME='가수'), 20, 90, 90);
COMMIT;
SELECT * FROM SCORE;
-- 2) 2를 누르면 원하는 직업 입력받아 직업별 조회후 총점 추가하여 총점이 높은 순으로 이름(번호)로 출력
SELECT ROWNUM RANK, S.*
    FROM (SELECT NAME||'('||NO||'번)' NAME, JNAME, KOR, ENG, MAT, KOR+ENG+MAT TOTAL 
            FROM JOB J, SCORE S WHERE J.JNO=S.JNO AND JNAME='배우' 
            ORDER BY TOTAL DESC) S;
-- 3) 데이터베이스에 입력된 사람 전체 조회 후 총점 추가하여 총점이 높은 순으로 출력
SELECT ROWNUM RANK, S.*
    FROM (SELECT NAME||'('||NO||'번)' NAME, JNAME, KOR, ENG, MAT, KOR+ENG+MAT TOTAL 
            FROM JOB J, SCORE S WHERE J.JNO=S.JNO 
            ORDER BY TOTAL DESC) S;
    