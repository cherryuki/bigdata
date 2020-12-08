package com.lec.ex01_store;
//20-12-08_abstract class	ⓒcherryuki(ji)

/*본사: 김치찌개-0 부대찌개-0 비빔밥-0 순대국-0 공기밥-0, 주변 환경에 맞게 가격 책정하세요.
 *상속받은 클래스에서 반드시 오버라이딩하게 설정(강제성 부여) 	<->오버라이딩 금지: final 
 *추상 클래스(abstract class): 추상 메소드가 1개 이상 있는 클래스
 */
public abstract class HeadQuarterStore {//추상(abstract) 클래스
	private String name;
	public HeadQuarterStore(String name) {
		this.name=name;
	}
	public abstract void kimchi(); //추상(abstract) 메소드
	public abstract void budae();
	public abstract void bibib();
	public abstract void sundae();
	public abstract void gonggib();
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name=name;
	}
}
