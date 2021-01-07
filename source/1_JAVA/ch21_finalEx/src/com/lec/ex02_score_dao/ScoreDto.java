package com.lec.ex02_score_dao;
//21-01-07_JDBC		ⓒcherryuki(ji)

public class ScoreDto {
	private int rank;
	private String name;
	private String jname;
	private int kor;
	private int eng;
	private int mat;
	private int total;
	public ScoreDto(String name, String jname, int kor, int eng, int mat) {
		super();
		this.name = name;
		this.jname = jname;
		this.kor = kor;
		this.eng = eng;
		this.mat = mat;
	}
	public ScoreDto(int rank, String name, String jname, int kor, int eng, int mat, int total) {
		super();
		this.rank = rank;
		this.name = name;
		this.jname = jname;
		this.kor = kor;
		this.eng = eng;
		this.mat = mat;
		this.total = total;
	}
	@Override
	public String toString() {
		if(name.length()>=7) {
			return rank + "\t" + name + "\t"+ jname + "\t" + kor + "\t" + eng
					+ "\t" + mat + "\t" + total;
		} else {
			return rank + "\t" + name + "\t\t"+ jname + "\t" + kor + "\t" + eng
					+ "\t" + mat + "\t" + total;
		}
	}
	//getter&setter
	public int getRank() {
		return rank;
	}
	public void setRank(int rank) {
		this.rank = rank;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getJname() {
		return jname;
	}
	public void setJname(String jname) {
		this.jname = jname;
	}
	public int getKor() {
		return kor;
	}
	public void setKor(int kor) {
		this.kor = kor;
	}
	public int getEng() {
		return eng;
	}
	public void setEng(int eng) {
		this.eng = eng;
	}
	public int getMat() {
		return mat;
	}
	public void setMat(int mat) {
		this.mat = mat;
	}
	public int getTotal() {
		return total;
	}
	public void setTotal(int total) {
		this.total = total;
	}
	
}
