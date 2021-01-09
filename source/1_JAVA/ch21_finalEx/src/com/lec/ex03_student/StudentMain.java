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
			System.out.println("1:�л� �߰�|2:�а��� ��ȸ|3:��ü �л� ��ȸ|4:������ ��ȸ|�� ��:����");
			fn = sc.next();
			switch(fn) {
			case "1"://insertStudent
				System.out.print("�߰��� �л� �̸���: ");
				String name = sc.next().trim();
				System.out.print("�а���: ");
				String mname = sc.next().trim();
				System.out.print("����: ");
				int score = sc.nextInt();
				if(score<0||score>100) {//check ����
					do {
						System.out.println("��ȿ���� ���� �����Դϴ�");
						System.out.print("����(0~100)�� �Է��ϼ���: ");
						score = sc.nextInt();
					}while(score<0||score>100);
				}
				StudentDto newStudent = new StudentDto(name, mname, score);
				int result = dao.insertStudent(newStudent);
				System.out.println(result==StudentDao.SUCCESS? result+"�� �߰�":"�߰� ����");
				break;
			case "2"://selectMname
				System.out.print("��ȸ�� �а����� �Է��ϼ���: ");
				mname = sc.next().trim();
				student = dao.selectMname(mname);
				if(student.size()==0) {
					System.out.println("��ȸ ������ �л��� �����ϴ�");
				} else {
					System.out.println("���\t�̸�(�й�)\t\t�а�\t����");
					for(StudentDto s:student)
						System.out.println(s);
				}
				break;
			case "3"://selectAll
				student = dao.selectAll();
				if(student.isEmpty()) {
					System.out.println("��ȸ ������ �л��� �����ϴ�");
				} else {
					System.out.println("���\t�̸�(�й�)\t\t�а�\t����");
					for(StudentDto s:student)
						System.out.println(s);
				}
			break;	
			case "4"://selectExpel
				student = dao.selectExpel();
				if(student.isEmpty()) {
					System.out.println("��ȸ ������ �л��� �����ϴ�");
				} else {
					System.out.println("���\t�̸�(�й�)\t\t�а�\t����");
					for(StudentDto s:student)
						System.out.println(s);
				}
			break;
			}
		} while(fn.equals("1")||fn.equals("2")||fn.equals("3")||fn.equals("4"));
		System.out.println("Bye");
	}
}
