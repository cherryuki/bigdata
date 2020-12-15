package com.lec.ex01_string;
//20-12-14_API(String)		ⓒcherryuki(ji)

/*이름, 전화번호, 생일(12-14)
*print(): [이름]홍길동 [전화]010-0000-0000 [생일]12-14
*Ex05_searchFriend 참고
*/
public class Friend {
	private String name;
	private String tel;
	private String birth;
	public Friend() {}
	public Friend(String name, String tel, String birth) {
		this.name=name;
		this.tel=tel;
		this.birth=birth;
	}
	public void print() {
		System.out.printf("[이름]%s [전화]$s [생일]%s\n", name, tel, birth);
	}
	@Override
	public String toString() {
		return "[이름]"+name+" [전화]"+tel+" [생일]"+birth;
	}
	public String getName() {
		return name;
	}
	public String getTel() {
		return tel;
	}
	public String getBirth() {
		return birth;
	}
}
