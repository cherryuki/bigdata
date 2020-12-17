package com.lec.ex03_set;
//20-12-17_Collection		ⓒcherryuki(ji)
import java.util.HashSet;
import java.util.Iterator;

public class Ex01_HashSet {
	public static void main(String[] args) {
		HashSet<String> hashset = new HashSet<String>();
		hashset.add("str0");
		hashset.add("str1");
		hashset.add("str2");
		hashset.add("str3");
		System.out.println(hashset);
		System.out.println("hashset 사이즈: "+hashset.size());
		hashset.add("str2");//중복 허용X
		System.out.println(hashset);//변함 없음(중복X)
		System.out.println("hashset 사이즈: "+hashset.size());//크기 변함 없음
		Iterator<String> iterator = hashset.iterator();
		while(iterator.hasNext()) {
			System.out.println(iterator.next());
		}
	}
}
