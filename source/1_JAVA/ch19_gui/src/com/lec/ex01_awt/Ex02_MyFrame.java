package com.lec.ex01_awt;
//20-12-21_GUI(awt)		ⓒcherryuki(ji)

import java.awt.Button;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.Label;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class Ex02_MyFrame extends Frame implements ActionListener {
	private Label lbl1; //추가할 컴포넌트 변수들 선언
	private Button btnExit;
	public Ex02_MyFrame() {
		setLayout(new FlowLayout()); //add순서대로 차곡차곡 왼쪽부터 쌓임
		lbl1 = new Label("Good day");
		lbl1.setPreferredSize(new Dimension(150,200));//컴포넌트 사이즈
		btnExit = new Button("Exit");
		btnExit.setPreferredSize(new Dimension(200,200));//컴포넌트 사이즈
		add(lbl1);
		add(btnExit);
		setVisible(true);
		setSize(new Dimension(500,300));
		setLocation(100,100);
		//btnExit 클릭 이벤트 걸기
		//1) 액션 리스너를 임플리먼트 2) addActionListener(this) 3) actionPerformed 오버라이드
		btnExit.addActionListener(this);//btnExit 클릭 이벤트 발생되면 this.actionPerformed 호출
		
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				setVisible(false);
				dispose();
				System.exit(0);
			}//windowClosing
		});//addWindowListener
	}//MyFrame
	
	public Ex02_MyFrame(String title) {
		this();
		setTitle(title);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {//이벤트 처리 메소드
		if(e.getSource()==btnExit) {
			setVisible(false);
			dispose();
			System.exit(0);
		}
	}
	
	public static void main(String[] args) {
		new Ex02_MyFrame("두번째 예제");
	}

}
