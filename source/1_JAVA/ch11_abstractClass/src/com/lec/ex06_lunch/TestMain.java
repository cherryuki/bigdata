package com.lec.ex06_lunch;
//20-12-08_abstract class	ⓒcherryuki(ji)
import com.lec.cons.PriceTable;

public class TestMain {
	public static void main(String[] args) {
		Child1 child1 = new Child1(PriceTable.RICE, PriceTable.BULGOGI, PriceTable.SOUP,
						PriceTable.BANANA, PriceTable.MILK, PriceTable.ALMOND);
		Child2 child2 = new Child2(PriceTable.RICE, PriceTable.BULGOGI, PriceTable.SOUP,
						PriceTable.BANANA, PriceTable.MILK, PriceTable.ALMOND);
		System.out.println("child1형 식대: "+child1.calculate());
		System.out.println("child2형 식대: "+child2.calculate());
	}
}
