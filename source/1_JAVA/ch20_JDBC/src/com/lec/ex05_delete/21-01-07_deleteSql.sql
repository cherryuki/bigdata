-- 21-01-07 JDBC_Delete		(c)cherryuki(ji)

SELECT * FROM DEPT;
DELETE FROM DEPT WHERE DEPTNO=60;
ROLLBACK;
SELECT * FROM DEPT WHERE DEPTNO=50;