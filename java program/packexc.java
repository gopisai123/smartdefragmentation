//example of exception handling using try,catch, throw key words
import java.util.*;
public class packexc {
    public static long factorial(int n) {
        long fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }
    public static void main(String args[]) {
        Scanner obj = new Scanner(System.in);
        try {
            int n = obj.nextInt();
            if (n < 0) {
                throw new IllegalArgumentException("Error: Negative value of N");
            }
            long res = factorial(n);
            System.out.println(res);
        } catch (IllegalArgumentException A) {
            System.out.println(A.getMessage());
        }
    }

    
}

