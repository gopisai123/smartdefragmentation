// structers is collection of different data types

# include <stdio.h>
# include <string.h>
struct student { //syntax
    char name[100];
    int roll;
    float cgpa;
}; //semicolon
int main () {
    struct student s1;
    struct student IT[60];  //array of structures
    // s1.name = "gopi"; // we cannot modify value because its char array , by pointers we can 
    
    strcpy(s1.name,"gopi");
    s1.roll = 64;
    s1.cgpa = 9.2;

    IT[0].roll =  1122;
    IT[0].cgpa = 2.2;
    strcpy(IT[0].name,"sai-j");

    printf("student info : \n");
    printf("name = %s\n", s1.name);
    printf("roll no = %d\n", s1.roll);
    printf("cgpa = %f\n", s1.cgpa);

    printf("name = %s\n",IT[0].name);

    //intiaizing structers (we can give in one line )
    struct student s2 = {"Rajat", 1552, 8.6};
    printf("roll n0: %d\n",s2.roll);

    struct student *ptr = &s2;
    printf("name: %s\n",(*ptr).name);
    


    return 0;
}