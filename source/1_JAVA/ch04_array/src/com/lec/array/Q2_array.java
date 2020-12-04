package com.lec.array;
//다차원 배열의 합계
public class Q2_array {
	public static void main(String[] args) {
		int[][] arr= { {5,5,5,5,5,}, 
					{10,10,10,10,10}, 
					{20,20,20,20,20},
					{30,30,30,30,30}};
		int tot = 0;
		for(int i=0; i<arr.length; i++) {
			for(int j=0; j<arr.length; j++) {
				tot += arr[i][j];
			}
		}
		System.out.println("배열에 저장된 값들에 합계는 "+tot);
	}
}