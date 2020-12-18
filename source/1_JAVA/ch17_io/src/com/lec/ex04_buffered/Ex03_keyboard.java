package com.lec.ex04_buffered;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Writer;

/* 1.키보드로부터 출력할 파일 이름(txt/2.txt)
 * while 2. 출력할 파일 내용? (x:종료)
 * 		 3. 키보드에서 입력한 내용을 파일로 출력
 */
public class Ex03_keyboard {
	public static void main(String[] args) {
		BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
		Writer writer = null;
		System.out.print("파일명을 입력하세요: "); //없으면 파일 생성
		try {
			String fileName = keyboard.readLine();
			writer = new FileWriter(fileName, true);
			while(true) {
				System.out.print("출력할 파일 내용을 입력하세요(x:종료): ");
				String content = keyboard.readLine();
				if(content.equalsIgnoreCase("x")) break;
				writer.write(content+"\r\n");
			}
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(writer!=null) writer.close();
				if(keyboard!=null) keyboard.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
