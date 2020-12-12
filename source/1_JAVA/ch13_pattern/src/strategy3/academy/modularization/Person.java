package strategy3.academy.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy3.academy.component.IGet;
import strategy3.academy.component.IJob;

public class Person {
	private String id;
	private String name;
	private IJob job;
	private IGet get;
	public Person(String id, String name) {
		this.id=id;
		this.name=name;
	}
	public void job() {
		job.job();
	}
	public void get() {
		get.get();
	}
	public void print() {
		System.out.print("[ID]"+id+"\t[이름]"+name);
	}
	//setter
	public void setId(String id) {
		this.id = id;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setJob(IJob job) {
		this.job = job;
	}
	public void setGet(IGet get) {
		this.get = get;
	}
}
