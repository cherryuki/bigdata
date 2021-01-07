package com.lec.ex01_score;
//21-01-07_JDBC		ⓒcherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

/* 1) 1을 누르면 데이터 입력(이름, 직업, 국어, 영어, 수학점수 입력받아 데이터 베이스 번호를 포함하여 입력)
 *  1-1) 번호는 시퀀스 이용하여 순차적으로 입력 
 *  1-2) 직업은 JNAME입력시 JNO로 자동 변환해서 저장
 * 2) 2를 누르면 원하는 직업 입력받아 직업별 조회후 총점 추가하여 총점이 높은 순으로 이름(번호)로 출력
 * 3) 데이터베이스에 입력된 사람 전체 조회 후 총점 추가하여 총점이 높은 순으로 출력
 */
public class Score {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
		Scanner sc = new Scanner(System.in);
		Connection 		  conn  = null;
		PreparedStatement pstmt = null;
		ResultSet 		  rs	= null;
		String fn;
		try {
			Class.forName(driver); //1단계는 한 번만
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		}
		do {
			System.out.print("1:입력 | 2:직업별 조회 | 3:전체 조회 ");
			fn=sc.next();
			switch(fn) {
			case "1": //데이터 입력
				System.out.print("추가할 이름을 입력하세요: ");
				String name = sc.next();
				System.out.print("직업( 배우 | 가수 | 기타 )?: ");
				String jname = sc.next();
				System.out.print("국어 점수: ");
				int kor = sc.nextInt();
				System.out.print("영어 점수: ");
				int eng = sc.nextInt();
				System.out.print("수학 점수: ");
				int mat = sc.nextInt();
				String sql1 = "INSERT INTO SCORE VALUES(S_SEQ.NEXTVAL, ?, "
						+ "			(SELECT JNO FROM JOB WHERE JNAME=?), ?, ?, ?)";
				try {
					conn = DriverManager.getConnection(url, "scott", "tiger");
					pstmt = conn.prepareStatement(sql1);
					pstmt.setString(1, name);
					pstmt.setString(2, jname);
					pstmt.setInt(3, kor);
					pstmt.setInt(4, eng);
					pstmt.setInt(5, mat);
					int result = pstmt.executeUpdate();
					System.out.println(result+"행 추가하였습니다");
				} catch (SQLException e) {
					System.out.println(e.getMessage());
				} finally {
					try {
						if(pstmt!=null) pstmt.close();
						if(conn!=null) conn.close();
					} catch (SQLException e) {
						System.out.println(e.getMessage());
					}
				}//finally
				break;
			case "2": //직업별 조회
				System.out.println("조회하려는 직업(배우 | 가수 | 기타)?");
				jname = sc.next().trim();
				String sql2 = "SELECT ROWNUM RANK, S.*\r\n" + 
							"    FROM (SELECT NAME||'('||NO||'번)' NAME, JNAME, KOR, ENG, MAT, KOR+ENG+MAT TOTAL" + 
							"            FROM JOB J, SCORE S WHERE J.JNO=S.JNO AND JNAME=?" + 
							"            ORDER BY TOTAL DESC) S";
				try {
					conn = DriverManager.getConnection(url, "scott", "tiger");
					pstmt = conn.prepareStatement(sql2);
					pstmt.setString(1, jname);
					rs = pstmt.executeQuery();
					if(rs.next()) {
						System.out.println("등수\t이름(번호)\t\t직업\t국어\t영어\t수학\t총점");
						do {
							int rank = rs.getInt("rank");
							name = rs.getString("name");
							jname = rs.getString("jname");
							kor = rs.getInt("kor");
							eng = rs.getInt("eng");
							mat = rs.getInt("mat");
							int total = rs.getInt("total");
							if(name.length()>6) {
								System.out.println(rank+"\t"+name+"\t"+jname+"\t"+kor+"\t"+eng+"\t"+mat+"\t"+total);
							} else {
								System.out.println(rank+"\t"+name+"\t\t"+jname+"\t"+kor+"\t"+eng+"\t"+mat+"\t"+total);
							}
						} while(rs.next());
					} else {
						System.out.println("해당 직업의 사람이 없습니다");
					}
				} catch (SQLException e) {
					System.out.println(e.getMessage());
				} finally {
					try {
						if(rs!=null) rs.close();
						if(pstmt!=null) pstmt.close();
						if(conn!=null) conn.close();
					} catch (SQLException e) {
						System.out.println(e.getMessage());
					}
				}//finally
				break;
			case "3": //전체 조회
				String sql3 = "SELECT ROWNUM RANK, S.*" + 
							"    FROM (SELECT NAME||'('||NO||'번)' NAME, JNAME, KOR, ENG, MAT, KOR+ENG+MAT TOTAL" + 
							"            FROM JOB J, SCORE S WHERE J.JNO=S.JNO" + 
							"            ORDER BY TOTAL DESC) S";
				try {
					conn = DriverManager.getConnection(url, "scott", "tiger");
					pstmt = conn.prepareStatement(sql3);
					rs = pstmt.executeQuery();
					if(rs.next()) {
						System.out.println("등수\t이름(번호)\t\t직업\t국어\t영어\t수학\t총점");
						do {
							int rank = rs.getInt("rank");
							name = rs.getString("name");
							jname = rs.getString("jname");
							kor = rs.getInt("kor");
							eng = rs.getInt("eng");
							mat = rs.getInt("mat");
							int total = rs.getInt("total");
							if(name.length()>6) {
								System.out.println(rank+"\t"+name+"\t"+jname+"\t"+kor+"\t"+eng+"\t"+mat+"\t"+total);
							} else {
								System.out.println(rank+"\t"+name+"\t\t"+jname+"\t"+kor+"\t"+eng+"\t"+mat+"\t"+total);
							}
						} while(rs.next());
					} else {
						System.out.println("조회할 수 없습니다");
					}
				} catch (SQLException e) {
					System.out.println(e.getMessage());
				} finally {
					try {
						if(rs!=null) rs.close();
						if(pstmt!=null) pstmt.close();
						if(conn!=null) conn.close();
					} catch (SQLException e) {
						System.out.println(e.getMessage());
					}
				}//finally
				break;
			}
		} while(fn.equals("1")||fn.equals("2")||fn.equals("3"));
		System.out.println("종료되었습니다");
	}
}
