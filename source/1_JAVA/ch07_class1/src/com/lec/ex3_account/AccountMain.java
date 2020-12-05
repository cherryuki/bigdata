package com.lec.ex3_account;

public class AccountMain {
	public static void main(String[] args) {
		Account hong = new Account("110-1", "홍길동", 10000);
		Account kong = new Account("220-1", "공유");
		Account park = new Account();
		park.setAccountNo("110-2");
		park.setOwnerName("박보검");
		hong.deposit(10000);
		hong.info();
		kong.withdraw(10000);
		kong.info();
		park.deposit(1000);
		park.withdraw(10000);
		park.info();
	}
}
