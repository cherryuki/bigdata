package com.lec.array;
//배열의 합계 
public class Q1_array {
	public static void main(String[] args) {
		int[] arr= {10,20,30,40,50};
		int tot = 0;
//		for(int i=0; i<arr.length; i++) {//일반 for문
//			tot += arr[i];
//		}
		for(int temp:arr) {//확장 for문
			tot += temp;
		}
		System.out.println("배열에 담긴 값들의 합은 "+tot);
	}
}
