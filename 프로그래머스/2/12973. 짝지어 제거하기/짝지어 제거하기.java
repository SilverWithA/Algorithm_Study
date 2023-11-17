import java.util.Stack;

// 스택을 이용해 풀어보자
class Solution{
    public int solution(String s){
        // 자바 스택 이용법은? - 제네릭에 char과 int가 안되는 이유
        // stk.pop() 해주면 Object가 되는 이유
        
         Stack<Character> stk = new Stack<>();
        
        for(char c : s.toCharArray()){
            //짝지어 제거하기
            if(!stk.isEmpty() && stk.peek() == c){
                stk.pop();
            }else{
                stk.push(c);
            }
        }
        
        return stk.isEmpty() ? 1 : 0;
    }
}
