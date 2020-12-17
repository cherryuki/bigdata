package com.lec.ex01_list;
//20-12-17_Collection		ⓒcherryuki(ji)
import java.util.ArrayList;

public class Ex01_ArrayList {
	public static void main(String[] args) {
		String[] array = new String[3];
		array[0]="str0";
		array[1]="str1";
		array[2]="str2";
		for(int idx=0; idx<array.length; idx++) {
			System.out.println("array["+idx+"] = "+array[idx]);
		}
		for(String arr:array) {
			System.out.println(arr);
		}
		ArrayList<String> arrayList = new ArrayList<String>();
		arrayList.add("str0"); //0인덱스
		arrayList.add("str1"); //1인덱스->2인덱스
		arrayList.add("str2"); //2인덱스->3인덱스
		arrayList.add(1,"11111"); //1인덱스
		for(int idx=0; idx<arrayList.size(); idx++) {//collection에서는 length가 아닌 size()
			System.out.println(idx+"번째: "+arrayList.get(idx));
		}
		arrayList.remove(1); //1번 인덱스값 삭제(2인덱스->1인덱스, 3인덱스->2인덱스)
		System.out.println(arrayList);//List형들은 toString이 override 되어 있음
		arrayList.clear(); //arrayList의 모든 데이터 삭제
		if(arrayList.isEmpty()) {
			System.out.println("arrayList 비워짐");
		}
		System.out.println(arrayList);
		//arrayList=null; //cf) 주소값을 없애 버린 것
		if(arrayList.size()==0) {//주소값 사라지면 NullPointerException
			System.out.println("arrayList비워짐");
		}
	}
}
