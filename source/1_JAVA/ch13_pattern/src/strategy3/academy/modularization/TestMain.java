package strategy3.academy.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		Student st1 = new Student("10101", "강학생", "python반");
		Student st2 = new Student("20020", "나학생", "java반");
		Lecturer le1 = new Lecturer("A0100", "박강사", "db");
		Lecturer le2 = new Lecturer("A1000", "홍강의", "hadoop");
		Staff s1 = new Staff("S0321", "신직원", "취업지원");
		Person[] person = {st1, st2, le1, le2, s1};
		System.out.println("<9:00-18:00>");
		for(Person p:person) 
			p.job();
		System.out.println("<월말에 지급 예정>");
		for(Person p:person)
			p.get();
		System.out.println("<정보 출력>");
		for(Person p:person)	
			p.print();
	}
}
