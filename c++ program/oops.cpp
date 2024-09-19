#include<iostream>
using namespace std;
class student {
	string name;  //by default private, cant be accessed from out side class
	public:
		int age;
		bool gender;
	void setname(string s)  {  //to acess that private member from outside we are using this , in place of setname u can use getname or anything else.....
		name = s;
		
	}
	
	void printinfo()  {
		cout << age << endl;
		cout << gender << endl;
		cout << name << endl;
	}
};
int main()  {
	int i;
	student arr[3];
//	for(i=1;i<=3;i++)  {
//		cin >> arr[i].age;
//		cin >> arr[i].gender;
//		cin >> arr[i].name;
//	}
//dont use above cause array starts from arr[0]; not arr[1],
    for(i=0;i<3;i++)  {
    	string s;
		cin >> arr[i].age;
		cin >> arr[i].gender;
		cin >> s;
		arr[i].setname(s);
	}
	for(i=0;i<3;i++)  {
		arr[i].printinfo();
	}
	return 0;
}
