-- 21-01-11 JDBC_Dao&Dto_GUI �л���� ���α׷� ����		(c)cherryuki(ji)
DROP TABLE STUDENT;
DROP TABLE MAJOR;
CREATE TABLE MAJOR(
    MNO     NUMBER(2)   PRIMARY KEY,
    MNAME   VARCHAR2(50)
    );
DESC MAJOR;
INSERT INTO MAJOR VALUES (1, '��������');
INSERT INTO MAJOR VALUES (2, '�濵������');
INSERT INTO MAJOR VALUES (3, '��ǻ�Ͱ���');
INSERT INTO MAJOR VALUES (4, '����Ʈ����');
INSERT INTO MAJOR VALUES (5, '���ؿ�ȭ��');
INSERT INTO MAJOR VALUES (6, '����������');
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
                                '���켺', (SELECT MNO FROM MAJOR WHERE MNAME='��������'), 90, 0);
INSERT INTO STUDENT VALUES (EXTRACT(YEAR FROM SYSDATE)||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                '�ڼ���', (SELECT MNO FROM MAJOR WHERE MNAME='��������'), 80, 0);
INSERT INTO STUDENT (SNO, SNAME, MNO, SCORE) 
    VALUES (TO_NUMBER(TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000'))),
                '�����', (SELECT MNO FROM MAJOR WHERE MNAME='��ǻ�Ͱ���'), 20);
INSERT INTO STUDENT VALUES (TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                'ȫ�浿', (SELECT MNO FROM MAJOR WHERE MNAME='����Ʈ����'), 95, 0);
INSERT INTO STUDENT VALUES (TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                '������', (SELECT MNO FROM MAJOR WHERE MNAME='���ؿ�ȭ��'), 100, 0);
INSERT INTO STUDENT VALUES (EXTRACT(YEAR FROM SYSDATE)||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                'ȫö��', (SELECT MNO FROM MAJOR WHERE MNAME='����Ʈ����'), 80, 1);
SELECT * FROM STUDENT;
COMMIT;

-- SwingStudentMng���� �ʿ��� Query
-- 0. ùȭ�鿡 �����̸��� �޺��ڽ��� �߰�(mName) : DAO���� public Vector<String> getMNamelist()
SELECT MNAME FROM MAJOR ORDER BY MNO;
-- 1. �й��˻� (sNo, sName, mName, score) : DAO���� public StudentSwingDto sNogetStudent(String sNo)
SELECT SNAME, MNAME, SCORE 
    FROM STUDENT S, MAJOR M 
    WHERE S.MNO=M.MNO AND SNO='2021001';
-- 2. �̸��˻� (sNo, sName, mName, score)  : DAO���� public ArrayList<StudentSwingDto> sNamegetStudent(String sName)
SELECT SNO, SNAME, MNAME, SCORE 
    FROM STUDENT S, MAJOR M
    WHERE S.MNO=M.MNO AND SNAME='���켺';
-- 3. �����˻� (rank, sName(sNo����), mName(mNo����), score) : DAO���� public ArrayList<StudentSwingDto> mNamegetStudent(String mName)
--- ��� : 1 ���켺(2021001) ��������(1) 90 
SELECT ROWNUM||'��' RANK, SNAME||'('||SNO||')' NAME, MNAME||'('||MNO||')' MAJOR, SCORE
    FROM (SELECT S.*, MNAME FROM STUDENT S, MAJOR M 
            WHERE S.MNO=M.MNO AND MNAME='��������' AND SEXPEL=0
            ORDER BY SCORE DESC);
SELECT ROWNUM||'��' RANK, SM.*
    FROM (SELECT SNAME||'('||SNO||')' NAME, MNAME||'('||S.MNO||')' MAJOR, SCORE
            FROM STUDENT S, MAJOR M 
            WHERE S.MNO=M.MNO AND MNAME='��������' AND SEXPEL=0 --�л��� ��½�
            ORDER BY SCORE DESC) SM;
-- 4. �л��Է� : DAO���� public int insertStudent(String sName, String mName, int score)
--              DAO���� public int insertStudent(StudentSwingDto dto)
INSERT INTO STUDENT VALUES (TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')), 
                                '���켺', (SELECT MNO FROM MAJOR WHERE MNAME='��������'), 90, 0);
-- 5. �л����� : DAO���� public int updateStudent(String sNo, String sName, String mName, int score)
--              DAO���� public int updateStudent(StudentSwingDto dto)
UPDATE STUDENT SET SNAME='�����', MNO=(SELECT MNO FROM MAJOR WHERE MNAME='��ǻ�Ͱ���'), SCORE=50 WHERE SNO=2021003;
-- 6. �л���� (rank, sName(sNo����), mName(mNo����), score) : DAO���� public ArrayList<StudentSwingDto> getStudents()
-- ��� : 1 ���켺(2021001) ��������(1) 90
SELECT ROWNUM||'��' RANK, SNAME||'('||SNO||')' NAME, MNAME||'('||MNO||')' MAJOR, SCORE
    FROM (SELECT S.*, MNAME FROM STUDENT S, MAJOR M 
            WHERE S.MNO=M.MNO AND SEXPEL=0
            ORDER BY SCORE DESC);
-- 7. ���������  (rank, sName(sNo����), mName(mNo����), score) : DAO���� public ArrayList<StudentSwingDto> getStudentsExpel()
-- ��� : 1 ������(2021004) ��ǻ�Ͱ���(3) 10
SELECT ROWNUM||'��' RANK, SNAME||'('||SNO||')' NAME, MNAME||'('||MNO||')' MAJOR, SCORE
    FROM (SELECT S.*, MNAME FROM STUDENT S, MAJOR M 
            WHERE S.MNO=M.MNO AND SEXPEL=1
            ORDER BY SCORE DESC);
-- 8. ����ó�� : DAO���� public int sNoExpel(String sNo)
UPDATE STUDENT SET SEXPEL=1 WHERE SNO=2021002;