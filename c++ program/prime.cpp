#include <iostream>
using namespace std ;
int main()   {
	int i,n;
	cin >> n;
	for (i=2;i<n;i++)   {
		if (n%i == 0)  {
			cout << "its not a prime"<< endl;
			break;
		}
    } 
    if (i==n)  {
    	cout << "prime";
	}
  	
	
	return 0;
}
		
