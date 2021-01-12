package com.lec.supermarket;
//21-01-12_JDBC_Dao&Dto_GUI		(c)cherryuki(ji)

import java.awt.Container;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Vector;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class SwingSupermarket extends JFrame implements ActionListener {
	private Container contenPane;
	private JPanel jpup, jpbtn;
	private JTextField txtCId, txtCTel, txtCName, txtCPoint, txtCAmount;
	private Vector<String> levelname;
	private JComboBox<String> comLevelName;
	private JButton btnCIdSearch, btnCTelSearch, btnCNameSearch, btnBuyWithPoint,
					btnBuy, btnLevelNameOutput, btnAllOutput, btnInsert, 
					btnCTelUpdate, btnDelete, btnExit;
	private JTextArea txtPool;
	private JScrollPane scrollPane;
	private SupermarketDao dao = SupermarketDao.getInstance();
	private ArrayList<SupermarketDto> customer;
	private SupermarketDto dto;
	public SwingSupermarket(String title) {
		super(title);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		contenPane = getContentPane();
		contenPane.setLayout(new FlowLayout());
		jpup = new JPanel(new GridLayout(6, 3));
		jpbtn = new JPanel(new FlowLayout());
		txtCId = new JTextField(20);
		txtCTel = new JTextField(20);
		txtCName  = new JTextField(20);
		txtCPoint = new JTextField(20);
		txtCAmount = new JTextField(20);
		levelname = dao.levellist();
		comLevelName = new JComboBox<String>(levelname);
		btnCIdSearch = new JButton("���̵� �˻�");
		btnCTelSearch = new JButton("��4�ڸ�(FULL) �˻�");
		btnCNameSearch = new JButton("�� �̸� �˻�");
		btnBuyWithPoint = new JButton("����Ʈ�θ� ����");
		jpup.add(new JLabel(" �� �� �� ",(int) CENTER_ALIGNMENT));
		jpup.add(txtCId);
		jpup.add(btnCIdSearch);
		jpup.add(new JLabel("�� �� �� ȭ",(int) CENTER_ALIGNMENT));
		jpup.add(txtCTel);
		jpup.add(btnCTelSearch);
		jpup.add(new JLabel("�� �� �� ��",(int) CENTER_ALIGNMENT));
		jpup.add(txtCName);
		jpup.add(btnCNameSearch);
		jpup.add(new JLabel("��  ��  Ʈ",(int) CENTER_ALIGNMENT));
		jpup.add(txtCPoint);
		jpup.add(btnBuyWithPoint);
		jpup.add(new JLabel("�� �� �� ��",(int) CENTER_ALIGNMENT));
		jpup.add(txtCAmount);
		jpup.add(new JLabel(""));//�� �� �߰��ϴ� �κ�
		jpup.add(new JLabel("�� �� �� ��",(int) CENTER_ALIGNMENT));
		jpup.add(comLevelName);
		btnBuy = new JButton("��ǰ ����");
		btnLevelNameOutput = new JButton("��޺����");
		btnAllOutput = new JButton("��ü���");
		btnInsert = new JButton("ȸ������");
		btnCTelUpdate = new JButton("��ȣ����");
		btnDelete = new JButton("ȸ��Ż��");
		btnExit = new JButton("������");
		jpbtn.add(btnBuy);
		jpbtn.add(btnLevelNameOutput);
		jpbtn.add(btnAllOutput);
		jpbtn.add(btnInsert);
		jpbtn.add(btnCTelUpdate);
		jpbtn.add(btnDelete);
		jpbtn.add(btnExit);
		txtPool = new JTextArea(6, 70);
		scrollPane = new JScrollPane(txtPool);
		contenPane.add(jpup);
		contenPane.add(jpbtn);
		contenPane.add(scrollPane);
		txtPool.setText("\t�� �� �� ���˻� �� �����ϼ��� �� �� ��");
		setVisible(true);
		setLocation(200,200);
		setSize(new Dimension(800, 400));
		setResizable(false);
		btnCIdSearch.addActionListener(this);
		btnCTelSearch.addActionListener(this);
		btnCNameSearch.addActionListener(this);
		btnBuyWithPoint.addActionListener(this);
		btnBuy.addActionListener(this);
		btnLevelNameOutput.addActionListener(this);
		btnAllOutput.addActionListener(this);
		btnInsert.addActionListener(this);
		btnCTelUpdate.addActionListener(this);
		btnDelete.addActionListener(this);
		btnExit.addActionListener(this);
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==btnCIdSearch) {//1
			String id = txtCId.getText().trim();
			if(id.equals("")) {
				txtPool.setText("��ȿ�� �� ���̵� �Է� �� ���̵� �˻����ּ���");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				return;
			}
			dto = dao.searchId(id);
			txtPool.setText("ID\t��ȭ\t  �̸�\t����Ʈ\t���� ���ž�\t�� ���\t�������� ���� �߰� ���� �ݾ�\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(dto!=null) {
				txtCTel.setText(dto.getTel());
				txtCName.setText(dto.getName());
				txtCPoint.setText(dto.getPoint()+"");
				txtCAmount.setText("");
				comLevelName.setSelectedItem(dto.getLevel());
				txtPool.append(dto.toString());
			} else {
				txtPool.setText("�������� ���� ID�Դϴ�");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
			}
		} else if(e.getSource()==btnCTelSearch) {//2
			String postTel = txtCTel.getText().trim();
			if(postTel.length()<4) {
				txtPool.setText("��ȭ��ȣ �� 4�ڸ��� �Է��ϼ���");
				txtCId.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				return;
			}
			
			customer = dao.searchTel(postTel);
			txtPool.setText("ID\t��ȭ\t  �̸�\t����Ʈ\t���� ���ž�\t�� ���\t�������� ���� �߰� ���� �ݾ�\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(customer.isEmpty()) {
				txtPool.setText("�ش� ��ȭ��ȣ�� ȸ���� �����ϴ�");
				txtCId.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				return;
			} else {
				for(SupermarketDto c:customer) {
					txtPool.append(c.toString()+"\n");
				}
				txtCId.setText(customer.get(customer.size()-1).getId());
				txtCTel.setText(customer.get(customer.size()-1).getTel());
				txtCName.setText(customer.get(customer.size()-1).getName());
				txtCPoint.setText(customer.get(customer.size()-1).getPoint()+"");
				txtCAmount.setText("");
				comLevelName.setSelectedItem(customer.get(customer.size()-1).getLevel());
			}
		} else if(e.getSource()==btnCNameSearch) {//3
			String name = txtCName.getText().trim();
			if(name.length()==0) {
				txtPool.setText("�̸��� �Է� �� �̸� �˻��� �ּ���");
				txtCId.setText("");
				txtCTel.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				return;
			} 
			customer = dao.searchName(name);
			txtPool.setText("ID\t��ȭ\t  �̸�\t����Ʈ\t���� ���ž�\t�� ���\t�������� ���� �߰� ���� �ݾ�\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(customer.isEmpty()) {
				txtPool.setText("�ش� �̸��� ���� �˻����� �ʽ��ϴ�. ȸ�������� �������ּ���");
				txtCId.setText("");
				txtCTel.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
			} else {
				for(SupermarketDto c:customer) {
					txtPool.append(c.toString()+"\n");
				}
				txtCId.setText(customer.get(customer.size()-1).getId());
				txtCTel.setText(customer.get(customer.size()-1).getTel());
				txtCName.setText(customer.get(customer.size()-1).getName());
				txtCPoint.setText(customer.get(customer.size()-1).getPoint()+"");
				txtCAmount.setText("");
				comLevelName.setSelectedItem(customer.get(customer.size()-1).getLevel());
			}
			
		} else if(e.getSource()==btnBuyWithPoint) {//4
			String id = txtCId.getText().trim();
			String priceStr = txtCAmount.getText().trim();
			String pointStr = txtCPoint.getText().trim();
			int price = Integer.parseInt(priceStr);
			int point = Integer.parseInt(pointStr);
			if(price>point) {
				txtPool.setText("����Ʈ�� �����Ͽ� ����Ʈ�θ� ���Ŵ� �Ұ����մϴ�");
				return;
			} else {
				int result = dao.updatePoint(id, price);
				if(result==SupermarketDao.SUCCESS) {
					txtPool.setText("����Ʈ�θ� ���� ����");
					txtCPoint.setText((point-price)+"");
					txtCAmount.setText("");
				} else {
					txtPool.setText("����Ʈ�θ� ���� ���� �����ڿ��� �����ϼ���");
				}
			}
		} else if(e.getSource()==btnBuy) {//5
			String id = txtCId.getText().trim();
			String priceStr = txtCAmount.getText().trim();
			String pointStr = txtCPoint.getText().trim();
			int price = Integer.parseInt(priceStr);
			int point = Integer.parseInt(pointStr);
			int result = dao.updateAmount(id, price);
			if(result==SupermarketDao.SUCCESS) {
				txtPool.setText("��ǰ ���� �� ����Ʈ ���� ����(���� Ȯ�� �Ϸ�)");
			}
		} else if(e.getSource()==btnLevelNameOutput) {//6
			String level = comLevelName.getSelectedItem().toString().trim();
			if(level.equals("")) {
				txtPool.setText("�� ����� ���� �� ��޺� ��� ��ư�� Ŭ���ϼ���");
				txtCId.setText("");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				return;
			}
			customer = dao.selectLevel(level);
			txtPool.setText("ID\t��ȭ\t  �̸�\t����Ʈ\t���� ���ž�\t�� ���\t�������� ���� �߰� ���� �ݾ�\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(customer.isEmpty()) {
				txtPool.setText("���� �ش� ��޿��� ���� �����ϴ�");
				txtCId.setText("");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
			} else {
				txtCId.setText("");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				for (SupermarketDto c:customer) {
					txtPool.append(c.toString()+"\n");
				}
				txtPool.append("�� "+customer.size()+"��");
			}
		} else if(e.getSource()==btnAllOutput) {//7
			customer = dao.selectAll();
			txtPool.setText("ID\t��ȭ\t  �̸�\t����Ʈ\t���� ���ž�\t�� ���\t�������� ���� �߰� ���� �ݾ�\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(customer.isEmpty()) {
				txtPool.setText("���� ��ȸ������ ���� �����ϴ�");
				txtCId.setText("");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
			} else {
				txtCId.setText("");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				for (SupermarketDto c:customer) {
					txtPool.append(c.toString()+"\n");
				}
				txtPool.append("�� "+customer.size()+"��");
			}
		} else if(e.getSource()==btnInsert) {//8
			String tel = txtCTel.getText().trim();
			String name = txtCName.getText().trim();
			if(tel.equals("")||name.equals("")) {
				txtPool.setText("��ȭ��ȣ�� ������ �ʼ� �Է»����Դϴ�");
				txtCId.setText("");
				txtCTel.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				return;
			} 
			int result = dao.insertCustomer(tel, name);
			if(result==SupermarketDao.SUCCESS) {
				txtPool.setText("ȸ������ �����մϴ�. ����Ʈ 1000���� ȸ������ ������ �����Ͽ����ϴ�");
				txtCPoint.setText("1000");
				comLevelName.setSelectedIndex(1);
			}
		} else if(e.getSource()==btnCTelUpdate) {//9
			String id = txtCId.getText().trim();
			String tel = txtCTel.getText().trim();
			if(id.equals("")||tel.equals("")) {
				txtPool.setText("��ȿ�� ��ID�� �˻� �� ��ȣ ������ �����Ͻñ� �ٶ��ϴ�");
				return;
			}
			int result = dao.updateCustomer(tel, id);
			if(result==SupermarketDao.SUCCESS) {
				txtPool.setText("��ȭ��ȣ�� �����Ǿ����ϴ�");
			}
		} else if(e.getSource()==btnDelete) {//10
			String tel = txtCTel.getText().trim();
			if(tel.length()==0) {
				txtPool.setText("��ȭ��ȣ�� �־�� ȸ��Ż�� �����մϴ�\n��ȭ��ȣ Ȯ�� �� ȸ�� Ż�� �����Ͻñ� �ٶ��ϴ�");
				return;
			}
			int result = dao.deleteCustomer(tel);
			if(result==SupermarketDao.SUCCESS) {
				txtPool.setText(tel+"���� ȸ�� Ż�� �Ϸ�Ǿ����ϴ�");
			}
		} else if(e.getSource()==btnExit) {
			setVisible(false);
			dispose();
			System.exit(0);
		}
		
	}
	public static void main(String[] args) {
		new SwingSupermarket("���۸��� ����");
	}
}
