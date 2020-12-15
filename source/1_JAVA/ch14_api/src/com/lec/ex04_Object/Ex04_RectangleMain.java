package com.lec.ex04_Object;
//20-12-15_API(Object)		ⓒcherryuki(ji)

public class Ex04_RectangleMain {
	public static void main(String[] args) {
		Rectangle[] rect = {new Rectangle(), new Rectangle(3,5,"빨강"),
							new Rectangle(3,4,"노랑"), new Rectangle(3,4, "노랑")};
		for(Rectangle r:rect) {
			System.out.println(r);
		}
		System.out.println("r1과 r2가 같은가? "+rect[1].equals(rect[2]));
		System.out.println("r2와 r3이 같은가? "+rect[2].equals(rect[3]));
		System.out.println("r2: "+rect[2]);
//		for(int i=0 ; i<rect.length-1 ; i++) {
//			if(rect[i].equals(rect[i+1]) ){
//				System.out.println(i+"번째와 "+(i+1)+"번째는 같은 사각형");
//			}else {
//				System.out.println(i+"번째와 "+(i+1)+"번째는 다른 사각형");
//			}
//		}
	}
}
