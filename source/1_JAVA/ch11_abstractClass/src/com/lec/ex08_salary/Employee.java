package com.lec.ex08_salary;
//20-12-08_abstract class	ⓒcherryuki(ji)

//Employee: name, computeIncentive(), computePay()
public abstract class Employee {
	private final String name;
	public Employee(String name) {
		this.name=name;
	}
	public abstract int computePay();
	public final int computeIncentive() {
		int pay = computePay();
		if(pay>2000000) {
			return (int)(pay*0.1);
		}
		return 0;
	}
	public String getName() {
		return name;
	}
}
