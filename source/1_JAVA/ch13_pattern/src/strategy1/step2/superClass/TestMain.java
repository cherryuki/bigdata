package strategy1.step2.superClass;
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
			//robot.actionFly(); //불가능(Robot안에는 Fly, Missile, Knife가 들어있지 않으므로)
			if(robot instanceof SuperRobot) {//명시적 형전환 전 확인 작업
				SuperRobot tempRobot = (SuperRobot)robot;
				tempRobot.actionFly();
				tempRobot.actionMissile();
				tempRobot.actionKnife();
			}else if(robot instanceof StandardRobot) {
				StandardRobot tempRobot = (StandardRobot)robot;
				tempRobot.actionFly();
				tempRobot.actionMissile();
				tempRobot.actionKnife();
			}else if(robot instanceof LowRobot) {
				LowRobot tempRobot = (LowRobot)robot;
				tempRobot.actionFly();
				tempRobot.actionMissile();
				tempRobot.actionKnife();
			}
		}
	}
}
