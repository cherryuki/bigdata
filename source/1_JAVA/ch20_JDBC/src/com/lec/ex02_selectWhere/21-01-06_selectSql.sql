-- 21-01-06_JDBC		(c)cherryuki(ji)

SELECT * FROM DEPT WHERE DEPTNO=10;
SELECT EMPNO, ENAME, SAL, (SELECT ENAME FROM EMP WHERE E.MGR=EMPNO(+)) MGRNAME FROM EMP E WHERE DEPTNO=10;
SELECT W.EMPNO, W.ENAME, W.SAL, M.ENAME MGRNAME FROM EMP W, EMP M WHERE W.MGR=M.EMPNO AND W.DEPTNO=10; 

SELECT * FROM DEPT WHERE DNAME='RESEARCH';
SELECT EMPNO, ENAME, SAL, GRADE FROM EMP E, DEPT D, SALGRADE 
    WHERE E.DEPTNO=D.DEPTNO AND SAL BETWEEN LOSAL AND HISAL AND DNAME='SALES';
SELECT EMPNO, ENAME, SAL, GRADE FROM EMP, SALGRADE
    WHERE SAL BETWEEN LOSAL AND HISAL AND DEPTNO=(SELECT DEPTNO FROM DEPT WHERE DNAME='RESEARCH');
    
SELECT * FROM DEPT;

-- 21-01-07 JDBC_SELECT  (c)cherryuki(ji)
SELECT EMPNO, ENAME, JOB, SAL FROM EMP WHERE DEPTNO=(SELECT DEPTNO FROM DEPT WHERE DNAME='SALES');
SELECT EMPNO, ENAME, JOB, SAL FROM EMP E, DEPT D WHERE E.DEPTNO=D.DEPTNO AND DNAME='SALES';