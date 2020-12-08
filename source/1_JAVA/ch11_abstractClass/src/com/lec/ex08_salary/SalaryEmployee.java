package com.lec.ex08_salary;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class SalaryEmployee extends Employee {
	private int annualSalary;
	public SalaryEmployee(String name, int annualSalary) {
		super(name);
		this.annualSalary=annualSalary;
	}
	@Override
	public int computePay() {
		return (int)(annualSalary/14);
	}
	public int getAnnualSalary() {
		return annualSalary;
	}
	public void setAnnualSalary(int annualSalary) {
		this.annualSalary = annualSalary;
	}
}
