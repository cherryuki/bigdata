package com.lec.ex01_string;
//20-12-14_API(StringToken)		ⓒcherryuki(ji)
import java.util.StringTokenizer;

public class Ex08_stringToken {
	public static void main(String[] args) {
		String str1 = "공유 박보검 한지민 남주혁 수지";
		String str2 = "2020/12/14";
		StringTokenizer token1 = new StringTokenizer(str1); // space, \t, \n 기준 분할
		StringTokenizer token2 = new StringTokenizer(str2, "/");// 기준" "으로 분할
		System.out.println("token1의 갯수: "+token1.countTokens());
		while(token1.hasMoreTokens()) {
			System.out.println(token1.nextToken());
		}
		System.out.println("token2의 갯수: "+token2.countTokens());
		while(token2.hasMoreElements()) {//Token과 Element 같은 결과
			System.out.println(token2.nextElement());
		}
	}
}
