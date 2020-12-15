package com.lec.ex02_date;
//20-12-14_API(Date_GregorianCalendar)		ⓒcherryuki(ji)

import java.text.SimpleDateFormat;
import java.util.GregorianCalendar;

public class Ex05_gcSimpleDateFormat {
	public static void main(String[] args) {
		GregorianCalendar gc = new GregorianCalendar();
		SimpleDateFormat sdf = new SimpleDateFormat("M월 d일(E) a h시 m분");
		System.out.println(sdf.format(gc.getTime()));
		
	}
}
