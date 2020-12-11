package strategy1.step1.object;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		SuperRobot 		superRobot	  = new SuperRobot();
		StandardRobot 	standardRobot = new StandardRobot();
		LowRobot 		lowRobot 	  = new LowRobot();
		superRobot.shape();
		superRobot.actionWalk();
		superRobot.actionRun();
		superRobot.actionFly();
		superRobot.actionMissile();
		superRobot.actionKnife();
		standardRobot.shape();
		standardRobot.actionWalk();
		standardRobot.actionRun();
		standardRobot.actionFly();
		standardRobot.actionMissile();
		standardRobot.actionKnife();
		lowRobot.shape();
		lowRobot.actionWalk();
		lowRobot.actionRun();
		lowRobot.actionFly();
		lowRobot.actionMissile();
		lowRobot.actionKnife();
	}
}
