package com.lec.ex02_score_dao;
//21-01-08_JDBC_Dao&Dto		(c)cherryuki(ji)

import java.util.ArrayList;
import java.util.Scanner;

public class ScoreMain {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ScoreDao dao = ScoreDao.getInstance();
		String fn;
		ArrayList<ScoreDto> person;
		do {
			System.out.println(" 1:입력 | 2: 직업별 조회 | 3: 전체 조회 | 그 외: 종료 ");
			fn=sc.next();
			switch(fn) {
			case "1"://이름, 직업명, 국영수 점수 입력받아 dao.insertPerson() 호출
				System.out.print("추가할 이름을 입력하세요: ");
				String name = sc.next();
				System.out.print("직업명: ");
				String jname = sc.next();
				System.out.print("국어 점수: ");
				int kor = sc.nextInt();
				System.out.print("영어 점수: ");
				int eng = sc.nextInt();
				System.out.print("수학 점수: ");
				int mat = sc.nextInt();
				ScoreDto newPerson = new ScoreDto(name, jname, kor, eng, mat);
				int result = dao.insertScore(newPerson); //입력 끝
				System.out.println(result==ScoreDao.SUCCESS? result+"행 추가":"입력 오류");
				break;
			case "2"://직업명 입력받아 dao.selectJname() 호출 + 결과 출력
				System.out.print("조회할 직업명(배우, 가수, 기타)을 입력하세요: ");
				jname = sc.next();
				person = dao.selectJname(jname);
				if(person.size()==0) {
					System.out.println("해당 직업인 사람이 없습니다");
				}else {
					System.out.println("등수\t이름\t\t직업\t국어\t영어\t수학\t총점");
					for(ScoreDto p:person)
						System.out.println(p);
				}
				break;
			case "3"://dao.selectAll()호출 + 전체 리스트 출력
				person = dao.selectAll();
				if(person.isEmpty()) {
					System.out.println("등록된 사람이 없습니다");
				} else {
					System.out.println("등수\t이름\t\t직업\t국어\t영어\t수학\t총점");
					for(ScoreDto p:person)
						System.out.println(p);
				}
				break;
			}
		} while(fn.equals("1")||fn.equals("2")||fn.equals("3"));
		System.out.println("종료");
	}//main
}//class
