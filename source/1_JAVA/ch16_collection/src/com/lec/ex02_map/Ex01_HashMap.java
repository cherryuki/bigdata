package com.lec.ex02_map;
//20-12-17_Collection		ⓒcherryuki(ji)

//HashMap<key, value>; key는 중복X
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;

public class Ex01_HashMap {
	public static void main(String[] args) {
		ArrayList<String> strlist = new ArrayList<String>();
		strlist.add("str11"); //list, set형은 add
		HashMap<Integer, String> hashmap = new HashMap<Integer, String>();
		hashmap.put(9, "str11"); //map형은 add가 아닌 put
		hashmap.put(15, "str22");
		hashmap.put(23, "str30");
		System.out.println(hashmap.get(23));
		System.out.println("remove전: "+hashmap);
		hashmap.remove(9);
		System.out.println("remove후: "+hashmap);
		hashmap.clear(); //hashmap의 데이터 모두 삭제
		hashmap.put(0, "Kong Yoo");
		hashmap.put(2, "Son Soyou");
		hashmap.put(5, "Yang Maehwa");
		hashmap.put(3, "Lee jieun");
		System.out.println(hashmap);
		Iterator<Integer> iterator = hashmap.keySet().iterator();
		while(iterator.hasNext()) {
			Integer key = iterator.next();
			System.out.println(key+"의 데이터는 "+hashmap.get(key));
		}
	}
}
