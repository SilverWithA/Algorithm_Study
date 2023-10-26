class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for(int i=0;i<queries.length;i++){
            int prim_ele = arr[queries[i][0]];
            int second_ele = arr[queries[i][1]];
            arr[queries[i][0]] = second_ele;
            arr[queries[i][1]] = prim_ele;
        }
        return arr;
    }
}