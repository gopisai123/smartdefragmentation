//#include<iostream>
//using namespace std;
//class num {
//	public:
//		int a;
//		int b;
//};
//void add() {
//	cin >> a;
//	cin >> b;
//	cout << a+b << endl;
//}
//	class B:public num{
//		
//	};
//int main()  {
//	B b;
//	b.add();
//	return 0;
//}  (incorrect )



//#include<iostream>
//using namespace std;
//
//class num {
//public:
//    int a;
//    int b;
//};
//
//class B : public num {
//public:
//    void add() {
//        cin >> a;
//        cin >> b;
//        cout << "Sum: " << a + b << endl;
//    }
//};
//
//int main()  {
//    B b;
//    b.add();
//    return 0;
//}



#include<iostream>
using namespace std;
class shape {
	public :
		int l;
	    int b;
    	int r;	
};
class rect : public shape{
	public:
		
		void getarea()  {
		    cin >> l ;
		    cin >> b ;
			cout << l*b << endl;
		}
};
class circle : public shape {
	public:
		void getarea()  {
		    cin >> r ;
			cout << 3.14*r*r << endl;
		}
};
int main()  {
	rect q;
	q.getarea();
	circle c;
	c.getarea();
	return 0;
}

