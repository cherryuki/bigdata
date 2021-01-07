package com.lec.ex06_preparedStatement;
//21-01-07_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

//부서명을 입력받아 해당 부서 사원정보 리스트(사번, 이름, 직책, 급여) 콘솔창에 출력
//SELECT EMPNO, ENAME, JOB, SAL FROM EMP E, DEPT D WHERE E.DEPTNO=D.DEPTNO AND DNAME='SALES'
public class SelectWhereDname {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Scanner sc = new Scanner(System.in);
		Connection 		  conn  = null;
		PreparedStatement pstmt = null;
		ResultSet 		  rs	= null;
		String selectSql = "SELECT EMPNO, ENAME, JOB, SAL "
						+ "		FROM EMP E, DEPT D "
						+ "		WHERE E.DEPTNO=D.DEPTNO AND DNAME=?";
		System.out.println("조회하려는 부서명을 입력하세요: ");
		String dname = sc.next().trim().toUpperCase();
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(selectSql);
			pstmt.setString(1, dname); //pstmt.setString(1, sc.next().trim().toUpperCase());
			rs = pstmt.executeQuery();
			if(rs.next()) {
				System.out.println("사번\t이름\t직업\t\t급여\t");
				do {
					int empno = rs.getInt("empno");
					String ename = rs.getString("ename");
					String job = rs.getString("job");
					int sal = rs.getInt(4);
					if(job.length()>7) {
						System.out.println(empno+"\t"+ename+"\t"+job+"\t"+sal);						
					} else {
						System.out.println(empno+"\t"+ename+"\t"+job+"\t\t"+sal);
					}
				} while(rs.next());
			} else {
				System.out.println("없는 부서명이거나 사원이 존재하지 않습니다");
			}
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(rs!=null) rs.close();
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
				sc.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
