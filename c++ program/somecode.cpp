// int - 4bytes
// char - 1 byte
// float - 4byte
// bool - 1byte 
// double - 8 bytes 

// #include<iostream>
// using namespace std;
// int main()  {
//   char a = 'd';
//   char b = 'G';
//   if(a >= 'a' && a<= 'z'){
//     cout << "its in lower case";
//   }
//   else {
//     cout << "upper case";
//   }
//   cout << "\n";
//   if(b >= 65 && b<= 90){
//     cout << "its in upper case";
//   }
//   else {
//     cout << "lower case";
//   }

//   return 0;
// }


// #include <iostream>
// using namespace std;
// int main() {
//     cout << "hi" <<"\n";
//     cout << "ho" << endl;
//     int x=5,y=2;
//     cout << (float)x/y <<endl;
//     cout << x/y << endl;
//     cout <<x++ <<endl;
//     cout << x << endl;
//     cout << ++y << endl;
//     cout << y << endl;

//     return 0;
// }

    //modulus functions
    //  a%b = a(if a<b);
    //  a%(-b) =a%b;
    //  (-a)%b= -(a%b);

    // ex:
    // 2%7 = 2;
    // 2%-7 =2%7 = 2;
    // -2%7 =-2

      
// Sample Input
// 3 12345678912345 a 334.23 14049.30493
// Sample Output
// 3
// 12345678912345
// a
// 334.230
// 14049.304930000

// int main() {
//     int a;
//     long b;
//     char c;
//     float d;
//     double e;
//     cin >> a >> b >>c >>d >> e;
//     printf("%d\n",a);
//     printf("%ld\n",b);
//     printf("%c\n",c);
//     printf("%.3f\n",d);
//     printf("%.9lf",e);   
//     return 0;
// }

//variables should start with alphabet,_ or $;
//secial characters are not allowed between variables

//#include<iostream>
//using namespace std;
//int main()  {
//	char arr[100] = "hello";
//	int i;
//	while(arr[i]!='\0')  {  //\0 is null charcter
//		cout << arr[i]<< endl;
//		i++;
//	}
//	return 0;
//}


//shift operator
// #include <iostream>
// using namespace std ;
// int main()   {
// 	int a = 1003;
// 	int c = a << 1; 
// 	cout << c << endl;
// 	return 0;
// a<<n   is a*2^n  left shift operator by n digits 
//a>>n  is a/2^n     right shift operator  by...........
 
// }


//Armstrong number:
//	example ;  153  = 1^3+5^3+3^3
//	if its not then its not an armstrong number;

// armstrong number
// #include<iostream>
// #include<math.h> //not import 
// using namespace std;
// int main()  {
// 	int n;
// 	cin >> n;
// 	int original = n; //because we have done so many operations on n
// 	int sum =0;
// 	while (n>0)  {
// 		int lastdigit = n%10;
// 		sum = sum + pow(lastdigit,3);
// 		n=n/10;
// 	}
// 	if(sum == original)  {
// 		cout << "armstrong";
// 	}
// 	else {
// 		cout << "not armstrong";
// 	}
// 	return 0;
// }


//continue statement examle
// #include <iostream>
// using namespace std ;
// int main()   {
// 	int i;
// 	for (i=0;i<100;i++)   {
// 		if (i%3 ==0) {
// 			continue;
// 		}
// 		cout << i << "\n" << endl;
// 	}
// 	return 0;
// }

//reverse a number
// #include<iostream>
// using namespace std;
// int main()  {
// 	int n;
// 	cin >> n;
// 	int reverse = 0;
// 	while (n>0)  {
// 		int lastdigit = n%10;
// 		reverse = reverse*10 + lastdigit;
// 		n= n/10;
		
// 	}
// 	cout << reverse;
// 	return 0;
	  
// }
	

// #include<iostream>
// using namespace std;
// int main()  {
// 	int k;
// 	char arr[100];
// 	int i;
// 	cin >> k;
// 	for(i=0;i<k;i++) {
// 		cin >> arr[i];
// 	}
// 	int s=0;
// 	for(i=0;i<=k/2;i++) {
// 		if(arr[i] != arr[k-1-i]){
// 			s++;
// 		}
// 	}
// 	if(s>0) { 
// 		cout << "not paindrome!";
		
// 	}
// 	else {
// 		cout << "palindrome";
// 	}
// 	return 0;
// }


// binary to decimal
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


// #include <iostream>
// using namespace std;
// int main() {
//     int n;
//     cin >>n;
//     while(n>0)  {
//         int k = n%8;
//         n=n/8;
//         cout << k;

//     }
    
//     return 0;
// }

 
//INCREMENT AND  DECREMENT

//#include <iostream>
//using namespace std ;
//int main()   {
//	int a = 10;
//	int b,c;
//	b = ++a;
//	cout << b  << endl;
//	return 0;
//}  output:11

//#include <iostream>
//using namespace std ;
//int main()   {
//	int a = 10;
//	int b;
//	b = a++;
//	cout << b << endl;
//	return 0;
//}  output:10

// #include <iostream>
// using namespace std ;
// int main()   {
// 	int i = 10;
// 	int j =20;
// 	int k;
// 	k = i-- - i++ + --j - ++j + --i - j-- + ++i - j++ + j++;
// //      10  - 9   + 19  - 20  + 9   - 20  + 10  - 19 + 20;
//     cout << i << endl;
//     cout << j << endl;
// 	cout << k << endl;
	
// 	return 0;
// }

//switch case
// #include <iostream>
// using namespace std ;
// int main()   {
// 	int n1,n2;
// 	char sa;
// 	cin >> n1;
// 	cin >> n2;
// 	cin >> sa;

   //In switch case break is important  , if you didnt keep break to a particular case , if that case runned and the cases below it also will run
   //and default case also write surely
	
// 	switch(sa)   {
// 		case'+':
// 			cout << n1+n2;
// 			break;
// 		case'-':
// 			cout << n1-n2;
// 			break;
// 		default:
// 			cout << "dont know";
// 			break;
// 	}
	
// 	return 0;
// }


// while  case

//unlimited while
// #include <iostream>
// using namespace std ;
// int main()   {
// 	int n; 
// 	cin >> n;
// 	while (n>0)  {
// 		cout << n;
// 		cin >> n;
// 	}
// 	return 0;
// }

//do while
// #include <iostream>
// using namespace std ;
// int main()   {
// 	int n; 
// 	cin >> n;
// 	do {
// 		cout << n ;
// 		cin >> n;
// 	}
// 	while (n>0)  ;
// 	return 0;
// }

//prime 
// #include <iostream>
// using namespace std ;
// int main()   {
// 	int i,n;
// 	cin >> n;
// 	for (i=2;i<n;i++)   {
// 		if (n%i == 0)  {
// 			cout << "its not a prime"<< endl;
// 			break;
// 		}
//     } 
//     if (i==n)  {
//     	cout << "prime";
// 	}
  	
	
// 	return 0;
// }
		
