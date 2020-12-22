package com.lec.ex02_swing;
//20-12-22_GUI(swing)		ⓒcherryuki(ji)

import java.awt.Container;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Vector;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;



public class Ex02_Frame extends JFrame implements ActionListener {
	private JPanel jPanel; //컨테이너 얻어와서 받을 변수
	private Container container; //컨테이너 얻어와서 받을 변수
	private JLabel jl;
	private ImageIcon icon;
	private JButton jbtn;
	private JTextField jtxtField;
	private Vector<String> item; //콤보 박스에 들어갈 리스트
	private JComboBox<String> jcombo;
	private JCheckBox jcheck;
	private JLabel jlBlank;
	private JButton jbtnExit;
	public Ex02_Frame(String title) {
		super(title);
		setDefaultCloseOperation(EXIT_ON_CLOSE);//x버튼 누르면 종료
		container = getContentPane(); //컨테이너 얻어오기
//		jPanel = (JPanel) getContentPane();//컨테이너 얻어오기
		container.setLayout(new FlowLayout()); //레이아웃 세팅
		jl = new JLabel("Label");
		icon = new ImageIcon("icon/write.gif");
		jbtn = new JButton("Button", icon);
		jtxtField = new JTextField(20);
		item = new Vector<String>(); //콤보박스에 들어갈 리스트
		item.add("A"); item.add("B"); item.add("C");
		jcombo = new JComboBox<String>(item); //Vector로 생성
		jcheck = new JCheckBox("checkBox");
		jlBlank = new JLabel();
		jbtnExit = new JButton("Exit");
		//컴포넌트 크기 조정
		jl.setPreferredSize(new Dimension(50,50));
		jbtn.setPreferredSize(new Dimension(200,50));
		jtxtField.setPreferredSize(new Dimension(300,50));
		jcombo.setPreferredSize(new Dimension(100,50));
		jcheck.setPreferredSize(new Dimension(100,50));
		jlBlank.setPreferredSize(new Dimension(200,50));
		jbtnExit.setPreferredSize(new Dimension(100,50));
		container.add(jl);
		container.add(jbtn);
		container.add(jtxtField);
		container.add(jcombo);
		container.add(jcheck);
		container.add(jlBlank);
		container.add(jbtnExit);
		setVisible(true); //가시화
		pack(); //컴포넌트들이 배치될 수 있는 최소한의 사이즈로 세팅
		//이벤트 리스너 추가
		jbtn.addActionListener(this);
		jcombo.addActionListener(this);
		jcheck.addActionListener(this);
		jbtnExit.addActionListener(this);
		
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==jbtn) {
			String temp = jtxtField.getText().trim();
			if(!temp.equals("")) {
				jlBlank.setText(temp);//jlBlank자리에 temp를 추가
				jcombo.addItem(temp);//jcombo에 temp를 추가
				System.out.println(item);//콤보박스에 추가하면 item도 추가
				jtxtField.setText("");
				String name = JOptionPane.showInputDialog("name?");
				if(name!=null) {
					jcheck.setText(name);
				}
			}
		} else if(e.getSource()==jcombo) {
			jlBlank.setText(jcombo.getSelectedItem().toString());
		} else if (e.getSource()==jcheck) {
			if(jcheck.isSelected()) {//체크박스를 체크했는지 여부
				jlBlank.setText(jcheck.getText());
			}else {
				System.out.println("체크박스를 언체크함");
			}
		} else if (e.getSource()==jbtnExit) {
			setVisible(false);
			dispose();
			System.exit(0);
		}
		
	}
	
	public static void main(String[] args) {
		new Ex02_Frame("두번째 swing 예제");
	}
}
