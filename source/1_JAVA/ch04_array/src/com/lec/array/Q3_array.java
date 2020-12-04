package com.lec.array;
//거스름돈 2680원을 500, 100, 50, 10원짜리 동전으로 줄 때 몇개씩 주는지 출력
public class Q3_array {
	public static void main(String[] args) {
		int[] coinUnit = {500, 100, 50, 10};
		int money = 2680;
		System.out.println(money+"원은");
		for(int coin : coinUnit) {
					System.out.print(coin+"원짜리 "+money/coin+"개  ");
					money%=coin;
		}
	}
}
