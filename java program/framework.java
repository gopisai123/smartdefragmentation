/* an ArrayList is part of the java.util package and provides a dynamic array that can grow or shrink in size 
   The formula n + n/2 + 1 is related to how the ArrayList grows when it exceeds its current capacitu
*/
import java.util.*;
public class framework {
    public static void main (String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        System.out.println(list);
        list.add(3);
        System.out.println(list);
        list.add(1,50);
        System.out.println(list);
        List<Integer> l2 = new ArrayList<>();
        l2.add(45);
        l2.add(99);
        list.addAll(l2);
        System.out.println(list);
        System.out.println(list.get(4));
        list.remove(3);
        System.out.println(list);
        list.remove(Integer.valueOf(50));
        System.out.println(list);
        list.set(2,333);
        System.out.println(list);
        System.out.println(list.contains(99));
        for(int i=0;i<list.size();i++) {
            System.out.println("element is "+list.get(i));
        }

        for(Integer i: list) {
            System.out.print(i+" ");
        }
        // list.clear();
        // System.out.println(list);
    }
}


hash map: used to store key-value pairs
import java.util.*;
public class framework {
    public static void main (String args[]) {
        Map<String,Integer> a = new HashMap<>();
        a.put("red",1);
        a.put("blue",22);
        System.out.println(a.containsValue(34));
        //a.put("blue",44) , we cant change like this , keys should be unique and their value can be same 
        if(a.containsKey("blue")) {
            a.put("blue",44);
        }
        System.out.println(a);    //output is unordered
        if(!a.containsKey("yellow")) {
            a.put("yellow",55);
        }
        System.out.println(a);


        //to iterate 
        for(Map.Entry<String,Integer> i:a.entrySet())  {
            System.out.println(i);

        }
        for(Map.Entry<String,Integer> i:a.entrySet())  {
            System.out.println(i.getKey());
            System.out.println(i.getValue());

        }


        Set<String> keys = a.keySet(); //to create a key set from hashset
        for(String i:keys) {
            System.out.println(i+ " "+a.get(i));
        }


        set<Integer> value = new HashSet<>(line.values());





    }
}


import java.util.*;
class framework {
    public static void main(String args[])  {
        Scanner obj = new Scanner(System.in);
        Map<String,Integer> line = new HashMap<>();
        int n = obj.nextInt();
        obj.nextLine();
        int max =0;
        for(int i=0;i<n;i++) {
            String a = obj.nextLine();
            int b = obj.nextInt();
            obj.nextLine();
            line.put(a,b);
            if(i==0) {
                max = b;
            }
        }
        Set<Integer> num = new HashSet<>(line.values());
        for(int i: num) {
            if(i>max) {
                max =i;
            }
        }
        for(Map.Entry<String,Integer> j : line.entrySet())  {
            if(j.getValue()==max) {
                System.out.println(j.getKey());
            }
        }
    }
}

