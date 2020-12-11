package strategy1.step4.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy1.step4.component.FlyHigh;
import strategy1.step4.component.FlyYes;
//*(All)로 해두었다가 Ctrl+Shift+o 눌러서 필요한 것만 나오게함

public class TestMain {
	public static void main(String[] args) {
		SuperRobot superRobot = new SuperRobot();
		StandardRobot standardRobot = new StandardRobot();
		LowRobot lowRobot = new LowRobot();
		Robot[] robots = {superRobot, standardRobot, lowRobot};
		for(Robot robot:robots) {
			robot.shape();
			robot.actionWalk();
			robot.actionRun();
			robot.actionFly();
			robot.actionMissile();
			robot.actionKnife();
		}
		//요구사항 1: LowRobot을 날 수 있는 로봇으로 업그레이드
		//요구사항 2: SuperRobot을 고공 비행하는 로봇으로 업그레이드
		lowRobot.setFly(new FlyYes());
		superRobot.setFly(new FlyHigh());
		System.out.println();//개행
		System.out.println("<업그레이드 후>");
		for(Robot robot:robots) {
			robot.shape();
			robot.actionWalk();
			robot.actionRun();
			robot.actionFly();
			robot.actionMissile();
			robot.actionKnife();
		}
	}
}
