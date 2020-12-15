package com.lec.ex02_date;
//20-12-14_API(Date_Date)		ⓒcherryuki(ji)
import java.text.SimpleDateFormat;
import java.util.Date;

import com.lec.ex01_string.Friend;

public class Ex08_birthday {
	public static void main(String[] args) {
		Friend[] friends = {new Friend("홍길동", "010-0000-0000", "12-14"),
							new Friend("성춘향", "010-1234-1234", "05-07"),
							new Friend("이몽룡", "010-9999-9999", "12-15")};
		Date date = new Date();//new Date(110,11,14): 2020년 12월 14일
		boolean searchOk = false;
		SimpleDateFormat sdf = new SimpleDateFormat("MM-dd");
		String today = sdf.format(date);
		System.out.println("오늘 날짜: "+today);
		for(int idx=0; idx<friends.length; idx++) {
			String temp = friends[idx].getBirth();
			if(temp.equals(today)) {
				System.out.println("오늘 생일인 친구: "+friends[idx].getName());
				searchOk=true;
			}//if
		}//for
		if(!searchOk) {
			System.out.println("오늘 생일인 친구가 없습니다");
		}//if
	}//main
}//class
