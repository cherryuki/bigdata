package com.lec.ex02_score_dao;
//21-01-07_JDBC		ⓒcherryuki(ji)

import java.util.ArrayList;

public class TestMain {
	public static void main(String[] args) {
		System.out.println("-----1번 TEST-----");
		ScoreDto dto = new ScoreDto("장동건", "배우", 95, 70, 70);
		ScoreDao dao = ScoreDao.getInstance();
		int result = dao.insertScore(dto);
		System.out.println(result==ScoreDao.SUCCESS? "추가 성공":"추가 실패");
		System.out.println("-----2번 TEST-----");
		ArrayList<ScoreDto> dtos = dao.selectJname("배우");
		if(dtos.size()==0) {
			System.out.println("해당 직업인 사람이 없습니다");
		} else {
			for(ScoreDto d:dtos) 
				System.out.println(d);
		}
		System.out.println("-----3번 TEST-----");
		dtos = dao.selectAll();
		if(dtos.isEmpty()) {
			System.out.println("조회할 수 없습니다");
		} else {
			for(ScoreDto d:dtos)
				System.out.println(d);
		}
	}
}
