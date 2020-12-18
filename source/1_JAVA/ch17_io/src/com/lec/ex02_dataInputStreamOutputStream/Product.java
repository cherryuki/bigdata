package com.lec.ex02_dataInputStreamOutputStream;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

public class Product {
	private String name;
	private int price;
	private int ps;
	public Product() {}
	public Product(String name, int price, int ps) {
		this.name=name;
		this.price=price;
		this.ps=ps;
	}
	@Override
	public String toString() {
		return name.toLowerCase()+"\t"+price+"원\t"+ps+"개";
	}
}
