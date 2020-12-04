package com.lec.array;
//다차원 배열
public class Ex03_array {
	public static void main(String[] args) {
		int[][] test = {{10,20,30}, {40,50,60}};
		test[0][2] = 300;
		System.out.println(test[0][2]);
		for(int i=0; i<test.length; i++) {
			for(int j=0; j<test.length; j++) {
				System.out.printf("test[%d][%d] = %d\n", i, j, test[i][j]);
			}
		}
	}
}
