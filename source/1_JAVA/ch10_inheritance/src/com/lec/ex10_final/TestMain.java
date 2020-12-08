package com.lec.ex10_final;
//20-12-08_final	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		Animal animal = new Animal();
		animal.running();
		animal.running();
		animal.stop();
		animal.running();
		Dog dog = new Dog();
		dog.running();
		dog.stop();
		dog.method(); //가능
		Animal dog2 = new Dog();
		dog2.running();
		dog2.stop();
		//dog2.method();//불가능
		Rabbit rabbit = new Rabbit();
		rabbit.running();
		rabbit.stop();
	}
}
