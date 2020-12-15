package com.lec.ex02_date;
//20-12-14_API(Date_Calendar)		ⓒcherryuki(ji)
import java.util.Calendar;

public class Ex01_Calendar {
	public static void main(String[] args) {
		Calendar cal = Calendar.getInstance(); //Calendar는 싱글톤 클래스(new 생성자X)
		System.out.println(cal);
		int year = cal.get(Calendar.YEAR);
		int month = cal.get(Calendar.MONTH)+1; //시스템: 0~11월 +1 해줘야 함
		int day = cal.get(Calendar.DAY_OF_MONTH);
		int week = cal.get(Calendar.DAY_OF_WEEK); //1(일) 2(월) ... 7(토)
		int hour24 = cal.get(Calendar.HOUR_OF_DAY); //24시간
		int hour = cal.get(Calendar.HOUR); //12시간
		int ampm = cal.get(Calendar.AM_PM); //0(am), 1(pm)
		int minute = cal.get(Calendar.MINUTE); 
		int second = cal.get(Calendar.SECOND);
		int millisec = cal.get(Calendar.MILLISECOND);
		System.out.printf("%d년 %d월 %d일 ", year, month, day);
		switch(week) {
		case 1: System.out.println("일요일"); break;
		case 2: System.out.println("월요일"); break;
		case 3: System.out.println("화요일"); break;
		case 4: System.out.println("수요일"); break;
		case 5: System.out.println("목요일"); break;
		case 6: System.out.println("금요일"); break;
		case 7: System.out.println("토요일"); break;
		}
		System.out.printf("%d시 %d분 %d초 %d\n", hour24, minute, second, millisec);
		System.out.printf("%tY년 %tm월 %td일 %ta요일 %tH시 %tM분 %tS초\n", cal, cal, cal, cal, cal, cal, cal);
		System.out.printf("%1$tY년 %1$tm월 %1$td일 %1$ta요일 %1$tH시 %1$tM분 %1$tS초\n", cal);
		System.out.print((ampm==0)? "오전":"오후");
		System.out.printf("%d시 %d분 %d초\n", hour, minute, second);
		System.out.printf("%tl시 %tM분 %tS초\n", cal, cal, cal);
		System.out.printf("%1$tl시 %1$tM분 %1$tS초\n", cal);
		//tY(년) tm(월) td(일) ta(요일) tH(24시) tl(12시) tM(분) tS(초)
		//d(정수) f(실수) s(문자열) c(문자) b(true/false)
	}
}
