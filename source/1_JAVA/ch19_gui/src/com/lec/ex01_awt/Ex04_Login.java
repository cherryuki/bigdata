package com.lec.ex01_awt;
//20-12-21_GUI(awt)		ⓒcherryuki(ji)

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Dimension;
import java.awt.Frame;
import java.awt.GridLayout;
import java.awt.Label;
import java.awt.Panel;
import java.awt.TextField;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Ex04_Login extends Frame{
	private Panel panel;
	private TextField txtId, txtPw;
	private Button btnLogin;
	public Ex04_Login(String title) {
		super(title);
		panel = new Panel(new GridLayout(2,2));
//		panel.setLayout(new GridLayout(2,2));
		txtId = new TextField("ID", 20);
		txtPw = new TextField(20);
		txtPw.setEchoChar('*');
		btnLogin = new Button("Login");
		panel.add(new Label("ID", (int)CENTER_ALIGNMENT));
		panel.add(txtId);
		panel.add(new Label("PW", (int)CENTER_ALIGNMENT));
		panel.add(txtPw);
		add(panel, BorderLayout.NORTH);
		add(btnLogin, BorderLayout.SOUTH);
		setSize(new Dimension(400,200));
		setLocation(200,100); //setLocation(0,0) 기본값
		setVisible(true);
		
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				setVisible(false);
				dispose();
				System.exit(0);
			}
		});
	}
	public static void main(String[] args) {
		new Ex04_Login("로그인 화면");
	}
	

}
