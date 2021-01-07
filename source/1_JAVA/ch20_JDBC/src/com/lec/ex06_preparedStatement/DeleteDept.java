package com.lec.ex06_preparedStatement;
//21-01-07_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

/* 1) 삭제할 부서번호 입력받기
 * 2-1) 입력한 부서번호가 있을 경우 "XX번 부서를 삭제하시겠습니까(Y:삭제)?"
 * 2-1-1)  Y: 삭제 -> 삭제 완료 메시지 출력
 * 	        그 외: 삭제 안하고 종료
 * 2-2)	입력한 부서번호가 없을 경우 "입력한 부서번호는 없는 번호입니다"
 * 2-1-1) Y: 삭제 -> 삭제 완료 메시지 출력
 */
public class DeleteDept {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Scanner sc = new Scanner(System.in);
		Connection conn = null;
		PreparedStatement pstmt = null;
		//Statement  stmt = null;
		ResultSet  rs   = null;
		System.out.print("삭제하려는 부서번호를 입력하세요: ");
		int deptno = sc.nextInt();
		String selectSql = "SELECT * FROM DEPT WHERE DEPTNO=?";
		String deleteSql = "DELETE FROM DEPT WHERE DEPTNO=?";
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(selectSql);
			pstmt.setInt(1, deptno);
			rs   = pstmt.executeQuery();
			if(rs.next()) {
				System.out.println(deptno+"번 부서를 삭제하시겠습니까(Y:삭제)?");
				if(sc.next().equalsIgnoreCase("y")) {
					rs.close();
					pstmt.close();
					pstmt = conn.prepareStatement(deleteSql);
					pstmt.setInt(1, deptno);
					int result = pstmt.executeUpdate();
					if(result>0) {
						System.out.println(result+"행 삭제되었습니다");
					} 
				} else {
					System.out.println(deptno+"번 부서 삭제 취소. 종료합니다.");
				}
			} else {
				System.out.println("존재하지 않는 부서번호 입니다.");
			}
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(rs!=null)    rs.close();
				if(pstmt!=null) pstmt.close();
				if(conn!=null)  conn.close();
				sc.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		
	}
}
