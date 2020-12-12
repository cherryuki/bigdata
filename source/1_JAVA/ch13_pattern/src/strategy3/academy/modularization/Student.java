package strategy3.academy.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy3.academy.component.GetStudentPay;
import strategy3.academy.component.JobStudy;

public class Student extends Person {
	private String ban;
	public Student(String id, String name, String ban) {
		super(id, name);
		setJob(new JobStudy());
		setGet(new GetStudentPay());
		this.ban=ban;
	}
	@Override
	public void print() {
		super.print();
		System.out.println("\t[반]"+ban);
	}
}
