//#include<iostream>
//#include<string>
//using namespace std;
//int main()  {
//	string s(5,'g');
//
//	cout << s;
//	return 0;
//}



//#include<iostream>
//#include<string>
//using namespace std;
//int main()  {
//	string s;
//	cin >> s;  //if input is hi frnds
//	cout << s; //output is hi . only outpouts till space
//	return 0;
//}


 //now problem solved
//#include<iostream>
//#include<string>
//using namespace std;
//int main()  {
//	string s;
//	getline(cin,s);
//	cout << s;
//	return 0;
//}


         //append
//#include<iostream>
//#include<string>
//using namespace std;
//int main()  {
//	string s1 ="fam";
//	string s2 ="ily";
//	cout << s1.append(s2) << endl;  //or s1+s2 directly
//	cout << s1[2]; // access
//	return 0;
//}

//#include<iostream>
//#include<string>
//using namespace std;
//int main()  {
//	string s1 = "abc";
//	string s2 = "xyz";
//	cout << s1.compare(s2)  << endl;
//	return 0;
//}


#include<iostream>
using namespace std;
int factorial(int n)  {
	if(n==0)  {
		return 1;
	}
	return n* factorial(n-1);
}
int main() {
	int n;
	cin >> n;
	int s = factorial(n);
	cout << s  << endl;
	
	return 0;
}










