import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        
        int scores[] = new int[n];
        for(int i=0;i<n;i++){
            scores[i] = s.nextInt();
        }
        
        long m = 0;
        long sum =0;
        
        for(int i=0;i<n;i++){
            if(scores[i]>m) m =scores[i];
            sum =sum+scores[i];
        }
        System.out.print(sum*100.0/m/n);
        
    }
}