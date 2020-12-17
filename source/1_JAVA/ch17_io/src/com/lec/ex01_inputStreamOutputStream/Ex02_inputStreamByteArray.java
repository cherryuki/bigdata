package com.lec.ex01_inputStreamOutputStream;
//20-12-17_input&output Stream		ⓒcherryuki(ji)

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

public class Ex02_inputStreamByteArray {
	public static void main(String[] args) {
		InputStream is = null;
		try {
			is = new FileInputStream("txt/1.txt");//1. 파일 열기
			//2. 읽는다
			byte[] bs = new byte[10]; //10byte씩 읽기
			while(true) {
				int readByteCount = is.read(bs);//int i = is.read(); 1byte씩 읽음
				if(readByteCount==-1) break;
				for(int i=0; i<readByteCount; i++) {
					System.out.print((char)bs[i]);
				}
			}
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
				try {
					if(is!=null) is.close();//3.파읽을 닫는다
				} catch (IOException e) {
					System.out.println(e.getMessage());
				}
		}
	}//main
}
