package com.lec.ex07_timer;
//20-12-15_API(timer)		ⓒcherryuki(ji)
import java.util.Timer;
import java.util.TimerTask;

public class TimerMain {
	public static void main(String[] args) throws InterruptedException {
		System.out.println("시작");
		Timer timer = new Timer(true); //true:프로그램 종료되면 timer도 종료
		TimerTask task1 = new TimerTaskEx01(); //작업 정의 객체
		TimerTaskEx02 task2 = new TimerTaskEx02(); //작업 정의 객체
		timer.schedule(task1, 2000); //2000밀리세컨(2초) 후에 한 번 실행
		timer.schedule(task2, 500, 1000);//0.5초 후부터 1초마다 실행
		Thread.sleep(10000); //10초 대기
		System.out.println("끝");
	}
}
