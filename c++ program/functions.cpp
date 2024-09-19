//#include<iostream>
//using namespace std;
//int add(int n1, int n2){  // int in this line is return type
//	int sum = n1+n2;
//	return sum;
//}
//int main(){
//	int n1,n2;
//	cin >> n1 >> n2;
//	cout << add(n1,n2);
//	return 0;
//}
       //or we can do like this
// #include<iostream>
// using namespace std;
// int add(int n1,int n2);
// int main()  {
//     int n1,n2;
//     cin >> n1 >>n2;
//     cout << add(n1,n2);
// }
// int add(int n1,int n2) {
//     return n1+n2;
// }

//#include<iostream>
//using namespace std;
//int main() {
//	int n1,n2;
//	cin >> n1 >> n2;
//	int i;
//	int j;
//	
//	for(i=n1;i<=n2;i++)  {
//		int count =0;
//		for(j=2;j<i;j++) {
//			if(i%j==0) {
//				count++;
//			}
//		}
//		if(count==0) {
//				cout << i << endl;
//		}
//	}
//	
//	return 0;
//}


//prime or not
// #include<iostream>
// #include<math.h>
// using namespace std;
// bool isPrime(int n)  {
// 	for(int i=2;i<=sqrt(n);i++)  {
// 		if(n%i==0)  {
// 			return false ;
// 		}
// 		else {
// 			return true;
// 		}
// 	}
// }
// int main(){
// 	int k;
// 	cin >> k;
// 	if(isPrime(k)) {
// 		cout << "is prime ";
		
// 	}
// 	else {
// 		cout << "not prime";
// 	}
// 	return 0;
// }


//factorial
// #include<iostream>
// using namespace std ;
// int fact(int k) {
// 	int hi =1;
// 	for(int i=2;i<=k;i++) {
// 		hi *= i;
// 	}
// 	return hi;
// }
// int main() {
// 	int k;
// 	cin >> k;
// 	int s = fact(k);
// 	cout << s;
// 	return 0;
// }

// prime  numbers b/w 2 numbers
// #include<iostream>
// #include<math.h>
// using namespace std ;
// bool prime(int a) {
//     for(int i=2;i<=sqrt(a);i++) {
//         if(a%i ==0) {
//             return false;
//         }
//     }
//     return true;

// }
// int main() {
//     int a,b;
//     cin >> a >> b;
//     int i;
//     for (i=a;i<=b;i++) {
//         if(prime(i)) {
//             cout << i << endl;
//         }
//     }
    
//     return 0;
// }


//pscac triangle    
// 1(0c0)
// 1(1c0)  1 (1c1)
// 1(2c0 ) 2(2c1) 1(2c2) 
// 1 3 3 1 
// 1 4 6 4 1
// #include <iostream>
// using namespace std;
//  int fact(int s)  {
//     int factorial =1;
//     for(int i=2;i<=s;i++)  {
//         factorial *= i;
//     }
//     return factorial;
//  }

//  int main  () {
//     int k;
//     cin >> k;4
//     int i,j;
//     for (i=0;i<k;i++) {
//         for(j=0;j<=i;j++) {
//             cout << fact(i)/(fact(j)*fact(i-j)) << " " ;

//         }
//         cout << endl;
//     }
//     return 0;
//  }

// int sum(int s) { 
//     int m =0;
//     int i;
//     for(i=1;i<=s;i++) {
//        m+=i;
//     }
//     return m;
// }
// #include <iostream>
// using namespace std;
// int main() {
//     int l;
//     cin >> l;
//     cout << sum(l) << endl;
//     return 0;
// }

//pythagoran triplet
// #include <iostream>
// #include<algorithm>
// using namespace std;

// bool trip(int a, int b, int c) {
//     int x,y,z;
//     x = max(a,max(b,c));
//     if (x==a)  {
//         y =b;
//         z=c;
//     }
//     else if (x==b)  {
//         y=a;
//         z=c;
//     }
//     else{
//         y=a;
//         z=b;
//     }
//     if (x*x == y*y+z*z)  {
//         return true;
//     }
//     else {
//         return false;
//     }
// }

// int main()  {
//     int a,b,c;
//     cin >>a >> b >>c ;
//     if (trip(a,b,c)) {
//         cout << "pythagorous triplet";
//     }
//     else {
//         cout << "its not pythagarous triplet ";
//     }
//     return 0;
// }

// decimal to binary
// #include <iostream>
// using namespace std;
// int main() {
//     int n;
//     cin >>n;
//     int binary =0;
    
//     while(n>0)  {
//         int k = n%2;
//         n=n/2;
//         cout << k;

//     }
    
//     return 0;
// }






