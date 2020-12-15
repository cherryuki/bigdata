package com.lec.ex01_string;
//20-12-14_API(StringToken)		ⓒcherryuki(ji)
import java.util.StringTokenizer;

public class Ex09_tokenArray {
	public static void main(String[] args) {
		String str = "공유 박보검 한지민 남주혁 수지";
		String[] names;
		StringTokenizer tokenizer = new StringTokenizer(str);
		names = new String[tokenizer.countTokens()];
		int idx = 0;
		while(tokenizer.hasMoreTokens()) {
			names[idx++] = tokenizer.nextToken();
		}
		System.out.println("제대로 배열에 들어갔는지 확인");
		for(String name:names) {
			System.out.println(name);
		}
	}
}
