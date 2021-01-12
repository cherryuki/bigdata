package com.lec.supermarket;
//21-01-12_JDBC_Dao&Dto_GUI		(c)cherryuki(ji)

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Vector;

public class SupermarketDao {
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@localhost:1521:xe";
	public static final int SUCCESS = 1;
	public static final int FAIL = 0;
	private static SupermarketDao INSTANCE = new SupermarketDao();
	public static SupermarketDao getInstance() {
		return INSTANCE;
	}
	private SupermarketDao() {
		try {
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			System.out.println(e.getMessage());
		}
	}
	//0. comboBox level list
	public Vector<String> levellist() {
		Vector<String> levellist = new Vector<String>();
		levellist.add("");
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT LNAME FROM CUS_LEVEL ORDER BY LNO";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				levellist.add(rs.getString("lname"));
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
		return levellist;
	}
	//1. search id(String id)
	public SupermarketDto searchId(String id) {
		SupermarketDto dto = null;
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT CID, CTEL, CNAME, CPOINT, CAMOUNT, LNAME, "
					+ "		(SELECT LHIGH-CAMOUNT FROM CUSTOMER WHERE C.CID=CID AND LNO!=5) FORLEVELUP" + 
					"    FROM CUSTOMER C, CUS_LEVEL L" + 
					"    WHERE C.LNO=L.LNO AND CID=?";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, id);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				id = rs.getString("cid");
				String tel = rs.getString("ctel");
				String name = rs.getString("cname");
				int point = rs.getInt("cpoint");
				int amount = rs.getInt("camount");
				String level = rs.getString("lname");
				int forlevelup = rs.getInt("forlevelup");
				dto = new SupermarketDto(id, tel, name, point, amount, level, forlevelup);
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
	//2. search tel(String postTel)
	public ArrayList<SupermarketDto> searchTel(String postTel) {
		ArrayList<SupermarketDto> dtos = new ArrayList<SupermarketDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT CID, CTEL, CNAME, CPOINT, CAMOUNT, LNAME, "
				+ "			(SELECT LHIGH-CAMOUNT FROM CUSTOMER WHERE C.CID=CID AND LNO!=5) FORLEVELUP" + 
					"    FROM CUSTOMER C, CUS_LEVEL L" + 
					"    WHERE C.LNO=L.LNO AND CTEL LIKE '%'||?";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, postTel);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				String id = rs.getString("cid");
				String tel = rs.getString("ctel");
				String name = rs.getString("cname");
				int point = rs.getInt("cpoint");
				int amount = rs.getInt("camount");
				String level = rs.getString("lname");
				int forlevelup = rs.getInt("forlevelup");
				dtos.add(new SupermarketDto(id, tel, name, point, amount, level, forlevelup));
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
	//3. search name(String name)
	public ArrayList<SupermarketDto> searchName(String name) {
		ArrayList<SupermarketDto> dtos = new ArrayList<SupermarketDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT CID, CTEL, CNAME, CPOINT, CAMOUNT, LNAME," + 
					"        (SELECT LHIGH-CAMOUNT FROM CUSTOMER WHERE C.CID=CID AND LNO!=5) FORLEVELUP" + 
					"    FROM CUSTOMER C, CUS_LEVEL L" + 
					"    WHERE C.LNO=L.LNO AND CNAME=?";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, name);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				String id = rs.getString("cid");
				String tel = rs.getString("ctel");
				name = rs.getString("cname");
				int point = rs.getInt("cpoint");
				int amount = rs.getInt("camount");
				String level = rs.getString("lname");
				int forlevelup = rs.getInt("forlevelup");
				dtos.add(new SupermarketDto(id, tel, name, point, amount, level, forlevelup));
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
	//4. pay with point - update point(String id, int price)
	public int updatePoint(String id, int price) {
		int result = FAIL;
		Connection conn = null;
		PreparedStatement pstmt = null;
		String sql = "UPDATE CUSTOMER SET CPOINT=CPOINT-? WHERE CID=?";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, price);
			pstmt.setString(2, id);
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
	//5. pay - update amount, point, level(String id, int price)
	public int updateAmount(String id, int price) {
		int result = FAIL;
		Connection conn = null;
		PreparedStatement pstmt = null;
		String sql = "UPDATE CUSTOMER SET CAMOUNT=CAMOUNT+?," + 
					"                    CPOINT=CPOINT+(?*0.05)," + 
					"                    LNO=(SELECT L.LNO FROM CUSTOMER C, CUS_LEVEL L WHERE CAMOUNT+? BETWEEN LLOW AND LHIGH AND CID=?)" + 
					"    WHERE CID=?";
		
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, price);
			pstmt.setInt(2, price);
			pstmt.setInt(3, price);
			pstmt.setString(4, id);
			pstmt.setString(5, id);
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
	//6. level output - selectLevel(String level)
	public ArrayList<SupermarketDto> selectLevel(String level) {
		ArrayList<SupermarketDto> dtos = new ArrayList<SupermarketDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT CID, CTEL, CNAME, CPOINT, CAMOUNT, LNAME," + 
					"        (SELECT LHIGH-CAMOUNT FROM CUSTOMER WHERE C.CID=CID AND LNO!=5) FORLEVELUP" + 
					"    FROM CUSTOMER C, CUS_LEVEL L" + 
					"    WHERE C.LNO=L.LNO AND LNAME=?" + 
					"    ORDER BY CAMOUNT DESC";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, level);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				String id = rs.getString("cid");
				String tel = rs.getString("ctel");
				String name = rs.getString("cname");
				int point = rs.getInt("cpoint");
				int amount = rs.getInt("camount");
				level = rs.getString("lname");
				int forlevelup = rs.getInt("forlevelup");
				dtos.add(new SupermarketDto(id, tel, name, point, amount, level, forlevelup));
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
	//7. selectAll()
	public ArrayList<SupermarketDto> selectAll() {
		ArrayList<SupermarketDto> dtos = new ArrayList<SupermarketDto>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String sql = "SELECT CID, CTEL, CNAME, CPOINT, CAMOUNT, LNAME, " + 
					"        (SELECT LHIGH-CAMOUNT FROM CUSTOMER WHERE C.CID=CID AND LNO!=5) FORLEVELUP" + 
					"    FROM CUSTOMER C, CUS_LEVEL L" + 
					"    WHERE C.LNO=L.LNO" + 
					"    ORDER BY CAMOUNT DESC";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				String id = rs.getString("cid");
				String tel = rs.getString("ctel");
				String name = rs.getString("cname");
				int point = rs.getInt("cpoint");
				int amount = rs.getInt("camount");
				String level = rs.getString("lname");
				int forlevelup = rs.getInt("forlevelup");
				dtos.add(new SupermarketDto(id, tel, name, point, amount, level, forlevelup));
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
	//8. join - insert customer(String tel, String name)
	public int insertCustomer(String tel, String name) {
		int result = FAIL;
		Connection conn = null;
		PreparedStatement pstmt = null;
		String sql = "INSERT INTO CUSTOMER(CID, CTEL, CNAME) VALUES (CUS_SEQ.NEXTVAL, ?, ?)";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, tel);
			pstmt.setString(2, name);
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
	//9. update customer(String tel, int id)
	public int updateCustomer(String tel, String id) {
		int result = FAIL;
		Connection conn = null;
		PreparedStatement pstmt = null;
		String sql = "UPDATE CUSTOMER SET CTEL=? WHERE CID=?";
		try {
			conn = DriverManager.getConnection(url, "scott", "tiger");
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, tel);
			pstmt.setString(2, id);
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
	//10. delete customer(String tel)
		public int deleteCustomer(String tel) {
			int result = FAIL;
			Connection conn = null;
			PreparedStatement pstmt = null;
			String sql = "DELETE CUSTOMER WHERE CTEL=?";
			try {
				conn = DriverManager.getConnection(url, "scott", "tiger");
				pstmt = conn.prepareStatement(sql);
				pstmt.setString(1, tel);
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
	
}//Class
