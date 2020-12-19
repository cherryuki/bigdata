package com.lec.ex04_buffered;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;

//키보드로부터 파일 이름을 받아 해당 파일 출력
public class Ex02_BufferedReaderKeyboard {
	public static void main(String[] args) {
		BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
		Reader 		  reader = null;
		BufferedReader br 	 = null;
		System.out.print("파일명을 입력하세요: ");
		try {
			String fileName = keyboard.readLine();
			File file = new File(fileName);//입력한 파일 이름의 파일 객체
			if(file.exists()) {//파일 존재 여부 확인
				reader 	= new FileReader(file);
				br		= new BufferedReader(reader);
				while(true) {
					String line = br.readLine(); //1 줄씩 읽음
					if(line==null) break;
					System.out.println(line);
				}
			}else {
				System.out.println("입력하신 파일이 존재하지 않습니다");
			}
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(br!=null) br.close();
				if(reader!=null) reader.close();
				if(keyboard!=null) keyboard.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
