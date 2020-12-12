package strategy3.academy.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy3.academy.component.GetSalary;
import strategy3.academy.component.JobLec;

public class Lecturer extends Person {
	private String subject;
	public Lecturer(String id, String name, String subject) {
		super(id, name);
		this.subject=subject;
		setJob(new JobLec());
		setGet(new GetSalary());
	}
	@Override
	public void print() {
		super.print();
		System.out.println("\t[과목]"+subject);
	}
}
