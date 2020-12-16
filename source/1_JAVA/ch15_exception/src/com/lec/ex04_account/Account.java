package com.lec.ex04_account;
//20-12-16_Exception		ⓒcherryuki(ji)
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
	public void deposit(int amount) {
		/* 예금: 계좌정보 출력->예금->예금 후 계좌정보 출력
		 * Account a = new Account("110-1", "공")
		 * a.deposit(1000) -> 여기서 this==a
		 */
		System.out.println("예금 전: "+this);
		balance += amount;
		System.out.println(amount+"원\n예금 후: "+this);
	}
	//출금: 계좌정보 출력->출금->출금 후 계좌정보 출력
	public void withdraw(int amount) throws Exception{
		if(balance<amount) {//잔액 부족 시 강제 예외 발생
			throw new Exception(amount+"원 출금하기에는 잔액("+balance+"원)이 부족합니다");
		}
		System.out.println("출금 전: "+this);
		balance -= amount;
		System.out.println(amount+"원\n출금 후: "+this);
	}
	@Override
	public String toString() {
		String result = "계좌번호: "+accountNo+"\t예금주: "+ownerName;
		result += "\t잔액: "+balance+"원";
		return result;
	}
}
