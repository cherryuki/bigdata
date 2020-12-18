package com.lec.ex02_dataInputStreamOutputStream;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;

public class Ex04_ProductList {
	public static void main(String[] args) {
		InputStream fis = null;
		DataInputStream dis = null;
		ArrayList<Product> product = new ArrayList<Product>();
		String name;
		int price, ps;
		try {
			fis = new FileInputStream("txt/product.dat");
			dis = new DataInputStream(fis);
			while(true) {
				name = dis.readUTF();
				price = dis.readInt();
				ps = dis.readInt();
				product.add(new Product(name, price, ps));//ArrayList에 추가
			}
			
		} catch (IOException e) {
			System.out.println("저장된 데이터값 출력");
		} finally {
			try {
				if(dis!=null) dis.close();
				if(fis!=null) fis.close();
			} catch (IOException e) {
				System.out.println(e.getMessage());
			}
		}//try-catch-finally
		for(Product p:product) {
			System.out.println(p);
		}
		System.out.println("이상 "+product.size()+"가지 상품 데이터 입력 됨");
	}//main
}