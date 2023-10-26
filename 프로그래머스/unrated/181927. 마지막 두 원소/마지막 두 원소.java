import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(int[] num_list){
        int arr_length = num_list.length;
        int[] answer = new int[arr_length + 1];
        //1. 원소뽑기 = int[] 인덱싱
        int last_ele = num_list[arr_length-1];
        int compare_ele = num_list[arr_length-2];
        
        for(int i=0;i<arr_length;i++){
            answer[i] = num_list[i];
        }
        
        //두 원소 비교 & 비교후 원소 추가
        if(last_ele > compare_ele){
            answer[arr_length] = (last_ele-compare_ele);
        }else{
            answer[arr_length] = (last_ele*2);
        }
        return answer;

    }
}