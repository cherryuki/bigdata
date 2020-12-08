package com.lec.ex04_area;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		//Shape shape = new Shape(); //추상 클래스여서 객체 생성 불가
		Shape[] shape = {new Circle(5), new Rectangle(10,5), new Triangle(5,10)}; //배열
		for(Shape s:shape) {
			s.draw();
			s.computeArea();
		}
		System.out.println();
		for(int i=0; i<shape.length; i++) {
			shape[i].draw();
			shape[i].computeArea();
		}
//		for(int i=0; i<=shape.length; i++) {//예외 발생(실행단계 에러); i<shape.length로 수정 or 예외 처리 필요
//			shape[i].draw();
//			shape[i].computeArea();
//		}
	}
}
