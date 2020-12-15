package com.lec.ex05_scanner;
//20-12-15_API(Scanner)		ⓒcherryuki(ji)
import java.util.Scanner;

/*Ex01: next() -> nextLine()으로 버퍼 지우기 -> nextLine()이용
* Ex02: nextLine() 이용 -> next()이용
*/
public class Ex01 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("나이를 입력하세요: ");
		int age = sc.nextInt(); // 버퍼에 \n
		System.out.println("입력하신 나이는 "+age);
		System.out.print("이름을 입력하세요: ");
		String name = sc.next(); 
		System.out.println("입력하신 이름은 "+name);
		//버퍼에 처음 나오는 \n은 무시하고 whiteSpace 나오기 전까지 취함
		System.out.print("주소를 입력하세요: ");
		sc.nextLine(); //버퍼 지우기(\n)
		String address = sc.nextLine(); //버퍼에 \n이 나오는 앞까지 취함
		System.out.println("입력하신 주소는 "+address);
		System.out.println("=======프로그램 끝=======");
	}
}
