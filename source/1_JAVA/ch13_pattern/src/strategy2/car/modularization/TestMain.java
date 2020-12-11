package strategy2.car.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy2.car.component.Hybrid;
import strategy2.car.component.Km20;

public class TestMain {
	public static void main(String[] args) {
		Car genesis = new Genesis();
		Car sonata 	= new Sonata();
		Car accent 	= new Accent();
		Car[] cars = {genesis, sonata, accent};
		for(Car car:cars) {
			car.shape();
			car.drive();
			car.isEngine();
			car.isKm();
			car.isFuel();
		}//for
		//요청사항: 소나타를 하이브리드 차량, 연비를 20km/l로 업그레이드
		System.out.println();
		System.out.println("<업그레이드 후>");
		sonata.setFuel(new Hybrid());
		sonata.setKm(new Km20());
		for(Car car:cars) {
			car.shape();
			car.drive();
			car.isEngine();
			car.isKm();
			car.isFuel();
		}//for
	}//main
}//class
