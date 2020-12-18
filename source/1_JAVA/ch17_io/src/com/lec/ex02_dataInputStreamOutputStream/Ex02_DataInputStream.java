package com.lec.ex02_dataInputStreamOutputStream;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

public class Ex02_DataInputStream {
	public static void main(String[] args) {
		InputStream fis = null;
		DataInputStream dis = null;
		try {
			fis = new FileInputStream("txt\\dataFile.dat");
			dis = new DataInputStream(fis);
			String name = dis.readUTF();
			int grade = dis.readInt();
			double score = dis.readDouble();
			System.out.println("파일로부터 입력 받은 값: "+name+"\t"+grade+"\t"+score);
			
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(dis!=null) dis.close();
				if(fis!=null) fis.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}