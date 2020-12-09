package com.lec.ex06_toy;
//20-12-09_interface	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		IToy[] toy = {new PoohToy(), new MazingerToy(), new AirplaneToy()};
		for(IToy t:toy) {
			//t객체의 클래스 이름 출력
			System.out.println(t.getClass().getName());
			//t.toString()호출
			System.out.println(t);
			System.out.println("==============================");
		}
	}
}
