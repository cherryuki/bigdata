package com.lec.ex02_date;
//20-12-14_API(Date)		ⓒcherryuki(ji)

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.GregorianCalendar;

public class Staff {
	private String num;
	private String name;
	private String part;
	private Date enterDate;
	public Staff() {}
	public Staff(String num, String name, String part) {
		this.num=num;
		this.name=name;
		this.part=part;
		enterDate = new Date(); //오늘
	}
	public Staff(String num, String name, String part, int yyyy, int mm, int dd) {
		this.num=num;
		this.name=name;
		this.part=part;
		enterDate = new Date(new GregorianCalendar(yyyy, mm-1, dd).getTimeInMillis());
	}
	@Override
	public String toString() {
		SimpleDateFormat sdf = new SimpleDateFormat("yy-MM-dd");
		return "[사번]"+num+" [이름]"+name+" [입사일]"+sdf.format(enterDate);
	}
}
