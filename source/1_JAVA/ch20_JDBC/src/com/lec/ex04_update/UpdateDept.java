package com.lec.ex04_update;
//21-01-07_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class UpdateDept {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Scanner sc = new Scanner(System.in);
		Connection conn = null;
		Statement  stmt = null;
		System.out.print("수정할 부서번호를 입력하세요: ");
		int deptno = sc.nextInt(); 
		System.out.print("수정 부서명을 입력하세요: ");
		String dname = sc.next().trim().toUpperCase();
		System.out.print("수정 부서위치를 입력하세요: ");
		sc.nextLine();
		String loc = sc.nextLine().trim().toUpperCase();
		String updatesql = String.format("UPDATE DEPT SET DNAME='%s', LOC='%s'"
									+ "		WHERE DEPTNO=%d", dname, loc, deptno);
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, "scott", "tiger");
			stmt = conn.createStatement();
			int result = stmt.executeUpdate(updatesql);
			System.out.println(result+"행 수정 성공하였습니다");
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(stmt!=null) stmt.close();
				if(conn!=null) conn.close();
				sc.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		
		
	}
}
