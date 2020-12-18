package com.lec.ex04_buffered;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;

public class Ex01_BufferedReader {
	public static void main(String[] args) {
		Reader reader = null;
		BufferedReader br = null;
		try {
			reader = new FileReader("txt/2.txt");
			br = new BufferedReader(reader);
			while(true) {
				String line = br.readLine();
				if(line==null) break;
				System.out.println(line);
			}
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(br!=null) br.close();
				if(reader!=null) reader.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
