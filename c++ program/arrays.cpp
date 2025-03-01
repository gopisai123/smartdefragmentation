//#include<iostream>
//using namespace std;
//int main() {
//	int n;
//	int i;
//	int arr[100];
//	cin >> n;
//	for(i=0;i<n;i++)  {
//		cin >> arr[i];
//	}
//	int max = arr[0] ;
//	int min = arr[0];
//	for(i=0;i<n;i++) {
//		if(arr[i]>max)  {
//			max = arr[i];
//		}
//		if(arr[i]<min) {
//			min = arr[i];
//		}
//	}
//	cout << max << endl;
//	cout << min;
//	return 0;
//}


           //Linear search
// #include <iostream>
// using namespace std;
// int lsearch(int arr[],int n,int num) {
// 	int i;
// 	for(i=0;i<n;i++)  {
// 		if(arr[i] == num) {
// 			return num;
// 		}
// 	}
// 	return -1;
	
// }
// int main()  {
// 	int n;
// 	cin >> n;
// 	int arr[n];
// 	for (int i=0;i<n;i++)  {
// 		cin >> arr[i];
// 	}
// 	int num;
// 	cin >> num;
// 	int x = lsearch( arr,n,num);
// 	cout << x << endl;

// 	return 0;
// }

    //binary search useful to reduce time to run
// #include<iostream>
// using namespace std;
// int bsearch(int arr[],int n, int key)  {  
//     int f =0;
//     int s=n;
    
//     while(f<=s)   {
//         int mid = (f+s)/2;
//         if(arr[mid] ==key)  {
//             return mid;
//         }
//         else if(arr[mid]  < key)  {
//             f =mid+1;
//         }
//         else {
//             s =mid-1;
//         }
//     }
//     return -1;

// }
// int main()   {
//     int n;
//     cin >> n;
//     int arr[n]  ;
//     int i;
//     for(i=0;i<n;i++)  {
//         cin >> arr[i];
//     }
//     int key;
//     cin >> key;
//     int r =bsearch(arr,n,key);
//     cout << r;
//     return 0;

// }


//#include<iostream>
//using namespace std;
//int main() {
//	int n;
//	cin >> n;
//	int arr[100];
//	int i;
//	for(i=0;i<n;i++) {
//		cin >> arr[i] ;
//	}
//	int j;
//	int temp;
//	for(i=0;i<n-1;i++) {
//		for(j=i+1;j<n;j++) {
//			if (arr[j]>arr[i] ) {
//				temp = arr[j];
//				arr[j] = arr[i];
//				arr[i] = temp;
//			}
//			
//		}
//	}
//	for(i=0;i<n;i++) {
//		cout << arr[i] << endl;
//	}
//	return 0;
//}

//         Insertion sort once see bro code
// void assc(int n,arr[]) {
//     int i;
//       for(i=1;i<n;i++)  {
//         int current = arr[i];
//         int j=i-1;
//         while(arr[j]>current && j>=0)  {
//             arr[j+1] = arr[j];
//             j--;
//         }
//         arr[j+1] = current;
//     }
// }

// #include<iostream>
// using namespace std;
// int main()  {
//     int n;
//     cin >> n;
//     int i;
//     int arr[n];
//     for(i=0;i<n;i++)  {
//         cin >> arr[i];
//     }
//     for(i=1;i<n;i++)  {
//         int current = arr[i];
//         int j=i-1;
//         while(arr[j]>current && j>=0)  {
//             arr[j+1] = arr[j];
//             j--;
//         }
//         arr[j+1] = current;
//     }
//     for(i=0;i<n;i++)  {
//         cout << arr[i] << " ";
//     }
    
//     return 0;
// }




//bubble sort
//#include<iostream>
//using namespace std;
//int main() {
//	int n;
//	cin >> n;
//	int arr[100];
//	int i;
//	int s;
//	for(i=0;i<n;i++) {
//		cin >> arr[i] ;
//	}
//	int counter =1;
//	while(counter<n)  {
//		for(i=0;i<n-counter;i++)  {
//			if(arr[i]<arr[i+1])  {
//				s = arr[i];
//				arr[i] = arr[i+1];
//				arr[i+1]= s;
//			}
//		}
//		counter ++;
//	}
//	for(i=0;i<n;i++) {
//		cout << arr[i] << endl;
//	}
//	
//	return 0;	
//}


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


//
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




// // You are using GCC
// #include<stdio.h>
// int main() {
    
//     int n;
//     scanf("%d",&n);
//     int arr[100];
//     int i;
//     int j;

//     for(i=0;i<n;i++)  {
//         scanf("%d",&arr[i]);
//     }
//     int flag =1;
//    for(i=0;i<n;i++)  {
//        int k= 1;
//        for(j=0;j<n;j++) {
//            if(i!=j && arr[i]==arr[j])  {
//                k =0;
//                break;
//            }
//        }
//        if (k)  {
//            printf("%d ",arr[i]);
//            flag=0;
//            break;
           
//        }
       
       
//     }
    
//     if(flag) {
//         printf("%d",-1);
//     }
//     return 0;
// }


// removing duplicate
// #include<stdio.h>
// int main()  {
//     int n; 
//     scanf("%d",&n);
//     int i;
//     int j;
//     int h;
//     int arr[n];
//     for(i=0;i<n;i++)  {
//         scanf("%d",&arr[i]);
//     }
//     for(i=0;i<n;i++)  {
//         for(j=i+1;j<n;j++)  {
//             if (arr[i] == arr[j])  {
//                 for(h=j;h<n-1;h++)  {
//                     arr[h] = arr[h+1];
                    
//                 }
//                 n--;
//                 j--;
                
//             }
//         }
//     }
//     for(i=0;i<n;i++)  {
//         printf("%d ",arr[i]);
//     }  
//     return 0;
// }

                                               // VECTORS
// #include<iostream>
// #include<vector>
// using namespace std;
// int main() {
//     vector<int> vec = {1,3};
//     cout << vec[1] << endl;
//     vector<char> vec1 = {'a','b','c'};  
//     for(char i:vec1) { //for each loop
//         cout << i << " ";
//     }
//     cout << endl;
//     cout << "size = " << vec1.size() << endl;
//     vec1.push_back('d');
//     for(char i:vec1) { //for each loop
//         cout << i << " ";
//     }
//     cout << endl;
//     vec1.pop_back();
//     for(char i:vec1) { //for each loop
//         cout << i << " ";
//     }
//     cout << endl;
//     cout << vec1.front() << endl;
//     cout << vec1.back() << endl;
//     cout << vec1.at(2);
//     return 0;
// }


// #include<iostream>
// #include<vector>
// using namespace std;
// int main() {
//     vector <int> vec;
//     vec.push_back(1);
//     vec.push_back(2);
//     vec.push_back(3);
//     cout << vec.size() << " "<< vec.capacity() << endl;
//     vec.push_back(1);
//     vec.push_back(6);
//     cout << vec.size() << " "<< vec.capacity() << endl;
// }

//  n^n =0
//  n^0 = n 
//  n= number , ^ is  xor


// #include <iostream>
// #include <algorithm>

// // Custom comparator for sorting in descending order
// bool compare(int a, int b) {
//     return a > b;  // Return true if a should come before b
// }

// int main() {
//     int arr[] = {5, 3, 8, 1, 2};
//     int n = sizeof(arr) / sizeof(arr[0]);
//     std::sort(arr, arr + n, compare); // Using the custom comparator

//     for (int num : arr) {
//         std::cout << num << " ";
//     }
    
//     return 0;
// }  //similarly for  vector ( see letcode 1710)

// printing all possible subb arrays 
// #include<iostream>
// using namespace std;
// int main() {
//     int arr[] = { 2,3,-2,7,-9,34,-4};
//     int n = sizeof(arr)/sizeof(arr[0]);
//     for(int i=0;i<n;i++) {
//         for(int j=i;j<n;j++) {
//             for(int k=i;k<=j;k++) {
//                 cout << arr[k] << " ";
//             }
//             cout << endl;
//         }
//     }
//     return 0;
// }

// brute force approach
#include<iostream>
using namespace std;
int main() {
    int maxsum = INT16_MIN;
    int arr[] = { 2,3,-2,7,-9,34,-4};
    int n = sizeof(arr)/sizeof(arr[0]);
    for(int i =0;i<n;i++) {
        int cs =0;
        for(int j=i;j<n;j++) {
            cs+=arr[j];
            maxsum= max(cs,maxsum);
        }
    }
    cout<< maxsum;
    return 0;
} // we can also do it with the 3 loops of above problem

// kadanes algoithm in leet code for max sub array
