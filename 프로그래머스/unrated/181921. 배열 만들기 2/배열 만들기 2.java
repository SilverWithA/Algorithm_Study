import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.Arrays;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        String pattern1 = "^[^1-4-6-9]*$";
        for(int i=l; i<=r;i++){
            String number = String.valueOf(i);
            if(Pattern.matches(pattern1, number)){
                result.add(Integer.parseInt(number));
            }
        }
        if(result.size() == 0){
            int[] answer = {-1};
            return answer;
        }
        int[] answer = new int[result.size()];
    
        for(int i=0; i<answer.length;i++){
            answer[i]= result.get(i);
        }

        return answer;
    }
}