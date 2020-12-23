-- 2020-12-23 DBMS_SELECT   ��cherryuki(ji)
-- [II] SELECT��
-- 01. SQL���� �ۼ���
SELECT * FROM TAB; -- �� ����(SCOTT)�� ������ �ִ� ��� ���̺�
SELECT * FROM DEPT; -- DEPT ���̺��� ��� ��, ��� ��
SELECT * FROM EMP; -- EMP ���̺��� ��� ��, ��� ��
-- DEPT ���̺��� ����(ORACLE ����)
DESC DEPT;
-- 02. SQL���� ����(Ư�� ���� ���)
SELECT EMPNO, ENAME, SAL, JOB FROM EMP;
SELECT EMPNO AS "���", ENAME AS "�̸�", SAL AS "�޿�", JOB AS "����" FROM EMP; -- ���� ����(��Ī) ���(Ÿ��Ʋ ����)
SELECT EMPNO AS ���, ENAME AS �̸�, SAL AS �޿�, JOB AS ���� FROM EMP; --SPACE ���� ��� " " ���� ����
SELECT EMPNO ���, ENAME �̸�, SAL �޿�, JOB ���� FROM EMP; -- AS ���� ����
SELECT EMPNO NO, ENAME NAME, SAL SALARY, JOB FROM EMP; -- ��Ī�� �ѱ���, ���� ��� ����(�Ϻθ� �ٲٴ� �͵� ����, ���� ��õ)
-- 03. WHERE��(����) �� ������ �̿�(����, �ٸ���, �۰ų� ����, ũ�ų� ���� ��)
SELECT EMPNO "���", ENAME �̸�, SAL AS �޿� FROM EMP
    WHERE SAL=3000; --SAL�� 3000�� �ุ ���(���, �̸�, �޿�)
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL!=3000; --�ٸ���
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL^=3000; --�ٸ���
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL<>3000; --�ٸ���
SELECT EMPNO, ENAME, SAL FROM EMP WHERE NOT SAL=3000; --�ٸ���
-- 10�� �μ��� ����� ��� �ʵ带 ���
SELECT * FROM EMP WHERE DEPTNO=10;
-- ENAME�� 'FORD'�� ������ ��� �ʵ带 ���
SELECT * FROM EMP WHERE ENAME='FORD'; --������('DATA')�� ��ҹ��� ����, ��Ī�� " ", �����ʹ� ' '�ȿ� ����
-- 04. ��������(AND, OR, NOT) + �� ������
-- �޿��� 2000�̻� 3000�̸��� ������ ��� �ʵ带 ���
SELECT * FROM EMP WHERE SAL>=2000 AND SAL<3000;
-- �� ������ ����, ����, DATE�� ��� ����
SELECT * FROM EMP WHERE ENAME<'F'; --A,B,C,D,E�� �����ϴ� �̸�
SELECT * FROM EMP WHERE HIREDATE < '81/01/01'; --81�� 1�� 1�� �� �Ի���
SELECT * FROM EMP WHERE HIREDATE >= '82/01/01' AND HIREDATE <= '82/12/31'; --82�⵵ �Ի���
-- ��¥ ǥ��� ����(RR/MM/DD)
ALTER SESSION SET NLS_DATE_FORMAT='RR/MM/DD';
-- ������ 24000�̻��� ������ ENAME, SAL, ���� ���(����=SAL*12)
SELECT ENAME, SAL, SAL*12 ���� FROM EMP 
    WHERE SAL*12>=24000 --WHERE������ ��Ī ��� �Ұ�(���� �÷������θ� ����)
    ORDER BY ����; --ORDER BY������ ��Ī ��� ����
-- 05. ��� ǥ����
SELECT ENAME, SAL, SAL+300 UPGRADESAL FROM EMP;
-- ��� ����� �����, ����, �󿩱�, ����(SAL*12+COMM)
SELECT ENAME �����, SAL ����, COMM �󿩱�, SAL*12+NVL(COMM,0) ���� FROM EMP; -- NVL(COMM,0) COMM�� NULL�� ���� ��� 0���� ���
-- ��� ������ ����� NULL�� �����ϸ� ����� NULL�� ���� -> NVL(NULL�� �� �ִ� �ʵ��, ��ġ��), �� ���� Ÿ���� ���ƾ� ��
DESC EMP; -- �ʵ��� Ÿ�� Ȯ���ϴ� ��� (NUMBER:���� VARCHAR:���� DATE:��¥)
-- ��� ����� �����, ����, �󿩱�, ����(SAL*12+COMM) -- COMM�� NULL�̸� 0���� ���
SELECT ENAME, SAL, NVL(COMM,0), SAL*12+NVL(COMM,0) FROM EMP;
-- ��� ����� �����, ����� ��� -- ��簡 ������ 0���
SELECT ENAME, NVL(MGR,0) FROM EMP;
-- 06. ���� ������(||); ���̳� ���ڸ� ����
SELECT ENAME||'�� '||JOB||'�̴�' FROM EMP;
-- "SMITH IS CLERK"�� ��µǰ� TITLE�� EMPLOYEES�� ��� ���� ���
SELECT ENAME||' IS '||JOB EMPLOYEES FROM EMP;
-- 07. �ߺ� ����(DISTINCT)
SELECT DISTINCT JOB FROM EMP;
SELECT DISTINCT MGR FROM EMP;

-- �߰� ��������
--1. emp ���̺��� ���� ���
DESC EMP;
--2. emp ���̺��� ��� ������ ��� 
SELECT * FROM EMP;
--3. �� scott �������� ��밡���� ���̺� ���
SELECT * FROM TAB;
--4. emp ���̺��� ���, �̸�, �޿�, ����, �Ի��� ���
SELECT EMPNO ���, ENAME �̸�, SAL �޿�, JOB ����, HIREDATE �Ի��� FROM EMP;
--5. emp ���̺��� �޿��� 2000�̸��� ����� ���, �̸�, �޿� ���
SELECT EMPNO ���, ENAME �̸�, SAL �޿� FROM EMP WHERE SAL<2000;
--6. �Ի����� 81/02���Ŀ� �Ի��� ����� ���, �̸�, ����, �Ի��� ���
SELECT EMPNO ���, ENAME �̸�, JOB ����, HIREDATE �Ի��� FROM EMP WHERE HIREDATE>='81/02/01';
--7. ������ SALESMAN�� ����� ��� �ڷ� ���
SELECT * FROM EMP WHERE JOB='SALESMAN';
--8. ������ CLERK�� �ƴ� ����� ��� �ڷ� ���
SELECT * FROM EMP WHERE NOT JOB='CLERK';
SELECT * FROM EMP WHERE JOB<>'CLERK';
--9. �޿��� 1500�̻��̰� 3000������ ����� ���, �̸�, �޿� ���
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL>=1500 AND SAL<=3000;
--10. �μ��ڵ尡 10���̰ų� 30�� ����� ���, �̸�, ����, �μ��ڵ� ���
SELECT EMPNO, ENAME, JOB, DEPTNO FROM EMP WHERE DEPTNO=10 OR DEPTNO=30;
--11. ������ SALESMAN�̰ų� �޿��� 3000�̻��� ����� ���, �̸�, ����, �μ��ڵ� ���
SELECT EMPNO, ENAME, JOB, DEPTNO FROM EMP WHERE JOB='SALESMAN' OR SAL>=3000;
--12. �޿��� 2500�̻��̰� ������ MANAGER�� ����� ���, �̸�, ����, �޿� ���
SELECT EMPNO, ENAME, JOB, SAL FROM EMP WHERE SAL>=2500 AND JOB='MANAGER';
--13.��ename�� XXX �����̰� ������ XX�١� ��Ÿ�Ϸ� ��� ���
SELECT ENAME||'�� '||JOB||' �����̰� ������ '||(SAL*12+NVL(COMM,0))||'��' FROM EMP;


-- 08. SQL������(BETWEEN, IN, LIKE, IS NULL)
-- SAL�� 1500�̻��̰� 3000������ ���, �̸�, �޿�
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL>=1500 AND SAL<=3000;
-- �ʵ�� BETWEEN A AND B (A~B����, A�� B���� A<B)
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL BETWEEN 1500 AND 3000;
-- 82�⵵ �Ի��� ������ ��� �ʵ带 ���
SELECT * FROM EMP WHERE HIREDATE BETWEEN '82/01/01' AND '82/12/31';
-- �̸��� A~C�� �����ϴ� ���
SELECT * FROM EMP WHERE ENAME BETWEEN 'A' AND 'D' AND ENAME!='D';
-- �μ���ȣ(DEPTNO)�� 10, 20�� ����� ��� �ʵ�
SELECT * FROM EMP WHERE DEPTNO=10 OR DEPTNO=20;
SELECT * FROM EMP WHERE DEPTNO IN (10,20);
SELECT * FROM EMP WHERE DEPTNO NOT IN (10,20); 
-- EMPNO�� 7902, 7788, 7566�� ����� ��� �ʵ�
SELECT * FROM EMP WHERE EMPNO IN (7902,7788,7566);
-- �̸��� M���� �����ϴ� ����� ��� �ʵ�
SELECT * FROM EMP WHERE ENAME LIKE 'M%'; --%:0���� �̻� / _:�ѱ��� (���ڳ� ��¥���� ����)
-- �̸��� N�� ���� ����� ��� �ʵ�
SELECT * FROM EMP WHERE ENAME LIKE '%N%';
-- �̸��� S�� ������ ����� ��� �ʵ�
SELECT * FROM EMP WHERE ENAME LIKE '%S';
-- �̸��� %�� ���� ����� ��� �ʵ�
INSERT INTO EMP VALUES (9999, 'A%', NULL, NULL, NULL, 1000, 1000, 40); --�̸��� %�� ����ִ� ��� ���� �Է�
SELECT * FROM EMP WHERE ENAME LIKE '%\%%' ESCAPE '\';
ROLLBACK; --DML(������ ���۾�)�� ���(�̸��� %�� �� �ִ� ��� ����)
SELECT * FROM EMP;
-- SAL�� 5�� ������ ����� ��� �ʵ�
SELECT * FROM EMP WHERE SAL LIKE '%5'; --���ڿ����� ��� ����
DESC EMP; -- Ÿ�� Ȯ��
-- �Ի�⵵�� 82���� ����� ��� �ʵ�
SELECT * FROM EMP WHERE HIREDATE LIKE '82%'; --��¥������ ��� ����
SELECT * FROM EMP WHERE HIREDATE 
    BETWEEN TO_DATE('1982/01/01', 'YYYY/MM/DD') AND TO_DATE('1982/12/31', 'YYYY/MM/DD'); --Ÿ������ �ѱ��� �ƴ� ��쿡�� ����ϱ� ����
-- 1���� �Ի��� ����� ��� �ʵ�
SELECT * FROM EMP WHERE HIREDATE LIKE '__/01/__';
-- �󿩱��� ���� ����� ��� �ʵ� -- NULL�� IS NULL, IS NOT NULL�θ� ���� (=NULL �Ұ���)
SELECT * FROM EMP WHERE COMM IS NULL OR COMM=0;
-- �󿩱��� �ִ� ����� ��� �ʵ�
SELECT * FROM EMP WHERE COMM IS NOT NULL AND NOT COMM=0;
SELECT * FROM EMP WHERE COMM IS NOT NULL AND COMM!=0;
-- 09. ����(��������, ��������)
SELECT ENAME, SAL FROM EMP ORDER BY SAL ASC; --�޿� ��������(�⺻��) ����
SELECT ENAME, SAL FROM EMP ORDER BY SAL; --�޿� �������� ����
SELECT ENAME, SAL FROM EMP ORDER BY SAL DESC; -- �޿� �������� ����
-- SAL�� ���� ������ ���(��, ���� SAL�� ��� �Ի��� �ֽż����� ����, �Ի����� ���� ��� �̸������� ����)
SELECT * FROM EMP ORDER BY SAL DESC, HIREDATE DESC, ENAME;
-- �̸�, ����(SAL*12+COMM)�� ���(������ ���� ������)
SELECT ENAME, SAL*12+NVL(COMM,0) ���� FROM EMP ORDER BY ���� DESC;
SELECT ENAME, SAL*12+NVL(COMM,0) ���� FROM EMP ORDER BY SAL*12+NVL(COMM,0) DESC;
-- ������ 20000�̻��� ������ �̸�, ������ ���(������ ���� ��)
    -- ORDER BY �������� �ʵ庰�� ��� ����, WHERE �������� �ʵ庰�� ��� �Ұ�
    -- WHERE -> ALIAS -> ORDER BY -> SELECT ������ ����
SELECT ENAME, SAL*12+NVL(COMM,0) ���� FROM EMP 
    WHERE SAL*12+NVL(COMM,0)>=20000 
    ORDER BY ���� DESC;

--�� ��������
--1.	EMP ���̺��� sal�� 3000�̻��� ����� empno, ename, job, sal�� ���
SELECT EMPNO, ENAME, JOB, SAL FROM EMP WHERE SAL>=3000;
--2.	EMP ���̺��� empno�� 7788�� ����� ename�� deptno�� ���
SELECT ENAME, DEPTNO FROM EMP WHERE EMPNO=7788;
--3.	������ 24000�̻��� ���, �̸�, �޿� ��� (�޿�������)
SELECT EMPNO, ENAME, SAL FROM EMP WHERE (SAL*12+NVL(COMM,0))>=24000 ORDER BY SAL;
--4.	EMP ���̺��� hiredate�� 1981�� 2�� 20�� 1981�� 5�� 1�� ���̿� �Ի��� ����� 
--ename,job,hiredate�� ����ϴ� SELECT ������ �ۼ� (�� hiredate ������ ���)
SELECT ENAME, JOB, HIREDATE FROM EMP 
    WHERE HIREDATE BETWEEN '1981/02/20' AND '1981/05/01' 
    ORDER BY HIREDATE;
--5.	EMP ���̺��� deptno�� 10,20�� ����� ��� ������ ��� (�� ename������ ����)
SELECT * FROM EMP WHERE DEPTNO IN (10,20) ORDER BY ENAME;
--6.	EMP ���̺��� sal�� 1500�̻��̰� deptno�� 10,30�� ����� ename�� sal�� ���
-- (�� HEADING�� employee�� Monthly Salary�� ���)
SELECT ENAME "employee", SAL "Monthly Salary" FROM EMP WHERE SAL>=1500 AND DEPTNO IN (10,30);
--7.	EMP ���̺��� hiredate�� 1982���� ����� ��� ������ ���
SELECT * FROM EMP WHERE HIREDATE LIKE '82%';
--8.	�̸��� ù�ڰ� C����  P�� �����ϴ� ����� �̸�, �޿� �̸��� ����
SELECT ENAME, SAL FROM EMP WHERE ENAME BETWEEN 'C' AND 'Q' AND ENAME!='Q' ORDER BY ENAME;
SELECT ENAME FROM EMP WHERE ENAME BETWEEN 'C' AND 'Q' AND ENAME!='Q' ORDER BY SAL, ENAME;
--9.	EMP ���̺��� comm�� sal���� 10%�� ���� ��� ����� ���Ͽ� �̸�, �޿�, �󿩱��� 
--����ϴ� SELECT ���� �ۼ�
SELECT ENAME, SAL, COMM FROM EMP WHERE COMM>SAL*1.1;
--10.	EMP ���̺��� job�� CLERK�̰ų� ANALYST�̰� sal�� 1000,3000,5000�� �ƴ� ��� ����� ������ ���
SELECT * FROM EMP WHERE JOB IN ('CLERK', 'ANALYST') AND SAL NOT IN (1000,3000,5000);
--11.	EMP ���̺��� ename�� L�� �� �ڰ� �ְ� deptno�� 30�̰ų� �Ǵ� mgr�� 7782�� ����� 
--��� ������ ����ϴ� SELECT ���� �ۼ��Ͽ���.
SELECT * FROM EMP WHERE ENAME LIKE '%L%L%' AND DEPTNO=30 OR MGR=7782;
--12.	��� ���̺��� �Ի����� 81�⵵�� ������ ���,�����, �Ի���, ����, �޿��� ���
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP WHERE HIREDATE LIKE '81%';
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP 
    WHERE TO_CHAR(HIREDATE, 'YY') = '81';
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP 
    WHERE HIREDATE BETWEEN TO_DATE('1981/01/01', 'YYYY/MM/DD/') 
                        AND TO_DATE('1981/12/31', 'YYYY/MM/DD');
--13.	��� ���̺��� �Ի�����81���̰� ������ 'SALESMAN'�� �ƴ� ������ ���, �����, �Ի���, 
-- ����, �޿��� �˻��Ͻÿ�.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP 
    WHERE HIREDATE LIKE '81%' AND JOB<>'SALESMAN';
--14.	��� ���̺��� ���, �����, �Ի���, ����, �޿��� �޿��� ���� ������ �����ϰ�, 
-- �޿��� ������ �Ի����� ���� ������� �����Ͻÿ�.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP ORDER BY SAL DESC, HIREDATE;
--15.	��� ���̺��� ������� �� ��° ���ĺ��� 'N'�� ����� ���, ������� �˻��Ͻÿ�
SELECT EMPNO, ENAME FROM EMP WHERE ENAME LIKE '__N%';
--16.	��� ���̺�������(SAL*12)�� 35000 �̻��� ���, �����, ������ �˻� �Ͻÿ�.
SELECT EMPNO, ENAME, SAL*12 ���� FROM EMP WHERE SAL*12>=35000;
