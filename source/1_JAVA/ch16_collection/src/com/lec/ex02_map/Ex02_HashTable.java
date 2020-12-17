package com.lec.ex02_map;
//20-12-17_Collection		ⓒcherryuki(ji)

import java.util.Hashtable;
import java.util.Iterator;

public class Ex02_HashTable {
	public static void main(String[] args) {
		Hashtable<String, String> hashtable = new Hashtable<String, String>();
		hashtable.put("010-9999-9999", "공지철");
		hashtable.put("010-8888-8888", "박보검");
		hashtable.put("010-7777-7777", "손소유");
		hashtable.put("010-6666-6666", "유지수");
		System.out.println(hashtable);
		Iterator<String> iterator = hashtable.keySet().iterator();
		while(iterator.hasNext()) {
			String key = iterator.next();
			System.out.println(key+":"+hashtable.get(key));
		}
	}
}
