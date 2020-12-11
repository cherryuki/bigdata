package strategy2.car.component;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class Hybrid implements IFuel {

	@Override
	public void fuel() {
		System.out.println("하이브리드 차량");
	}

}
