#include<iostream>
using namespace std;
class student {
	string name;  
	public:
		int age;
		bool gender;
	
	student(string s,bool b,int a)  {
		name = s;
		age = a;
		gender = b;
	}//constructer (it should be inside class )
	
	void printinfo()  {
		cout << age << endl;
		cout << gender << endl;
		cout << name << endl;
	}

};
int main()  {
	
	student a("gopi",0,21);
	a.printinfo();
   

	return 0;
}

