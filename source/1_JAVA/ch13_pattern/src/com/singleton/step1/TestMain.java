package com.singleton.step1;
//20-12-10_singletonClass	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		SingletonClass obj1 = SingletonClass.getInstance();
		SingletonClass obj2 = SingletonClass.getInstance();
		System.out.println("초기화 된 i값: "+obj1.getI());
		obj1.setI(999);
		System.out.println("obj1의 i값을 변경한 후 obj2의 i값: "+obj2.getI());
		System.out.println("--------------------------------");
		AClass aObj = AClass.getInstance();
		aObj.setIntVar(555);
		AClass bObj = AClass.getInstance();
		System.out.println(bObj.getIntVar());
	}
}
