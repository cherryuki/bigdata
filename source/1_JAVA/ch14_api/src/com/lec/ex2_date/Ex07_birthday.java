package com.lec.ex2_date;
//20-12-14_API(Date_Calendar)		ⓒcherryuki(ji)
import java.util.Calendar;
import com.lec.ex1_string.Friend;

//배열에서 오늘 생일인 사람들의 목록 출력
//오늘 생일인 사람이 없으면 없다고 출력
public class Ex07_birthday {
	public static void main(String[] args) {
		Friend[] friends = {new Friend("홍길동", "010-0000-0000", "12-14"),
							new Friend("성춘향", "010-1234-1234", "05-07"),
							new Friend("이몽룡", "010-9999-9999", "12-15")};
		Calendar now = Calendar.getInstance();
		int month = now.get(Calendar.MONTH)+1;
		int day = now.get(Calendar.DAY_OF_MONTH);
		
		String monthString = (month<10)? "0"+month:""+month;
		String dayString = (day<10)? "0"+day:""+day;
		String today = monthString + "-" +dayString;
		System.out.println("오늘은 "+today);
		boolean searchOk = false;
		System.out.println("오늘 생일인 사람 목록");
		for(int idx=0; idx<friends.length; idx++) {
			String birthday = friends[idx].getBirth();
			if(birthday.equals(today)) {
				System.out.println(friends[idx]);
				searchOk=true;
			}//if
		}//for
		if(!searchOk) {
			System.out.println("오늘 생일인 사람이 없습니다");
		}
	}
}
