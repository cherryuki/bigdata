package com.lec.ex6_static_student;

public class StudentTestMain {
	public static void main(String[] args) {
		Student[] student = {new Student("정우성",90,80,95),
							new Student("김하늘",100,80,95),
							new Student("황정민",95,80,90),
							new Student("강동원",95,90,99),
							new Student("유아인",90,90,90)};
		String[] title = {"번호", "이름", "국어", "영어", "수학", "총점", "평균"};
		int tot[] = new int[5];
		int avg[] = new int[5];
	System.out.println("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■");	
	System.out.println("\t\t\t성적표");
	System.out.println("-----------------------------------------------------");
	for(String t:title) {
		System.out.print(t+"\t");
	}
	System.out.println();
	System.out.println("-----------------------------------------------------");
	for(Student s:student) {
		System.out.println(s.infoString());
		tot[0] += s.getKor();
		tot[1] += s.getEng();
		tot[2] += s.getMat();
		tot[3] += s.getTot();
		tot[4] += s.getAvg();
	}
	System.out.println("-----------------------------------------------------");
	for(int idx=0; idx<avg.length; idx++) {
		avg[idx] = tot[idx]/student.length; //버림
		avg[idx] = (int)((double)tot[idx]/student.length + 0.5); //반올림
	}
	System.out.print("\t총점\t");
	for(int t:tot) {
		System.out.print(t+"\t");
	}
	System.out.print("\n\t평균\t");
	for(int a:avg) {
		System.out.print(a+"\t");
	}
	System.out.println();
	System.out.println("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■");
	}
}

