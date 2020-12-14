package com.lec.ex2_date;
//20-12-14_API(Date_Calendar)		ⓒcherryuki(ji)

import java.text.SimpleDateFormat;
import java.util.Calendar;

/* yyyy (년도 4자리) yy(년도 2자리)
 * M(9) MM(09) 월
 * d(9) dd(09) 일
 * E 요일
 * a 오전/오후
 * H 24시간
 * h 12시간
 * m 분
 * s 초
 * S 밀리세컨
 * w (올해 몇번째 주) W(이번달 몇번째 주인지) D(올해 몇번째 날)
 */
public class Ex04_CalSimpleDateFormat {
	public static void main(String[] args) {
		Calendar cal = Calendar.getInstance();
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy년 MM월 dd일 E요일 a hh시 mm분 ss초");
		String today = sdf.format(cal.getTime());
		System.out.println(today);
	}
}
