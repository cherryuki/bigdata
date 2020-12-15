package com.lec.ex04_Object;
//20-12-15_API(Object)		ⓒcherryuki(ji)

public class Goods {
	private String goodsCode; //품번
	private String goodsName; //품명
	private int goodsPrice; //상품 가격
	private int stockNum; //재고 수량
	public Goods(String goodsCode, String goodsName, int goodsPrice, int stockNum) {
		this.goodsCode=goodsCode;
		this.goodsName=goodsName;
		this.goodsPrice=goodsPrice;
		this.stockNum=stockNum;
	}
	@Override
	public String toString() {
		return goodsName+"("+goodsCode+") "+goodsPrice+"원, 재고 수량: "+stockNum;
	}
}
