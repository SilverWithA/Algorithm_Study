
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> stk = new ArrayList<Integer>();
        int i = 0;

        while(i < arr.length){
            // stk가 비어있을 때
            if(stk.size() == 0){
                stk.add(arr[i]);
                i++;
            }
            
            //stk에 원소가 있을때
            else if(arr[i] > stk.get(stk.size()-1)){
                stk.add(arr[i]);
                i++;
            }else if(arr[i] <= stk.get(stk.size()-1)){
                stk.remove(stk.get(stk.size()-1));
            }
        }
        
        return stk.stream().mapToInt(j -> j).toArray();
    }
}