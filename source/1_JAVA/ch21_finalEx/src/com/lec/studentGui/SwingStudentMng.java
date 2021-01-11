package com.lec.studentGui;
//21-01-11_JDBC_Dao&Dto_GUI		(c)cherryuki(ji)

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

public class SwingStudentMng extends JFrame implements ActionListener {
	private Container contenPane;
	private JPanel jpup, jpbtn;
	private JTextField txtSNo, txtSName, txtScore;
	private Vector<String> mnames;
	private JComboBox<String> comMname;
	private JButton btnSNoSearch, btnSNameSearch, btnMNameSearch, 
					btnInput, btnUpdate, btnStudentOut, btnExpelOut, btnExpel, btnExit;
	private JTextArea txtPool;
	private JScrollPane scrollPane;
	private StudentSwingDao dao = StudentSwingDao.getInstance();
	private ArrayList<StudentSwingDto> student;
	private StudentSwingDto dto;
	public SwingStudentMng(String title) {
		super(title);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		contenPane = getContentPane();
		contenPane.setLayout(new FlowLayout());
		jpup = new JPanel(new GridLayout(4,3));
		jpbtn = new JPanel(new FlowLayout());
		txtSNo = new JTextField(10);
		txtSName = new JTextField(10);
		mnames = dao.mnamelist();
		comMname = new JComboBox<String>(mnames);
		txtScore = new JTextField(10);
		btnSNoSearch = new JButton("�й��˻�");
		btnSNameSearch = new JButton("�̸��˻�");
		btnMNameSearch = new JButton("�����˻�");
		//jpbtn
		btnInput = new JButton("�л��Է�");
		btnUpdate = new JButton("�л�����");
		btnStudentOut = new JButton("�л����");
		btnExpelOut = new JButton("���������");
		btnExpel = new JButton("����ó��");
		btnExit = new JButton("����");
		txtPool = new JTextArea(10, 50);
		scrollPane = new JScrollPane(txtPool);
		jpup.add(new JLabel("�й�", (int)CENTER_ALIGNMENT));
		jpup.add(txtSNo);
		jpup.add(btnSNoSearch);
		jpup.add(new JLabel("�̸�", (int)CENTER_ALIGNMENT));
		jpup.add(txtSName);
		jpup.add(btnSNameSearch);
		jpup.add(new JLabel("����", (int)CENTER_ALIGNMENT));
		jpup.add(comMname);
		jpup.add(btnMNameSearch);
		jpup.add(new JLabel("����", (int)CENTER_ALIGNMENT));
		jpup.add(txtScore);
		jpup.add(new JLabel(""));
		jpbtn.add(btnInput);
		jpbtn.add(btnUpdate);
		jpbtn.add(btnStudentOut);
		jpbtn.add(btnExpelOut);
		jpbtn.add(btnExpel);
		jpbtn.add(btnExit);
		contenPane.add(jpup);
		contenPane.add(jpbtn);
		contenPane.add(scrollPane);
		setVisible(true);
		setSize(new Dimension(600, 400));
		setResizable(false);
		setLocation(200,150);
		btnSNoSearch.addActionListener(this);
		btnSNameSearch.addActionListener(this);
		btnMNameSearch.addActionListener(this);
		btnInput.addActionListener(this);
		btnUpdate.addActionListener(this);
		btnStudentOut.addActionListener(this);
		btnExpelOut.addActionListener(this);
		btnExpel.addActionListener(this);
		btnExit.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource()==btnSNoSearch) {//select sno
			String snoStr = txtSNo.getText().trim();
			if(snoStr.equals("")) {
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
				txtPool.setText("�й��� �Է��� �й��˻� ��ư�� �����ּ���");
				return;
			}
			int sno = Integer.parseInt(snoStr);
			dto = dao.searchSno(sno);
			if(dto!=null) {
				txtSName.setText(dto.getName());
				comMname.setSelectedItem(dto.getMajor());
				txtScore.setText(""+dto.getScore());
				txtPool.setText("");
			} else {
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
				txtPool.setText(sno+"�� ��ȿ���� ���� �й��Դϴ�");
			}
		} else if(e.getSource()==btnSNameSearch) {//select sname
			String sname = txtSName.getText().trim();
			if(sname.equals("")) {
				txtPool.setText("�̸��� �Է��� �̸��˻� ��ư�� �����ּ���");
				return;
			}
			student = dao.selectSname(sname);
			if(student.size()==0) {
				txtPool.setText("�ش� �̸��� �л��� �����ϴ�");
				txtSNo.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			} else if(student.size()==1) {
				txtSNo.setText(student.get(0).getSno()+"");
				comMname.setSelectedItem(student.get(0).getMajor());
				txtScore.setText(student.get(0).getScore()+"");
				txtPool.setText("");
			} else {//�������� ���� ���
				txtPool.setText("\t�й�\t�̸�\t�а���\t����\n"
						+ "---------------------------------------------------------\n");
				for(StudentSwingDto s:student) {
					txtPool.append(s.toString()+"\n");
				}//0����� ������ size()=1, ������ �ε��� = student.size()-1
				txtSNo.setText(student.get(student.size()-1).getSno()+"");
				comMname.setSelectedItem(student.get(student.size()-1).getMajor());
				txtScore.setText(student.get(student.size()-1).getScore()+"");
			}
			
		} else if(e.getSource()==btnMNameSearch) {//select mname
			String mname = comMname.getSelectedItem().toString().trim();
			if(mname.equals("")) {
				txtPool.setText("������ ���� �� �����˻� ��ư�� �����ּ���");
				return;
			}
			student = dao.selectMname(mname);
			txtPool.setText("   ���\t�̸�(�й�)\t\t�а���(�а���ȣ)\t����\n"
					+ " -------------------------------------------------------------------------------------------------------------------------\n");
			if(student.isEmpty()) {
				txtPool.setText(txtPool.getText()+"�ش� �а����� �л��� �����ϴ�");
				txtSNo.setText("");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			} else {
				for(StudentSwingDto s:student) {
					txtPool.append(s.toString()+"\n");
				}
				txtSNo.setText("");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			}
			
		} else if(e.getSource()==btnInput) {//insert student
			String name = txtSName.getText().trim();
			String major = comMname.getSelectedItem().toString().trim();
			String scoreStr = txtScore.getText().trim();
			if(name.equals("")||major.equals("")) {
				txtPool.setText("�̸��� ������ �ʼ� �Է� �׸��Դϴ�(���� ���Է½� 0��)");
				return;
			}
			if(scoreStr.length()==0) {
				scoreStr = 0+"";
			} else {
				int score = Integer.parseInt(scoreStr);
			}
			if(Integer.parseInt(scoreStr)<0||Integer.parseInt(scoreStr)>100) {
					txtPool.setText("��ȿ���� ���� �����Դϴ�\n������ 0~100������ ���� �Է����ּ���(���Է½� 0��)");
				return;
			}
			StudentSwingDto newStudent = new StudentSwingDto(name, major, Integer.parseInt(scoreStr));
			int result = dao.insertStudent(newStudent);
			if(result==StudentSwingDao.SUCCESS) {
				txtPool.setText(name+" �л� �Է� ����");
				txtSNo.setText("");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			} 
			
		} else if(e.getSource()==btnUpdate) {//update student
			String snoStr = txtSNo.getText().trim();
			String name = txtSName.getText().trim();
			String major = comMname.getSelectedItem().toString().trim();
			String scoreStr = txtScore.getText().trim();
			if(snoStr.equals("")||name.equals("")||major.equals("")) {
				txtPool.setText("�й�, �̸�, ������ ��� �Է��ϼž� ������ �����մϴ�");
				return;
			} 
			if(scoreStr.length()==0) {
				scoreStr = 0+"";
			} else {
				int score = Integer.parseInt(scoreStr);
			}
			if(Integer.parseInt(scoreStr)<0||Integer.parseInt(scoreStr)>100) {
				txtPool.setText("��ȿ���� ���� �����Դϴ�\n������ 0~100������ ���� �Է����ּ���(���Է½�:0��)");
			return;
			}
			StudentSwingDto student = new StudentSwingDto(Integer.parseInt(snoStr), name, major, Integer.parseInt(scoreStr));
			int result = dao.updateStudent(student);
			if(result==StudentSwingDao.SUCCESS) {
				txtPool.setText(name+" �л� �Է� ����");
				txtSNo.setText("");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			}
			
		} else if(e.getSource()==btnStudentOut) {//select all
			student = dao.selectAll();
			txtPool.setText("   ���\t�̸�(�й�)\t\t�а���(�а���ȣ)\t����\n"
					+ " -------------------------------------------------------------------------------------------------------------------------\n");
			if(student.isEmpty()) {
				txtPool.setText(txtPool.getText()+"��ȸ ������ �л��� �����ϴ�");
				txtSNo.setText("");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			} else {
				for(StudentSwingDto s:student) {
					txtPool.append(s.toString()+"\n");
				}
				txtSNo.setText("");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			}
		} else if(e.getSource()==btnExpelOut) {//select expel
			student = dao.selectExpel();
			txtPool.setText("  ���\t�̸�(�й�)\t\t�а���(�а���ȣ)\t����\n"
					+ "-------------------------------------------------------------------------------------------------------------------------\n");
			if(student.isEmpty()) {
				txtPool.setText(txtPool.getText()+"��ȸ ������ �����ڰ� �����ϴ�");
				txtSNo.setText("");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			} else {
				for(StudentSwingDto s:student) {
					txtPool.append(s.toString()+"\n");
				}
				txtSNo.setText("");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			}
		} else if(e.getSource()==btnExpel) {//update expel
			String snoStr = txtSNo.getText().trim();
			int result = dao.updateExpel(snoStr);
			if(result==StudentSwingDao.SUCCESS) {
				txtPool.setText(snoStr+" �л� ���� ó�� �Ϸ�");
			}else {
				txtPool.setText("��ȿ���� ���� �й��Դϴ�");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
				return;
			}
		} else if(e.getSource()==btnExit) {
			setVisible(false);
			dispose();
			System.exit(0);
		}
	}
	
	public static void main(String[] args) {
		new SwingStudentMng("�л����");
	}

}
