package com.lec.ex1_string;
//20-12-14_API(String)		ⓒcherryuki(ji)
import java.util.Scanner;

public class Ex04_searchTel {
	public static void main(String[] args) {
		String[] tels = {"010-1111-1111", "010-2222-2222", "010-3333-3333", "010-4444-3333"};
		Scanner sc = new Scanner(System.in);
		boolean searchOk = false; //중복되는 뒷자리가 있을 경우를 대비
		System.out.println("전화번호 뒷자리를 입력해주세요(4자리)");
		String searchTel = sc.next();
		for(int idx=0; idx<tels.length; idx++) {
			String temp = tels[idx];
			String post = temp.substring(temp.lastIndexOf("-")+1);
			if(searchTel.equals(post)) {
				System.out.println("찾으시는 전체번호가 "+tels[idx]+"가 맞습니까?");
				searchOk = true;
			}//if
		}//for
		if(!searchOk) {//searchOk==false
			System.out.println("입력하신 전화번호를 찾을 수 없습니다");
		}//if
		sc.close();
	}//main
}//class
