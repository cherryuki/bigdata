package com.lec.ex02_swing;
//20-12-22_GUI(swing)		ⓒcherryuki(ji)

import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Ex01_Frame extends JFrame implements ActionListener {
	private JPanel panel;
	private JLabel jlbl;
	private JButton jbtn;
	public Ex01_Frame(String title) {
		super(title);
		setDefaultCloseOperation(EXIT_ON_CLOSE);//x를 누르면 종료
		panel = (JPanel)getContentPane();//스윙은 컨테이너(프레임)을 먼저 얻어옴(getContentPane();)
		panel.setLayout(new FlowLayout());
		
		jlbl = new JLabel("Good day", (int) CENTER_ALIGNMENT);
		jlbl.setPreferredSize(new Dimension(150,200));
		jbtn = new JButton("Exit");
		jbtn.setPreferredSize(new Dimension(200,200));
		panel.add(jlbl);
		panel.add(jbtn);
		setVisible(true);
		pack(); //최소한의 사이즈 세팅
//		setSize(new Dimension(500,300));
		setVisible(true);
		jbtn.addActionListener(this);
		
	}
	public static void main(String[] args) {
		new Ex01_Frame("첫 swing 예제");
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==jbtn) {
			setVisible(false);
			dispose();
			System.exit(0);
		}

	}

}
