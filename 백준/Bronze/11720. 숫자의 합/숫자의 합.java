import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); //n값 입력받기

        String sNum = sc.next();          //string 값을 받기
        char[] cNum = sNum.toCharArray(); //char[]로 변환하기
        int sum = 0;

        //loop를 돌며 cNum의 값 하나씩의 총합을 구하기
        for(int i=0;i<cNum.length;i++){
            sum += cNum[i] -'0'; //아스키 코드 이용 str형을 int형으로 만들기
            // '48'을 이용해도 가능함
        }
        System.out.print(sum);
    }
}