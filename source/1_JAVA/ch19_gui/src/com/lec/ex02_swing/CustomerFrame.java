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
import java.util.HashMap;
import java.util.Iterator;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class CustomerFrame extends JFrame implements ActionListener {
	private Container contenPane;
	private JPanel jpup, jpdown;
	private JTextField txtPhone, txtName, txtPoint;
	private JButton btnJoin, btnSearch, btnOutput, btnExit;
	private JTextArea jta;
	private JScrollPane scrollbar;
	HashMap<String, Customer> customer = new HashMap<String, Customer>();
	Writer writer = null;
	
	public CustomerFrame(String title) {
		super(title);
		setDefaultCloseOperation(EXIT_ON_CLOSE);//x클릭시 종료
		contenPane = getContentPane();
		contenPane.setLayout(new FlowLayout());
		jpup = new JPanel(new GridLayout(3,2));
		jpdown = new JPanel(new FlowLayout());//왼쪽부터 차곡차곡
		txtPhone = new JTextField(15);
		txtName = new JTextField(15);
		txtPoint = new JTextField(15);
		btnJoin = new JButton("Join");
		btnSearch = new JButton("Search");
		btnOutput = new JButton("Output");
		btnExit = new JButton("Exit");
		jta = new JTextArea(15,30);
		scrollbar = new JScrollPane(jta);
		jpup.add(new JLabel("phone", (int)CENTER_ALIGNMENT));
		jpup.add(txtPhone);
		jpup.add(new JLabel("name", (int)CENTER_ALIGNMENT));
		jpup.add(txtName);
		jpup.add(new JLabel("point", (int)CENTER_ALIGNMENT));
		jpup.add(txtPoint);
		jpdown.add(btnJoin);
		jpdown.add(btnSearch);
		jpdown.add(btnOutput);
		jpdown.add(btnExit);
		contenPane.add(jpup);
		contenPane.add(jpdown);
		contenPane.add(scrollbar);//스크롤바를 컨테이너에 올리기!
		setBounds(200,200, 400, 450);
		setVisible(true);
		btnJoin.addActionListener(this);
		btnSearch.addActionListener(this);
		btnOutput.addActionListener(this);
		btnExit.addActionListener(this);
		txtPoint.setText("1000");
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		String phone = txtPhone.getText().trim();
		String name = txtName.getText().trim();
		int point;
		try {
			point = Integer.parseInt(txtPoint.getText().trim());
		} catch (NumberFormatException e1) {
			point=0;
		}
		if(e.getSource()==btnJoin) {
			if(phone.equals("")||name.equals("")) {
				System.out.println("전화번호와 이름은 반드시 입력");
				return;
			} else {
				customer.put(phone, new Customer(phone, name, point));
//				String result = name+"("+phone+")님의 포인트: "+point+"\r\n";
//				jta.append(result);
				jta.append(customer.get(phone).toString()+"\r\n");
				txtPhone.setText("");
				txtName.setText("");
				txtPoint.setText("1000");
			}
			
		} else if(e.getSource()==btnSearch) {
			Iterator<String> iterator = customer.keySet().iterator();
			int cnt=0;
			while(iterator.hasNext()) {
				String key = iterator.next();
				String post = key.substring(key.lastIndexOf("-")+1);
				if(phone.equals(post)) {//전화번호 뒷자리 중복 없다고 가정
					txtPhone.setText(key);//customer.get(key).getPhone()
					txtName.setText(customer.get(key).getName());
					txtPoint.setText(""+customer.get(key).getPoint());
					//포인트는 int형이므로 String으로 바꿔줘야 함 ""+ or setText(Strig.valueOf(customer.get(key).getPoint());
					break; //찾았으면 while문 빠져 나가기
				}
				cnt++;
				if(cnt==customer.size()) {
					txtPhone.setText("회원이 아닙니다");
					txtName.setText("");
					txtPoint.setText("1000");
				}
			}//while
		} else if(e.getSource()==btnOutput) {
			try {
				writer = new FileWriter("icon/customer.txt",true);
				Iterator<String> iterator = customer.keySet().iterator();
				while(iterator.hasNext()) {
					String key = iterator.next();
					writer.write(customer.get(key).toString()+"\r\n");
					System.out.println(customer.get(key));
				}
			} catch (IOException e1) {
				System.out.println(e1.getMessage());
			} finally {
				try {
					if(writer!=null) writer.close();
				} catch (IOException e1) {
					System.out.println(e1.getMessage());
				}
			}
		} else if(e.getSource()==btnExit) {
			setVisible(false);
			dispose();
			System.exit(0);
		}
	}//actionPerformed
	
	public static void main(String[] args) {
		new CustomerFrame("회원관리");
	}

}
