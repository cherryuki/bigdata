package com.lec.ex01_selectAll;
//21-01-06_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;

public class SelectAllOracle {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Connection conn = null; //DB연결 객체 변수
		Statement  stmt = null; //SQL전송 객체 변수
		ResultSet  rs	= null; //SELECT문 결과 받는 객체 변수
		String sql = "SELECT * FROM EMP";
		try {
			Class.forName(driver); //(1) 드라이버 로드
			conn = DriverManager.getConnection(url, "scott", "tiger"); //(2) DB연결
			stmt = conn.createStatement(); //(3) SQL전송 객체 생성
			rs = stmt.executeQuery(sql); //(4) SQL전송 + (5) SQL실행 결과 받기
			//(6) 결과 받아 로직 수행 - rs에 있는 데이터 콘솔에 출력
			System.out.println("사번\t이름\t직책\t\t상사사번\t입사일\t\t급여\t상여\t부서번호");
			if(rs.next()) {
				//주로 number는 int, varchar2는 String, date는 Date나 Timestamp 사용
				//숫자나 날짜 등을 String으로 받아도 오류는 나지 않으나 상기와 같이 바꾸는 것이 일반적
				do {
					int	empno = rs.getInt(1); //칼럼 열순서 입력(1번째 열), "empno" 입력과 동일
					String ename = rs.getString("ename"); //2로 입력해도 같은 결과
					String job = rs.getString("job");
					int mgr = rs.getInt("mgr"); //null값은 0으로 출력
//					Date hiredate = rs.getDate("hiredate");
					Timestamp hiredate = rs.getTimestamp("hiredate");
					int sal = rs.getInt("sal");
					int comm = rs.getInt("comm");
					int deptno = rs.getInt("deptno");
					if(job!=null && job.length()<=7) {
						System.out.printf("%d\t%s\t%s\t\t%d\t%TF\t%d\t%d\t%d\n", 
								empno, ename, job, mgr, hiredate, sal, comm, deptno);
					} else {
						System.out.printf("%d\t%s\t%s\t%d\t%TF\t%d\t%d\t%d\n", 
								empno, ename, job, mgr, hiredate, sal, comm, deptno);	
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
			try {//(7). 닫기(닫을 때는 객체 생성 순서 반대로 닫기)
				if(rs!=null) rs.close();
				if(stmt!=null) stmt.close();
				if(conn!=null) conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
