package com.lec.ex09_account;
//CkeckingAccount ca1 = new CkeckingAccount(“111-1111”,”김길동”,[1000,] ”1234-1234-1234-1234”);
public class CheckingAccount extends Account {
	private String cardNo;
	public CheckingAccount() {}
	public CheckingAccount(String accountNo, String ownerName, int balance, String cardNo) {
		super(accountNo, ownerName, balance);
		this.cardNo=cardNo;
	}
	public CheckingAccount(String accountNo, String ownerName, String cardNo) {
		super(accountNo, ownerName);
		this.cardNo=cardNo;
	}
	public void pay(String cardNo, int amount) {
		if(this.cardNo.equals(cardNo)) {
			if(getBalance()>=amount) {
				setBalance(getBalance()-amount);
				System.out.println(amount+"원 사용되어 잔액: "+getBalance()+"원");
			}else {
				System.out.println("잔액이 부족합니다");
			}
		}else {
			System.out.println("(체크)카드 번호가 일치하지 않습니다");
		}
	}
	public String getCardNo() {
		return cardNo;
	}
	public void setCardNo(String cardNo) {
		this.cardNo = cardNo;
	}
}
