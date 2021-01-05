-- 2021-01-04 DBMS_11. INDEX   ��cherryuki(ji)
-- [XI] �ε���(INDEX); ���� �˻��� ���� ���(ó�� �ӵ� ���)
SELECT * FROM USER_INDEXES; -- ��ųʸ��信 USER(SCOTT)�� ������ �ε��� ����
-- ���̺� ������ PRIMARY KEY�� �ε��� �ڵ� ������
DROP TABLE EMP01;
CREATE TABLE EMP01 AS SELECT * FROM EMP;
SELECT * FROM EMP01;
INSERT INTO EMP01 SELECT * FROM EMP01; --1��(28��), 2��(56��)
SELECT TO_CHAR(COUNT(*), '9,999,999') FROM EMP01;
INSERT INTO EMP01 SELECT * FROM EMP01; -- 229,376��
INSERT INTO EMP01 (EMPNO, ENAME, DEPTNO) VALUES (1111, 'KONG', 40);
INSERT INTO EMP01 SELECT * FROM EMP01; -- �� 180����
DESC EMP01;
SELECT * FROM EMP01 WHERE ENAME='KONG'; --0.055��
SELECT * FROM EMP01 WHERE EMPNO=1111; --0.055��
-- �ε��� ���� �� ��ȸ
CREATE INDEX IDX_EMP01_ENAME ON EMP01(ENAME);
SELECT * FROM EMP01 WHERE ENAME='KONG'; --0.005��
SELECT * FROM EMP01 WHERE EMPNO=1111; --0.047��
SELECT * FROM USER_INDEXES;
DROP TABLE EMP01; -- TABLE ����� INDEX�� ���� ������

-- �ε����� ����� Į������ ����Ǹ� �̸� ���� ���� ����(B*Ʈ��)�� �Բ� ���� �� - ����Ŭ ������ ���� �ڵ� ����
-- ���� �ε����� �ִ� ��� ��ȸ �ӵ��� �������� DML ��ɾ�(ISNERT, UPDATE, DELETE) �۾��� �ӵ��� ������
-- (�ε���)�� ��ȸ�� ������ ����Ű�� ��ü