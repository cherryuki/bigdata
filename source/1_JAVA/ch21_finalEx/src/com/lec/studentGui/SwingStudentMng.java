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
		btnSNoSearch = new JButton("학번검색");
		btnSNameSearch = new JButton("이름검색");
		btnMNameSearch = new JButton("전공검색");
		//jpbtn
		btnInput = new JButton("학생입력");
		btnUpdate = new JButton("학생수정");
		btnStudentOut = new JButton("학생출력");
		btnExpelOut = new JButton("제적자출력");
		btnExpel = new JButton("제적처리");
		btnExit = new JButton("종료");
		txtPool = new JTextArea(10, 50);
		scrollPane = new JScrollPane(txtPool);
		jpup.add(new JLabel("학번", (int)CENTER_ALIGNMENT));
		jpup.add(txtSNo);
		jpup.add(btnSNoSearch);
		jpup.add(new JLabel("이름", (int)CENTER_ALIGNMENT));
		jpup.add(txtSName);
		jpup.add(btnSNameSearch);
		jpup.add(new JLabel("전공", (int)CENTER_ALIGNMENT));
		jpup.add(comMname);
		jpup.add(btnMNameSearch);
		jpup.add(new JLabel("점수", (int)CENTER_ALIGNMENT));
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
				txtPool.setText("학번을 입력후 학번검색 버튼을 눌러주세요");
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
				txtPool.setText(sno+"은 유효하지 않은 학번입니다");
			}
		} else if(e.getSource()==btnSNameSearch) {//select sname
			String sname = txtSName.getText().trim();
			if(sname.equals("")) {
				txtPool.setText("이름을 입력후 이름검색 버튼을 눌러주세요");
				return;
			}
			student = dao.selectSname(sname);
			if(student.size()==0) {
				txtPool.setText("해당 이름의 학생이 없습니다");
				txtSNo.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			} else if(student.size()==1) {
				txtSNo.setText(student.get(0).getSno()+"");
				comMname.setSelectedItem(student.get(0).getMajor());
				txtScore.setText(student.get(0).getScore()+"");
				txtPool.setText("");
			} else {//동명이인 있을 경우
				txtPool.setText("\t학번\t이름\t학과명\t점수\n"
						+ "---------------------------------------------------------\n");
				for(StudentSwingDto s:student) {
					txtPool.append(s.toString()+"\n");
				}//0방까지 있으면 size()=1, 마지막 인덱스 = student.size()-1
				txtSNo.setText(student.get(student.size()-1).getSno()+"");
				comMname.setSelectedItem(student.get(student.size()-1).getMajor());
				txtScore.setText(student.get(student.size()-1).getScore()+"");
			}
			
		} else if(e.getSource()==btnMNameSearch) {//select mname
			String mname = comMname.getSelectedItem().toString().trim();
			if(mname.equals("")) {
				txtPool.setText("전공을 선택 후 전공검색 버튼을 눌러주세요");
				return;
			}
			student = dao.selectMname(mname);
			txtPool.setText("   등수\t이름(학번)\t\t학과명(학과번호)\t점수\n"
					+ " -------------------------------------------------------------------------------------------------------------------------\n");
			if(student.isEmpty()) {
				txtPool.setText(txtPool.getText()+"해당 학과에는 학생이 없습니다");
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
				txtPool.setText("이름과 전공인 필수 입력 항목입니다(점수 미입력시 0점)");
				return;
			}
			if(scoreStr.length()==0) {
				scoreStr = 0+"";
			} else {
				int score = Integer.parseInt(scoreStr);
			}
			if(Integer.parseInt(scoreStr)<0||Integer.parseInt(scoreStr)>100) {
					txtPool.setText("유효하지 않은 점수입니다\n점수는 0~100사이의 수를 입력해주세요(미입력시 0점)");
				return;
			}
			StudentSwingDto newStudent = new StudentSwingDto(name, major, Integer.parseInt(scoreStr));
			int result = dao.insertStudent(newStudent);
			if(result==StudentSwingDao.SUCCESS) {
				txtPool.setText(name+" 학생 입력 성공");
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
				txtPool.setText("학번, 이름, 전공을 모두 입력하셔야 수정이 가능합니다");
				return;
			} 
			if(scoreStr.length()==0) {
				scoreStr = 0+"";
			} else {
				int score = Integer.parseInt(scoreStr);
			}
			if(Integer.parseInt(scoreStr)<0||Integer.parseInt(scoreStr)>100) {
				txtPool.setText("유효하지 않은 점수입니다\n점수는 0~100사이의 수를 입력해주세요(미입력시:0점)");
			return;
			}
			StudentSwingDto student = new StudentSwingDto(Integer.parseInt(snoStr), name, major, Integer.parseInt(scoreStr));
			int result = dao.updateStudent(student);
			if(result==StudentSwingDao.SUCCESS) {
				txtPool.setText(name+" 학생 입력 수정");
				txtSNo.setText("");
				txtSName.setText("");
				comMname.setSelectedIndex(0);
				txtScore.setText("");
			}
			
		} else if(e.getSource()==btnStudentOut) {//select all
			student = dao.selectAll();
			txtPool.setText("   등수\t이름(학번)\t\t학과명(학과번호)\t점수\n"
					+ " -------------------------------------------------------------------------------------------------------------------------\n");
			if(student.isEmpty()) {
				txtPool.setText(txtPool.getText()+"조회 가능한 학생이 없습니다");
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
			txtPool.setText("  등수\t이름(학번)\t\t학과명(학과번호)\t점수\n"
					+ "-------------------------------------------------------------------------------------------------------------------------\n");
			if(student.isEmpty()) {
				txtPool.setText(txtPool.getText()+"조회 가능한 제적자가 없습니다");
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
				txtPool.setText(snoStr+" 학생 제적 처리 완료");
			}else {
				txtPool.setText("유효하지 않은 학번입니다");
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
		new SwingStudentMng("학사관리");
	}

}
