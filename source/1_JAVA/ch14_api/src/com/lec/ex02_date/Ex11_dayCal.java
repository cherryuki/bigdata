package com.lec.ex02_date;

import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Scanner;

public class Ex11_dayCal {
	public static void main(String[] args) {
		Date checkOutDate
		= new Date(new GregorianCalendar(2020,10,15).getTimeInMillis());
		Date now = new Date();//now.getTime(): now 시점의 millisec
		long diff = now.getTime() - checkOutDate.getTime();
		long day = diff/(1000*60*60*24); //checkOutDate로부터 며칠 지났는지
		if(day>14) {
			day -= 14;
			System.out.print("연체료 "+(day*100)+"원을 받으셨나요(Y/N)? ");
			Scanner sc = new Scanner(System.in);
			String ok = sc.next();
			if(!ok.equalsIgnoreCase("y")) {
				System.out.println("연체료를 내셔야 반납처리 가능합니다");
				return;
			}
			sc.close();
		}
		System.out.println("반납 처리되었습니다");
	}
}
