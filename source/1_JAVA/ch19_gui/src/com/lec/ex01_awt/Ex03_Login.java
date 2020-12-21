package com.lec.ex01_awt;
//20-12-21_GUI(awt)		ⓒcherryuki(ji)

import java.awt.Button;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Ex03_Login extends Frame {
	private Label lbl1;
	private TextField txtId;
	private Label lbl2;
	private TextField txtPw;
	private Button btnLogin;
	public Ex03_Login(String title) {
		super(title);
		setLayout(new FlowLayout()); //프레임 레이아웃 세팅
		lbl1 = new Label("ID");
		txtId= new TextField("ID", 20);
		lbl2 = new Label("PW");
		txtPw = new TextField(20);
		txtPw.setEchoChar('*');
		btnLogin = new Button("Login");
		add(lbl1);
		add(txtId);
		add(lbl2);
		add(txtPw);
		add(btnLogin);
		setSize(new Dimension(250,150));
		setResizable(false); //사용자가 사이즈 조정 불가
		setLocation(100,100);
		setVisible(true);
		addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent e) {
				setVisible(false);
				dispose();
				System.exit(0);
			}//windowClosing
		});//addWindowListener
	}
	public static void main(String[] args) {
		new Ex03_Login("로그인 화면");
	}

}
