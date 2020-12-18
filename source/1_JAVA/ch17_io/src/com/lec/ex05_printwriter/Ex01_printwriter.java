package com.lec.ex05_printwriter;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.Writer;

public class Ex01_printwriter {
	public static void main(String[] args) {
		PrintWriter printWriter = null;
		OutputStream os = null;
		Writer writer = null;
		try {
//			os = new FileOutputStream("txt/out.txt");
//			printWriter = new PrintWriter(os);
//			writer = new FileWriter(writer); //스트림 객체 생성
			printWriter = new PrintWriter("txt/out.txt");
			System.out.println("안녕하세요\n반갑습니다");
			printWriter.println("안녕하세요\r\n반갑습니다");
			System.out.print(" 오늘도 좋은 하루 보내시길 바랍니다\n");
			printWriter.print(" 오늘도 좋은 하루 보내시길 바랍니다\r\n");
			System.out.printf("%5s %3d %3d %5.1f\n", "공유", 12, 18, 11.3);
			printWriter.printf("%5s %3d %3d %5.1f\r\n", "공유", 12, 18, 11.3);
			System.out.printf("%5s %3d %3d %5.1f\n", "공유", 100, 200, 100.0);
			printWriter.printf("%5s %3d %3d %5.1f\r\n", "공유", 100, 200, 100.0);
			
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(printWriter!=null) printWriter.close();
			} catch (Exception e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
