package com.lec.ex02_point;
//20-12-07_inheritance ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		Point point = new Point();
		point.setX(5);
		point.setY(6);
		point.pointPrint();
		System.out.println(point.pointInfoString());
		Point3D point3d = new Point3D();
		point3d.setX(10);
		point3d.setY(20);
		point3d.setZ(25);
		System.out.println(point3d.point3DInfoString());
		point3d.point3dPrint();
		//point3d.pointPrint(); //상속 받았으나 사용하지 않음
	}
}
