package com.lec.ex02_score_dao;

import java.awt.Container;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Vector;

import javax.swing.JFrame;
import javax.swing.*;

public class ScoreGui extends JFrame implements ActionListener{
	private Container contenPane;
	private JPanel jpup, jpbtn;
	private JTextField txtName, txtKor, txtEng, txtMat;
	private Vector<String> jnames;
	private JComboBox<String> comJob;
	private JButton btnInput, btnSearch, btnOutput, btnExit;
	private JTextArea txtPool;
	private JScrollPane scrollPane;
	private ScoreDao dao = ScoreDao.getInstance();
	private ArrayList<ScoreDto> dto;
	public ScoreGui(String title) {
		super(title);
		setDefaultCloseOperation(EXIT_ON_CLOSE); //x��ư ������ ����
		contenPane = getContentPane();
		contenPane.setLayout(new FlowLayout());
		jpup = new JPanel(new GridLayout(5,2));
		jpbtn = new JPanel(new FlowLayout());
		txtName = new JTextField(20);
		jnames = dao.jnamelist();
		comJob = new JComboBox<String>(jnames);
		txtKor = new JTextField(20);
		txtEng = new JTextField(20);
		txtMat = new JTextField(20);
		ImageIcon icon1 = new ImageIcon("icon/write.gif");
		btnInput = new JButton("�Է�", icon1);
		ImageIcon icon2 = new ImageIcon("icon/hot.gif");
		btnSearch = new JButton("���� ��ȸ", icon2);
		btnOutput = new JButton("��ü ��ȸ");
		btnExit = new JButton("����");
		txtPool = new JTextArea(10,60);
		scrollPane = new JScrollPane(txtPool); //��ũ�ѹٰ� �ʵ� ���ξ���
		jpup.add(new JLabel("�̸�", (int)CENTER_ALIGNMENT));
		jpup.add(txtName);
		jpup.add(new JLabel("����", (int)CENTER_ALIGNMENT));
		jpup.add(comJob);
		jpup.add(new JLabel("����", (int)CENTER_ALIGNMENT));
		jpup.add(txtKor);
		jpup.add(new JLabel("����", (int)CENTER_ALIGNMENT));
		jpup.add(txtEng);
		jpup.add(new JLabel("����", (int)CENTER_ALIGNMENT));
		jpup.add(txtMat);
		jpbtn.add(btnInput);
		jpbtn.add(btnSearch);
		jpbtn.add(btnOutput);
		jpbtn.add(btnExit);
		contenPane.add(jpup);
		contenPane.add(jpbtn);
		contenPane.add(scrollPane);
		setVisible(true);
		setSize(new Dimension(700,450));
		setLocation(300,200);
		btnInput.addActionListener(this);
		btnSearch.addActionListener(this);
		btnOutput.addActionListener(this);
		btnExit.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==btnInput) {//�̸�, ����, ������ ���� �Է¹޾� dao.insert ȣ��
			String name = txtName.getText().trim();
			String jname = comJob.getSelectedItem().toString().trim();
			String korStr = txtKor.getText().trim();
			String engStr = txtEng.getText().trim();
			String matStr = txtMat.getText().trim();
			if(name.equals("")||jname.equals("")||korStr.equals("")||engStr.equals("")||matStr.equals("")) {
				txtPool.setText("�̸�, ����, ��/��/�� ������ �Է��ϼž� �߰��� �� �ֽ��ϴ�");
				return;
			}
			int kor = Integer.parseInt(korStr);
			int eng = Integer.parseInt(engStr);
			int mat = Integer.parseInt(matStr);
			ScoreDto newPerson = new ScoreDto(name, jname, kor, eng, mat);
			int result = dao.insertScore(newPerson);
			if(result==ScoreDao.SUCCESS) {
				txtPool.setText(result+"�� �߰��Ͽ����ϴ�");
				txtName.setText("");
				comJob.setSelectedIndex(0); //�޺��ڽ� 0��° ����
				txtKor.setText("");
				txtEng.setText("");
				txtMat.setText("");
			}
		} else if(e.getSource()==btnSearch) {//������ ��ȸ dao.selectJname ȣ��
			String jname = comJob.getSelectedItem().toString().trim();
			if(jname.equals("")) {
				txtPool.setText("������ �����Ͻ� �� ��ȸ�ٶ��ϴ�");
				return;
			}
			dto = dao.selectJname(jname);
			txtPool.setText("���\t�̸�\t\t����\t����\t����\t����\t����\n");
			if(dto.isEmpty()) {
				txtPool.setText(txtPool.getText()+"��ȸ ������ �ο��� �����ϴ�"); 
				//txtPool.getText()�� �Է��ؾ� ������ �Է��� ����(ex: ���̺� �ʵ��) ���� ���
			} else {
				for(ScoreDto d:dto) {
					txtPool.append(d.toString()+"\n");
				}
			}
			
		} else if(e.getSource()==btnOutput) {
			dto = dao.selectAll();
			txtPool.setText("���\t�̸�\t\t����\t����\t����\t����\t����\n");
			if(dto.isEmpty()) {
				txtPool.setText(txtPool.getText()+"��ȸ ������ �ο��� �����ϴ�"); 
				//txtPool.getText()�� �Է��ؾ� ������ �Է��� ����(ex: ���̺� �ʵ��) ���� ���
			} else {
				for(ScoreDto d:dto) {
					txtPool.append(d.toString()+"\n");
				}
			}
		} else if(e.getSource()==btnExit) {
			setVisible(false);
			dispose();
			System.exit(0);
		}
		
	}
	
	public static void main(String[] args) {
		new ScoreGui("������ ���� ����");
	}
}