package com.lec.ex01_store;
//20-12-09_interface	ⓒcherryuki(ji)

/*본사: 김치찌개-0 부대찌개-0 비빔밥-0 순대국-0 공기밥-0, 주변 환경에 맞게 가격 책정하세요.
 *HeadQuarterStore h = new HeadQuarterStore(); 불가능
 *h.kimchi()
 */
public interface HeadQuarterStore {//class를 interface로 변경
	public abstract void kimchi(); //추상(abstract) 메소드
	public abstract void budae();
	public abstract void bibib();
	public abstract void sundae();
	public abstract void gonggib();
	public String getName();
}
