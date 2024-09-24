//class and objects
//the main class should be the file name 
//classes name starts with capital and functions with small

// class pen {
//     String color;
//     String type; 

//     public void write() {
//         System.out.println("writing something");
//     }
//     public void printcolor() {
//         System.out.println(this.color);  // this keyword is a reference to the current object,
//     }
//     pen() {    //non paramaretrized  constructor
//         System.err.println("constuct called");
//     }
// }
// class student {
//     String name ;
//     int age;
//     public void printinfo() {
//         System.out.println(this.name);
//         System.out.println(this.age);
//     }
//     student(String name,int age) {  //paramtrized constructors
//         this.name = name;
//         this.age=age;
//     }
// }

// public class oops{
//     public static void main(String args[]) {
//         pen pen1 = new pen(); //pen1 is object of class pen and when peb1 created automatically constructor called
//         pen1.color = "blue";
//         pen1.type = "gel";
//         pen1.write();
//         pen1.printcolor();
//         student s1 = new student("gopi",22);
//         s1.printinfo();
//     }
// }


// Constructor is a special method called when object is created.
// It is used to initialize the data members of new objects generally. 
// Constructors have the same name as class or structure. 
// Constructors don’t have a return type. (Not even void)
// Constructors are only called once, at object creation

//construcors three types 
// 1.non paramaretrized
// 2.parama....
// 3.copy constu (in c++ default and user defined but un java all user define );


//copy constructors ex
//  class car {
//     String name;
//     int year;
//     //constructor
//     car (String name ,int year ) {
//         this.name = name;
//         this.year = year;
//     }
//     public void print() {
//         System.out.println("1."+this.name+" 2."+this.year);
//     }
//     //copy constructor
//     car(car s2) {
//         this.name =s2.name;
//         this.year =s2.year;
//     }
//  }
//  class oops {
//     public static void main (String  args [] ) {
//         car obj1 = new car ("gopi",23);
//         car obj2 = new car(obj1);
//         obj1.print();
//         obj2.print();
//     }
//  }

// Note : Unlike languages like C++, Java has no Destructor. 
// Instead, Java has an efficient  garbage collector that deallocates memory automatically.

 
                                               /*polymorphism */
// Polymorphism is the ability to present the same interface for differing underlying forms (data types) 
// Types of Polymorphism IMP 
// 1. Compile Time Polymorphism (Static)  (method overloading)
class Student {
    String name;
    int age;
    public void displayInfo(String name) {
        System.out.println(name);
    }
    public void displayInfo(int age) {
        System.out.println(age);
    }
    public void displayInfo(String name, int age) {
        System.out.println(name);
        System.out.println(age);
    }
 }
 
// 2. Runtime Polymorphism (Dynamic)





