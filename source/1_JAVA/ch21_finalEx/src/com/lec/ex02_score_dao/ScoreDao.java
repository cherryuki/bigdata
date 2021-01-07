package com.lec.ex02_score_dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

//21-01-07_JDBC		ⓒcherryuki(ji)



/* 1번: insertPerson_Score(PersonScore dto)
 * 2번: selectJname(String jname)
 * 3번: selectAll()
 */
public class ScoreDao {
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@localhost:1521:xe";
	public static final int SUCCESS = 1;
	public static final int FAIL = 0;
	private static ScoreDao INSTANCE; //Singleton parttern(ch13_pattern참조)
	public static ScoreDao getInstance() {
		if(INSTANCE==null) {
			INSTANCE = new ScoreDao();
		}
		return INSTANCE;
	}
	private ScoreDao() {
		try {
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		}
	}
	//1번
	public int insertScore(ScoreDto dto) {
		int result = FAIL;
		//dto 값들을 DB에 넣기
		Connection conn = null;
		PreparedStatement pstmt = null;
		String sql = "INSERT INTO SCORE VALUES(S_SEQ.NEXTVAL, ?, "
				+ "			(SELECT JNO FROM JOB WHERE JNAME=?), ?, ?, ?)";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, dto.getName());
			pstmt.setString(2, dto.getJname());
			pstmt.setInt(3, dto.getKor());
			pstmt.setInt(4, dto.getEng());
			pstmt.setInt(5, dto.getMat());
			result = pstmt.executeUpdate(); //0: fail, 1: success
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(pstmt!=null) pstmt.close();
				if(conn!=null)  conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return result;
	}
	//2번
	public ArrayList<ScoreDto> selectJname(String jname) {
		ArrayList<ScoreDto> dtos = new ArrayList<ScoreDto>();
		//jname 직업인 사람들 리스트 dtos에 add
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT ROWNUM RANK, S.*\r\n" + 
				"    FROM (SELECT NAME||'('||NO||'번)' NAME, JNAME, KOR, ENG, MAT, KOR+ENG+MAT TOTAL" + 
				"            FROM JOB J, SCORE S WHERE J.JNO=S.JNO AND JNAME=?" + 
				"            ORDER BY TOTAL DESC) S";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, jname);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				int rank = rs.getInt("rank");
				String name = rs.getString("name");
//				jname = rs.getString("jname");
				int kor = rs.getInt("kor");
				int eng = rs.getInt("eng");
				int mat = rs.getInt("mat");
				int total = rs.getInt("total");
				dtos.add(new ScoreDto(rank, name, jname, kor, eng, mat, total));
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(rs!=null) rs.close();
				if(pstmt!=null) pstmt.close();
				if(conn!=null)  conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return dtos;
	}
	//3번
	public ArrayList<ScoreDto> selectAll() {
		ArrayList<ScoreDto> dtos = new ArrayList<ScoreDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT ROWNUM RANK, S.*" + 
					"    FROM (SELECT NAME||'('||NO||'번)' NAME, JNAME, KOR, ENG, MAT, KOR+ENG+MAT TOTAL" + 
					"            FROM JOB J, SCORE S WHERE J.JNO=S.JNO" + 
					"            ORDER BY TOTAL DESC) S";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				int rank = rs.getInt("rank");
				String name = rs.getString("name");
				String jname = rs.getString("jname");
				int kor = rs.getInt("kor");
				int eng = rs.getInt("eng");
				int mat = rs.getInt("mat");
				int total = rs.getInt("total");
				dtos.add(new ScoreDto(rank, name, jname, kor, eng, mat, total));
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(rs!=null) rs.close();
				if(pstmt!=null) pstmt.close();
				if(conn!=null)  conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return dtos;
	}
}
