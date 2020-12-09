package com.lec.ex08_robot;
//20-12-09_interface	ⓒcherryuki(ji)
public class RobotOrder {
	public void action(IRobot robot) {
		if(robot instanceof DanceRobot) {
			((DanceRobot)robot).dance();
		}else if(robot instanceof DrawRobot) {
			((DrawRobot)robot).draw();
		}else if(robot instanceof SingRobot) {
			//((SingRobot)robot).sing(); //아래와 동일
			SingRobot sRobot = (SingRobot)robot; 
			sRobot.sing();
		}
	}
}
