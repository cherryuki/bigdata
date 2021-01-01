-- 2020-12-30 DBMS_07.DDL_DML   ��cherryuki(ji)
-- [VII] DDL, DML, DCL
-- SQL = DDL(���̺� ����, ����, ��������, ���̺� ������ ����)
    --  +DML(SELECT, INSERT, UPDATE, DELETE)
    --  +DCL(����� ���� ����, ����� ���� �ο�, ���� ��Ż, Ʈ����� ��ɾ�)
    
-- �� 01. DDL �� --
-- 1) ���̺� ���� (CREATE TABLE)
-- CREATE TABLE ���̺��(Į���� ������_Ÿ��, ...);
CREATE TABLE BOOK(
    BOOKID      NUMBER(4),    --������ȣ
    BOOKNAME    VARCHAR2(20), --������
    PUBLISHER   VARCHAR2(20), --���ǻ�
    RDATE       DATE,         --������
    PRICE       NUMBER(8),    --����
    PRIMARY KEY(BOOKID)       --���̺� �� ��Ű(PRIMARY KEY); ������ �ʵ�, NOT NULL
    );
DROP TABLE BOOK; -- BOOK ���̺� ����
CREATE TABLE BOOK(
    BOOKID      NUMBER(4)       PRIMARY KEY,
    BOOKNAME    VARCHAR2(20)    NOT NULL,
    PUBLISHER   VARCHAR2(20),
    RDATE       DATE,
    PRICE       NUMBER(8)
    );
SELECT * FROM BOOK;

-- ��������(������, ������, ��¥��)
-- VARCHAR2(N); �ּ� ũ��:1, �ִ�ũ��:N (�ִ� 2000BYTES ���� ����)
-- NUMBER(W); �ִ�ũ��:W (�ִ� 38�ڸ�)
-- DATE

-- EMP�� ������ EMP01: EMPNO(����4), ENAME(����20), SAL(����7,2)
CREATE TABLE EMP01(
    EMPNO   NUMBER(4),
    ENAME   VARCHAR2(20),
    SAL     NUMBER(7,2)
    );
SELECT * FROM EMP01;
DESC EMP01;

-- DEPT�� ������ DEPT01: DEPTNO(����2), DNAME(����14), LOC(����13)
CREATE TABLE DEPT01(
    DEPTNO  NUMBER(2),
    DNAME   VARCHAR2(14),
    LOC     VARCHAR2(13)
    );
SELECT * FROM DEPT01;
DESC DEPT01;

-- ���������� �̿��� ���̺� ����
CREATE TABLE EMP02
    AS
    SELECT * FROM EMP; --�������� ����� EMP02���̺�� ����(�������� ������)
SELECT * FROM EMP02;
DESC EMP02;
INSERT INTO EMP02 (EMPNO, ENAME, DEPTNO) VALUES (7369, 'KONG', 90); --�������� �������̹Ƿ� ����
-- EMP03; EMP ���̺��� EMPNO, ENAME, DEPTNO�� ����
CREATE TABLE EMP03
    AS
    SELECT EMPNO, ENAME, DEPTNO FROM EMP;
SELECT * FROM EMP03;
-- EMP04; EMP ���̺��� 10�� �μ��� ����
CREATE TABLE EMP04
    AS
    SELECT * FROM EMP WHERE DEPTNO=10;
SELECT * FROM EMP04;
-- EMP05; EMP ���̺��� ������ ����
CREATE TABLE EMP05
    AS
    SELECT * FROM EMP WHERE 1=0; --������ ������ ������ �Է��ϸ� ������ ����
                                -- (������ ���� �����Է½�(=���� ������) �����ͱ��� ��� ������)
SELECT * FROM EMP05;

-- 2) ���̺� ���� ����(ALTER TABLE); ADD, MODIFY, DROP
-- ALTER TABLE ���̺��
-- ADD || MODIFY || DROP (�ʵ��, �ʵ� Ÿ��, ...);
SELECT * FROM EMP03;
-- (1) �ʵ� �߰�(ADD)
ALTER TABLE EMP03 ADD (JOB VARCHAR2(10), SAL NUMBER(7,2)); 
SELECT * FROM EMP03; --�̹� �����Ͱ� �ִ� ���̺� Į��(�ʵ�) �߰��� �����Ϳ� NULL�� ��
ALTER TABLE EMP03 ADD (MGR NUMBER(4));
-- (2) �ʵ� Ÿ�� ����(MODIFY)
ALTER TABLE EMP03 MODIFY (EMPNO VARCHAR2(5)); -- ���� ������ �ִ� ���¶� �ٲ� �� ����
ALTER TABLE EMP03 MODIFY (JOB VARCHAR2(5)); --NULL�� ������ �� �ٲ� �� ����
ALTER TABLE EMP03 MODIFY (ENAME VARCHAR2(200));
ALTER TABLE EMP03 MODIFY (ENMAE VARCHAR2(5)); --5BYTE �ʰ� ������ ���� ���̶� ���� �Ұ���
-- (3) �ʵ� ����(DROP)
ALTER TABLE EMP03 DROP COLUMN JOB; --NULL�� �ִ� Į�� ����
SELECT * FROM EMP03;
ALTER TABLE EMP03 DROP COLUMN DEPTNO; -- ������ ���� ���̴� Į�� ���� -> ������ ���� �Ұ�
-- <������ ���� ���� Į�� ������>
-- �������� Ư�� �ʵ带 ���� ���ϵ��� (��, ������ ����ϴ� ����� ���� �ð���)
ALTER TABLE EMP03 SET UNUSED(SAL);
SELECT * FROM EMP03; -- �ʵ� ���� �Ұ� ����
-- �������� ���� �Ұ��ߴ� �ʵ带 ���� (����, ������ ����ϴ� ����� ���ų� ���� �ð���)
ALTER TABLE EMP03 DROP UNUSED COLUMNS; --�ʵ� ������ ������ ���̺� �׼��� �Ұ�

-- 3) ���̺� ����(DROP TABLE)
SELECT * FROM EMP01;
DROP TABLE EMP01;
DROP TABLE DEPT; --DEPT���̺��� �����͸� �����ϴ� ���̺�(EMP)�� �����Ƿ� ���� �Ұ�
-- �ٸ� ���̺��� �����ϴ� �����Ͱ� ���� ��� DROP �Ұ�

-- 4) ���̺� �� ������ ���� ����(TRUNCATE TABLE)
SELECT * FROM TAB;
SELECT * FROM EMP02;
TRUNCATE TABLE EMP02; --������ ����, DDL ��ɾ�� ��� �Ұ�(������ ���� �Ұ�)

-- 5) ���̺� �̸� ����(RENAME)
SELECT * FROM EMP03;
RENAME EMP03 TO EMP3; --EMP03�� EMP3���� �̸� ����
SELECT * FROM EMP3;

-- 6) ������ ��ųʸ�(���� �Ұ�)�� ������ ��ųʸ� ��(����� ���ٿ�)
    -- DBA_TABLES, DBA_INDEXES, DBA_CONSTRAINTS, DBA_VIEWS;     (������)
    -- USER_TABLES, USER_INDEXES, USER_CONSTRAINTS, USER_VIEWS; (�����)
    -- ALL_TABLES, ALL_INDEXES, ALL_CONSTRAINTS, ALL_VIEWS;
-- USER_XXX; ����ڰ� ������ ��ü(���̺�, �ε���, ...) ������ȸ
SHOW USER; -- ���� SCOTT
SELECT * FROM USER_TABLES;
SELECT TABLE_NAME FROM USER_TABLES;
SELECT * FROM USER_INDEXES;
SELECT * FROM USER_CONSTRAINTS; --P: PRIMARY KEY, R: REFERENXE, C: NOT NULL
SELECT * FROM USER_VIEWS;
DESC BOOK;
-- DBA_XXX; DBA ������ ���� �����(=������)�� ���� ������ ��ü ����
SELECT * FROM DBA_TABLES;
SELECT TABLE_NAME, OWNER FROM DBA_TABLES;
SELECT * FROM DBA_INDEXES;
SELECT * FROM DBA_CONSTRAINTS;
SELECT * FROM DBA_VIEWS;
-- ALL_XXX; �� ����(SCOTT)�� ������ ��ü�� ������ �ο��� ��ü ����
SELECT * FROM ALL_TABLES;
SELECT * FROM ALL_CONSTRAINTS;
SELECT * FROM ALL_INDEXES;
SELECT * FROM ALL_VIEWS;

-- �� 02. DML �� --
-- 7) DML; SELECT, INSERT, UPDATE, DELETE
-- (1) INSERT INTO ���̺�� (�ʵ��1, �ʵ��2, ..) VALUES (��1, ��2, ...); -- �ʵ��1�� ��1, �ʵ��2�� ��2 (���� ���Ѿ� ��)
-- INSERT INTO ���̺�� VALUES (��1, ��2, ...); �ʵ�� ������� ������ ��
SELECT * FROM DEPT01;
INSERT INTO DEPT01 (DEPTNO, DNAME, LOC) VALUES (10, 'ACCOUNGTING', 'NEW YORK');
INSERT INTO DEPT01 (DNAME, LOC, DEPTNO) VALUES ('SALES', 'BOSTON', 20);
-- NULL �� �Է��� NULL�� �Է��ϰų� �����͸� �Է����� ������ NULL�� �ڵ� �Է�
INSERT INTO DEPT01 (DEPTNO, DNAME, LOC) VALUES (30, 'IT', NULL);
INSERT INTO DEPT01 (DEPTNO, DNAME) VALUES (40, 'OPERATION');
-- INSERT������ �ʵ�� ������ �ݵ�� ��� �ʵ� �� �Է��ؾ� ��
INSERT INTO DEPT01 VALUES (50, 'RESEARCH', 'TORONTO');
DESC DEPT01; --��Ű(PK)���� DEPT01
-- DEPT01 ���̺� DEPT���̺� 10~30�� �μ����� ������ INSERT
INSERT INTO DEPT01 SELECT * FROM DEPT WHERE DEPTNO<40;
SELECT * FROM DEPT01 ORDER BY DEPTNO;
-- BOOK ���̺� 100��, 'MEDICAL', 'POOH', ������ ����, ���� 13000�� ����
INSERT INTO BOOK VALUES (100, 'MEDICAL', 'POOH', SYSDATE, 13000);
SELECT * FROM BOOK;
-- DML ��ɾ�� Ʈ����� ������ ����
COMMIT; -- �� Ʈ������� �۾��� �ݿ�
ROLLBACK; -- Ʈ����� �ȿ� �ִ� DML ��ɾ ���

DROP TABLE SAM01;
CREATE TABLE SAM01 (
    EMPNO   NUMBER(4) PRIMARY KEY,
    ENAME   VARCHAR2(10),
    JOB     VARCHAR2(9),
    SAL     NUMBER(7,2)
    );
SELECT * FROM SAM01;
INSERT INTO SAM01 VALUES (1000, 'APPLE', 'POLICE', 10000);
INSERT INTO SAM01 VALUES (1010, 'BANANA', 'NURSE', 15000);
INSERT INTO SAM01 VALUES (1020, 'ORANGE', 'DOCTOR', 25000);
INSERT INTO SAM01 (EMPNO, ENAME, SAL) VALUES (1030, 'VERY', 25000);
INSERT INTO SAM01 VALUES (1040, 'CAT', NULL, 2000);
INSERT INTO SAM01 SELECT EMPNO, ENAME, JOB, SAL FROM EMP WHERE DEPTNO=10;

-- (2) UPDATE ���̺�� SET �ʵ��1=��1, �ʵ��2=��2,... [WHERE ����];
DROP TABLE EMP01;
CREATE TABLE EMP01
    AS SELECT * FROM EMP;
SELECT * FROM EMP01;
-- ��� ������ �޿��� 10% �λ�
UPDATE EMP01 SET SAL=SAL*1.1;
-- �μ���ȣ 20���� 30���� ����
UPDATE EMP01 SET DEPTNO=30 WHERE DEPTNO=20;
-- Ư�� ���� �����͸� �����ϰ��� �� ���� WHERE�� �߰�
-- 10�� �μ� ������ �Ի����� ���÷� �����ϰ�, �μ���ȣ�� 30�� �μ��� ����
UPDATE EMP01 SET HIREDATE=SYSDATE, DEPTNO=30 WHERE DEPTNO=10;
-- SAL�� 3000�̻��� ����� �޿��� 10% �λ�
UPDATE EMP01 SET SAL=SAL*1.1 WHERE SAL>=3000;
-- 'DALLAS'�� �ٹ��ϴ� �������� �޿��� 1000�λ�
UPDATE EMP01 SET SAL=SAL+1000 WHERE DEPTNO=(SELECT DEPTNO FROM DEPT WHERE LOC='DALLAS');

-- �� ���蹮�� ���� (������ ���� ����)
-- SCOTT����� �μ���ȣ�� 20���� JOB�� MANAGER�� �����ϴ� SQL
UPDATE EMP01 SET DEPTNO=20, JOB='MANAGER' WHERE ENAME='SCOTT';
-- SCOTT����� �Ի����� ���÷�, �޿��� 500, �󿩱��� 400���� ����
UPDATE EMP01 SET HIREDATE=SYSDATE, SAL=500, COMM=400 WHERE ENAME='SCOTT';
SELECT * FROM EMP01 WHERE ENAME='SCOTT';

-- ���������� �̿��� UPDATE��
SELECT * FROM DEPT01;
UPDATE DEPT01 SET LOC='SEOUL' WHERE DEPTNO=40;
-- DEPT01���� 20�� �μ��� �������� 40�� �μ��� �μ���, ���������� ����
UPDATE DEPT01 SET DNAME=(SELECT DNAME FROM DEPT01 WHERE DEPTNO=40), LOC=(SELECT LOC FROM DEPT01 WHERE DEPTNO=40) WHERE DEPTNO=20;
UPDATE DEPT01 SET (DNAME, LOC) = (SELECT DNAME, LOC FROM DEPT01 WHERE DEPTNO=40) WHERE DEPTNO=20; --���������� ���� ��� �� ���� �ٲٴ� �� ����
SELECT * FROM DEPT01 WHERE DEPTNO IN (20,40);
-- EMP01 ���̺��� ��� ����� �޿��� �Ի����� 'KING'�� �޿��� �Ի��Ϸ� ����
SELECT * FROM EMP01;
UPDATE EMP01 SET (SAL, HIREDATE) = (SELECT SAL, HIREDATE FROM EMP01 WHERE ENAME='KING');

-- cf) UPDATE ���̺�� SET �ʵ��=��, ...;
-- (3) DELETE FROM ���̺�� WHERE ����; -- FROM �ݵ�� �ʿ��
COMMIT;
SELECT * FROM EMP01;
DELETE FROM EMP01; -- ������ ���� ����(���� ���� ����)
ROLLBACK;
-- EMP01 ���̺��� 30�� �μ��� ����
DELETE FROM EMP01 WHERE DEPTNO=30;
-- SAM01 ���̺��� JOB�� �������� ���� ����� ����
SELECT * FROM SAM01;
DELETE FROM SAM01 WHERE JOB IS NULL;
-- EMP01 ���̺��� �μ����� SALES�� ����� ����
SELECT * FROM EMP01;
DELETE FROM EMP01
    WHERE DEPTNO=(SELECT DEPTNO FROM DEPT WHERE DNAME='SALES');
-- EMP01 ���̺��� RESERCH �μ� �Ҽ��� ��� ����
DELETE FROM EMP01
    WHERE DEPTNO=(SELECT DEPTNO FROM DEPT WHERE DNAME='RESEARCH');

-- PPT 1������ ��������
--01. ���̺� ����
CREATE TABLE MY_DATA(
    ID      NUMBER(4),
    NAME    VARCHAR2(10),
    USERID  VARCHAR2(30),
    SALARY  NUMBER(10,2),
    PRIMARY KEY(ID)
    );
--02. ���̺� ������ �Է�
INSERT INTO MY_DATA VALUES(1, 'Scott', 'sscott', 10000.00);
INSERT INTO MY_DATA VALUES(2, 'Ford', 'fford', 13000.00);
INSERT INTO MY_DATA VALUES(3, 'Patel', 'ppatel', 33000.00);
INSERT INTO MY_DATA VALUES(4, 'Report', 'rreport', 23500.00);
INSERT INTO MY_DATA VALUES(5, 'Good', 'ggood', 44450.00);
--03. �ڷ� Ȯ��
SELECT * FROM MY_DATA;
SELECT ID, NAME, USERID, TO_CHAR(SALARY, '999,999.99') SALARY FROM MY_DATA;
--04. �ڷḦ ���������� DB�� ���
COMMIT;
--06. ID�� 3���� ����� �޿��� 65,000.00���� �����ϰ� ���������� ������ ���̽��� �ݿ�
UPDATE MY_DATA SET SALARY=65000.00 WHERE ID=3;
COMMIT;
--07. �̸��� Ford�� ����� ���� ����
DELETE FROM MY_DATA WHERE NAME='Ford';
COMMIT;
--08. �޿��� 15,000������ ����� �޿��� 15,000���� ����
UPDATE MY_DATA SET SALARY=15000 WHERE SALARY<=15000;
--09. 1������ ������ ���̺��� ����
DROP TABLE MY_DATA;

-- �� ERD: (����ȭ�� �����͸� �����ϱ� ���� DB ���) 
--        DB�� ������ ���� ���� �� �پ��� ����� �����ϴ� �� 
CREATE TABLE DEPT1 (
    DEPTNO  NUMBER(2),
    DNAME   VARCHAR2(14),
    LOC     VARCHAR2(13),
    PRIMARY KEY(DEPTNO)
    );
SELECT * FROM DEPT1;
CREATE TABLE EMP1(                          --��������: �������� ������ ���� ���� ����
    EMPNO   NUMBER(4)       PRIMARY KEY,    --��������1. PRIMARY KEY
    ENAME   VARCHAR2(10)    UNIQUE,         --��������2. UNIQUE
    JOB     VARCHAR2(9)     NOT NULL,       --��������3. NOT NULL
    MGR     NUMBER(4),
    HIREDATE    DATE        DEFAULT SYSDATE,--��������4. DEFAULT
    SAL     NUMBER(7,2)     CHECK(SAL>0),   --��������5. CHECK
    COMM    NUMBER(7,2),
    DEPTNO  NUMBER(2)       REFERENCES DEPT1(DEPTNO)    --��������6.FOREIGN KEY
    );
SELECT * FROM EMP1;
DESC EMP1;
-- DEPT1 �Է�
INSERT INTO DEPT1 VALUES (10, 'ACCOUNTING', 'SEOUL');
INSERT INTO DEPT1 VALUES (20, 'MARKETING', 'PUSAN');
INSERT INTO DEPT1 VALUES (30, 'SALES', 'INCHEON');
INSERT INTO DEPT1 VALUES (40, 'IT', 'GIMPO');
--EMP1 �Է�
INSERT INTO EMP1 (EMPNO, ENAME, JOB, MGR, SAL, DEPTNO)
    VALUES (1111, 'KONG', 'CEO', NULL, 9000, 40);
INSERT INTO EMP1 (EMPNO, ENAME, JOB, MGR, SAL, DEPTNO)
    VALUES (1112, 'KONGU', 'MARKETER', 1111, 1000, 20);
COMMIT;

-- 2020-12-31 DBMS_07.DCL   ��cherryuki(ji)
-- �� 03. DCL �� --
-- ����� ���� ����, ����� ���� �ο�, ���� ��Ż, Ʈ����� ��ɾ�(TCL)
-- 1) ���� �߰� (�� scott ������ DBA�����̹Ƿ�)
CREATE USER kim IDENTIFIED BY tiger; --kim(PW: tiger)���� ����
-- 2) ���� �ο�(GRANT)
GRANT CREATE SESSION, CREATE TABLE TO kim;
GRANT SELECT ON EMP TO kim;
SHOW USER;
-- 3) ���� ��Ż(REVOKE)
REVOKE SELECT ON EMP FROM kim;
-- 4) ���� ����
DROP USER kim; 