import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String result = "";
        
        
        for(int i=0;i<a.length();i++){
            if(Character.isUpperCase(a.charAt(i))){
                // System.out.println(i+"번째 문자는 대문자입니다.");
                result += Character.toLowerCase(a.charAt(i));

            }else{
                result += Character.toUpperCase(a.charAt(i));
            }
        }
        System.out.println(result);
                

    }
}