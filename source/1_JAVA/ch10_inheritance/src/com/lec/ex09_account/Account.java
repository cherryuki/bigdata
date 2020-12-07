package com.lec.ex09_account;
//Account a1 = new Account(“111-1111”,”홍길동”,10);
//Account a1 = new Account(“111-1111”,”홍길동”);
public class Account {
	private String accountNo;
	private String ownerName;
	private int balance;
	public Account() {}
	public Account(String accountNo, String ownerName, int balance) {
		this.accountNo=accountNo;
		this.ownerName=ownerName;
		this.balance=balance;
	}
	public Account(String accountNo, String ownerName) {
		System.out.println(accountNo+", "+ownerName);
		this.accountNo=accountNo;
		this.ownerName=ownerName;
	}
	public void deposit(int amount) {
		balance += amount;
	}
	public void withdraw(int amount) {
		if(balance>=amount) {
			balance -= amount;
		}else {
			System.out.println("잔액이 부족합니다");
		}
	}
	public void printAccount() {
		System.out.println("계좌번호: "+accountNo+", "+ownerName+"님 잔액은 "+balance+"원");
	}
	public String getAccountNo() {
		return accountNo;
	}
	public void setAccountNo(String accountNo) {
		this.accountNo = accountNo;
	}
	public String getOwnerName() {
		return ownerName;
	}
	public void setOwnerName(String ownerName) {
		this.ownerName = ownerName;
	}
	public int getBalance() {
		return balance;
	}
	public void setBalance(int balance) {
		this.balance = balance;
	}
}
