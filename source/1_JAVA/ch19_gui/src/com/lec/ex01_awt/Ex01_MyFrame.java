package com.lec.ex01_awt;
//20-12-21_GUI(awt)		ⓒcherryuki(ji)

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Dimension;
import java.awt.Frame;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Ex01_MyFrame extends Frame {
	private Button btn, btn1;
	public Ex01_MyFrame() {
		this("");
	}
	
	public Ex01_MyFrame(String title) {//버튼 2개 추가된 프레임 생성
		super(title);
		btn=new Button("Button");
		btn1=new Button("Button1");
		add(btn, BorderLayout.NORTH);
		add(btn1, BorderLayout.CENTER);
		setVisible(true);
		setSize(new Dimension(300,200));
		setLocation(200,100);
		addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent e) {
				setVisible(false);
				dispose();
				System.exit(0);
			};
		});
	}//MyFrame
	
	public static void main(String[] args) {
		new Ex01_MyFrame("첫번째 GUI 예제");
	}
}
