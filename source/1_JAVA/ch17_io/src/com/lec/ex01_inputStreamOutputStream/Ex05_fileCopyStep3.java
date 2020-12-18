package com.lec.ex01_inputStreamOutputStream;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

/* 1. 스트림 객체 생성(inputStream, outputStream)
 * 2. 읽고 쓰기(반복); 파일 크기만큼(한 번에 읽어 들임)
 * 3. 스트림 닫기(finally)
 */

public class Ex05_fileCopyStep3 {
	public static void main(String[] args) {
		InputStream is = null;
		OutputStream os = null;
		try {
			File originalFile = new File("txt\\kongU.jpg");
			is = new FileInputStream(originalFile); //입력
			os = new FileOutputStream("txt/kongU_copy.jpg"); //출력
			byte[] bs = new byte[(int)originalFile.length()]; //파일 크기만큼씩(한 번에 읽어 들이기 위함)
			int cnt=0;
			while(true) {
				int readByteCount = is.read(bs);//1byte씩
				if(readByteCount==-1) break;
				os.write(bs, 0, readByteCount);
				++cnt;
			}
			System.out.println(cnt+"번 반복문 실행 후 파일 복사 성공");
			
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(is!=null) is.close();
				if(os!=null) os.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
