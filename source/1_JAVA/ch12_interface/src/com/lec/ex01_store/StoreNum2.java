package com.lec.ex01_store;
//20-12-09_interface	ⓒcherryuki(ji)

//2호점: 김치찌개-5,000 부대찌개-5,000 비빔밥-5,000 순대국-5,000  공기밥-무료
public class StoreNum2 implements HeadQuarterStore {
	private String name;
	public StoreNum2(String name) {
		this.name=name;
	}
	@Override
	public void kimchi() {
		System.out.println("김치찌개 5,000원");
	}
	@Override
	public void budae() {
		System.out.println("부대찌개 5,000원");
	}
	@Override
	public void bibib() {
		System.out.println("비빔밥 5,000원");
	}
	@Override
	public void sundae() {
		System.out.println("순대국 5,000원");
	}
	@Override
	public void gonggib() {
		System.out.println("공기밥 무료");
	}
	@Override
	public String getName() {
		return name;
	}
}
