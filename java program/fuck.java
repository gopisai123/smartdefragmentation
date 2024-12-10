
import java.util.*;
public class fuck {
    public static void main(String args[]) {
        Scanner obj = new Scanner(System.in);
        
        // Read the number of strings
        int n = Integer.parseInt(obj.nextLine().trim()); // Read the integer input as a line and trim any whitespace
        
        // Read each string and add it to the list
        List<String> s = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String a = obj.nextLine().trim(); // Read each string line
            s.add(a);
        }
        
        // Read the search string
        String t = obj.nextLine().trim();
        
        // Sort the list
        Collections.sort(s);
        System.out.println("Sorted List: " + s);
        
        // Search for the element in the sorted list
        int b = s.indexOf(t);
        if (b >= 0) {
            System.out.println(t + " is in the list at index " + b);
        } else {
            System.out.println(t + " is not in the list");
        }
        
        // Reverse the list
        Collections.reverse(s);
        System.out.println("List after Reversing: " + s);
        
        obj.close();
    }
}

// You are using Java
import java.util.*;
class fuck {
    public static void main (String args[]) {
        Scanner obj = new Scanner (System.in);
        int n = obj.nextInt();
        obj.nextLine();
        List<String> s = new ArrayList<>();
        int i;
        for(i=0;i<n;i++) {
        
            String a = obj.nextLine();
            s.add(a);
        }
        String t = obj.nextLine();
        Collections.sort(s);
        
        System.out.println("Sorted List: "+s);
        int b = s.indexOf(t);
        if(b>=0) {
            System.out.println(t+"is in the list at index "+b);
            
        }
        else {
            System.out.println(t+"is not in the list");
        }
        Collections.reverse(s);
        System.out.println("List after Reversing: "+s);
       
        obj.close();
    }
}

impo java.oi
imp java.util 
class {
    publ sya  nvoid m{
        scanner obj = new 
        String a = "data."'
        String b = "dd'
        BufferedReader c = new Bufferedreader (new FileReader(a);
        double s = Double.parseDouble()
'
        
}