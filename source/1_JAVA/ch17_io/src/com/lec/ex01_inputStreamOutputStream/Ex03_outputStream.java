package com.lec.ex01_inputStreamOutputStream;
//20-12-17_input&output Stream		ⓒcherryuki(ji)

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class Ex03_outputStream {
	public static void main(String[] args) {
		OutputStream os = null;
		try {
			os = new FileOutputStream("txt/out.txt");
			//1.파일 열기(스트림 객체 생성); 파일이 없을 경우 생성, but 경로가 잘못 되어 있으면(폴더가 없으면) 에러 발생
			byte[] bs = {'H','e','l','l','o','\r','\n','J','A','V','A'};//\r\n -> enter
			for(int i=0; i<bs.length; i++) {
				os.write(bs[i]); //2.파일에 데이터 쓰기(1byte씩 반복)
			}
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(os!=null) os.close();//3.파일 닫기
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
