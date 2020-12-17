package com.lec.ex01_list;
//20-12-17_Collection		ⓒcherryuki(ji)

//순차적(끝에서부터)으로 추가or삭제할 때는 ArrayList, 비순차적(중간 아무데서나)으로 추가or삭제할 때는 LinkedList 적합(속도 빠르다)
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Ex03_arrayListvsLinkedList {
	public static void main(String[] args) {
		ArrayList<String> array = new ArrayList<String>();
		LinkedList<String> linked = new LinkedList<String>();
		System.out.println("arrayList 순차적(끝에서) 추가 시간: "+addSeqTime(array));
		System.out.println("linkedList 순차적(끝에서) 추가 시간: "+addSeqTime(linked));
		System.out.println("arrayList 중간 인덱스로 추가 시간: "+addRandomTime(array));
		System.out.println("linkedList 중간 인덱스로 추가 시간: "+addRandomTime(linked));
		System.out.println("arrayList 끝부터 삭제 시간: "+removeSeqTime(array));
		System.out.println("linkedList 끝부터 삭제 시간: "+removeSeqTime(linked));
		System.out.println("arrayList 중간 인덱스 삭제 시간: "+removeRandomTime(array));
		System.out.println("linkedList 중간 인덱스 삭제 시간: "+removeRandomTime(linked));
	}
	private static long addSeqTime(List<String> list) {
		long start = System.currentTimeMillis(); //시작 시간
		for(int i=0; i<1000000; i++) {
			list.add("순차적으로 추가");
		}
		long end = System.currentTimeMillis(); //for문 수행 후 시간
		return end-start;
	}
	private static long addRandomTime(List<String> list) {
		long start = System.currentTimeMillis();
		for(int i=0; i<1000; i++) {
			list.add(100, "중간에 추가");
		}
		long end = System.currentTimeMillis();
		return end-start;
	}
	private static long removeSeqTime(List<String> list) {
		long start = System.currentTimeMillis();
		for(int i=list.size()-1; i>100000; i--) {
			list.remove(i);
		}
		long end = System.currentTimeMillis();
		return end-start;
	}
	private static long removeRandomTime(List<String> list) {
		long start = System.currentTimeMillis();
		for(int i=0; i<100000; i++) {
			list.remove(0);
		}
		long end = System.currentTimeMillis();
		return end-start;
	}
}
