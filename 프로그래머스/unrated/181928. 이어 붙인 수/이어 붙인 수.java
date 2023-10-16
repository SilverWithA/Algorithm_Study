class Solution {
    public int solution(int[] num_list) {
        String even = "";
        String odd = "";
        for(int i =0;i<num_list.length;i++){
            if(num_list[i]%2==0){
                even += String.valueOf(num_list[i]);
            }else{
                odd += String.valueOf(num_list[i]);
            }
        }

        int a = Integer.parseInt(even);
        int b = Integer.parseInt(odd);
        return a+b;
    }
}