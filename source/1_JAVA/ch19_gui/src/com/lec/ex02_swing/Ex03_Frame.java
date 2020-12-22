package com.lec.ex02_swing;
//20-12-22_GUI(swing)		ⓒcherryuki(ji)

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class Ex03_Frame extends JFrame implements ActionListener {
	private Container container;
	private JPanel jp;
	private JTextField jtxtName, jtxtTel, jtxtAge;
	private ImageIcon icon;
	private JButton btnOut;
	private JTextArea jta;
	private JScrollPane scrollbar;
	public Ex03_Frame(String title) {
		super(title);
		setDefaultCloseOperation(EXIT_ON_CLOSE);//x버튼 누르면 종료
		container = getContentPane();
//		container.setLayout(new BorderLayout());//기본값이라 생략 가능
		jp = new JPanel(new GridLayout(3,2));//3행 2열
		jtxtName = new JTextField();
		jtxtTel = new JTextField();
		jtxtAge = new JTextField();
		icon = new ImageIcon("icon/output.png");
		btnOut = new JButton("Print", icon);
		jta = new JTextArea(5,30);
		scrollbar = new JScrollPane(jta);//스크롤바
		jp.add(new JLabel("Name", (int) CENTER_ALIGNMENT));
		jp.add(jtxtName);
		jp.add(new JLabel("Tel", (int) CENTER_ALIGNMENT));
		jp.add(jtxtTel);
		jp.add(new JLabel("Age", (int)CENTER_ALIGNMENT));
		jp.add(jtxtAge);
		container.add(jp, BorderLayout.NORTH);
		container.add(btnOut, BorderLayout.CENTER);
		container.add(scrollbar, BorderLayout.SOUTH); //스크롤바를 추가해줘야 함! (jta가 아닌)
		setVisible(true);
		setBounds(100,100, 400,300); //setLocation(100,100); 과 setSize(new Dimension(400,300)을 한 번에
		btnOut.addActionListener(this);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==btnOut) {
			String name = jtxtName.getText().trim();
			String tel = jtxtTel.getText().trim();
			if(name.equals("") || tel.equals("")) {
				System.out.println("이름과 전화번호는 반드시 입력");
				return;
			}
			int age;
			try {
				age = Integer.parseInt(jtxtAge.getText().trim());
			} catch (NumberFormatException ex) {
				age = -1;
			}
			String result = "[Name]"+name+"\t[Tel]"+tel;
			if(age>=0 && age<130) {
				result += "\t[Age]"+age;
			} else {
				result += "\t[Age]유효하지 않은 나이입니다";
			}
			System.out.println(result);
			jta.append(result+"\r\n");
			jtxtName.setText("");
			jtxtTel.setText("");
			jtxtAge.setText("");
		}//if
	}//actionPerformed
	
	public static void main(String[] args) {
		new Ex03_Frame("3번째 swing 예제");
	}

}
