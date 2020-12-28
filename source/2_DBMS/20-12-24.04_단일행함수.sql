-- 2020-12-24 DBMS_05.������ �Լ�   ��cherryuki(ji)
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

-- 2020-12-28 DBMS_������ �Լ�   ��cherryuki(ji)
-- 4) ����ȯ �Լ�
-- TO_CHAR(��¥, ����); ��¥���� ���Ͽ� �°� ���������� ��ȯ
    -- YY(�⵵) MM(��) MON(N�� ex:12��) DD(��) DY(����)
    -- HH24(0~23��) AM(����/����) HH(0~11��) MI(��) SS(��)
SELECT ENAME, TO_CHAR(HIREDATE, 'YYYY-MM-DD') FROM EMP;
SELECT ENAME, TO_CHAR(HIREDATE, 'YYYY"��"MM"��"DD"��" DY"����"') FROM EMP;
SELECT ENAME, TO_CHAR(SYSDATE, 'YY"��"MONDD"��" AMHH"��"MI"��"SS"��"') FROM EMP;

-- TO_CHAR(����, ����); ���ڰ��� ���Ͽ� �°� ���ڷ� ����ȯ
    -- ���� �� 0: �ڸ���, �ڸ����� ���� ������ 0���� ä��
    -- ���� �� 9: �ڸ���, �ڸ����� ���� ������ ä���� ����(�ڹٿ����� #)
    -- ���� �� $: ��ȭ ����, $�� ���� �տ� ����
    -- ���� �� L: ������ȭ ������ ���� �տ� ����
SELECT ENAME, TO_CHAR(SAL, 'L999,999') SAL FROM EMP;
SELECT ENAME, TO_CHAR(SAL, '$9,999') SAL FROM EMP;
SELECT ENAME, TO_CHAR(SAL, '$000,000') SAL FROM EMP;

-- TO_DATE(����, ����); '81/01/01' ���ڸ� ���Ͽ� �°� ��¥������ ����ȯ
-- 81/05/01~83/05/01 ���̿� �Ի��� ���� ���
SELECT * FROM EMP
    WHERE HIREDATE BETWEEN '81/05/01' AND '83/05/01';
SELECT * FROM EMP 
    WHERE HIREDATE BETWEEN TO_DATE('19810501', 'YY/MM/DD') AND TO_DATE('19830501', 'YY/MM/DD'); --���� 4�ڸ���
-- 2020�� 11�� 30�Ϻ��� ������� ��¥���� ���(�ý����� ��¥�� ���� ��)
SELECT TRUNC(SYSDATE-TO_DATE('2020/11/30', 'YYYY/MM/DD')) ����� FROM DUAL; --28��(����)
SELECT CEIL(SYSDATE-TO_DATE('2020-11-30', 'YYYY-MM-DD')) ����� FROM DUAL; --29��(�ø�)
SELECT * FROM EMP WHERE TO_CHAR(HIREDATE, 'YY/MM/DD') BETWEEN '81/05/01' AND '83/05/01';

-- TO_NUMBER(����, ����); ���ڸ� ���Ͽ� �°� ���������� ��ȯ
SELECT TO_NUMBER('1,000', '9,999') FROM DUAL;
SELECT TO_NUMBER('1,000', '9,999')*1.1 FROM DUAL;

-- 5) NULL ���� �Լ�: NVL(NULL�� ���� �ִ� ������, NULL�̸� ����� ��) --�Ű����� 2���� Ÿ���� ��ġ�ؾ� ��
-- ��� �̸�, ���� ����� �̸�(���� ��簡 ������ CEO ���)
SELECT W.ENAME "�����", NVL(M.ENAME, 'CEO') "���� ����" 
    FROM EMP W, EMP M
    WHERE W.MGR=M.EMPNO(+);
-- ��� �̸�, ���� ����� ���(���� ��簡 ������ CEO ���)
SELECT ENAME, NVL(TO_CHAR(MGR), 'CEO') MGR FROM EMP; --CEO�� ���ڷ� �ٲ� �� �����Ƿ� MGR(����)�� ���ڷ� ����ȯ

-- 6) DECODE(������, ��1, ���1, ��2, ���2, ..., ��N, ���N, �� �� ���)
-- �̸�, �μ���ȣ, �μ��̸�
SELECT ENAME, EMPNO, DNAME 
    FROM EMP E, DEPT D
    WHERE E.DEPTNO=D.DEPTNO; --EQUI JOIN
SELECT ENAME, DEPTNO, 
    DECODE(DEPTNO, 10, 'ACCOUNTING', 20, 'RESEARCH', 30, 'SALES', 40, 'OPERATIONS', 'ETC') DNAME 
    FROM EMP;
-- DECODE�� �����ϰ� ����� �� �ִ� CASE
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

-- �̸�, �޿�, �λ� ���� �޿� ���(DECODE, CASE)
  -- JOB�� ���� �λ���: 'ANALYST' 10% �λ�, 'MANAGER' 20% �λ�, 'PRESIDENT' 30% �λ�, 'SALESMAN' 40% �λ�, 'CLERK' �λ�X
SELECT ENAME, SAL "���� �޿�", 
    DECODE(JOB, 'ANALYST', SAL*1.1, 'MANAGER', SAL*1.2, 
                'PRESIDENT', SAL*1.3, 'SALESMAN', SAL*1.4, 'CLERK', SAL) "�λ� ���� �޿�" 
    FROM EMP;
SELECT ENAME, SAL "���� �޿�", 
    DECODE(JOB, 'ANALYST', SAL*1.1, 'MANAGER', SAL*1.2, 
                'PRESIDENT', SAL*1.3, 'SALESMAN', SAL*1.4, SAL) "�λ� ���� �޿�" 
    FROM EMP;
SELECT ENAME, SAL "���� �޿�", 
    CASE JOB WHEN 'ANALYST' THEN SAL*1.1
             WHEN 'MANAGER' THEN SAL*1.2
             WHEN 'PRESIDENT' THEN SAL*1.3
             WHEN 'SALESMAN' THEN SAL*1.4
             WHEN 'CLERK' THEN SAL
    END AS "�λ� ���� �޿�" FROM EMP;

-- 7) �� ��: EXTRACT, LEVEL�� ���
SELECT EXTRACT(YEAR FROM HIREDATE) YEAR FROM EMP;
SELECT TO_CHAR(HIREDATE, 'YYYY') YEAR FROM EMP;
SELECT EXTRACT(MONTH FROM HIREDATE) MONTH FROM EMP;
SELECT TO_CHAR(HIREDATE, 'MM') MONTH FROM EMP;
-- LEVEL, START WITH(�ֻ��� ������ ����), CONNECT BY PRIOR(���Ϸ��� ���� ����)
SELECT LEVEL, LPAD(' ', LEVEL*2)||ENAME, MGR FROM EMP
    START WITH MGR IS NULL
    CONNECT BY PRIOR EMPNO=MGR;
    
-- <�� ��������>
-- 1. ���� ��¥�� ����ϰ� TITLE�� ��Current Date���� ����ϴ� SELECT ������ ����Ͻÿ�.
SELECT SYSDATE "Current Date" FROM DUAL;
-- 2. EMP ���̺��� ���� �޿��� 15%�� ������ �޿��� ����Ͽ�,
-- �����ȣ,�̸�,����,�޿�,������ �޿�(New Salary),������(Increase)�� ����ϴ� SELECT ����
SELECT EMPNO, ENAME, JOB, SAL, SAL*1.15 "New Salary", SAL*0.15 "Increase" FROM EMP;
--3. �̸�, �Ի���, �Ի��Ϸκ��� 6���� �� ���ƿ��� ������ ���Ͽ� ����ϴ� SELECT ������ ����Ͻÿ�.
SELECT ENAME, HIREDATE, NEXT_DAY(ADD_MONTHS(HIREDATE, 6), '��') "6���� �� ������" FROM EMP;
--4. �̸�, �Ի���, �Ի��Ϸκ��� ��������� ������, �޿�, �Ի��Ϻ��� ��������� ���� �޿��� �Ѱ踦 ���
SELECT ENAME, HIREDATE, TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE)) �ټӿ���, 
    SAL, SAL*TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE)) "�޿� �Ѱ�" FROM EMP;
--5. ��� ����� �̸��� �޿�(15�ڸ��� ��� ������ �� ���� ��*���� ��ġ)�� ���
SELECT ENAME, LPAD(SAL, 15, '*') �޿� FROM EMP;
--6. ��� ����� ������ �̸�,����,�Ի���,�Ի��� ������ ����ϴ� SELECT ������ ����Ͻÿ�.
SELECT ENAME, JOB, HIREDATE, TO_CHAR(HIREDATE, 'DY"����"') "�Ի��� ����" FROM EMP;
--7. �̸��� ���̰� 6�� �̻��� ����� ������ �̸�,�̸��� ���ڼ�,������ ���
SELECT ENAME, LENGTH(ENAME), JOB
    FROM EMP
    WHERE LENGTH(ENAME)>=6;
--8. ��� ����� ������ �̸�, ����, �޿�, ���ʽ�, �޿�+���ʽ��� ���
SELECT ENAME, JOB, SAL, COMM, SAL+NVL(COMM,0) "�޿�+���ʽ�" FROM EMP;
-- 9.��� ���̺��� ������� 2��° ���ں��� 3���� ���ڸ� �����Ͻÿ�. 
SELECT SUBSTR(ENAME, 2, 3) FROM EMP;
--10. ��� ���̺��� �Ի����� 12���� ����� ���, �����, �Ի����� �˻��Ͻÿ�. 
SELECT EMPNO, ENAME, HIREDATE FROM EMP
    WHERE TO_CHAR(HIREDATE, 'MM')=12;
SELECT EMPNO, ENAME, HIREDATE FROM EMP
    WHERE EXTRACT(MONTH FROM HIREDATE)=12;
--11. ������ ���� ����� �˻��� �� �ִ� SQL ������ �ۼ��Ͻÿ�
--EMPNO		ENAME		�޿�
--7369		SMITH		*******800
--7499		ALLEN		******1600
--7521		WARD		******1250
SELECT EMPNO, ENAME, LPAD(SAL, 10, '*') �޿� FROM EMP;
-- 12. ������ ���� ����� �˻��� �� �ִ� SQL ������ �ۼ��Ͻÿ�
-- EMPNO	 ENAME 	�Ի���
-- 7369	  SMITH		1980-12-17
-- ��.
SELECT EMPNO, ENAME, TO_CHAR(HIREDATE, 'YYYY-MM-DD') �Ի��� FROM EMP;
--13. ��� ���̺��� �μ� ��ȣ�� 20�� ����� ���, �̸�, ����, �޿��� ����Ͻÿ�.
    --(�޿��� �տ� $�� �����ϰ�3�ڸ����� ,�� ����Ѵ�)
SELECT EMPNO, ENAME, JOB, TO_CHAR(SAL, '$9,999') �޿� 
    FROM EMP 
    WHERE DEPTNO=20;
-- 14. ��� ���̺��� �޿��� ���� ���, �̸�, �޿�, ����� �˻��ϴ� SQL ������ �ۼ� �Ͻ� ��.
-- �޿��� 0~1000 E / 1001~2000 D / 2001~3000 C / 3001~4000 B / 4001~5000 A
SELECT EMPNO, ENAME, SAL, 
    DECODE(TRUNC((SAL-1)/1000), 0, 'E', 1, 'D', 2, 'C', 3, 'B', 4, 'A') ���
    FROM EMP;
SELECT EMPNO, ENAME, SAL,
    CASE TRUNC((SAL-1)/1000) WHEN 0 THEN 'E'
                             WHEN 1 THEN 'D'
                             WHEN 2 THEN 'C'
                             WHEN 3 THEN 'B'
                             WHEN 4 THEN 'A'
    END AS "���"
    FROM EMP;
SELECT EMPNO, ENAME, SAL,
    CASE WHEN SAL BETWEEN 0 AND 1000 THEN 'E'
         WHEN SAL BETWEEN 1001 AND 2000 THEN 'D'
         WHEN SAL BETWEEN 2001 AND 3000 THEN 'C'
         WHEN SAL BETWEEN 3001 AND 4000 THEN 'B'
         WHEN SAL BETWEEN 4001 AND 5000 THEN 'A'
    END "���"
    FROM EMP;