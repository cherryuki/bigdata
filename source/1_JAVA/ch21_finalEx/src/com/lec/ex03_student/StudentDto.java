package com.lec.ex03_student;
//21-01-08_JDBC_Dao&Dto		(c)cherryuki(ji)

public class StudentDto {
	private String rank; //String
	private int sno;
	private String name; //name & sname
	private String mname;
	private int score;
	public StudentDto(String name, String mname, int score) {
		super();
		this.name = name;
		this.mname = mname;
		this.score = score;
	}
	public StudentDto(String rank, String name, String mname, int score) {
		super();
		this.rank = rank;
		this.name = name;
		this.mname = mname;
		this.score = score;
	}
	public StudentDto(int sno, String name, String mname, int score) {
		super();
		this.sno = sno;
		this.name = name;
		this.mname = mname;
		this.score = score;
	}
	@Override
	public String toString() {
		return rank+"\t"+name+"\t"+mname+"\t"+score;
	}
	public String getRank() {
		return rank;
	}
	public void setRank(String rank) {
		this.rank = rank;
	}
	public int getSno() {
		return sno;
	}
	public void setSno(int sno) {
		this.sno = sno;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getMname() {
		return mname;
	}
	public void setMname(String mname) {
		this.mname = mname;
	}
	public int getScore() {
		return score;
	}
	public void setScore(int score) {
		this.score = score;
	}
	
}
