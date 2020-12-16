package com.lec.ex04_account;
//20-12-16_Exception		ⓒcherryuki(ji)
public class AccountMain {
	public static void main(String[] args) {
		Account obj1 = new Account("110-11", "공유");
		Account obj2 = new Account("110-20", "박보검", 20000);
		obj1.deposit(10000);
		obj2.deposit(10000);
		try {
			obj1.withdraw(15000);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
}
