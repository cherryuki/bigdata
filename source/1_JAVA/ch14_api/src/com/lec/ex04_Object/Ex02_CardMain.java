package com.lec.ex04_Object;
//20-12-15_API(Object)		ⓒcherryuki(ji)

public class Ex02_CardMain {
	public static void main(String[] args) {
		Card[] cards = {new Card('♥',3),
						new Card('◆', 5),
						new Card('♣', 7)};
		Card yours = new Card('♣', 7);
		System.out.println("당신 카드: "+yours);
		for(Card card:cards) {
			System.out.print(card);
			if(yours.equals(card)) {
				System.out.println(" -당신 카드와 일치합니다");
			}else {
				System.out.println(" -당신 카드와 일치하지 않습니다");
			}
		}
	}
}
