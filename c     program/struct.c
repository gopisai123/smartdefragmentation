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
    // s1.name = "Shradha"; // we cannot modify value because its char array , by pointers we can 
    strcpy(s1.name,"Shradha");
    s1.roll = 64;
    s1.cgpa = 9.2;
    printf("student info : \n");
    printf("name = %s\n", s1.name);
    printf("roll no = %d\n", s1.roll);
    printf("cgpa = %f\n", s1.cgpa);

    return 0;
}