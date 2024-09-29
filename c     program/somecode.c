#include<stdio.h>
int main() {
    int n;
    scanf("%d",&n);
    int i;
    int j;
    int arr[n];
    for(i=0;i<n;i++)  {
        scanf("%d",&arr[i]);
    }
    int high=0;
    int t;
    int final = arr[0];
    for(i=0;i<n;i++) {
        int k=0;
        for(j=i+1;j<n;j++) {
            if(arr[i]==arr[j]) {
                k++;
                for(t=j;t<n-1;t++) {
                    arr[t] = arr[t+1];
                }
                n--;
                j--;
            }
        }
        if(k>high) {
            high =k;
            final = arr[i];
        }
    }
    printf("%d",final);
    return 0;
}