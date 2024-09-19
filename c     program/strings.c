// string is a character array terminated by '\0'(null character)
//for string we no need to tell size
// exanple:
// char arr[]={'h','i','\0'};  we can create string like this

// #include<stdio.h>
// int main()  {
    //1
    // char arr[] = "hello";   //here we gave name so it will take the length automat
    // for(int i=0;arr[i]!='\0';i++) {
    //     printf("%c",arr[i]);
    // }
    // printf("\n");
    //2
    // char name[50];  //char array
    // scanf("%s",name);  //no need to use & name for string  and scanf cannot take multi word as input
    // printf("ur name is %s",name);   
    // return 0;
//}

// #include<stdio.h>
// int main() {
//     char str[100];
//     fgets(str,100,stdin);  // instead you can use gets(str) but not reccomendable
//     puts(str);  //puts prints and make crusser to got to next line but when you use gets you wont get extra line after executing 
//     return 0;
// }

//string as character pointer and character array 
// #include<stdio.h>
// int main()  {
//     char *p1 = "hello world";  //where the address of 1st index is pointed by p1
//     p1 = "hi buddy"; //we can change the value os char pointer
//     puts(p1);
//     char arr[] = "hello frnd";
//     arr = "lets go ";  //here its showing error in the line mean we cant change the char arraay
//     puts(arr);

//     return 0;
// }

//now to count the length of the sting
#include<stdio.h>
void print(string h);
int length(string h);
int main()  {
    char name[100];
    fgets(name,100,stdin);
    void(print(name));
}

//string change mate
//


