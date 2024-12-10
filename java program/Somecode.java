// public class somecode {
//     public static void main(String[] args) {
//         System.out.println("Hello World");
//       }
    
// }
// in some compilers use class Somecode(file name as a class name )  without that public 

// float Upto 7 decimal digits
// double Upto 16 decimal digits

/* when you're reading a String input with scanner.nextLine(); after reading other data types like
 int, double, or char, you should use an extra scanner.nextLine();
       int a = scanner,nextInt();
       scanner.nextLine(); 
        String eligibleForDeduction = scanner.nextLine(); */
        
// public class somecode {
//   public static void main(String[] args) {
//     byte hi = 12;
//     long ho = 12345645777777L;
//     float hh= 3.23F;
//     char hg = '@'; //double quotes is for strings
//     String ht = "hello"; // captial s in java for declaration and small s in c++;
//     boolean hq = false;
//     String hw = ht.replace('e','m');
//     System.out.println(hi);
//     System.out.println(ho); 
//     System.out.println(hh);
//     System.out.println(hg);
//     System.out.println(ht);
//     System.out.println(hq);
//     System.out.println(ht.length());
//     System.out.println(ht.charAt(1)); //in c++ we can use cout << ht[1] directly ;
//     System.out.println(hw);
//     System.err.println(ht.substring(1,4)); //substring where 4 not includes here
    
//     }
// }

// }
/*data types catogarized into two primitive is already defined in njava ex float, int ,boolean and non primitive are arrays ,string , list etc*/


// public class somecode {
//   public static void main (String[] args) {
//     int a =1;
//     int b =2;
//     int s = Math.abs(a-b);
//     double p = Math.pow(b,a); // for power,qrt function we should use double 
//     double d1 = Math.sqrt(a*a+b*b);  // we can use this   In C, include <math.h> to use the sqrt() function.
//                                     // In C++, include <cmath> for the sqrt() function.
//     System.out.println(s);
//     System.out.println(p);
//   }
// }


 /* Casting = to convert one data type to other and are 2 types implicit  and explit 
  * 
  */
/*Integer Data Types
char: Typically 1 byte (8 bits)
short: Typically 2 bytes (16 bits)
int: Typically 4 bytes (32 bits)
long: Typically 8 bytes (64 bits)
long long: Typically 8 bytes (64 bits)
Floating-Point Data Types
float: Typically 4 bytes (32 bits)
double: Typically 8 bytes (64 bits)
long double: Typically 16 bytes (128 bits)
Boolean Data Type
bool: Typically 1 byte (8 bits)
 * 
 */
//   public class somecode {
//     public static void main (String[] args) {
//       double price = 100.00;
//       double newprice  = price +29;
//       System.out.println(newprice);   //new is key word dont use for varible


//     }
//  }


//convert number into string
// int number = 12345;
// String numberStr = String.valueOf(number);
//to find lenth of string kength=numberstr.length();

//convert stirng to int,double etc (we check whether input is double or int etc)
// we can convert "12" to double and int , but  "12.2" first convert into double and then int excplicitly
// public class Somecode {
//   public static void main(String args[]) {
//     String a = "12.2";
//     String b = "45";
//     double k = Double.parseDouble(a);
//     double m = Double.parseDouble(b);
//     int l = (int)k;
//     int n = Integer.parseInt(b);
    // int g = Integer.parseInt(a)
    // System.err.println(k);
    // System.err.println(m);
    // System.err.println(l);
    // System.out.println(n);
//   }
// }



//enhanced for loop
// public class Main {
//   public static void main(String[] args) {
//       for (char ch : "12345".toCharArray()) {
//           System.out.print(ch + " ");
//       }
//   }
// }

//for prime no logic is for i=2 to i<Math.sqrt;i++ divide givn number by i


//int target = obj.nextInt();
// int row=-1;
// int column=-1;
// for(i=0;i<n;i++) {
// for(j=0;j<m;j++) {
// if(arr[i][j] == target) {
// row =i;
// column =j;
// break;
// }
// }
// if 


//when to use .equals() and == in java ?
// == when comparing primitive data types (e.g., int, char, boolean)
// .equals() when comparing the contents (i.e., values) of two objects, like strings


// You are using Java
// import java.util.*;
// // import java.util.*;

// class Main {
//     public static void main(String args[]) {
//         Scanner obj = new Scanner(System.in);
        
//         // Read the number of strings
//         int n = Integer.parseInt(obj.nextLine().trim()); // Read the integer input as a line and trim any whitespace
        
//         // Read each string and add it to the list
//         List<String> s = new ArrayList<>();
//         for (int i = 0; i < n; i++) {
//             String a = obj.nextLine().trim(); // Read each string line
//             s.add(a);
//         }
        
//         // Read the search string
//         String t = obj.nextLine().trim();
        
//         // Sort the list
//         Collections.sort(s);
//         System.out.println("Sorted List: " + s);
        
//         // Search for the element in the sorted list
//         int b = s.indexOf(t);
//         if (b >= 0) {
//             System.out.println(t + " is in the list at index " + b);
//         } else {
//             System.out.println(t + " is not in the list");
//         }
        
//         // Reverse the list
//         Collections.reverse(s);
//         System.out.println("List after Reversing: " + s);
        
//         obj.close();
//     }
// }


// important
// input:(should take by user)
// 5
// re 4 
// rr 4 
// ww 5 
// tu 3 
// wit 4
// output:
// 4 ( most repeating)
// re
// rr wit

// You are using Java
//whitelist: uniqueChars
// import java.util.Scanner;
// import java.util.LinkedHashSet;

// public class Main {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         String input = sc.nextLine();
//         System.out.println("Unique Characters: " + getUniqueCharacters(input));
//     }

//     public static String getUniqueCharacters(String input) {
//         LinkedHashSet<Character> uniqueChars = new LinkedHashSet<>();
//         StringBuilder result = new StringBuilder();
        
//         for (char c : input.toCharArray()) {
//             if (!uniqueChars.contains(c)) {
//                 uniqueChars.add(c);
//                 result.append(c);
//             }
//         }
        
//         return result.toString();
//     }
// }


///normallyb we have to sovle through linedhashset something
import java.util.Scanner;
public class somecode {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input from user
        System.out.print("Enter a string: ");
        String s = scanner.nextLine();
        StringBuilder unique = new StringBuilder();
        
        for(int i=0;i<s.length();i++) {
            char c = s.charAt(i);
            if(s.indexOf(c) == s.lastIndexOf(c)) {
                unique.append(c);

            }

        }
        System.out.println(unique);
        scanner.close();
    }
}

//also learn permutations of the string 
// You are using Java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        System.out.println("Permutations of the string:");
        generatePermutations(input, "");
    }

    public static void generatePermutations(String str, String permutation) {
        if (str.length() == 0) {
            System.out.println(permutation);
            return;
        }

        for (int i = 0; i < str.length(); i++) {
            char currentChar = str.charAt(i);
            String remaining = str.substring(0, i) + str.substring(i + 1);
            generatePermutations(remaining, permutation + currentChar);
        }
    }
}


