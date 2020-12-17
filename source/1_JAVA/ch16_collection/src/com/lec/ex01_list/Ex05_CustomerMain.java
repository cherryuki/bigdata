package com.lec.ex01_list;
//20-12-17_Collection		ⓒcherryuki(ji)
import java.util.ArrayList;
import java.util.Scanner;

public class Ex05_CustomerMain {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String answer, name, phone, address;
		ArrayList<Customer> customer = new ArrayList<Customer>();
		do {
			System.out.print("회원가입을 진행하시겠습니까(Y/N)? ");
			answer=sc.next();
			if(answer.equalsIgnoreCase("y")) {//회원가입 진행
				System.out.print("성함을 입력해주세요: ");
				sc.nextLine();//버퍼 지우기
				name=sc.nextLine(); //스페이스 포함
				System.out.print("전화번호를 입력해주세요: ");
				phone=sc.next();
				System.out.print("주소를 입력해주세요: ");
				sc.nextLine();
				address=sc.nextLine();
				customer.add(new Customer(name, phone, address));
			}else if(answer.equalsIgnoreCase("n")) {
				break;
			}
		}while(true);
		System.out.println("가입한 회원 리스트 목록");
		for(Customer c:customer) {
			System.out.println(c);
		}
	}
}
