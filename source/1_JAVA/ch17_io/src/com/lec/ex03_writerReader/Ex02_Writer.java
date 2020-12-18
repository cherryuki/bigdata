package com.lec.ex03_writerReader;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

public class Ex02_Writer {
	public static void main(String[] args) {
		Writer writer = null;
		try {
			writer = new FileWriter("txt/2.txt");
			String str = "안녕하세요\r\n";
			writer.write(str);
			String str1 = "오늘도 빅데이터 전문가가 되기 위해 복습 중입니다\r\n오늘은 2020년 12월 18일 입니다\r\n감사합니다";
			writer.write(str1);
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(writer!=null) writer.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
