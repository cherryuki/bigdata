package com.lec.ex06_preparedStatement;
//21-01-07_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class UpdateDept {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Scanner sc = new Scanner(System.in);
		Connection 		  conn  = null;
		PreparedStatement pstmt = null;
		ResultSet 		  rs	= null;
		String selectSql = "SELECT * FROM DEPT WHERE DEPTNO=?";
		String updateSql = "UPDATE DEPT SET DNAME=?, LOC=? WHERE DEPTNO=?";
		System.out.print("수정할 부서번호: ");
		int deptno = sc.nextInt();
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(selectSql);
			pstmt.setInt(1, deptno);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				//수정
				rs.close();
				pstmt.close();
				System.out.print("수정 부서명: ");
				String dname = sc.next().trim().toUpperCase();
				System.out.print("수정 부서위치: ");
				sc.nextLine();
				String loc = sc.nextLine().trim().toUpperCase();
				pstmt = conn.prepareStatement(updateSql);
				pstmt.setString(1, dname);
				pstmt.setString(2, loc);
				pstmt.setInt(3, deptno);
				int result = pstmt.executeUpdate();
				System.out.println(result+"행 업데이트 되었습니다");
			} else {
				System.out.println("존재하지 않는 부서번호 입니다");
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
