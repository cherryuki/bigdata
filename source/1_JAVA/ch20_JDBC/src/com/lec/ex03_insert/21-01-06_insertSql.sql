-- 21-01-06_JDBC		(c)cherryuki(ji)
INSERT INTO DEPT VALUES(50, 'IT', 'SEOUL');
SELECT * FROM DEPT;

SELECT * FROM DEPT WHERE DEPTNO=10;
ROLLBACK;
SELECT * FROM DEPT;

