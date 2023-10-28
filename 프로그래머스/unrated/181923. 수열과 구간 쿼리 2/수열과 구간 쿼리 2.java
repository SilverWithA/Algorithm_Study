// import java.util.ArrayList;
// import java.util.Collections;

// class Solution {
//     public int[] solution(int[] arr, int[][] queries) {
//         int[] result = new int[queries.length];

//         for(int j=0;j<queries.length;j++){
//             ArrayList<Integer> temp= new ArrayList<Integer>();
//             ArrayList<Integer> arrTemp= new ArrayList<Integer>();
//             int s = queries[j][0];
//             int e = queries[j][1];
//             int k = queries[j][2];
            
//             //s와 e사이의 i들을 저장 temp에 저장
//             for(int i=0;i<arr.length;i++){
//                 if(arr[i] >= s && arr[i] <= e){
//                     temp.add(arr[i]);
//                 }
//             }
//             for(int i=0;i<temp.size();i++){
//                 arrTemp.add(arr[temp.get(i)]);
//             }
//             Collections.sort(arrTemp);
//             for(int i =0;i<arrTemp.size();i++){
//                 if(arrTemp.get(i) > k){
//                     result[j] = arrTemp.get(i);
//                     break;
//                 }
//                 result[j] = -1;
//             }

//         }
//         return result;
//     }
// }

import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[][] queries){
        int[] answer = new int[queries.length];
        Arrays.fill(answer, -1);
        
        for(int idx =0;idx<queries.length;idx++){
            int[] query = queries[idx];
            int s = query[0], e=query[1], k = query[2];
            for(int i=s; i<=e;i++){
                if(arr[i] > k){
                    answer[idx] = answer[idx] == -1 ? arr[i] : Math.min(arr[i],answer[idx]);
                }
            }
        }
        return answer;
        
    }
}