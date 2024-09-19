#include<iostream>
using namespace std;
class A{
	public:
		void func()  {
			cout << "hi frnds";
		}
};
class B : public A{  //func() is inherited from class A to class B
};
int main()  {
	B b;
	b.func();
	return 0;
}
