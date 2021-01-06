package com.lec.ex02_selectWhere;
//21-01-06_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

//사용자에게 원하는 부서명을 입력 받아 해당 부서정보 콘솔창에 출력
public class SelectWhereDname {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Connection conn = null;
		Statement  stmt = null;
		ResultSet  rs	= null;
		Scanner sc = new Scanner(System.in);
		System.out.print("조회하고자 하는 부서명을 입력하세요: ");
		String dname = sc.next().trim().toUpperCase();
		String sql = "SELECT * FROM DEPT WHERE DNAME='"+dname+"'";
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, "scott", "tiger");
			stmt = conn.createStatement();
			rs = stmt.executeQuery(sql);
			if(rs.next()) {
				System.out.println("부서번호: "+rs.getInt("deptno"));
				System.out.println("부서명: "+dname);
				System.out.println("부서 위치:"+rs.getString("loc"));
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
