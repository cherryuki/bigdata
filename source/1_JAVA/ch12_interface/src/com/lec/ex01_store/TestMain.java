package com.lec.ex01_store;
//20-12-09_interface	ⓒcherryuki(ji)

//HeadQuarterStore h = new HeadQuarterStore(); //불가
public class TestMain {
	public static void main(String[] args) {
//		HeadQuarterStore st = new HeadQuarterStore("===본 사===");
//		System.out.println(st.getName());
//		st.kimchi();
//		st.budae();
//		st.bibib();
//		st.sundae();
//		st.gonggib();
		StoreNum1 st1 = new StoreNum1("===주택가 1호점===");
		System.out.println(st1.getName());
		st1.kimchi();
		st1.budae();
		st1.bibib();
		st1.sundae();
		st1.gonggib();
		StoreNum2 st2 = new StoreNum2("===대학가 2호점===");
		System.out.println(st2.getName());
		st2.kimchi();
		st2.budae();
		st2.bibib();
		st2.sundae();
		st2.gonggib();
		StoreNum3 st3 = new StoreNum3("===증권가 3호점===");
		System.out.println(st3.getName());
		st3.kimchi();
		st3.budae();
		st3.bibib();
		st3.sundae();
		st3.gonggib();
//		HeadQuarterStore[] store = {st, st1, st2, st3};//TestMain2에서 실행
	}
}
