package com.lec.supermarket;
//21-01-12_JDBC_Dao&Dto_GUI		(c)cherryuki(ji)
public class SupermarketDto {
	private String id; 		//���̵�
	private String tel; 	//��ȭ��ȣ
	private String name;	//�̸�
	private int point;		//����Ʈ
	private int amount;		//���� ���űݾ�
	private String level;	//�� ���
	private int forlevelup;	//�������� ���� �ʿ��� ���űݾ�
	public SupermarketDto(String id, String tel, String name, int point, int amount, String level, int forlevelup) {
		super();
		this.id = id;
		this.tel = tel;
		this.name = name;
		this.point = point;
		this.amount = amount;
		this.level = level;
		this.forlevelup = forlevelup;
	}
	@Override
	public String toString() {
		return id+"\t"+tel+"\t  "+name+"\t"+point+"\t"+amount+"\t"+level+"\t"+forlevelup;
	}
	//getter&setter
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getTel() {
		return tel;
	}
	public void setTel(String tel) {
		this.tel = tel;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getPoint() {
		return point;
	}
	public void setPoint(int point) {
		this.point = point;
	}
	public int getAmount() {
		return amount;
	}
	public void setAmount(int amount) {
		this.amount = amount;
	}
	public String getLevel() {
		return level;
	}
	public void setLevel(String level) {
		this.level = level;
	}
	public int getForlevelup() {
		return forlevelup;
	}
	public void setForlevelup(int forlevelup) {
		this.forlevelup = forlevelup;
	}
	
}
