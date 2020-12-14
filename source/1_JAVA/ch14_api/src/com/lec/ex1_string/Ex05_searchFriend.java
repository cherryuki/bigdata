package com.lec.ex1_string;
//20-12-14_API(String)		ⓒcherryuki(ji)

import java.util.Scanner;
/*전화번호 뒷자리로 친구 찾기
*Friend 참고
*/
public class Ex05_searchFriend {
	public static void main(String[] args) {
		Friend[] friends = {new Friend("홍길동", "010-0000-0000", "12-14"),
							new Friend("성춘향", "010-1234-1234", "05-07"),
							new Friend("이몽룡", "010-9999-9999", "07-08")};
		Scanner sc = new Scanner(System.in);
		System.out.println("찾으려는 친구 전화번호 뒷자리를 입력하세요(4자리)");
		String searchTel = sc.next();
		int idx;
		boolean searchOk = false;
		for(idx=0; idx<friends.length; idx++) {
			String post = friends[idx].getTel().substring(friends[idx].getTel().lastIndexOf("-")+1);
			if(post.equals(searchTel)) {
				System.out.println(friends[idx]); //toString Override
				searchOk = true;
				//break; //중복된 뒷번호가 없을 경우
			}
		}
		if(!searchOk) {
			System.out.println("해당 번호의 친구가 없습니다");
		}
		sc.close();
	}
}
