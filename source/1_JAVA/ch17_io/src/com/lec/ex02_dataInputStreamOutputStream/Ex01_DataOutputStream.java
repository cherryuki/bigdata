package com.lec.ex02_dataInputStreamOutputStream;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.DataOutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class Ex01_DataOutputStream {
	public static void main(String[] args) {
		OutputStream fos = null;
		DataOutputStream dos = null;
		try {
			fos = new FileOutputStream("txt/dataFile.dat");
			dos = new DataOutputStream(fos);
			dos.writeUTF("공유"); 	//String값 저장
			dos.writeInt(5); 	 	//int값 저장
			dos.writeDouble(100.5); //double값 저장
			System.out.println("저장 완료");
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			try {
				if(dos!=null) dos.close();
				if(fos!=null) fos.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}
	}
}
