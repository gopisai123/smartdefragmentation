//class and objects
//classes name starts with capital and functions with small
class pen {
    String color;
    String type; 

    public void write() {
        System.out.println("writing something");
    }
    public void printcolor() {
        System.out.println(this.color);  // this keyword is a reference to the current object,
    }
    pen() {    //normal constructor
        System.err.println("constuct called");
    }
}
class student {
    String name ;
    int age;
    public void printinfo() {
        System.out.println(this.name);
    }
}

public class Main{
    public static void main(String args[]) {
        pen pen1 = new pen(); //pen1 is object of class pen and when peb1 created automatically constructor called
        pen1.color = "blue";
        pen1.type = "gel";
        pen1.write();
        pen1.printcolor();
        student s1 = new student();
        s1.name = "gopi";
        s1.printinfo();

    }
}

// Constructor is a special method called when object is created.
// It is used to initialize the data members of new objects generally. 
// Constructors have the same name as class or structure. 
// Constructors don’t have a return type. (Not even void)
// Constructors are only called once, at object creation.
