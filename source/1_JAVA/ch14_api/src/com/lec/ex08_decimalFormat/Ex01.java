package com.lec.ex08_decimalFormat;
//20-12-15_API(DecimalFormat)		ⓒcherryuki(ji)
import java.text.DecimalFormat;

/* 숫자 자리에 #(있으면 출력, 없으면 출력 안함), 0(반드시 출력)
 * , %, E(지수형)
 */
public class Ex01 {
	public static void main(String[] args) {
		double num = 1234567.8889;
		DecimalFormat df1 = new DecimalFormat("00000000.00000");
		System.out.println(df1.format(num));
		DecimalFormat df2 = new DecimalFormat("########.##");
		System.out.println(df2.format(num));
		DecimalFormat df3 = new DecimalFormat("#,###.00000");
		System.out.println(df3.format(num));
		DecimalFormat df4 = new DecimalFormat("#.#%");
		System.out.println(df4.format(num));
		DecimalFormat df5 = new DecimalFormat("#.####E00");//En=10의 n승
		System.out.println(df5.format(num));
	}
}
