-- 21-01-11 JDBC_Dao&Dto_GUI 학사관리 프로그램 구현		(c)cherryuki(ji)
DROP TABLE STUDENT;
DROP TABLE MAJOR;
CREATE TABLE MAJOR(
    MNO     NUMBER(2)   PRIMARY KEY,
    MNAME   VARCHAR2(50)
    );
DESC MAJOR;
INSERT INTO MAJOR VALUES (1, '빅데이터학');
INSERT INTO MAJOR VALUES (2, '경영정보학');
INSERT INTO MAJOR VALUES (3, '컴퓨터공학');
INSERT INTO MAJOR VALUES (4, '소프트웨어');
INSERT INTO MAJOR VALUES (5, '연극영화학');
INSERT INTO MAJOR VALUES (6, '정보전자학');
COMMIT;
SELECT * FROM MAJOR;
CREATE TABLE STUDENT(
    SNO     NUMBER(7)   PRIMARY KEY, -- YEAR||S_SEQ
    SNAME   VARCHAR(30) NOT NULL,
    MNO     NUMBER(2)   REFERENCES MAJOR(MNO),
    SCORE   NUMBER(3)   DEFAULT 0 CHECK(SCORE BETWEEN 0 AND 100),
    SEXPEL  NUMBER(1)   DEFAULT 0 CHECK(SEXPEL IN (0,1))
    );
DESC STUDENT;
DROP SEQUENCE S_SEQ;
CREATE SEQUENCE S_SEQ
    MAXVALUE 999
    NOCYCLE
    NOCACHE;
SELECT * FROM STUDENT;
INSERT INTO STUDENT VALUES (TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                '정우성', (SELECT MNO FROM MAJOR WHERE MNAME='빅데이터학'), 90, 0);
INSERT INTO STUDENT VALUES (EXTRACT(YEAR FROM SYSDATE)||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                '박세영', (SELECT MNO FROM MAJOR WHERE MNAME='빅데이터학'), 80, 0);
INSERT INTO STUDENT (SNO, SNAME, MNO, SCORE) 
    VALUES (TO_NUMBER(TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000'))),
                '배수지', (SELECT MNO FROM MAJOR WHERE MNAME='컴퓨터공학'), 20);
INSERT INTO STUDENT VALUES (TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                '홍길동', (SELECT MNO FROM MAJOR WHERE MNAME='소프트웨어'), 95, 0);
INSERT INTO STUDENT VALUES (TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                '송혜교', (SELECT MNO FROM MAJOR WHERE MNAME='연극영화학'), 100, 0);
INSERT INTO STUDENT VALUES (EXTRACT(YEAR FROM SYSDATE)||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                '홍철수', (SELECT MNO FROM MAJOR WHERE MNAME='소프트웨어'), 80, 1);
SELECT * FROM STUDENT;
COMMIT;

-- SwingStudentMng에서 필요한 Query
-- 0. 첫화면에 전공이름들 콤보박스에 추가(mName) : DAO에서 public Vector<String> getMNamelist()
SELECT MNAME FROM MAJOR ORDER BY MNO;
-- 1. 학번검색 (sNo, sName, mName, score) : DAO에서 public StudentSwingDto sNogetStudent(String sNo)
SELECT SNAME, MNAME, SCORE 
    FROM STUDENT S, MAJOR M 
    WHERE S.MNO=M.MNO AND SNO='2021001';
-- 2. 이름검색 (sNo, sName, mName, score)  : DAO에서 public ArrayList<StudentSwingDto> sNamegetStudent(String sName)
SELECT SNO, SNAME, MNAME, SCORE 
    FROM STUDENT S, MAJOR M
    WHERE S.MNO=M.MNO AND SNAME='정우성';
-- 3. 전공검색 (rank, sName(sNo포함), mName(mNo포함), score) : DAO에서 public ArrayList<StudentSwingDto> mNamegetStudent(String mName)
--- 출력 : 1 정우성(2021001) 빅데이터학(1) 90 
SELECT ROWNUM||'등' RANK, SNAME||'('||SNO||')' NAME, MNAME||'('||MNO||')' MAJOR, SCORE
    FROM (SELECT S.*, MNAME FROM STUDENT S, MAJOR M 
            WHERE S.MNO=M.MNO AND MNAME='빅데이터학' AND SEXPEL=0
            ORDER BY SCORE DESC);
SELECT ROWNUM||'등' RANK, SM.*
    FROM (SELECT SNAME||'('||SNO||')' NAME, MNAME||'('||S.MNO||')' MAJOR, SCORE
            FROM STUDENT S, MAJOR M 
            WHERE S.MNO=M.MNO AND MNAME='빅데이터학' AND SEXPEL=0 --학생만 출력시
            ORDER BY SCORE DESC) SM;
-- 4. 학생입력 : DAO에서 public int insertStudent(String sName, String mName, int score)
--              DAO에서 public int insertStudent(StudentSwingDto dto)
INSERT INTO STUDENT VALUES (TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                '정우성', (SELECT MNO FROM MAJOR WHERE MNAME='빅데이터학'), 90, 0);
-- 5. 학생수정 : DAO에서 public int updateStudent(String sNo, String sName, String mName, int score)
--              DAO에서 public int updateStudent(StudentSwingDto dto)
UPDATE STUDENT SET SNAME='배수지', MNO=(SELECT MNO FROM MAJOR WHERE MNAME='컴퓨터공학'), SCORE=50 WHERE SNO=2021003;
-- 6. 학생출력 (rank, sName(sNo포함), mName(mNo포함), score) : DAO에서 public ArrayList<StudentSwingDto> getStudents()
-- 출력 : 1 정우성(2021001) 빅데이터학(1) 90
SELECT ROWNUM||'등' RANK, SNAME||'('||SNO||')' NAME, MNAME||'('||MNO||')' MAJOR, SCORE
    FROM (SELECT S.*, MNAME FROM STUDENT S, MAJOR M 
            WHERE S.MNO=M.MNO AND SEXPEL=0
            ORDER BY SCORE DESC);
-- 7. 제적자출력  (rank, sName(sNo포함), mName(mNo포함), score) : DAO에서 public ArrayList<StudentSwingDto> getStudentsExpel()
-- 출력 : 1 김제적(2021004) 컴퓨터공학(3) 10
SELECT ROWNUM||'등' RANK, SNAME||'('||SNO||')' NAME, MNAME||'('||MNO||')' MAJOR, SCORE
    FROM (SELECT S.*, MNAME FROM STUDENT S, MAJOR M 
            WHERE S.MNO=M.MNO AND SEXPEL=1
            ORDER BY SCORE DESC);
-- 8. 제적처리 : DAO에서 public int sNoExpel(String sNo)
UPDATE STUDENT SET SEXPEL=1 WHERE SNO=2021002;