class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String str1 = String.valueOf(a)+String.valueOf(b);
        int first = Integer.valueOf(str1); 
        int second = (2*a*b);

        if( first>second ){
            answer = first;
        }else{
            answer = second;
        }
        return answer;
    }
}