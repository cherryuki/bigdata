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
		btnCIdSearch = new JButton("아이디 검색");
		btnCTelSearch = new JButton("폰4자리(FULL) 검색");
		btnCNameSearch = new JButton("고객 이름 검색");
		btnBuyWithPoint = new JButton("포인트로만 구매");
		jpup.add(new JLabel(" 아 이 디 ",(int) CENTER_ALIGNMENT));
		jpup.add(txtCId);
		jpup.add(btnCIdSearch);
		jpup.add(new JLabel("고 객 전 화",(int) CENTER_ALIGNMENT));
		jpup.add(txtCTel);
		jpup.add(btnCTelSearch);
		jpup.add(new JLabel("고 객 이 름",(int) CENTER_ALIGNMENT));
		jpup.add(txtCName);
		jpup.add(btnCNameSearch);
		jpup.add(new JLabel("포  인  트",(int) CENTER_ALIGNMENT));
		jpup.add(txtCPoint);
		jpup.add(btnBuyWithPoint);
		jpup.add(new JLabel("구 매 금 액",(int) CENTER_ALIGNMENT));
		jpup.add(txtCAmount);
		jpup.add(new JLabel(""));//빈 라벨 추가하는 부분
		jpup.add(new JLabel("고 객 등 급",(int) CENTER_ALIGNMENT));
		jpup.add(comLevelName);
		btnBuy = new JButton("물품 구매");
		btnLevelNameOutput = new JButton("등급별출력");
		btnAllOutput = new JButton("전체출력");
		btnInsert = new JButton("회원가입");
		btnCTelUpdate = new JButton("번호수정");
		btnDelete = new JButton("회원탈퇴");
		btnExit = new JButton("나가기");
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
		txtPool.setText("\t★ ★ ★ 고객검색 후 구매하세요 ★ ★ ★");
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
				txtPool.setText("유효한 고객 아이디를 입력 후 아이디 검색해주세요");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				return;
			}
			dto = dao.searchId(id);
			txtPool.setText("ID\t전화\t  이름\t포인트\t누적 구매액\t고객 등급\t레벨업을 위한 추가 구매 금액\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(dto!=null) {
				txtCTel.setText(dto.getTel());
				txtCName.setText(dto.getName());
				txtCPoint.setText(dto.getPoint()+"");
				txtCAmount.setText("");
				comLevelName.setSelectedItem(dto.getLevel());
				txtPool.append(dto.toString());
			} else {
				txtPool.setText("존재하지 않은 ID입니다");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
			}
		} else if(e.getSource()==btnCTelSearch) {//2
			String postTel = txtCTel.getText().trim();
			if(postTel.length()<4) {
				txtPool.setText("전화번호 뒷 4자리를 입력하세요");
				txtCId.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				return;
			}
			
			customer = dao.searchTel(postTel);
			txtPool.setText("ID\t전화\t  이름\t포인트\t누적 구매액\t고객 등급\t레벨업을 위한 추가 구매 금액\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(customer.isEmpty()) {
				txtPool.setText("해당 전화번호의 회원이 없습니다");
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
				txtPool.setText("이름을 입력 후 이름 검색해 주세요");
				txtCId.setText("");
				txtCTel.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				return;
			} 
			customer = dao.searchName(name);
			txtPool.setText("ID\t전화\t  이름\t포인트\t누적 구매액\t고객 등급\t레벨업을 위한 추가 구매 금액\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(customer.isEmpty()) {
				txtPool.setText("해당 이름의 고객이 검색되지 않습니다. 회원가입을 진행해주세요");
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
				txtPool.setText("포인트가 부족하여 포인트로만 구매는 불가능합니다");
				return;
			} else {
				int result = dao.updatePoint(id, price);
				if(result==SupermarketDao.SUCCESS) {
					txtPool.setText("포인트로만 구매 성공");
					txtCPoint.setText((point-price)+"");
					txtCAmount.setText("");
				} else {
					txtPool.setText("포인트로만 구매 실패 관리자에게 문의하세요");
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
				txtPool.setText("물품 구매 및 포인트 조정 성공(레벨 확인 완료)");
			}
		} else if(e.getSource()==btnLevelNameOutput) {//6
			String level = comLevelName.getSelectedItem().toString().trim();
			if(level.equals("")) {
				txtPool.setText("고객 등급을 선택 후 등급별 출력 버튼을 클릭하세요");
				txtCId.setText("");
				txtCTel.setText("");
				txtCName.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				return;
			}
			customer = dao.selectLevel(level);
			txtPool.setText("ID\t전화\t  이름\t포인트\t누적 구매액\t고객 등급\t레벨업을 위한 추가 구매 금액\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(customer.isEmpty()) {
				txtPool.setText("현재 해당 등급에는 고객이 없습니다");
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
				txtPool.append("총 "+customer.size()+"명");
			}
		} else if(e.getSource()==btnAllOutput) {//7
			customer = dao.selectAll();
			txtPool.setText("ID\t전화\t  이름\t포인트\t누적 구매액\t고객 등급\t레벨업을 위한 추가 구매 금액\n"
					+ "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
			if(customer.isEmpty()) {
				txtPool.setText("현재 조회가능한 고객이 없습니다");
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
				txtPool.append("총 "+customer.size()+"명");
			}
		} else if(e.getSource()==btnInsert) {//8
			String tel = txtCTel.getText().trim();
			String name = txtCName.getText().trim();
			if(tel.equals("")||name.equals("")) {
				txtPool.setText("전화번호와 고객명은 필수 입력사항입니다");
				txtCId.setText("");
				txtCTel.setText("");
				txtCPoint.setText("");
				txtCAmount.setText("");
				comLevelName.setSelectedIndex(0);
				return;
			} 
			int result = dao.insertCustomer(tel, name);
			if(result==SupermarketDao.SUCCESS) {
				txtPool.setText("회원가입 감사합니다. 포인트 1000점을 회원가입 선물로 적립하였습니다");
				txtCPoint.setText("1000");
				comLevelName.setSelectedIndex(1);
			}
		} else if(e.getSource()==btnCTelUpdate) {//9
			String id = txtCId.getText().trim();
			String tel = txtCTel.getText().trim();
			if(id.equals("")||tel.equals("")) {
				txtPool.setText("유효한 고객ID를 검색 후 번호 변경을 진행하시기 바랍니다");
				return;
			}
			int result = dao.updateCustomer(tel, id);
			if(result==SupermarketDao.SUCCESS) {
				txtPool.setText("전화번호가 수정되었습니다");
			}
		} else if(e.getSource()==btnDelete) {//10
			String tel = txtCTel.getText().trim();
			if(tel.length()==0) {
				txtPool.setText("전화번호가 있어야 회원탈퇴가 가능합니다\n전화번호 확인 후 회원 탈퇴를 진행하시기 바랍니다");
				return;
			}
			int result = dao.deleteCustomer(tel);
			if(result==SupermarketDao.SUCCESS) {
				txtPool.setText(tel+"님의 회원 탈퇴가 완료되었습니다");
			}
		} else if(e.getSource()==btnExit) {
			setVisible(false);
			dispose();
			System.exit(0);
		}
		
	}
	public static void main(String[] args) {
		new SwingSupermarket("슈퍼마켓 관리");
	}
}
