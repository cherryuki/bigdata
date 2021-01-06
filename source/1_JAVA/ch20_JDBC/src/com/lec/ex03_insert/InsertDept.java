package com.lec.ex03_insert;
//21-01-06_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class InsertDept {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Connection conn = null;
		Statement  stmt = null;
		Scanner sc = new Scanner(System.in);
		System.out.print("추가할 부서번호를 입력하세요: ");
		int deptno = sc.nextInt();
		System.out.print("추가할 부서명을 입력하세요: ");
		String dname = sc.next().trim().toUpperCase();
		System.out.print("추가할 부서 위치를 입력하세요: ");
		sc.nextLine(); // '\n'버퍼 지우기
		String loc = sc.nextLine().trim().toUpperCase();
		String sql = String.format("INSERT INTO DEPT VALUES(%d, '%s', '%s')", deptno, dname, loc);
		try {
			Class.forName(driver); //(1)
			conn = DriverManager.getConnection(url, "scott", "tiger"); //(2)
			stmt = conn.createStatement(); //(3)
			int result = stmt.executeUpdate(sql); //(4)+(5) 
			System.out.println(result>0? result+"행 삽입되었습니다":"부서입력 실패"); //(6)
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
