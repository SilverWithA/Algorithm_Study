class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = true;
        boolean union;
        boolean intersection;
        
        if(!x1 && !x2){
            union = false;
        }else{
            union = true;
        }
        
        if(!x3 && !x4){
            intersection = false;
        }else{
            intersection = true;
        }
        
        if(union && intersection){
            answer = true;
        }else{
            answer = false;
        }
        
        
        return answer;
    }
}