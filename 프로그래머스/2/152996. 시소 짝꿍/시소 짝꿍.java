import java.util.*;
// class Solution {
//     public int solution(int[] weights) {
//         int answer = 0;
        
//         Arrays.sort(weights);
        
//         Map<Double, Integer> result = new HashMap<>();
        
//         // 1:1 이거나 2:3이거나 2:4, 3:4 중 하나
//         for(int weight : weights){
//             double a = weight * 1.0;
//             double b = (weight * 3.0)/4.0;
//             double c = (weight * 2.0)/3.0;
//             double d = (weight * 1.0)/2.0;
            
//             if(result.containsKey(a)) answer += result.get(a);
//             if(result.containsKey(b)) answer += result.get(b);
//             if(result.containsKey(c)) answer += result.get(c);
//             if(result.containsKey(d)) answer += result.get(d);
            
//             result.put((weight * 1.0), result.getOrDefault((weight * 1.0),0) + 1);
                       
            
//         }
//         return answer;
//     }
// }


class Solution {
    public long solution(int[] weights) {
    	long answer = 0;
        Arrays.sort(weights);
        Map<Double, Integer> map = new HashMap<>();
        for(int i : weights) {
    		double a = i*1.0;
    		double b = (i*2.0)/3.0;
    		double c = (i*1.0)/2.0;
    		double d = (i*3.0)/4.0;
            
    		if(map.containsKey(a)) answer += map.get(a);
    		if(map.containsKey(b)) answer += map.get(b);
    		if(map.containsKey(c)) answer += map.get(c);
    		if(map.containsKey(d)) answer += map.get(d);
            
    		map.put((i*1.0), map.getOrDefault((i*1.0), 0)+1);
        }
        
        return answer;
    }
}