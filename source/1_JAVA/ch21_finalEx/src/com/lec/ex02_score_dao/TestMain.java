package com.lec.ex02_score_dao;
//21-01-07_JDBC_Dao&Dto		(c)cherryuki(ji)

import java.util.ArrayList;

public class TestMain {
	public static void main(String[] args) {
		System.out.println("-----1�� TEST-----");
		ScoreDto dto = new ScoreDto("��ȿ��", "����", 95, 70, 70);
		ScoreDao dao = ScoreDao.getInstance();
		int result = dao.insertScore(dto);
		System.out.println(result==ScoreDao.SUCCESS? "�߰� ����":"�߰� ����");
		System.out.println("-----2��TEST-----");
		ArrayList<ScoreDto> dtos = dao.selectJname("����");
		if(dtos.size()==0) {
			System.out.println("�ش� ������ ����� �����ϴ�");
		} else {
			for(ScoreDto d:dtos) 
				System.out.println(d);
		}
		System.out.println("-----3�� TEST-----");
		dtos = dao.selectAll();
		if(dtos.isEmpty()) {
			System.out.println("��ȸ�� �ο��� �����ϴ�");
		} else {
			for(ScoreDto d:dtos)
				System.out.println(d);
		}
	}
}
