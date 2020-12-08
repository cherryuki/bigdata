package com.lec.ex09_account;
//20-12-07_inheritance ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		Account a1 = new Account("111-1111", "홍길동");
		CheckingAccount a2 = new CheckingAccount("222-2222", "성춘향", 2000, "1234-1234-1234-1323");
		CheckingAccount a3 = new CreditLineAccount("222-3333", "이몽룡", 2000, "1234-1234-1234-9999", 10000);
		a1.deposit(3000);
		a2.withdraw(200);
		a3.deposit(3000);
		a1.printAccount();
		a2.pay("1234-1234-1234-1323", 200);
		a2.pay("1234-1234-1234-0000", 200);
		a3.pay("1234-1234-1234-9999", 5000);
		a3.pay("1234-1234-1234-9999", 7000);
		a3.pay("1234-1234-1234-0000", 7000);
		}
}
