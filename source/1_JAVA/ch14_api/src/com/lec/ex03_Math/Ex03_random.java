package com.lec.ex03_Math;
//20-12-15_API(Math)		ⓒcherryuki(ji)
import java.util.Random;

public class Ex03_random {
	public static void main(String[] args) {
		System.out.println((int)(Math.random()*45)+1);//1~45사이 임의의 정수
		Random random = new Random();
		System.out.println("int 난수: "+random.nextInt());//임의의 정수
		System.out.println("0~100까지 int 난수: "+random.nextInt(101));
		System.out.println("0~44까지 int 난수: "+random.nextInt(45));
		System.out.println("1~45까지 int 난수: "+(random.nextInt(45)+1));
		System.out.println("double 난수(0~1미만): "+random.nextDouble());//Math.random()
		System.out.println("T/F 중에 하나 선택: "+random.nextBoolean());
	}
}
