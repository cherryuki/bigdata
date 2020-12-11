package strategy1.step3.abst;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		SuperRobot 		superRobot	  = new SuperRobot();
		StandardRobot 	standardRobot = new StandardRobot();
		LowRobot 		lowRobot 	  = new LowRobot();
		Robot[] robots = {superRobot, standardRobot, lowRobot}; //동일 자료형만 배열로 묶을 수 있음
		for(Robot robot:robots) {
			robot.shape();
			robot.actionWalk();
			robot.actionRun();
			robot.actionMissile();
			robot.actionKnife();
		}
	}
}
