class Solution{
    public int solution(int a, int b){
        
        //int형 to String형
        String str1 = String.valueOf(a);
        String str2 = String.valueOf(b);
        

        String answer1 = str1+ str2;
        String answer2 = str2+ str1;
        //String형 to int형
        int res1 = Integer.valueOf(answer1);
        int res2 = Integer.valueOf(answer2);
        if(res1 > res2){
            return res1;
        }else{
            return res2;
        }
    }
}