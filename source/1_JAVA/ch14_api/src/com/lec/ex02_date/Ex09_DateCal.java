package com.lec.ex02_date;
//20-12-14_API(Date)		ⓒcherryuki(ji)
import java.util.Date;
import java.util.GregorianCalendar;

public class Ex09_DateCal {
	public static void main(String[] args) {
		GregorianCalendar now = new GregorianCalendar(); //지금
		GregorianCalendar thatTime = new GregorianCalendar(2020, 10, 30, 9, 30, 0);//특정 시점
		long nowMillis = now.getTimeInMillis(); //1970~현재
		long thatMillis = thatTime.getTimeInMillis(); //1970~11/30
		long day = (nowMillis-thatMillis)/(1000*60*60*24); //초->분->시간->일
		System.out.println("개강일로부터 "+day+"일 지남");
		Date thatDay = new Date(new GregorianCalendar(2020, 10, 30, 9, 30, 0).getTimeInMillis());
		
	}
}
