package com.lec.ex03_insert;
//21-01-06_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class InsertDept2 {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Connection conn = null;
		Statement  stmt = null;
		ResultSet  rs 	= null;
		Scanner sc = new Scanner(System.in);
		System.out.print("추가할 부서번호를 입력하세요: ");
		int deptno = sc.nextInt();
		String selectSql = "SELECT * FROM DEPT WHERE DEPTNO="+deptno;
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, "scott", "tiger");
			stmt = conn.createStatement();
			rs   = stmt.executeQuery(selectSql);
			if(rs.next()) {
				System.out.println("입력하신 부서번호는 이미 존재하는 부서번호입니다. 새로운 부서번호를 입력해주세요");
			} else {
				System.out.print("추가할 부서명을 입력하세요: ");
				String dname = sc.next().trim().toUpperCase();
				System.out.print("추가할 부서 위치를 입력하세요: "); 
				sc.nextLine(); 
				String loc = sc.nextLine().trim().toUpperCase(); //SEOUL KOREA 가능
				String insertSql = String.format("INSERT INTO DEPT VALUES(%d, '%s', '%s')", 
																		deptno, dname, loc);
				int result = stmt.executeUpdate(insertSql);
				if(result>0) {
					System.out.println(result+"행 삽입되었습니다");
				}
			}
		} catch (ClassNotFoundException e1) {
			System.out.println(e1.getMessage());
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(rs!=null) 	rs.close();
				if(stmt!=null) 	stmt.close();
				if(conn!=null) 	conn.close();
				sc.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
