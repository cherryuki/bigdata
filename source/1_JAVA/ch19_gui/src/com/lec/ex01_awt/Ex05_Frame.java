package com.lec.ex01_awt;
//20-12-21_GUI(awt)		ⓒcherryuki(ji)

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Dimension;
import java.awt.Frame;
import java.awt.Label;
import java.awt.List;
import java.awt.Panel;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

//Layout 세팅, 컴포넌트 생성 후 add, setVisible, setSize
public class Ex05_Frame extends Frame implements ActionListener{
	private Panel panel;
	private TextField txtField;
	private Button btnOk;
	private Button btnExit;
	private List list;
	public Ex05_Frame() {
		//setLayout(new BorderLayout()); 기본값이므로 생략 가능
		panel = new Panel(); //panel은 FlowLayout이 기본값
		txtField = new TextField(20);
		btnOk = new Button("OK");
		btnExit = new Button("EXIT");
		list = new List();
		panel.add(new Label("write"));
		panel.add(txtField);
		panel.add(btnOk);
		panel.add(btnExit);
		add(panel, BorderLayout.NORTH);
		add(list, BorderLayout.CENTER);
		setVisible(true);
		setSize(new Dimension(400,200));
		/* 1. implements ActionListener 추가
		 * 2. 이벤트 리스너 추가
		 * 3. 로직 추가
		 */
		btnOk.addActionListener(this);
		btnExit.addActionListener(this);
		
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				setVisible(false);
				dispose();
				System.exit(0);
			}
		});
		
	}
	
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==btnOk) {
			list.add(txtField.getText());//txtField의 텍스트를 list로 추가
			txtField.setText(""); 
		}else if(e.getSource()==btnExit) {
			setVisible(false);
			dispose();
			System.exit(0);
		}
	}
	public static void main(String[] args) {
		new Ex05_Frame();
	}
}
