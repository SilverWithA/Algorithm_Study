import java.util.*;
class Solution {
    public int solution(String dirs) {
        int answer = 0;
        
        Set<String> path = new HashSet<>();
        int currentX = 0;
        int currentY = 0;
    
        // 움직이기
        for(int i = 0 ; i < dirs.length(); i++){
            int nextX = currentX;
            int nextY = currentY;
            char s = dirs.charAt(i);
            
            if(s == 'U'){
                nextY = currentY + 1;
            }else if(s == 'D'){
                nextY = currentY - 1;
            }else if(s == 'R'){
                nextX = currentX + 1;
            }else if(s == 'L'){
                nextX = currentX - 1;
            }
            

            
            if(nextX < -5 || nextX > 5 || nextY < -5 || nextY > 5){
                continue;
            }
            
            
            String temp1 = String.valueOf(currentX) + String.valueOf(currentY) 
                     + String.valueOf(nextX) + String.valueOf(nextY);
            String temp2 =String.valueOf(nextX) + String.valueOf(nextY) 
                     + String.valueOf(currentX) + String.valueOf(currentY);
            
            path.add(temp1);
            path.add(temp2);

            currentX = nextX;
            currentY = nextY;
        }
    
        
        return path.size() / 2;
    }
}