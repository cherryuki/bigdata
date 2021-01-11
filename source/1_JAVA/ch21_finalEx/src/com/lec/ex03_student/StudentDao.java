package com.lec.ex03_student;
//21-01-08_JDBC_Dao&Dto		(c)cherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Vector;

import com.lec.studentGui.StudentSwingDto;

/* 1: insertStudent
 * 2: selectMname(String mname)
 * 3: selectAll()
 * 4: selectExpel()
 */

public class StudentDao {
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@localhost:1521:xe";
	public static final int SUCCESS = 1;
	public static final int FAIL = 0;
	private static StudentDao INSTANCE;
	public static StudentDao getInstance() {//Single ton pattern
		if(INSTANCE==null) {
			INSTANCE = new StudentDao();
		}
		return INSTANCE;
	}
	private StudentDao() {
		try {
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		}
	}
	//1. insert student
	public int insertStudent(StudentDto dto) {
		int result = FAIL;
		Connection conn = null;
		PreparedStatement pstmt = null;
		String sql = "INSERT INTO STUDENT VALUES (TO_CHAR(SYSDATE, 'YYYY')||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000'))," + 
						"                         	?, (SELECT MNO FROM MAJOR WHERE MNAME=?), ?, 0)";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, dto.getName());
			pstmt.setString(2, dto.getMname());
			pstmt.setInt(3, dto.getScore());
			result = pstmt.executeUpdate();
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
	//2. select where mname
	public ArrayList<StudentDto> selectMname(String mname) {
		ArrayList<StudentDto> dtos = new ArrayList<StudentDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT ROWNUM||'µî' RANK, SM.*" + 
					"    FROM (SELECT SNAME||'('||SNO||')' NAME, MNAME, SCORE FROM STUDENT S, MAJOR M" + 
					"            WHERE S.MNO=M.MNO AND SEXPEL=0 AND MNAME=?" + 
					"            ORDER BY SCORE DESC) SM";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, mname);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				String rank = rs.getString("rank");
				String name = rs.getString("name");
				int score = rs.getInt("score");
				dtos.add(new StudentDto(rank, name, mname, score));
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
	// 3. select all student 
	public ArrayList<StudentDto> selectAll() {
		ArrayList<StudentDto> dtos = new ArrayList<StudentDto>();
	
	Connection conn = null;
	PreparedStatement pstmt = null;
	ResultSet rs = null;
	String sql = "SELECT ROWNUM||'µî' RANK, SM.*" + 
				"    FROM (SELECT SNAME||'('||SNO||')' NAME, MNAME, SCORE FROM STUDENT S, MAJOR M" + 
				"            WHERE S.MNO=M.MNO AND SEXPEL=0" + 
				"            ORDER BY SCORE DESC) SM";
	try {
		conn = DriverManager.getConnection(url, "scott", "tiger");
		pstmt = conn.prepareStatement(sql);
		rs = pstmt.executeQuery();
		while(rs.next()) {
			String rank = rs.getString("rank");
			String name = rs.getString("name");
			String mname = rs.getString("mname");
			int score = rs.getInt("score");
			dtos.add(new StudentDto(rank, name, mname, score));
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
	//4. select expel
	public ArrayList<StudentDto> selectExpel() {
		ArrayList<StudentDto> dtos = new ArrayList<StudentDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT ROWNUM||'µî' RANK, SM.*" + 
					"    FROM (SELECT SNAME||'('||SNO||')' NAME, MNAME, SCORE FROM STUDENT S, MAJOR M" + 
					"            WHERE S.MNO=M.MNO AND SEXPEL=1" + 
					"            ORDER BY SCORE DESC) SM";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				String rank = rs.getString("rank");
				String name = rs.getString("name");
				String mname = rs.getString("mname");
				int score = rs.getInt("score");
				dtos.add(new StudentDto(rank, name, mname, score));
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
}//class