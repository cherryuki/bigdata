package com.lec.ex03_set;
//20-12-17_Collection		ⓒcherryuki(ji)

import java.util.HashSet;
import java.util.Iterator;

public class Ex03_StudentSet {
	public static void main(String[] args) {
		HashSet<Student> student = new HashSet<Student>();
		Student s = new Student("유지수", 4);
		student.add(s);
		student.add(s); //중복X
		System.out.println(student);
		student.add(new Student("유체리", 4));
		student.add(new Student("김도진", 6));
		student.add(new Student("김도진", 6));
		System.out.println(student);
		Iterator<Student> iterator = student.iterator();
		while(iterator.hasNext()) {
			System.out.println(iterator.next());
		}
		
	}
}
