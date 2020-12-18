package com.lec.ex02_dataInputStreamOutputStream;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.DataOutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Scanner;

public class Ex03_ProductWrite {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String answer;
		OutputStream fos = null;
		DataOutputStream dos = null;
		try {
			fos = new FileOutputStream("txt/product.dat", true);
			dos = new DataOutputStream(fos);
			while(true) {
				System.out.print("재고 데이터를 입력하시겠습니까(x:종료)? ");
				answer = sc.next();
				if(answer.equalsIgnoreCase("x")) break;
				System.out.print("상품명을 입력하세요: ");
				dos.writeUTF(sc.next());
				System.out.print("상품의 가격을 입력하세요: ");
				dos.writeInt(sc.nextInt());
				System.out.print("상품의 재고 수량을 입력하세요: ");
				dos.writeInt(sc.nextInt());
			}
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
		sc.close();
		System.out.println("종료합니다");
	}//main
}
