package com.lec.ex01_store;
//20-12-09_interface	ⓒcherryuki(ji)

/*1호점: 김치찌개-4,500 부대찌개-5,000 비빔밥-6,000 순대국-안팔아 공기밥-1,000원
*StoreNum1 store = new StroeNum("주택가 1호점")
*/
public class StoreNum1 implements HeadQuarterStore {
	private String name;
	public StoreNum1(String name) {
		this.name=name;
	}
	@Override
	public void kimchi() {
		System.out.println("김치찌개 4,500원");
	}
	@Override
	public void budae() {
		System.out.println("부대찌개 5,000원");
	}
	@Override
	public void bibib() {
		System.out.println("비빔밥 6,000원");
	}
	@Override
	public void sundae() {
		System.out.println("순대국은 팔지 않습니다");
	}
	@Override
	public void gonggib() {
		System.out.println("공기밥 1,000원");
	}
	@Override
	public String getName() {
		return name;
	}
}
