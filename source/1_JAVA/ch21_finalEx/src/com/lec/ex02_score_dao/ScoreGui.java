package com.lec.ex02_score_dao;
//21-01-08_JDBC_Dao&Dto		(c)cherryuki(ji)

import java.awt.Container;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Vector;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

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
		setDefaultCloseOperation(EXIT_ON_CLOSE); //x버튼 누르면 종료
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
		btnInput = new JButton("입력", icon1);
		ImageIcon icon2 = new ImageIcon("icon/hot.gif");
		btnSearch = new JButton("직업 조회", icon2);
		btnOutput = new JButton("전체 조회");
		btnExit = new JButton("종료");
		txtPool = new JTextArea(10,60);
		scrollPane = new JScrollPane(txtPool); //스크롤바가 필드 감싸야함
		jpup.add(new JLabel("이름", (int)CENTER_ALIGNMENT));
		jpup.add(txtName);
		jpup.add(new JLabel("직업", (int)CENTER_ALIGNMENT));
		jpup.add(comJob);
		jpup.add(new JLabel("국어", (int)CENTER_ALIGNMENT));
		jpup.add(txtKor);
		jpup.add(new JLabel("영어", (int)CENTER_ALIGNMENT));
		jpup.add(txtEng);
		jpup.add(new JLabel("수학", (int)CENTER_ALIGNMENT));
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
		if(e.getSource()==btnInput) {//이름, 직업, 국영수 점수 입력받아 dao.insert 호출
			String name = txtName.getText().trim();
			String jname = comJob.getSelectedItem().toString().trim();
			String korStr = txtKor.getText().trim();
			String engStr = txtEng.getText().trim();
			String matStr = txtMat.getText().trim();
			if(name.equals("")||jname.equals("")||korStr.equals("")||engStr.equals("")||matStr.equals("")) {
				txtPool.setText("이름, 직업, 국/영/수 점수를 입력하셔야 추가할 수 있습니다");
				return;
			}
			int kor = Integer.parseInt(korStr);
			int eng = Integer.parseInt(engStr);
			int mat = Integer.parseInt(matStr);
			ScoreDto newPerson = new ScoreDto(name, jname, kor, eng, mat);
			int result = dao.insertScore(newPerson);
			if(result==ScoreDao.SUCCESS) {
				txtPool.setText(result+"행 추가하였습니다");
				txtName.setText("");
				comJob.setSelectedIndex(0); //콤보박스 0번째 선택
				txtKor.setText("");
				txtEng.setText("");
				txtMat.setText("");
			}
		} else if(e.getSource()==btnSearch) {//직업별 조회 dao.selectJname 호출
			String jname = comJob.getSelectedItem().toString().trim();
			if(jname.equals("")) {
				txtPool.setText("직업을 선택하신 후 조회바랍니다");
				return;
			}
			dto = dao.selectJname(jname);
			txtPool.setText("등수\t이름\t\t직업\t국어\t영어\t수학\t총점\n");
			if(dto.isEmpty()) {
				txtPool.setText(txtPool.getText()+"조회 가능한 인원이 없습니다"); 
				//txtPool.getText()를 입력해야 이전에 입력한 사항(ex: 테이블 필드명) 같이 출력
			} else {
				for(ScoreDto d:dto) {
					txtPool.append(d.toString()+"\n");
				}
			}
			
		} else if(e.getSource()==btnOutput) {
			dto = dao.selectAll();
			txtPool.setText("등수\t이름\t\t직업\t국어\t영어\t수학\t총점\n");
			if(dto.isEmpty()) {
				txtPool.setText(txtPool.getText()+"조회 가능한 인원이 없습니다"); 
				//txtPool.getText()를 입력해야 이전에 입력한 사항(ex: 테이블 필드명) 같이 출력
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
		new ScoreGui("연예인 성적 관리");
	}
}
