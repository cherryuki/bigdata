package com.lec.ex04_Object;
//20-12-15_API(Object)		ⓒcherryuki(ji)

public class Card {
	private char kind; //카드 모양
	private int num; //카드 번호
	public Card(char kind, int num) {
		this.kind=kind;
		this.num=num;
	}
	@Override
	public String toString() {
		return "카드: "+kind+" "+num;
	}
	@Override
	public boolean equals(Object obj) {
		if(obj!=null && obj instanceof Card) {
			return kind==((Card)obj).kind && num==((Card)obj).num;
		}
		return false;
	}
}
