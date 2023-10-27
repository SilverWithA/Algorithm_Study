import java.math.BigInteger;

class Solution {
    public int solution(String number) {
        BigInteger intNumber = new BigInteger(number);
        BigInteger nine = new BigInteger("9");
        BigInteger mod = intNumber.remainder(nine);
        
        int result = mod.intValue();
        return result;
    }
}