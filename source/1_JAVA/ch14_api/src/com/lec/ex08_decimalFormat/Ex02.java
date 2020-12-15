package com.lec.ex08_decimalFormat;
//20-12-15_API(DecimalFormat)		ⓒcherryuki(ji)
import java.text.DecimalFormat;

public class Ex02 {
	public static void main(String[] args) {
		String[] pattern = {"00000000.00000", "########.##", "#,###.00000",
							"#.#%", "#.####E00"};
		double num = 1234567.8889;
		for(String p:pattern) {
			DecimalFormat df = new DecimalFormat(p);
			System.out.println(df.format(num));
		}
	}
}
