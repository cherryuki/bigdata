package com.lec.ex06_account;
//20-12-21_Thread		ⓒcherryuki(ji)

public class Account {
	private int balance;
	public Account() {}
	public Account(int balance) {
		this.balance=balance;
	}
	
	public synchronized void deposit(int amount, String who) {
		System.out.println(who+"가 입금 시작 ~ ~ ~");
		System.out.println("입금전 잔액: "+balance+"원");
		balance += amount;
		System.out.println(amount+"원 입금  후 잔액: "+balance+"원");
		System.out.println(who+"가 입금 완료 ~ ~ ~");
	}
	public synchronized void withdraw(int amount, String who) {
		System.out.println(who+"가 출금 시작 = = =");
		System.out.println("출금전 잔액: "+balance+"원");
		if(balance<amount ) {
			System.out.println("잔액 부족으로 출금 불가");
		}else {
			balance-=amount;
			System.out.println(amount+"원 출금 후 잔액: "+balance+"원");
		}
		System.out.println(who+"가 출금 완료 = = =");
	}
	public int getBalance() {
		return balance;
	}
	public void setBalance(int balance) {
		this.balance = balance;
	}
}
