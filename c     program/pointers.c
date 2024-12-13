/*pointers are variables that stores the address of another variable
* is value at adress operator
&adress of operator
(*ptr) is the variable remember we use to print and **pptr also*/
//int *ptr declares a pointer variable ptr that is intended to store the address of an int type.
//char *ptr declares a pointer variable ptr that is intended to store the address of an char type.
// syntax
// int age =20;
// int *ptr = &age; (ptr stores the adress of age ex-2010)
// int _age = *ptr;(_age stores the value at adress of ptr which is 20);

// #include<stdio.h>
// int main() {
//     int name =88;
//     int *ptr = &name;
//     int m = *ptr;
//     printf("%d",m);
//     return 0;
// }
//to print the adress we use %p which usually shows in hexdecimal form and %u is unsigned unit
// int main() {
//     int a =20;
//     int *ptr=&a;
//     printf("%p\n",&a);
//     printf("%p\n",ptr);
//     printf("%u\n",&a);
//     printf("%u\n",ptr);
//     printf("%u\n",&ptr); // adress of the ptr value
//     return 0;
// }

// #include<stdio.h>
// int main() {
//     int age =20;
//     int *ptr = &age;
//     printf("%d\n",age);
//     printf("%d\n",*ptr);
//     printf("%d\n",*(&age));
//     return 0;
// }

//guess the output 
// #include <stdio.h>
// int main() {
//     int *ptr;
//     int x;
//     ptr = &x;
//     *ptr = 0;
//     printf("x = %d\n", x);
//     printf("*ptr = %d\n", *ptr);
//     *ptr += 5;
//     printf("x = %d\n", x);
//     printf("*ptr = %d\n", *ptr);
//     (*ptr)++;
//     printf("x = %d\n", x);
//     printf("*ptr = %d\n", *ptr);
//     return 0;
// }

                    //pointer to pointer
//variable that stores the adress of the another pointer
/* syntax
  int ** pptr =   
  char **pptr
  float ** pptr  */
// int main() {
//     float a = 22;
//     float *ptr =&a;
//     float **pptr = &ptr;
//     printf("%f",**pptr);
//     return 0;
// }

// //     pointers in function call
// argument is the value passed through a function when its called 
//parameter is the value passed through a functin when its created we say
// 1.call by valuue - we pass value of a variable as argument 
// 2.call by refrence - we pass adress of variable as argument 

// ex call by value 
// #include<stdio.h>
//     void square(int n);
//     int main() {
//         int a =2;
//         square(a);  //a is doubled and is 4 (here a is argument) ,this argument is a copy of main one and changes does not reflect in main one 
//         printf("%d",a); //but here a =2;
//         return 0;
//     }
//     //call by value (passing value as an argument )
//     void square (int n) {  //here n is parameter
//         n = n*n;
//         printf("%d\n",n);
//     }


// // ex call by reference (here we are directly updating the value through the adress permanantly)
// #include<stdio.h>
//     void square(int *n)  ; //passing some address
//     int main () {
//         int a =2;
//         square(&a);
//         printf("%d",a);
//         return 0;
//     }
//     void square (int *n) {
//         *n = (*n) * (*n);
//         printf("%d\n",*n);
//     }

// ex - swap 2 numbers by call by reference and call by value
// #include<stdio.h>
// void swap (int *a,int *b);
// void swap1(int a,int b);

// int main() {
//   int a = 2;
//   int b = 4;
//   swap (&a, &b);
//   swap1(a,b);
//   return 0;
// }
// void swap (int *a,int *b) {
//   int s = *a;
//   *a = *b;
//   *b = s;
//   printf("%d and %d\n",*a,*b);
// }
// void swap1 (int a , int b ) {
//   int s =a;
//   a=b;
//   b=s;
//   printf("%d and %d",a,b);
// }

//will adress change  ?
// #include<stdio.h>
// void pri(int n);
// int main () {
//   int n= 2;
//   pri(n);        //adress have changed as  when it is called by value it creates duplicate n which has different adress  
//   printf("%u",&n);
//   return 0;
// }
// void pri(int s) {
//   printf("%u\n",&s);
// }

// call by reference
// #include<stdio.h>
// void pri(int *n);
// int main () {
//   int n= 2;
//   pri(&n);       
//   printf("%u",&n);
//   return 0;
// }
// void pri(int *s) {
//   printf("%u\n",s);
// }


/*calculate sum,product and average of 2 no.s and return 3 values to main function
as we can only return 1 value , we use pointer to return multiple values*/
// #include<stdio.h>
// void work(int a,int b,int *sum,int *mul,int *avg);
// int main() {
//   int sum,mul,avg;
//   int a=3,b=4;
//   work(a,b,&sum,&mul,&avg);
//   printf("%d and %d and %d ",sum,mul,avg);
//   return 0;
// }
// void work(int a, int b,int *sum,int *mul,int *avg) {
//   *sum=a+b;
//   *mul= a*b;
//   *avg =(a+b)/2;
// }










