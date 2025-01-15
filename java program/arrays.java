import java.util.Arrays; //to do operations on arrays


public class arrays {
    public static void main(String[] args) {
        int[] car = new int[3];
        car[0] = 22;
        car[1] = 3;
        // or we can store as int[] car = {12,34,44};
        System.out.println(car[0]);
        System.out.println(car[2]);  //we didnt gave anythin so zero . for boolean type false
        System.out.println(car.length); //no need to keep in .length() in arrays
        Arrays.sort(car);  // A capital
        System.out.println(car[1]); //after sorting asseding order
       
    }  
}

/*for 2d arrays 
 * int arry[][] ={{1,2,3} , {44,33,55}};
 * System.out.println(marks[1][3]); like this
 */


//  import java.util.Scanner;

// public class MatrixColumnSum {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);

//         // Read the number of columns
//         int n = scanner.nextInt();

//         // Initialize two arrays to store the two rows
//         int[] row1 = new int[n];
//         int[] row2 = new int[n];

//         // Read the first row
//         for (int i = 0; i < n; i++) {
//             row1[i] = scanner.nextInt();
//         }
//         for (int i = 0; i < n; i++) {
//             row2[i] = scanner.nextInt();
//         }
//         for (int i = 0; i < n; i++) {
//             System.out.print((row1[i] + row2[i]) + " ");
//         }
//         scanner.close();
//     }
// }

//after lunch

