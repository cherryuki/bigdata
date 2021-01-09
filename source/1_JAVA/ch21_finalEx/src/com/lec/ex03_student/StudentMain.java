package com.lec.ex03_student;
//21-01-08_JDBC_Dao&Dto		(c)cherryuki(ji)

import java.util.ArrayList;
import java.util.Scanner;

public class StudentMain {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StudentDao dao = StudentDao.getInstance();
		String fn;
		ArrayList<StudentDto> student;
		do {
			System.out.println("1:학생 추가|2:학과별 조회|3:전체 학생 조회|4:제적자 조회|그 외:종료");
			fn = sc.next();
			switch(fn) {
			case "1"://insertStudent
				System.out.print("추가할 학생 이름을: ");
				String name = sc.next().trim();
				System.out.print("학과명: ");
				String mname = sc.next().trim();
				System.out.print("점수: ");
				int score = sc.nextInt();
				if(score<0||score>100) {//check 조건
					do {
						System.out.println("유효하지 않은 점수입니다");
						System.out.print("점수(0~100)을 입력하세요: ");
						score = sc.nextInt();
					}while(score<0||score>100);
				}
				StudentDto newStudent = new StudentDto(name, mname, score);
				int result = dao.insertStudent(newStudent);
				System.out.println(result==StudentDao.SUCCESS? result+"행 추가":"추가 실패");
				break;
			case "2"://selectMname
				System.out.print("조회할 학과명을 입력하세요: ");
				mname = sc.next().trim();
				student = dao.selectMname(mname);
				if(student.size()==0) {
					System.out.println("조회 가능한 학생이 없습니다");
				} else {
					System.out.println("등수\t이름(학번)\t\t학과\t점수");
					for(StudentDto s:student)
						System.out.println(s);
				}
				break;
			case "3"://selectAll
				student = dao.selectAll();
				if(student.isEmpty()) {
					System.out.println("조회 가능한 학생이 없습니다");
				} else {
					System.out.println("등수\t이름(학번)\t\t학과\t점수");
					for(StudentDto s:student)
						System.out.println(s);
				}
			break;	
			case "4"://selectExpel
				student = dao.selectExpel();
				if(student.isEmpty()) {
					System.out.println("조회 가능한 학생이 없습니다");
				} else {
					System.out.println("등수\t이름(학번)\t\t학과\t점수");
					for(StudentDto s:student)
						System.out.println(s);
				}
			break;
			}
		} while(fn.equals("1")||fn.equals("2")||fn.equals("3")||fn.equals("4"));
		System.out.println("Bye");
	}
}
