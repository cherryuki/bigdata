package com.lec.ex01_awt;
//20-12-21_GUI(awt)		ⓒcherryuki(ji)

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Dimension;
import java.awt.Frame;
import java.awt.List;
import java.awt.Panel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Ex06_RockPaperScissor extends Frame implements ActionListener {
	private Panel panel;
	private Button btn0;
	private Button btn1;
	private Button btn2;
	private List list;
	private Button btnExit;
	public Ex06_RockPaperScissor(String title) {
		super(title);
		panel = new Panel();
		btn0 = new Button("Scissor");
		btn1 = new Button("Rock");
		btn2 = new Button("Paper");
		list = new List();
		btnExit = new Button("EXIT");
		panel.add(btn0);
		panel.add(btn1);
		panel.add(btn2);
		add(panel, BorderLayout.NORTH);
		add(list, BorderLayout.CENTER);
		add(btnExit, BorderLayout.SOUTH);
		setVisible(true);
		setSize(new Dimension(300,200));
		setLocation(200,100);
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				setVisible(false);
				dispose();
				System.exit(0);
			}
		});
		btnExit.addActionListener(this);
		btn0.addActionListener(this);
		btn1.addActionListener(this);
		btn2.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		int computer = (int)(Math.random()*3); //가위(0), 바위(1), 보(2)
		if(e.getSource()==btnExit) {
			setVisible(false);
			dispose();
			System.exit(0);
		}else if(e.getSource()==btn0) {
			if(computer==0) {
				list.add("Draw  You:Scissor, Computer:Scissor ");
			}else if(computer==1) {
				list.add("Computer Win!  You:Scissor, Computer:Rock ");
			}else {
				list.add("You Win!  You:Scissor, Computer:Paper");
			}
		} else if(e.getSource()==btn1) {
			if(computer==0) {
				list.add("You Win!  You:Rock, Computer:Scissor ");
			}else if(computer==1) {
				list.add("Draw  You:Rock, Computer:Rock");
			}else {
				list.add("Computer Win!  You:Rock, Computer:Paper");
			}
		} else if(e.getSource()==btn2) {
			if(computer==0) {
				list.add("Computer Win!  You:Paper, Computer:Scissor ");
			}else if(computer==1) {
				list.add("You Win!  You:Paper, Computer:Rock ");
			}else {
				list.add("Draw  You:Paper, Computer:Paper");
			}
		}
	}
	public static void main(String[] args) {
		new Ex06_RockPaperScissor("가위 바위 보");
	}
		
}
