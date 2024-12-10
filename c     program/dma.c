// Dynamic Memory Allocation

// It is a way to allocate memory to a data structure during
// the runtime.

// # include <stdio.h>
// # include <stdlib.h>  //for dma
// //Dynamic Memory Allocation
// int main() {
//     //sizeof function
//     printf("%d\n", sizeof(int));
//     printf("%d\n", sizeof(float));
//     printf("%d\n", sizeof(char));

//     // malloc(): takes number of bytes to be allocated
//     // & returns a pointer of type void
//     int *ptr;
//     ptr = (int*)malloc(5 * sizeof(int)); // for 5 integers
//     //we can use as arrays
//     ptr[0] = 1;
//     ptr[1] = 1;
//     ptr[3] = 4;
//     ptr[4] = 6;
//     ptr[5] = 9;
//     for(int i=0;i<5;i++) {
//         printf("%d\n",ptr[i]);
//     }
//     return 0;
// }



//calloc(): initializes with 0 (defaul value is zero)
//not guarenteed in malloc 
// # include <stdio.h>
// # include <stdlib.h>  
// int main() {
//     float *ptr;
//     // int n =scanf("%d",&n); //not the syntax , here we are trying to assign 
//     //return value of scanf
//     int n;
//     scanf("%d",&n);
//     ptr = (float *)calloc(n , sizeof(float)); 
//     for(int i=0;i<n;i++) {
//         printf("%f\n",ptr[i]);
//     }
//     return 0;
// }

// free()
// We use it to free memory that is allocated
// using malloc & calloc

// realloc()
// reallocate (increase or decrease) memory
// using the same pointer & size.


//ex of realloc , allocate memory to store first 5 odd numbers 
//then reallocate it to store firs 6 even number
# include <stdio.h>
# include <stdlib.h>  
int main( )  {
    int *ptr;
    ptr = (int*)calloc(5,sizeof(int));
    for(int i=0;i<5;i++) {
        ptr[i] = 2*i+1;
    }
    for(int i=0;i<5;i++) {
        printf("%d\n",ptr[i]);
    }
    ptr = realloc(ptr,6*sizeof(int));
    ptr[0]=0;
    for(int i=1;i<6;i++) {
        ptr[i]  =ptr[i-1] +2;
        
    }
    for(int i=0;i<6;i++) {
        printf("%d\n",ptr[i]);
    }
    free(ptr);
    return 0;
}