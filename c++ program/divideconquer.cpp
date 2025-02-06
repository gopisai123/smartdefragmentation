// #include<iostream>
// using namespace std;
// int max(int arr[],int i,int j) {
//     if(i==j)  {
//         return arr[i];
//     }
//     else if(j == i-1)  {
//         if(arr[i]>arr[j]) {
//             return arr[i];
//         }
//         else {
//             return arr[j];
//         }
//     }
//     else {
//         int mid = (i+j)/2;
//         int max1 = max(arr,i,mid);
//         int max2 = max(arr,mid+1,j);
//         if(max1>max2) {
//             return max1;
//         }
//         else {
//             return max2;
//         }

//     }
// }
// int main() {
//     int arr[]  = { 1,333,43,566,89,43};
//     int k = max(arr,0,5);
//     cout << k;
//     return 0;
// }

#include<iostream>
#include<climits>
#include<float.h>  // For FLT_MIN and FLT_MAX

using namespace std;

float max_value = -FLT_MAX, min_value = FLT_MAX;  // Initialize to extreme float values

float hi(float arr[], int i, int j) {
    if (i == j) {
        // Base case: only one element
        max_value = min_value = arr[i];
    } else if (j == i + 1) {  // Adjacent elements
        if (arr[i] > arr[j]) {
            max_value = arr[i];
            min_value = arr[j];
        } else {
            max_value = arr[j];
            min_value = arr[i];
        }
    } else {
        int mid = (i + j) / 2;
        hi(arr, i, mid);    // Recursive call for the left half
        float max1 = max_value, min1 = min_value;
        hi(arr, mid + 1, j); // Recursive call for the right half
        
        // Merge the results
        if (max1 > max_value) {
            max_value = max1;
        }
        if (min1 < min_value) {
            min_value = min1;
        }
    }
    return max_value - min_value;
}

int main() {
    int n;
    cin >> n;  // Input size of the array
    float arr[n];  // Array to store float values
    
    // Input elements of the array
    for (int h = 0; h < n; h++) {
        cin >> arr[h];  // Input float elements
    }
    
    // Find the maximum difference
    float result = hi(arr, 0, n - 1);
    
    // Output the result
    cout << result;  
    return 0;
}
