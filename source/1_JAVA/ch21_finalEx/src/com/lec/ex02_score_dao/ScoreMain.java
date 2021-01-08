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
			System.out.println("1:�엯�젰 | 2: 吏곸뾽蹂� 議고쉶 | 3: �쟾泥� 議고쉶 | 洹� �쇅: 醫낅즺");
			fn=sc.next();
			switch(fn) {
			case "1": //�씠由�, 吏곸뾽紐�, 援��쁺�닔 �젏�닔 �엯�젰 諛쏆븘�꽌 dao.insertScore() �샇異�
				System.out.print("異붽��븷 �씠由꾩쓣 �엯�젰�븯�꽭�슂: ");
				String name = sc.next();
				System.out.print(name+"�쓽 吏곸뾽: ");
				String jname = sc.next();
				System.out.print("援��뼱 �젏�닔: ");
				int kor = sc.nextInt();
				System.out.print("�쁺�뼱 �젏�닔: ");
				int eng = sc.nextInt();
				System.out.print("�닔�븰 �젏�닔: ");
				int mat = sc.nextInt();
				ScoreDto newPerson = new ScoreDto(name, jname, kor, eng, mat);
				int result = dao.insertScore(newPerson);
				System.out.println(result==ScoreDao.SUCCESS? result+"�뻾 異붽� �꽦怨�":"�엯�젰 �떎�뙣");
				break;
			case "2": //吏곸뾽蹂� 議고쉶 dao.selectJname() �샇異쒗븯�뿬 寃곌낵 異쒕젰
				System.out.print("議고쉶�븷 吏곸뾽紐�(諛곗슦|媛��닔|湲고�)瑜� �엯�젰�븯�꽭�슂: ");
				jname = sc.next();
				person = dao.selectJname(jname);
				if(person.size()==0) {
					System.out.println("議고쉶 媛��뒫�븳 �씤�썝�씠 �뾾�뒿�땲�떎");
				} else {
					System.out.println("�벑�닔\t�씠由�\t\t吏곸뾽\t援��뼱\t�쁺�뼱\t�닔�븰\t珥앹젏");
					for(ScoreDto p:person) 
						System.out.println(p);
				}
				break;
			case "3": //�쟾泥� 議고쉶 dao.selectAll() �샇異쒗븯�뿬 寃곌낵 異쒕젰
				person = dao.selectAll();
				if(person.isEmpty()) {
					System.out.println("議고쉶 媛��뒫�븳 �씤�썝�씠 �뾾�뒿�땲�떎");
				} else {
					System.out.println("�벑�닔\t�씠由�\t\t吏곸뾽\t援��뼱\t�쁺�뼱\t�닔�븰\t珥앹젏");
					for(ScoreDto p:person) 
						System.out.println(p);
				}
				break;
			}//switch
		} while(fn.equals("1")||fn.equals("2")||fn.equals("3"));
		System.out.println("醫낅즺�빀�땲�떎");
	}//main
}//class
