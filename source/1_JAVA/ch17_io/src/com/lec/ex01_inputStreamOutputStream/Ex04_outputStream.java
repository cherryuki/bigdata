package com.lec.ex01_inputStreamOutputStream;
//20-12-17_input&output Stream		ⓒcherryuki(ji)

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class Ex04_outputStream {
	public static void main(String[] args) {
		OutputStream os = null;
		try {										//true추가시: 파일에 append, 없으면 덮어씀
			os = new FileOutputStream("txt/out.txt", true);//1. 스트림 객체 생성
			String str = "오늘도 열심히 복습 중\r\n";
			byte[] bs = str.getBytes(); //스트링을 바이트 배열로
			os.write(bs); //2. 파일쓰기
		} catch (FileNotFoundException e) {
			System.out.println("파일 못찾음 "+e.getMessage());
		} catch (IOException e) {
			System.out.println("파일 쓰기 오류 "+e.getMessage());
		} finally {
			try {
				if(os!=null) os.close();
			} catch (Exception ignore) { }
		}
	}
}
