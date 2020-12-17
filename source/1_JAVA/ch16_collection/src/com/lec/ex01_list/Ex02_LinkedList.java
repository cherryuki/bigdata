package com.lec.ex01_list;
//20-12-17_Collection		ⓒcherryuki(ji)
import java.util.LinkedList;

public class Ex02_LinkedList {
	public static void main(String[] args) {
		LinkedList<String> linkedList = new LinkedList<String>();
		linkedList.add("str0");
		linkedList.add("str1");
		linkedList.add("str2");
		linkedList.add(1, "1111");
		System.out.println(linkedList); //List형들은 toString이 override 되어 있음
		for(int i=0; i<linkedList.size(); i++) 
			System.out.println(linkedList.get(i));
		linkedList.remove("1111");
		System.out.println(linkedList);
		linkedList.clear();
		System.out.println(linkedList.isEmpty() ? "비워졌다":"안 비워졌다");
	}
}
