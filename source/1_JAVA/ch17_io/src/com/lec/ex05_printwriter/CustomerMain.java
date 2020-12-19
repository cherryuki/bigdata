package com.lec.ex05_printwriter;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Writer;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class CustomerMain {
	public static void main(String[] args) {
		BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
		Writer writer = null;
		ArrayList<Customer> customer = new ArrayList<Customer>();
		String name, tel, birth, address;
		Date today = new Date();
		SimpleDateFormat sdf = new SimpleDateFormat("MM-dd");
		
		try {
			while(true) {
				System.out.print("회원 정보를 입력하시겠습니까(N:종료)? ");
				String answer = keyboard.readLine();
				if(answer.equalsIgnoreCase("n")) break;
				System.out.print("성함을 입력하세요: ");
				name=keyboard.readLine();
				System.out.print("전화번호를 입력하세요: ");
				tel=keyboard.readLine();
				System.out.print("생일을 입력하세요(MM-dd): ");
				birth=keyboard.readLine();
				if(birth.equals(sdf.format(today))) {
					System.out.println(name+"님 생일 축하합니다");
				}
				System.out.print("주소를 입력하세요: ");
				address=keyboard.readLine();
				customer.add(new Customer(name, tel, birth, address));
			}//while
			writer = new FileWriter("txt/customer.txt",true);
			for(Customer c:customer) {
				System.out.println(c);
				writer.write(c.toString()+"\r\n");
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
