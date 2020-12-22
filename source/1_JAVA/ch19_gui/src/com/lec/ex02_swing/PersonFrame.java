package com.lec.ex02_swing;
//20-12-22_GUI(swing)		ⓒcherryuki(ji)

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class PersonFrame extends JFrame implements ActionListener{
	private Container container;
	private JPanel jp1, jp2;
	private JTextField jtxtName, jtxtTel, jtxtAge;
	private ImageIcon iconIn, iconOut;
	private JButton btnIn, btnOut;
	ArrayList<Person> person = new ArrayList<Person>();
	Writer writer = null;
	
	public PersonFrame(String title) {
		super(title);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		container = getContentPane();
		jp1 = new JPanel(new GridLayout(3,2)); //3행2열
		jp2 = new JPanel(new FlowLayout()); //왼쪽부터 차곡차곡
		jtxtName = new JTextField();
		jtxtTel = new JTextField();
		jtxtAge = new JTextField();
		iconIn = new ImageIcon("icon/join.png");
		iconOut = new ImageIcon("icon/output.png");
		btnIn = new JButton("Input", iconIn);
		btnOut = new JButton("Output", iconOut);
		jp1.add(new JLabel("Name", (int) CENTER_ALIGNMENT));
		jp1.add(jtxtName);
		jp1.add(new JLabel("Tel", (int) CENTER_ALIGNMENT));
		jp1.add(jtxtTel);
		jp1.add(new JLabel("Age", (int) CENTER_ALIGNMENT));
		jp1.add(jtxtAge);
		jp2.add(btnIn);
		jp2.add(btnOut);
		container.add(jp1, BorderLayout.CENTER);
		container.add(jp2, BorderLayout.SOUTH);
		setBounds(100,100, 300, 200);
		setVisible(true);
		btnIn.addActionListener(this);
		btnOut.addActionListener(this);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==btnIn) {
			String name = jtxtName.getText().trim();
			String tel = jtxtTel.getText().trim();
			int age;
			try {
				age = Integer.parseInt(jtxtAge.getText().trim());
				if(age<0 || age>130) {
					age=-1;
				}
			} catch (NumberFormatException ex) {
				age = -1;
			}
			if(name.equals("")||tel.equals("")||age==-1) {
				System.out.println("유효하지 않은 값입니다");
				return;
			} else {
				person.add(new Person(name, tel, age));
				jtxtName.setText("");
				jtxtTel.setText("");
				jtxtAge.setText("");
			}
		} else if(e.getSource()==btnOut) {
			for(Person p:person) {
				System.out.println(p);
				try {
					writer = new FileWriter("icon/person.txt", true);
					writer.write(p.toString()+"\r\n");
				} catch (IOException e1) {
					System.out.println(e1.getMessage());
				} finally {
					try {
						if(writer!=null) writer.close();
					} catch (IOException e1) {
						System.out.println(e1.getMessage());
					}
				}
				
			}//for
		}
		
	}

	public static void main(String[] args) {
		new PersonFrame("GUI 예제");
	}
}
