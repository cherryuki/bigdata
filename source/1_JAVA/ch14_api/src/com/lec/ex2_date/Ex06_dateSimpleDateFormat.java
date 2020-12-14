package com.lec.ex2_date;
//20-12-14_API(Date_Date)		ⓒcherryuki(ji)
import java.text.SimpleDateFormat;
import java.util.Date;

public class Ex06_dateSimpleDateFormat {
	public static void main(String[] args) {
		Date date = new Date();
		SimpleDateFormat sdf = new SimpleDateFormat("yy-MM-dd(E) HH:mm");
		System.out.println(sdf.format(date));
	}
}
