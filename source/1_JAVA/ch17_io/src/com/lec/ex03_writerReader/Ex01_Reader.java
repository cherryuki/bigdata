package com.lec.ex03_writerReader;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;


public class Ex01_Reader {
	public static void main(String[] args) {
		Reader reader = null;
		try {
			reader = new FileReader("txt/1.txt");
			while(true) {
				int i = reader.read();
				if(i==-1) break;
				System.out.print((char)i);
			}
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(reader!=null) reader.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
		
	}
}
