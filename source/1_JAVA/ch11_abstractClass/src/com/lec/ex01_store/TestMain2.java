package com.lec.ex01_store;
//20-12-08_abstract class	ⓒcherryuki(ji)

//HeadQuarterStore h = new HeadQuaterStore(); //불가
public class TestMain2 {
	public static void main(String[] args) {
		HeadQuarterStore[] store = {//new HeadQuarterStore("--- 본 사 ---"), //불가능
									new StoreNum1("--- 주택가 1호점 ---"),
									new StoreNum2("--- 대학가 2호점 ---"),
									new StoreNum3("--- 증권가 3호점 ---")};
		for(HeadQuarterStore s:store) {//확장 for문
			System.out.println(s.getName());
			s.kimchi();
			s.budae();
			s.bibib();
			s.sundae();
			s.gonggib();
		}
		for(int idx=0; idx<store.length; idx++) {//일반 for문
			System.out.println(store[idx].getName());
			store[idx].kimchi();
			store[idx].budae();
			store[idx].bibib();
			store[idx].sundae();
			store[idx].gonggib();
		}
		
	}
}
