package com.lec.ex08_salary;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		Employee[] employee = {new SalaryEmployee("홍길동", 24000000), new SalaryEmployee("공유", 36000000), new SalaryEmployee("박보검", 30000000),
								new HourlyEmployee("알바1", 200, 8000), new HourlyEmployee("알바2", 100, 9000)};
		for(Employee e:employee) {//확장 for문 이용하기!
			System.out.println("---급여 명세서---");
			System.out.println("*성함: "+e.getName());
			System.out.println("*급여: "+e.computePay()+"원");
			if(e.computeIncentive()!=0) {
				System.out.println("*상여: "+e.computeIncentive()+"원");
			}
//			int incentive = e.computeIncentive();
//			if(incentive!=0) {
//				System.out.println("*상여: "+incentive+"원");
//			}
			System.out.println(" 수고하셨습니다");
		}
	}
}
