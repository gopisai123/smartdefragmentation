/*pointers are variables that stores the address of another variable
* is value at adress operator
&adress of operator*/
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
#include <stdio.h>
int main() {
    int *ptr;
    int x;
    ptr = &x;
    *ptr = 0;
    printf("x = %d\n", x);
    printf("*ptr = %d\n", *ptr);
    *ptr += 5;
    printf("x = %d\n", x);
    printf("*ptr = %d\n", *ptr);
    (*ptr)++;
    printf("x = %d\n", x);
    printf("*ptr = %d\n", *ptr);
    return 0;
}

// iam sai gopi  
