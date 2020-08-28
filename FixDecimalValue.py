import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the plusMinus function below.
    static void plusMinus(int[] arr) {
        int count=0;
        int pc=0;
        int zc=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]<0){
                count++;
            }
            else if(arr[i]>0){
                pc++;
            }
            else{
                zc++;
            }
        }
        int n=arr.length;
        System.out.println(String.format("%.6f",((double)pc/n)));
        System.out.println(String.format("%.6f",((float)count/n)));
        System.out.println(String.format("%.6f",((float)zc/n)));

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        plusMinus(arr);

        scanner.close();
    }
}
