package com.lec.ex1_string;
//20-12-14_API(StringBuffer, StringBuilder)		ⓒcherryuki(ji)

/* System.currentTimeMillis(); 1970년~현재 밀리세컨(1/1,000초) 단위로 표시
 * 밀리세컨 조회 사이트: https://www.epochconverter.com/cloc (초단위로 올라감)
 * String의 경우 변수 변경이 빈번할 경우 새로운 메모리를 생성해야 해서 속도가 저하됨(StringBuilder가 가장 빠름)
 */
public class Ex07_speedCheck {
	public static void main(String[] args) {
		String str = "A";
		long start = System.currentTimeMillis(); //시작 시간 측정
		for(int i=0; i<100000; i++) {
			str=str.concat("a");
		}
		long end = System.currentTimeMillis(); //끝나는 시간 측정
		System.out.println("String 변경 시간: "+(end-start));
		
		StringBuffer strBuff = new StringBuffer("A");
		start = System.currentTimeMillis(); //시작 시간
		for(int i=0; i<100000; i++) {
			strBuff.append("a");
		}
		end = System.currentTimeMillis(); //끝 시간
		System.out.println("StringBuffer 변경 시간: "+(end-start));
		
		StringBuilder strBuil = new StringBuilder("A");
		start = System.currentTimeMillis(); //시작 시간
		for(int i=0; i<100000; i++) {
			strBuil.append("a");
		}
		end=System.currentTimeMillis(); //끝 시간
		System.out.println("StringBuilder 변경 시간: "+(end-start));
	}
}
