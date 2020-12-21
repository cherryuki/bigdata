package com.lec.ex06_account;
//20-12-21_Thread		ⓒcherryuki(ji)

public class ATM_cardTestMain {
	public static void main(String[] args) {
		Account account = new Account(2000);
		Runnable target = new ATM_card(account);
		Thread mom = new Thread(target, "mom");
		Thread dad = new Thread(target, "dad");
		mom.start();
		dad.start();
	}
}
