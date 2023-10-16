class Solution {
    public int solution(int[] num_list) {
        int pos1 = 0;
        int pos2 = 1;
        for(int i=0;i<num_list.length;i++){
            pos1 += num_list[i];
            pos2 *= num_list[i];
        }
        
        pos1 = (pos1 * pos1) ;
        if(pos1 > pos2){
            return 1;
        }else{
            return 0;
        }
    }
}