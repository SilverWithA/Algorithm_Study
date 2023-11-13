import java.util.ArrayList;
class Solution {
    public ArrayList solution(int[] numbers) {
        ArrayList answer = new ArrayList();
        for(int number : numbers){
            answer.add(number*2);
        }
        return answer;
    }
}