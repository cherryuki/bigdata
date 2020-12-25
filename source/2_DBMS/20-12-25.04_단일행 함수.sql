-- 2020-12-24 DBMS_������ �Լ�(1)   ��cherryuki(ji)
-- [IV] ������ �Լ�
-- �Լ�: ������ �Լ�, �׷��Լ�([V] ����)
SELECT HIREDATE, TO_CHAR(HIREDATE, 'YY"��"MM"��"DD"��"') �Ի����� FROM EMP;
SELECT ENAME, INITCAP(ENAME) FROM EMP; -- ������ �Լ�
SELECT SUM(SAL) FROM EMP; --�׷� �Լ�(���� ���� ����� �ϳ��� ������ ��Ÿ��) --[V] �׷��Լ� ����
SELECT DEPTNO, SUM(SAL) FROM EMP GROUP BY DEPTNO; --�׷� �Լ�(���� ���� ����� �׷����� ��� ��Ÿ��)
-- EX) ���� �Լ�, ���� �Լ�, ��¥ �Լ�, ����ȯ �Լ�, NVL(), ETC

-- 1) ���� �Լ�
DESC DUAL; --����Ŭ���� �����ϴ� 1�� 1��¥�� DEUMMY TABLE(�����̺� �Է���)
-- ���밪
SELECT ABS(-9) FROM DUAL; 
-- ����, �ø�, �ݿø� -- ROUND(������, -e^n); �����͸� -e(1/10)�� n�ڸ����� ��Ÿ��  
SELECT FLOOR(1234.567) FROM DUAL; --�Ҽ��� ù°�ڸ����� ����(���� �ڸ����� ��Ÿ��)
SELECT FLOOR(1234.567*10)/10 FROM DUAL; --�Ҽ��� ��°�ڸ����� ����
SELECT TRUNC(1234.567) FROM DUAL; --�Ҽ��� ù°�ڸ����� ����(���� �ڸ����� ��Ÿ��)
SELECT TRUNC(1234.567, 0) FROM DUAL; --0�� �⺻������ ���� ����(1/10(-e)�� 0��(1�� �ڸ�)���� ��Ÿ��)
SELECT TRUNC(1234.567, 1) FROM DUAL; -- �Ҽ��� ��°�ڸ� ����(1/10�� 1��(�Ҽ��� ù°�ڸ�)���� ��Ÿ��)
SELECT TRUNC(1234.567, -1) FROM DUAL; -- ���� �ڸ� ����(1/10�� -1��=10�� �ڸ����� ��Ÿ��)
-- EMP ���̺��� �̸�, �޿�(���� �ڸ����� ����=���� �ڸ����� ��Ÿ��)
SELECT ENAME, TRUNC(SAL, -2) FROM EMP; 
SELECT CEIL(1234.567) FROM DUAL; -- �Ҽ��� ù°�ڸ����� �ø�(���� �ڸ����� ��Ÿ��)
SELECT ROUND(1234.567) FROM DUAL; -- �Ҽ��� ù°�ڸ����� �ݿø�(���� �ڸ����� ��Ÿ��)
SELECT ROUND(1234.567, 1) FROM DUAL; -- �Ҽ��� ��°�ڸ����� �ݿø�(�Ҽ��� ù°�ڸ����� ��Ÿ��)
SELECT ROUND(1234.567, -1) FROM DUAL; --���� �ڸ����� �ݿø�(10���ڸ����� ��Ÿ��)

SELECT FLOOR(10/4) FROM DUAL;
SELECT MOD(9,2) FROM DUAL; -- ������ ����
SELECT MOD('9', 2) FROM DUAL; -- 9/2�� ������
-- Ȧ���޿� �Ի��� �������� ��� �ʵ�
SELECT * FROM EMP WHERE MOD(TO_CHAR(HIREDATE, 'MM'),2)=1;

-- 2) ���� ó�� �Լ�
SELECT UPPER('abcABC') FROM DUAL; --���� �빮�ڷ�
SELECT LOWER('abcABC') FROM DUAL; --���� �ҹ��ڷ�
SELECT INITCAP('abcABC') FROM DUAL; --ù���ڸ� �빮��(�̴ϼ� ĸ), �ڿ��� �ҹ��ڷ�
-- JOB�� MANAGER�� ������ ��� �ʵ�
SELECT * FROM EMP WHERE UPPER(JOB)='MANAGER';
SELECT EMPNO, INITCAP(ENAME) FROM EMP;
-- ���� ����
SELECT 'AB'||'CD'||'EF'||'GH' FROM DUAL;
SELECT CONCAT(CONCAT('AB','CD'),CONCAT('EF','GH')) FROM DUAL;
--- XXX�� XX��(ENAME�� JOB�̴�)
SELECT ENAME||'�� '||JOB||'�̴�' FROM EMP;
SELECT CONCAT(CONCAT(ENAME, '�� '), CONCAT(JOB, '�̴�')) FROM EMP;
-- SUBSTR(STR, ������ġ, ���� ��) --ù ��ġ�� 1����(JAVA�� 0����)
-- SUBSTRB(STR, ������ġ, ���� ����Ʈ ��)
SELECT SUBSTR('WELCOME TO ORACLE', 3, 2) FROM DUAL; --LC(3��° ���� 2����)
SELECT SUBSTRB('WELCOME TO ORACLE', 3, 2) FROM DUAL; --LC(3��°BYTE���� 2BYTE) --������ ��� 1����=1BYTE���� ����
SELECT SUBSTR('�޸�ũ��������', 4, 3) FROM DUAL; --������(4��° ���ں��� 3����)
SELECT SUBSTRB('�޸�ũ��������', 4, 3) FROM DUAL; --��(4��°BYTE���� 3BYTE)
-- ����� �� ����(����)=1BYTE, �ѱ��� �� ����(����)=3BYTE 
-- 9���� �Ի��� ����� ��� �ʵ� 81/01/01
SELECT * FROM EMP WHERE SUBSTR(HIREDATE, 4, 2)='09';
SELECT SUBSTR('02-123-0000', -4, 4) FROM DUAL; --��ȭ��ȣ �� 4�ڸ�
-- ���� �� ���� ���
--  1  2  3  4  5  6  (�տ������� �� ��)
-- -6 -5 -4 -3 -2 -1  (�ڿ������� �� ��)

-- 9�Ͽ� �Ի��� ����� ��� �ʵ� 
SELECT * FROM EMP WHERE SUBSTR(HIREDATE, -2, 2)='09';
SELECT LENGTH('ORACLE') FROM DUAL; --���� ��:4
SELECT LENGTHB('ORACLE') FROM DUAL; --BYTE��: 4 (����� 1����=1BYTE)
SELECT LENGTH('����Ŭ') FROM DUAL; --���� ��:3
SELECT LENGTHB('����Ŭ') FROM DUAL; --BYTE��: 9 (�ѱ��� 1����=3BYTE)
DESC DEPT;
-- INSTR(STR, ã�� ����); STR���� ã�� ������ ù ��ġ(1���� ī��Ʈ), ������ 0���
-- INSTR(STR, ã�� ����, ���� ��ġ); STR���� ������ġ���� ã�Ƽ� ã�� ������ ��ġ(1���� ī��Ʈ), ������ 0
SELECT INSTR('ABCABC', 'B') FROM DUAL; --2
SELECT INSTR('ABCABC', 'B', 3) FROM DUAL; --5
-- 9���� �Ի��� ��� ����(INSTR �̿�)
SELECT * FROM EMP WHERE INSTR(HIREDATE, '09')=4;
-- 9�Ͽ� �Ի��� ��� ����(INSTR �̿�)
SELECT * FROM EMP WHERE INSTR(HIREDATE, '09')=7;
-- LPADE(����, �ڸ���, '*'); ���ڿ� *�� �ڸ��� ��ŭ Ȯ��(*�� ���� ����(L)���� ä��)
SELECT LPAD('ORACLE', 10, '#') FROM DUAL; --####ORACLE
SELECT RPAD('ORACLE', 10, '*') FROM DUAL; --ORACLE**** --������(R) ���ڸ��� *�� ä��
SELECT ENAME, LPAD(SAL, 6, '*') FROM EMP;
-- ���, �̸��� ù���ڸ� ����ϰ� �������� *�� ���(S****)
SELECT EMPNO, RPAD(SUBSTR(ENAME, 1, 1), LENGTH(ENAME), '*') NAME FROM EMP;
-- ���, �̸�(S*****), �Ի���(80/12/**) ���
SELECT EMPNO ���, RPAD(SUBSTR(ENAME, 1, 1), LENGTH(ENAME), '*') �̸�, 
    RPAD(SUBSTR(HIREDATE, 1, 6), LENGTH(HIREDATE), '*') �Ի����� FROM EMP;
-- ���, �̸�(****H), �Ի���(80/12/**) ���
SELECT EMPNO, LPAD(SUBSTR(ENAME, -1, 1), LENGTH(ENAME), '*') �̸�, 
    RPAD(SUBSTR(HIREDATE, 1, 6), LENGTH(HIREDATE), '*') �Ի����� FROM EMP;
-- �̸��� ����° �ڸ��� R�� ��� ���(INSTR, SUBSTR, LIKE)
SELECT * FROM EMP WHERE INSTR(ENAME, 'R')=3;
SELECT * FROM EMP WHERE SUBSTR(ENAME, 3, 1)='R';
SELECT * FROM EMP WHERE ENAME LIKE '__R%';
SELECT TRIM('        ORACLE DB    ') FROM DUAL; --�� ���� SPACE ����(���� ���� SPACE�� �״��)
SELECT LTRIM('       ORACLE DB    ') FROM DUAL;  --����(��) SPACE ����
SELECT RTRIM('       ORACLE DB    ') FROM DUAL;  --������(��) SPACE ����
SELECT REPLACE(ENAME, 'A', 'XX') FROM EMP;

-- 3) ��¥ ���� �����, �Լ�
SELECT SYSDATE FROM DUAL; --����(��¥ �� �ð�)
SELECT TO_CHAR(SYSDATE, 'YY-MM-DD HH24:MI:SS') "���� ��¥ �� �ð�" FROM DUAL;
SELECT SYSDATE-1 ����, SYSDATE ����, SYSDATE+1 ���� FROM DUAL; --��¥���� ���� ����
-- 14�� ��
SELECT SYSDATE+14 FROM DUAL;

-- �̸�, �Ի���, �ٹ����� ���
SELECT ENAME, HIREDATE, TRUNC(SYSDATE-HIREDATE) �ټ��ϼ� FROM EMP;
SELECT ENAME, HIREDATE, FLOOR(SYSDATE-HIREDATE) �ټ��ϼ� FROM EMP;
-- �̸�, �Ի���, �ٹ��ּ�, �ٹ���� ���
SELECT ENAME, HIREDATE, TRUNC((SYSDATE-HIREDATE)/7) �ٹ��ּ�, 
    FLOOR((SYSDATE-HIREDATE)/365) �ٹ���� FROM EMP;
-- MONTHS_BETWEEN(): Ư���� �� ���� ������ ���� ��
-- �̸�, �Ի���, �ٹ�����(MONTHS_BETWEEN �Լ� ���)
SELECT ENAME, HIREDATE, TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE)) �ٹ����� FROM EMP;
-- ADD_MONTHS(Ư����¥, ���� ��): Ư���� ��¥�κ��� �� ���� ���� ����
-- �̸�, �Ի���, �����Ⱓ ������(�����Ⱓ�� 6����)
SELECT ENAME, HIREDATE, ADD_MONTHS(HIREDATE, 6) "�����Ⱓ ������" FROM EMP;
-- NEXT_DAY(Ư����¥, 'E����'): Ư����¥�κ��� ó�� �����ϴ� E����
SELECT NEXT_DAY(SYSDATE, '��') FROM DUAL; 
SELECT NEXT_DAY(SYSDATE, '�Ͽ���') FROM DUAL;
-- LAST_DAY(Ư����¥): Ư����¥�� ���� ���� ����
SELECT LAST_DAY(SYSDATE) FROM DUAL;
-- �̸�, �Ի���, ���޳�(������ ����)
SELECT ENAME, HIREDATE, LAST_DAY(HIREDATE) "ù ���޳�" FROM EMP;
-- ROUND: ��¥ �ݿø�
SELECT ROUND(SYSDATE-30, 'YEAR') FROM DUAL; --���: ����� �⵵ 1�� 1��
SELECT ROUND(SYSDATE-30, 'MONTH') FROM DUAL; --���: ����� �� 1�� --EX: 15�ϱ��� ���, 16�Ϻ��� �Ϳ�
SELECT ROUND(SYSDATE, 'DAY') FROM DUAL; --���: ����� �Ͽ���
SELECT TO_CHAR(ROUND(SYSDATE), 'YY-MM-DD HH24:MI:SS') FROM DUAL; -- ���: ����� �� 0��
SELECT ROUND(SYSDATE) FROM DUAL; --���: ����� ��(0��) EX) ������ ��� ����(0��), ������ ��� ����(0��)
-- TRUNC: ��¥ ����
SELECT TRUNC(SYSDATE-30, 'YEAR') FROM DUAL; --���: ���س⵵ 1�� 1��(���� 1�� 1��)
SELECT TRUNC(SYSDATE-30, 'MONTH') FROM DUAL; --���: ��� 1��(���� 1��)
SELECT TRUNC(SYSDATE, 'DAY') FROM DUAL; --���: ���� �Ͽ���(�ش����ڰ� �Ͽ����� ��� �ش����� ���)
SELECT TO_CHAR(TRUNC(SYSDATE), 'YY-MM-DD HH24:MI:SS') FROM DUAL; --���: ���� 0��(���� 0��)
SELECT TRUNC(SYSDATE) FROM DUAL; --���: ����(0��)

-- ��������
-- EX1. �̸�, �Ի���, �Ի����� ���� ���� 1��
SELECT ENAME, HIREDATE, TRUNC(HIREDATE, 'MONTH') FROM EMP;
-- EX2. �̸�, �Ի���, ���޳�(25��) - 25�� �� �Ի�� �Ի��� �� 25��, 25�� ���ĸ� ���� �� 25��
SELECT ENAME, HIREDATE, ROUND(HIREDATE-9, 'MONTH')+24 "ù ���޳�" FROM EMP;
-- ROUND(�ش糯¥, 'MONTH')�� ��� 15�ϱ����� ��� 1��, 16�Ϻ��ʹ� �Ϳ� 1�Ϸ� ��µ� 
-- 24�ϱ��� �Ի��ϸ� ����� ǥ�õǰ� �Ի���-9��(24-9=15), �޿����� +24��(1+24=25)�� ���(24���� ���޳��� ��� -8, +23)
-- EX3. �̸�, �Ի���, SAL(����), �̶����� ���� ���� ��
SELECT ENAME, HIREDATE, SAL, TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE))*SAL "������ ��" FROM EMP;
-- EX4. �̸�, �Ի���, SAL, COMM, �̶����� ���� ����(SAL*12+COMM)
SELECT ENAME, HIREDATE, SAL, COMM, TRUNC((SYSDATE-HIREDATE)/365)*(SAL*12+NVL(COMM,0)) "������ ��" FROM EMP;