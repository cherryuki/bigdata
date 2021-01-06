package com.lec.ex02_selectWhere;
//21-01-06_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

//사용자에게 원하는 부서명을 입력 받아 해당 부서정보 및 리스트(사번, 이름, 급여, 급여등급) 출력
public class SelectWhereDname2 {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Connection conn = null;
		Statement  stmt = null;
		ResultSet  rs	= null;
		Scanner sc = new Scanner(System.in);
		System.out.print("조회하고자 하는 부서명을 입력하세요: ");
		String dname = sc.next().trim().toUpperCase();
		String sql1 = "SELECT * FROM DEPT WHERE DNAME='"+dname+"'";
		String sql2 = String.format("SELECT EMPNO, ENAME, SAL, GRADE FROM EMP E, DEPT D, SALGRADE" + 
				"    WHERE E.DEPTNO=D.DEPTNO AND SAL BETWEEN LOSAL AND HISAL AND DNAME='%s'", dname);
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, "scott", "tiger");
			stmt = conn.createStatement();
			rs = stmt.executeQuery(sql1);
			if(rs.next()) {
				System.out.println("부서번호: "+rs.getInt("deptno"));
				System.out.println("부서명: "+dname);
				System.out.println("부서 위치:"+rs.getString("loc"));
				rs.close();
				rs = stmt.executeQuery(sql2);
				if(rs.next()) {
					System.out.println("사번\t이름\t급여\t등급");
					do {
						int empno = rs.getInt(1);
						String ename = rs.getString(2);
						int sal = rs.getInt("sal");
						int grade = rs.getInt(4);
						System.out.printf("%d\t%s\t%d\t%d\n", empno, ename, sal, grade);
					} while(rs.next());
				} else {
					System.out.println("현재 해당 부서에는 사원이 없습니다");
				}
			} else {
				System.out.println("해당 부서는 존재하지 않습니다");
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
