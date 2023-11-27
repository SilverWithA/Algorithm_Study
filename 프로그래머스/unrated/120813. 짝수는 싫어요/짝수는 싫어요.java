import java.util.*;
class Solution {
    public List<Integer> solution(int n) {
        List<Integer> arr = new ArrayList<>();
        for(int i =1;i < n+1;i += 2){
            arr.add(i);
        }
        
        return arr;
    }
}