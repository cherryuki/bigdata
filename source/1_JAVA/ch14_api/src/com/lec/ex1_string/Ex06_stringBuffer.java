package com.lec.ex1_string;
//20-12-14_API(StringBuffer, StringBuilder)		ⓒcherryuki(ji)

//문자열 변경이 빈번히 일어날 경우 String이 아닌 StringBuffer나 StringBuilder가 적합함
public class Ex06_stringBuffer {
	public static void main(String[] args) {
		String str = new String("abc");
		StringBuilder strBu = new StringBuilder("abc");
		System.out.println("1. "+strBu);
		strBu.append("def"); //abcdef
		System.out.println("2. "+strBu);
		strBu.insert(3,  "XXX"); //3번 인덱스에 "XXX"추가: abcXXXdef
		System.out.println("3. "+strBu);
		strBu.delete(3,6); //3번 인덱스부터 6번 앞까지 삭제(3~5): abcdef
		System.out.println("4. "+strBu);
		int capacitySize = strBu.capacity(); //가용 크기
		System.out.println("가용크기: "+capacitySize);
		System.out.println("현 strBu의 해시코드: "+strBu.hashCode());
		strBu.append("123456789101112131415");
		capacitySize = strBu.capacity();
		System.out.println("가용크기 변경 후: "+capacitySize);
		System.out.println("변경 후 strBu의 해시코드: "+strBu.hashCode());
		strBu.ensureCapacity(1000);//가용크기를 인위적으로 키우기
		capacitySize = strBu.capacity();
		System.out.println("가용크기 변경: "+capacitySize);
		System.out.println("변경 후 strBu의 해시코드: "+strBu.hashCode());
	}
}
