package strategy3.academy.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy3.academy.component.GetSalary;
import strategy3.academy.component.JobMng;

public class Staff extends Person {
	private String part;
	public Staff(String id, String name, String part) {
		super(id, name);
		this.part=part;
		setJob(new JobMng());
		setGet(new GetSalary());
	}
	@Override
	public void print() {
		super.print();
		System.out.println("\t[부서]"+part);
	}
}
