-- 2020-12-31 DBMS_07.DCL   ��cherryuki(ji)
SHOW USER; -- KIM�������� ���� ��
SELECT * FROM TAB;
SELECT * FROM DBA_TABLES; --DBA������ �ƴϹǷ� ���� �Ұ�
SELECT * FROM USER_TABLES; -- �� ������ ������ ���̺� ����
SELECT * FROM ALL_TABLES; --�� �������� ���� ������ ���̺� ����
SELECT * FROM ALL_TABLES WHERE TABLE_NAME='EMP';
SELECT * FROM SCOTT.EMP; --�� ������ ������ ���̺��� �ƴϹǷ� '�����ڸ�.���̺��'���� �Է��ؾ� ��
EXIT; --���� ����

SHOW USER;
SELECT * FROM SCOTT.EMP; --���� ��Ż �� ���� �Ұ�
EXIT;