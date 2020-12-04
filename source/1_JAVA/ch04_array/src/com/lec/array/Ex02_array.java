package com.lec.array;
//배열의 복사
public class Ex02_array {
	public static void main(String[] args) {
		int[] score = {10,20,30,40,50};
		int[] s = new int[score.length];
//		for(int i=0; i<s.length; i++) {
//			s[i] = score[i];
//			System.out.printf("s[%d]=%d, score[%d]=%d\n", i, s[i], i, score[i]);
//		}
//		System.out.println("***************************");
		System.arraycopy(score, 0, s, 0, score.length);
		s[0] = 999;
		for(int i=0; i<s.length; i++) {
			System.out.printf("s[%d]=%d, score[%d]=%d\n", i, s[i], i, score[i]);
		}
	}
}
