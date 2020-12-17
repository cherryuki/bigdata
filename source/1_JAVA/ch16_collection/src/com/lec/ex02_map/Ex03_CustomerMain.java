package com.lec.ex02_map;
//20-12-17_Collection		ⓒcherryuki(ji)

import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;

import com.lec.ex01_list.Customer;

public class Ex03_CustomerMain {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String answer, name, phone, address;
		HashMap<String, Customer> customer = new HashMap<String, Customer>();
		while(true){
			System.out.print("회원가입을 진행하시겠습니까(Y/N)? ");
			answer=sc.next();
			if(answer.equalsIgnoreCase("n")) {
				break;
			}else {//회원가입 진행
				System.out.print("성함을 입력하세요: ");
				sc.nextLine();//버퍼 지우기
				name=sc.nextLine(); //space 포함
				System.out.print("연락처를 입력하세요: ");
				phone=sc.nextLine();
				System.out.print("주소를 입력하세요: ");
				address=sc.nextLine();
				customer.put(phone, new Customer(name, phone, address));
			}
		}
		sc.close();
		if(customer.isEmpty()) {
			System.out.println("가입한 회원이 없습니다");
		}else {
			System.out.println("가입한 회원 목록");
			Iterator<String> iterator = customer.keySet().iterator();
			while(iterator.hasNext()) {
				String key = iterator.next();
				System.out.println(customer.get(key));
			}
		}	
	}
}
