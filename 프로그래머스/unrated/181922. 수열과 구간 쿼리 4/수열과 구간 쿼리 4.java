class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[arr.length];
        //deepCopy: 깊은 복사
        answer = arr.clone();
        
        for(int idx =0;idx<queries.length;idx++){
            int[] query = queries[idx];
            int s = query[0], e = query[1], k = query[2];
            
            for(int i=s; i<=e;i++){
                if(i % k == 0){
                    answer[i]++;
                }
            }
        }
        return answer;
    }
}