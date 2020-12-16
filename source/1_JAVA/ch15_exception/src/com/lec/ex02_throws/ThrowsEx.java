package com.lec.ex02_throws;
//20-12-16_Exception		ⓒcherryuki(ji)
public class ThrowsEx {
	public ThrowsEx() throws Exception{
		actionC();
	}
	private void actionC() throws Exception{
		System.out.println("actionC 전반부");
		actionB();
		System.out.println("actionC 후반부");
	}
	private void actionB() throws Exception{
		System.out.println("actionB 전반부");
		actionA();
		System.out.println("actionB 후반부");
	}
	private void actionA() throws ArrayIndexOutOfBoundsException{//throws Exception도 가능
		System.out.println("actionA 전반부");
		int[] arr = {0,1,2,3};
		System.out.println(arr[4]); //Exception
		System.out.println("actionA 후반부");
	}		
}
