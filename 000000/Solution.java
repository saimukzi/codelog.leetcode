import java.lang.AssertionError;
import java.util.*;
import java.util.regex.*;

class Solution {

    public boolean func(int x) {
        return false;
    }
    
    public static void main(String[] argv){
        test(123,true);
    }
    
    public static void test(int x,boolean expected){
        System.out.println(String.format("x=%d, expected=%s",x,expected));
        Solution solution = new Solution();
        boolean result = solution.func(x);
        System.out.println(String.format("result=%s",result));
        aassert(result == expected);
    }
    
    public static void aassert(boolean cond){
        if(!cond)throw new AssertionError();
    }
}