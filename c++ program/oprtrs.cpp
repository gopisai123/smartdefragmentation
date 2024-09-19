#include <iostream>
using namespace std ;
int main() {
	int a = 12;
	int b = 10;
	int c = a>b ? a+b : a-b;//ternary / conditional operator
	cout << c <<endl;
	char ch = 'a';
	cout << int(ch)<<endl;// cast operator (converts data type)
	int s;
	s = sizeof(a);
	cout << s;
	return 0;
}
