package com.lec.studentGui;
//21-01-11_JDBC_Dao&Dto_GUI		(c)cherryuki(ji)

public class StudentSwingDto {
	private int sno; //textField시 String으로 변환 해야 하므로 처음부터 String으로 받음
	private String rank; //'등'포함 String
	private String name;
	private String major;
	private int score;
	public StudentSwingDto(String rank, String name, String major, int score) {
		super();
		this.rank = rank;
		this.name = name;
		this.major = major;
		this.score = score;
	}
	
	public StudentSwingDto(int sno, String name, String major, int score) {
		super();
		this.sno = sno;
		this.name = name;
		this.major = major;
		this.score = score;
	}

	public StudentSwingDto(String name, String major, int score) {//insert
		super();
		this.name = name;
		this.major = major;
		this.score = score;
	}
	@Override
	public String toString() {
		if(rank==null) {
			return "   "+sno +"\t" + name +"\t" + major +"\t" + score;
		}else {
			return "   "+rank +"\t" + name +"\t" + major +"\t\t" + score;
		}
	}
	public int getSno() {
		return sno;
	}
	public String getRank() {
		return rank;
	}
	public String getName() {
		return name;
	}
	public String getMajor() {
		return major;
	}
	public int getScore() {
		return score;
	}
	
}
