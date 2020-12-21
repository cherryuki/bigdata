package com.lec.ex06_account;
//20-12-21_Thread		ⓒcherryuki(ji)

public class ATM_card implements Runnable{
	private boolean flag = false;
	private Account obj;
	public ATM_card(Account obj) {
		this.obj=obj;
	}

	@Override
	public void run() {
		for(int i=0; i<10; i++) {
			if(flag) {
				obj.withdraw(1000, Thread.currentThread().getName());
				flag=false;
			} else {
				obj.deposit(1000, Thread.currentThread().getName());
				flag=true;
			}
		}//for
		
	}

}
