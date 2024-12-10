// You are using Java
import java.util.*;
class Main  {
    static int maxDigit(int n)  {
        int max =0;
        while(n>0) {
            int lastd = n%10;
            if(lastd>max) {
                max=lastd;
            }
            n=n/10;
        }
        return max;
    }
    public static void main(String args[])  {
        Scanner obj = new Scanner(System.in);
        int n = obj.nextInt();
        int hi = maxDigit(n);
        System.out.println(hi);
        
        
    }
}


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(calculateLCM(arr));
    }

    public static int calculateLCM(int[] arr) {
        int lcm = arr[0];
        for (int i = 1; i < arr.length; i++) {
            lcm = lcm(lcm, arr[i]);
        }
        return lcm;
    }

    public static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }

    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}


