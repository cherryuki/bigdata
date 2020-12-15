package com.lec.ex03_Math;
//20-12-15_API(Math)		ⓒcherryuki(ji)
import java.util.Random;

//중복된 로또 번호를 발생하지 않게 처리할 것
public class Ex04_lotto {
	public static void main(String[] args) {
		Random random = new Random();
		int[] lotto = new int[6];
		for(int i=0; i<lotto.length; i++) {
			int temp = random.nextInt(45)+1;
			boolean ok = true;
			for(int j=0; j<i; j++) {
				if(temp==lotto[j]) {//중복된 수가 뽑힌 경우
					i--;
					ok=false;
					break; //for(j) 반복문 빠져나감
				}
			}//for(j) - 중복 확인 과정
			if(ok) {
				lotto[i]=temp;
			}
		}
		for(int l:lotto) {
			System.out.print(l+"\t");
		}
	}
}
