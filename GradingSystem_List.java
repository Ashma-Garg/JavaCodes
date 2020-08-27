import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    public static List<Integer> gradingStudents(List<Integer> grades) {
    for(int i=0;i<grades.size();i++){
        if(grades.get(i)<38){
            grades.set(i,grades.get(i));
        }
        else if(grades.get(i)%5!=0){
            int x=grades.get(i)%5;
            x=5-x;
            if(x<3){
                grades.set(i,(grades.get(i)+x));
            }
        }
    }
    return grades;
    }

}

public class GradingSystem_List{
    public static void main(String[] args) throws IOException {
        List<Integer> al = new ArrayList<>(); 
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	for(int i=0;i<n;i++){
		al.add(sc.nextInt());
	}
	List<Integer> result=Result.gradingStudents(al);
	for(int i=0;i<n;i++){
		System.out.println(result.get(i));
	}

    }
}
