-- 21-01-07 JDBC_Update		(c)cherryuki(ji)

SELECT * FROM DEPT;
UPDATE DEPT SET DNAME='CRM', LOC='PUSAN' WHERE DEPTNO=60;
ROLLBACK;
SELECT * FROM DEPT WHERE DEPTNO=60;