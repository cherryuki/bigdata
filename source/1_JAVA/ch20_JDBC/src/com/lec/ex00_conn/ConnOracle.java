package com.lec.ex00_conn;
//21-01-06_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnOracle {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe"; //@127.0.0.1=@localhost(내 컴퓨터), xe버전
		Connection conn = null;
		try {
			//1. 드라이버 로드
			Class.forName(driver);
			System.out.println("드라이버 로드 성공");
			//2. DB와 연결 객체 생성
			conn = DriverManager.getConnection(url, "scott", "tiger");
			System.out.println("DB연결 성공");
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage()+": 드라이버 로드 오류");
		} catch (SQLException e) {
			System.out.println(e.getMessage()+": conn객체 생성 실패");
		} finally {
			try {
				if(conn!=null) conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage()+": 닫기 오류");
			}
		}
	}
}
