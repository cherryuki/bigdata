package com.lec.var;
//형변환: 묵시적 형변환, 명시적 형변환
public class Ex03_var {
	public static void main(String[] args) {
		int i1 = 10; // 4byte
		long l1 = 2200000000L;
		l1 = 10; //long형 8byte에 4byte짜리 10을 할당하기 위해
		   //4byte짜리 10이 8byte짜리 long형으로 묵시적인 형변환을 함
		double d = i1; //묵시적인 형변환
		d = 10.7;
		i1 = (int)d; //명시적인 형변환시에는 데이터 손실이 올 수 있다
		System.out.print("i1="+i1);
	}
}
