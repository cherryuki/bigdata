package strategy3.academy.component;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class GetStudentPay implements IGet {

	@Override
	public void get() {
		System.out.println("훈련 수당을 받습니다");
	}

}
