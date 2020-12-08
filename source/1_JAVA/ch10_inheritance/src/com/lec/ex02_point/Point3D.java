package com.lec.ex02_point;
//20-12-07_inheritance ⓒcherryuki(ji)
public class Point3D extends Point {
	private int z;
	public void point3dPrint() {
		System.out.printf("3차원 좌표: %d, %d, %d\n", getX(), getY(), z);
	}
	public String point3DInfoString() {
		return "3차원 좌표: "+getX()+", "+getY()+", "+z;
	}
	public int getZ() {
		return z;
	}
	public void setZ(int z) {
		this.z = z;
	}
	
}
