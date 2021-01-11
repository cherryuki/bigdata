package com.lec.studentGui;
//21-01-11_JDBC_Dao&Dto_GUI		(c)cherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Vector;

import com.lec.ex03_student.StudentDao;

/*
0. 첫화면에 전공이름들 콤보박스에 추가(mName) 
	: public Vector<String> getMNamelist()
1. 학번검색 (sNo, sName, mName, score) 
	: public StudentSwingDto sNogetStudent(String sNo)
2. 이름검색 (sNo, sName, mName, score) 
	: public ArrayList<StudentSwingDto> sNamegetStudent(String sName)
3. 전공검색 (rank, sName(sNo포함), mName(mNo포함), score) 
	: public ArrayList<StudentSwingDto> mNamegetStudent(String mName)
4. 학생입력 
	: public int insertStudent(String sName, String mName, int score)
    public int insertStudent(StudentSwingDto dto)
5. 학생수정 
	: public int updateStudent(String sNo,String sName,String mName,int score)
    public int updateStudent(StudentSwingDto dto)
6. 학생출력 (rank, sName(sNo포함), mName(mNo포함), score) 
	: public ArrayList<StudentSwingDto> getStudents()
7. 제적자출력  (rank, sName(sNo포함), mName(mNo포함), score) 
	: public ArrayList<StudentSwingDto> getStudentsExpel()
8. 제적처리 : public int sNoExpel(String sNo)
*/

public class StudentSwingDao {
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@localhost:1521:xe";
	public static final int SUCCESS = 1;
	public static final int FAIL = 0;
	private static StudentSwingDao INSTANCE;
	public static StudentSwingDao getInstance() {//Single ton pattern
		if(INSTANCE==null) {
			INSTANCE = new StudentSwingDao();
		}
		return INSTANCE;
	}
	private StudentSwingDao() {
		try {
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		}
	}
	//0. comboBox mName list
	public Vector<String> mnamelist() {
		Vector<String> mnamelist = new Vector<String>();
		mnamelist.add("");
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT MNAME FROM MAJOR ORDER BY MNO";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while (rs.next()) {
				mnamelist.add(rs.getString("mname"));
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return mnamelist;
	}

	//1. Select sno
	public StudentSwingDto searchSno(int sno) {
		StudentSwingDto dto = null;
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT SNO, SNAME, MNAME, SCORE FROM STUDENT S, MAJOR M WHERE S.MNO=M.MNO AND SNO=?";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, sno);
			rs = pstmt.executeQuery();
			if (rs.next()) {
				String name = rs.getString("sname");
				String major = rs.getString("mname");
				int score = rs.getInt("score");
				dto = new StudentSwingDto(sno, name, major, score);
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return dto;
	}

	//2. select sname
	public ArrayList<StudentSwingDto> selectSname(String sname) {
		ArrayList<StudentSwingDto> dtos = new ArrayList<StudentSwingDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT SNO, SNAME, MNAME, SCORE FROM STUDENT S, MAJOR M WHERE S.MNO=M.MNO AND SNAME=?";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, sname);
			rs = pstmt.executeQuery();
			while (rs.next()) {
				int sno = rs.getInt("sno");
				sname = rs.getString("sname");// name
				String mname = rs.getString("mname");// major
				int score = rs.getInt("score");
				dtos.add(new StudentSwingDto(sno, sname, mname, score));
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return dtos;
	}

	//3. select mname
	public ArrayList<StudentSwingDto> selectMname(String mname) {
		ArrayList<StudentSwingDto> dtos = new ArrayList<StudentSwingDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT ROWNUM||'등' RANK, SM.*"
				+ "    FROM (SELECT SNAME||'('||SNO||')' NAME, MNAME||'('||S.MNO||')' MAJOR, SCORE"
				+ "            FROM STUDENT S, MAJOR M" + "            WHERE S.MNO=M.MNO AND MNAME=?"
				+ "            ORDER BY SCORE DESC) SM";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, mname);
			rs = pstmt.executeQuery();
			while (rs.next()) {
				String rank = rs.getString("rank");
				String name = rs.getString("name");
				String major = rs.getString("major");
				int score = rs.getInt("score");
				dtos.add(new StudentSwingDto(rank, name, major, score));
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return dtos;
	}

	//4. insert student
	public int insertStudent(StudentSwingDto dto) {
		int result = FAIL;
		Connection conn = null;
		PreparedStatement pstmt = null;
		String sql = "INSERT INTO STUDENT  VALUES (TO_NUMBER(EXTRACT(YEAR FROM SYSDATE)||TRIM(TO_CHAR(S_SEQ.NEXTVAL, '000')))," + 
					"                                ?, (SELECT MNO FROM MAJOR WHERE MNAME=?), ?, 0)";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, dto.getName());
			pstmt.setString(2, dto.getMajor());
			pstmt.setInt(3, dto.getScore());
			result = pstmt.executeUpdate();
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return result;
	}
	//5. update student
	public int updateStudent(StudentSwingDto dto) {
		int result = FAIL;
		Connection conn = null;
		PreparedStatement pstmt = null;
		String sql = "UPDATE STUDENT SET SNAME=?, MNO=(SELECT MNO FROM MAJOR WHERE MNAME=?), SCORE=? WHERE SNO=?";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, dto.getName());
			pstmt.setString(2, dto.getMajor());
			pstmt.setInt(3, dto.getScore());
			pstmt.setInt(4, dto.getSno());
			result = pstmt.executeUpdate();
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return result;
	}
	//6. select all student
	public ArrayList<StudentSwingDto> selectAll() {
		ArrayList<StudentSwingDto> dtos = new ArrayList<StudentSwingDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT ROWNUM||'등' RANK, SM.*" + 
				"    FROM (SELECT SNAME||'('||SNO||')' NAME, MNAME||'('||S.MNO||')' MAJOR, SCORE" + 
				"            FROM STUDENT S, MAJOR M" + 
				"            WHERE S.MNO=M.MNO AND SEXPEL=0" + 
				"            ORDER BY SCORE DESC) SM";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				String rank = rs.getString("rank");
				String name = rs.getString("name");
				String major = rs.getString("major");
				int score = rs.getInt("score");
				dtos.add(new StudentSwingDto(rank, name, major, score));
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
		}	
		return dtos;
	}
	//7. select expel
	public ArrayList<StudentSwingDto> selectExpel() {
		ArrayList<StudentSwingDto> dtos = new ArrayList<StudentSwingDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT ROWNUM||'등' RANK, SM.*" + 
				"    FROM (SELECT SNAME||'('||SNO||')' NAME, MNAME||'('||S.MNO||')' MAJOR, SCORE" + 
				"            FROM STUDENT S, MAJOR M" + 
				"            WHERE S.MNO=M.MNO AND SEXPEL=1" + 
				"            ORDER BY SCORE DESC) SM";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				String rank = rs.getString("rank");
				String name = rs.getString("name");
				String major = rs.getString("major");
				int score = rs.getInt("score");
				dtos.add(new StudentSwingDto(rank, name, major, score));
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
		}	
		return dtos;
	}
	//8. update expel
	public int updateExpel(String snoStr) {
		int result = FAIL;
		Connection conn = null;
		PreparedStatement pstmt = null;
		String sql = "UPDATE STUDENT SET SEXPEL=1 WHERE SNO=?";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1,  snoStr);
			result = pstmt.executeUpdate();
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		return result;
	}
}//class
