package com.lec.ex02_selectWhere;
//21-01-06_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

/* 사용자에게 원하는 부서번호를 입력받아
 * (1) 해당 부서번호가 존재하는 경우: 부서정보 출력
 * (2) 해당 부서에 사원이 존재할 경우 리스트(사번, 이름, 급여, 상사명) 출력, 존재하지 않을 경우 사원 없음 출력
 * (3) 해당 부서번호가 존재하지 않을 경우: 존재하지 않는 부서번호라고 출력
 */
public class SelectWhereDeptno2 {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Connection conn = null;
		Statement  stmt = null;
		ResultSet  rs	= null;
		Scanner sc = new Scanner(System.in);
		System.out.print("조회하고자 하는 부서번호를 입력하세요: ");
		int deptno = sc.nextInt();
		String sql1 = "SELECT * FROM DEPT WHERE DEPTNO="+deptno;
		String sql2 = "SELECT EMPNO, ENAME, SAL, (SELECT ENAME FROM EMP WHERE E.MGR=EMPNO) MGRNAME FROM EMP E WHERE DEPTNO="+deptno;
		//"SELECT W.EMPNO, W.ENAME, W.SAL, M.ENAME MGRNAME FROM EMP W, EMP M WHERE W.MGR=M.EMPNO(+) AND W.DEPTNO="+deptno; //같은 결과(직속 상사 없는 사람까지 출력)
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, "scott", "tiger");
			stmt = conn.createStatement();
			rs = stmt.executeQuery(sql1);
			if(rs.next()) {
				System.out.println("부서번호: "+deptno);
				System.out.println("부서명: "+rs.getString("dname"));
				System.out.println("부서 위치:"+rs.getString("loc"));
				rs.close();
				rs = stmt.executeQuery(sql2);
				if(rs.next()) {
					System.out.println("사번\t이름\t급여\t상사명");
					do {
						int empno = rs.getInt("empno");
						String ename = rs.getString("ename");
						int sal = rs.getInt("sal");
						String mgrname = rs.getString("mgrname");
						System.out.printf("%d\t%s\t%d\t%s\n", empno, ename, sal, mgrname);
					} while(rs.next());
				} else {
					System.out.println(deptno+"번 부서에는 사원이 없습니다");
				}
			} else {
				System.out.println(deptno+"번 부서는 존재하지 않습니다");
			}
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			sc.close();
			try {
				if(rs!=null) rs.close();
				if(stmt!=null) stmt.close();
				if(conn!=null) conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
