package strategy2.car.component;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class EngineLow implements IEngine {

	@Override
	public void engine() {
		System.out.println("저급 엔진");
	}

}
