package com.lec.ex08_robot;
//20-12-09_interface	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		DanceRobot aRobot = new DanceRobot();
		DrawRobot bRobot = new DrawRobot();
		SingRobot cRobot = new SingRobot();
		RobotOrder order = new RobotOrder();
		order.action(aRobot);
		order.action(bRobot);
		System.out.println();
		IRobot[] robot = {aRobot, bRobot, cRobot};
		for(IRobot r:robot) {
			order.action(r);
		}
	}
}
