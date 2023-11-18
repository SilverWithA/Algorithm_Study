class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int evenSum = 0;
        int oddSum = 0;
        for(int even = 0; even < num_list.length; even += 2){
            evenSum += num_list[even];
        }
        
        for(int odd = 1; odd < num_list.length; odd += 2){
            oddSum += num_list[odd];
        }
        return evenSum > oddSum ? evenSum : oddSum;
    }
}