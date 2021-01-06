package com.lec.ex01_selectAll;
//21-01-06_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;

public class SelectAllMySQL {
	public static void main(String[] args) {
		String driver = "com.mysql.cj.jdbc.Driver"; // 8.0
		String url = "jdbc:mysql://localhost:3306/kimdb?serverTimezone=UTC";
		Connection conn = null;
		Statement  stmt = null;
		ResultSet  rs   = null;
		String sql = "SELECT * FROM PERSONAL";
		try {
			Class.forName(driver); //(1) 드라이버 로드
			conn = DriverManager.getConnection(url, "root", "mysql"); //(2) DB연결
			stmt = conn.createStatement(); //(3) SQL문 수행할 객체 생성
			rs = stmt.executeQuery(sql); //(4) SQL문 전송 +(5) SQL실행 결과 받기
			System.out.println("사번\t이름\t직책\t\t상사사번\t입사일\t\t급여\t상여\t부서번호");
			if(rs.next()) {//select 결과 있음
				//(6) 결과 받아서 로직 수행
				do {
					int 	pno 	= rs.getInt("pno");
					String 	pname 	= rs.getString("pname");
					String	job		= rs.getString("job");
					int 	manager	= rs.getInt("manager");
					Date	startdate = rs.getDate("startdate");
//					Timestamp startdate = rs.getTimestamp("startdate);
					int		pay		= rs.getInt("pay");
					int		bonus	= rs.getInt("bonus");
					int		dno		= rs.getInt("dno");
					if(job!=null && job.length()<=7) {
						System.out.printf("%d\t%s\t%s\t\t%d\t%TF\t%d\t%d\t%d\n", 
								pno, pname, job, manager, startdate, pay, bonus, dno);
					} else {
						System.out.printf("%d\t%s\t%s\t%d\t%TF\t%d\t%d\t%d\n", 
								pno, pname, job, manager, startdate, pay, bonus, dno);		
					}
				} while(rs.next());
			} else {
				System.out.println("사원 정보가 없습니다");
			}
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
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
