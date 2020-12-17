package com.lec.ex03_set;
//20-12-17_Collection		ⓒcherryuki(ji)
import java.util.HashSet;
import java.util.TreeSet;

public class Ex02_lotto {
	public static void main(String[] args) {
		HashSet<Integer> lotto1 = new HashSet<Integer>();
		while(lotto1.size()<6) {
			lotto1.add((int)(Math.random()*45)+1);
		}
		System.out.println(lotto1); //숫자 정렬X
		TreeSet<Integer> lotto2 = new TreeSet<Integer>();
		while(lotto2.size()<6) {
			lotto2.add((int)(Math.random()*45)+1);
		}
		System.out.println(lotto2); //숫자 정렬되어서 나옴
	}
}
