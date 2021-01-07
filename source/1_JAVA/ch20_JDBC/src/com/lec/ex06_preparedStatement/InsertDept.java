package com.lec.ex06_preparedStatement;
//21-01-07_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class InsertDept {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Scanner sc = new Scanner(System.in);
		Connection 		  conn  = null;
		PreparedStatement pstmt = null;
		ResultSet 		  rs 	= null;
		String selectSql = "SELECT * FROM DEPT WHERE DEPTNO=?";
		String insertSql = "INSERT INTO DEPT VALUES(?, ?, ?)";
		System.out.print("추가할 부서번호: ");
		int deptno = sc.nextInt();
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(selectSql);
			pstmt.setInt(1, deptno);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				System.out.println("이미 존재하는 부서번호입니다. 처음부터 다시 시도해주세요");
			} else {
				rs.close();
				pstmt.close();
				System.out.print("추가할 부서명: ");
				String dname = sc.next().trim().toUpperCase();
				System.out.print("추가할 부서위치: ");
				sc.nextLine();
				String loc = sc.nextLine().trim().toUpperCase();
				pstmt = conn.prepareStatement(insertSql);
				pstmt.setInt(1, deptno);
				pstmt.setString(2, dname);
				pstmt.setString(3, loc);
				int result = pstmt.executeUpdate();
				System.out.println(result+"행 추가하였습니다");
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
