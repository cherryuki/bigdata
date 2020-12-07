package com.lec.ex09_account;
//CreditLineAccount cla1 = new Account(“111-1111”,”박길동”,[1000,]”1234-1234-1234-1234”, 2200000000L);
public class CreditLineAccount extends CheckingAccount {
	private long creditLine;
	public CreditLineAccount() {}
	public CreditLineAccount(String accountNo, String ownerName, String cardNo, long creditLine) {
		super(accountNo, ownerName, cardNo);
		this.creditLine=creditLine;
	}
	public CreditLineAccount(String accountNo, String ownerName, int balance, String cardNo, long creditLine) {
		super(accountNo, ownerName, balance, cardNo);
		this.creditLine=creditLine;
	}
	public void pay(String cardNo, int amount) {
		if(getCardNo().equals(cardNo)) {
			if(creditLine>=amount) {
				creditLine -= amount;
				System.out.println(getOwnerName()+"님, "+amount+"원 출금(잔여 한도액: "+creditLine);
			}else {
				System.out.println(getOwnerName()+"님, 한도 초과입니다");
			}
		}else {
			System.out.println("(신용)카드번호가 일치하지 않습니다");
		}
	}
	public long getCreditLine() {
		return creditLine;
	}
	public void setCreditLine(long creditLine) {
		this.creditLine = creditLine;
	}
	
}
