package com.lec.ex01_inputStreamOutputStream;
//20-12-17_input&output Stream		ⓒcherryuki(ji)

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

/* 1. 파일을 연다(스트림 객체 생성)
 * 2. 데이터를 읽는다(1byte 단위로 반복); 문자열의 경우 영어만 있을 경우 1byte, 영어 외 다른 언어일 경우 2byte 단위로 반복
 * 3. 파일을 닫는다 (finally: 예외여부와 상관 없이 반드시 실행)
 */
public class Ex01_inputStream {
	public static void main(String[] args) {
		InputStream is = null; //try-catch절 전에 스트림 변수 선언
		try {
			is = new FileInputStream("txt/1.txt"); //1단계: 파일 열기
			//2. 데이터 읽기(1byte 단위로 반복)
			while(true) {
				int i = is.read(); //1byte 읽기
				if(i==-1) break; // 파일 끝에 -1 저장되어 있음
				//System.out.println((char)i + "-아스키코드: "+i);
				System.out.print((char)i);
			}
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {//3. 파일 닫기 
			try {
				if(is!=null) is.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
