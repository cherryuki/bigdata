package com.lec.ex3_account;
/* 은행계좌 클래스
 *  데이터: 계좌번호 (accountNo:String)
 *        예금주   (ownerName:String) 
 *        잔액      (balance:int or double - 22억 이상시)
 *  메소드: 예금 (void deposit(int money))new Account("110-352","홍",10)
 *        인출 (void withdraw(int money))new Account("110-352","홍")
 */
public class Account {
	private String accountNo;
	private String ownerName;
	private int balance;
	public Account() {}
	public Account(String accountNo, String ownerName) {
		this.accountNo=accountNo;
		this.ownerName=ownerName;
	}
	public Account(String accountNo, String ownerName, int balance) {
		this.accountNo=accountNo;
		this.ownerName=ownerName;
		this.balance=balance;
	}
	public void deposit(int money) {//예금은 조건 없이 가능
		balance += money;
	}
	public void withdraw(int money) {//잔액 부족시 인출 불가
		if(balance>=money) {
			balance -= money;
		}else {
			System.out.println("잔액이 부족합니다");
		}
	}
	public void info() {
		System.out.println("계좌번호: "+accountNo+", "+ownerName+"님 잔액은 "+balance+"원");
	}
	//accountNo, ownerNamer, balance setter&getter
	public void setAccountNo(String accountNo) {
		this.accountNo=accountNo;
	}
	public String getAccountNo() {
		return accountNo;
	}
	public void setOwnerName(String ownerName) {
		this.ownerName=ownerName;
	}
	public String setOwnerName() {
		return ownerName;
	}
	public void getBalnce(int balance) {
		this.balance=balance;
	}
	public int setBalance() {
		return balance;
	}
}
