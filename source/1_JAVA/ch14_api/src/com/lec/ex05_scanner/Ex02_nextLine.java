package com.lec.ex05_scanner;
//20-12-15_API(Scanner)		ⓒcherryuki(ji)
import java.util.Scanner;

/* Ex01: next() -> nextLine()으로 버퍼 지우기 -> nextLine()이용
 * Ex02: nextLine() 이용 -> next()이용
 */
public class Ex02_nextLine {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("주소를 입력하세요: ");
		String address = sc.nextLine();
		System.out.println("입력하신 주소는 "+address);
		System.out.print("이름을 입력하세요: ");
		String name = sc.nextLine(); //name에 space 포함될 경우
		System.out.println("입력하신 이름은 "+name);
		System.out.print("나이를 입력하세요");
		int age = sc.nextInt();
		System.out.println("입력하신 나이는 "+age);
		sc.close();
	}
}
