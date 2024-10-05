// string is a character array terminated by '\0'(null character)
//for string we no need to tell size
// example:
// char arr[]={'h','i','\0'};  we can create string like this

// #include<stdio.h>
// int main()  {
//     char arr[] = "hello";   //here we gave name so it will take the length automat
//     for(int i=0;arr[i]!='\0';i++) {  //automatically gives null character 
//         printf("%c",arr[i]);
//     }
//     printf("\n");
    
//     char name[50];  //char array
//     scanf("%s",name);  //no need to use &name for string  and scanf cannot take multi word as input
//     printf("ur name is %s",name);   
//     return 0;
// }

// fgets ; when user enter a word iam gopi and clicks enter it will store as iam gopi\n 
// #include<stdio.h>
// int main() {
//     char str[100];
//     fgets(str,100,stdin);  // instead you can use gets(str) but not recommendable
//     puts(str); // puts automatically gives next line 
//     return 0;
// }

//string as character pointer and character array 
/*in C, the & operator is used to get the address of a variable. For numbers or any other data type, you use & to get the memory address of the variable.
 However, for strings, which are essentially arrays of characters, the array's name itself acts as a pointer to the first element of the array.*/
// #include<stdio.h>
// int main()  {
//     char *p1 = "hello world";  //where the address of 1st index is pointed by p1
//     p1 = "hi buddy"; //we can change the value os char pointer
//     puts(p1);
//     printf("%p",&(*p1));//to print first char adress
//     // char arr[] = "hello frnd";
//     // arr = "lets go ";  //here its showing error in the line mean we cant change the char arraay
//     // puts(arr);

//     return 0;
// }

// #include<stdio.h>
// int main () {
//     char arr[] = "gopisai";
//     int n=0;
//     for(int i=0;arr[i]!='\0';i++) {
//         n++;
//     }
//     printf("%d\n",n);  //here no fgets so correct output
//     return 0;
// }

//now to count the length of the sting
// #include<stdio.h>
// void print(char arr[]);
// int length(char arr[]);
// int main()  {
//     char name[100];
//     fgets(name,100,stdin);
//     print(name);
//     printf("%d",length(name));
//     return 0;
// } 
// void print(char arr[])  {
//     for(int i=0;arr[i]!='\0';i++) {
//         printf("%c",arr[i]);
        
//     }
// }
// int length(char arr[]) {
//     int n=0;
//     for(int i=0;arr[i]!='\0';i++) {
//         n++;
//     }
//     return n-1; //because fgets counts newline character also
// }


//<string.h> standard library for strings
// #include<stdio.h>
// #include<string.h>
// int main () {
//     char arr[] = "gopi";
//     int n = strlen(arr);  //strlen gives unsigned long so first typecast into int
//     printf("length is : %d\n",n);

//     //string copy and you cannot directly use this while taking input and copy because input wll take "\n"
//     char oldVal[] = "oldValue";
//     char newVal[50];
//     strcpy(newVal, oldVal);
//     puts(newVal);

//     // string concatination 
//     char firstStr[50] = "Hello "; // give big size as we are storing in this 
//     char secStr[] = "World";
//     strcat(firstStr, secStr);
//     puts(firstStr); 

//     //to compare string (it will compare ascii value)
//     char str1[] = "Apple";
//     char str2[] = "Banana";
//     printf("%d\n", strcmp(str1, str2));
//     return 0;
// }

// #include<stdio.h>
// #include<string.h>
// int main() {
//     // enter String using %c
//     printf("enter string : ");
//     char str[100];
//     char ch;
//     int i = 0;
//     while(ch != '\n') {  //this while loop acts as fgets
//     scanf("%c", &ch);
//     str[i] = ch;
//     i++;
//     }
//     str[i] = '\0';  // for only string null character comes automati...
//     puts(str);
//     printf("%s",str);
//     return 0;
// }

// for(i=0;arr[i]!='\0';i++)  //this is only for printing
// write about that adding two input strings
// #include<stdio.h>
// #include<string.h>
// int main () {
//     char arr[100];
//     char arr1[100];
//     fgets(arr,1000,stdin);
//     fgets(arr1,1000,stdin);
//     arr[(strlen(arr)-1)]='\0';
//     arr1[(strlen(arr1)-1)]='\0';
//     strcat(arr,arr1); 
//     printf("%s",arr);
//     return 0;
// }

// strcspn() 
// #include <stdio.h> 
// #include <string.h> 
// int main() 
// { 
//     int size; 
//     // initializing strings 
//     char str1[] = "geeksforgeeks"; 
//     char str2[] = "kfc"; 
//     // using strcspn() to calculate initial chars 
//     // before 1st matching chars. 
//     // returns 3 
//     size = strcspn(str1, str2); 
//     printf("The unmatched characters before first matched character :  %d\n", size); 
// } 


#include<stdio.h>
#include<string.h>
int main () {
    char arr[100] = "hello";
    int *ptr = &arr;
    *ptr = "gopi";
    printf("%s",arr);
    
    return 0;
}


