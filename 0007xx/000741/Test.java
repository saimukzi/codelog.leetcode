import java.lang.AssertionError;
import java.util.*;
import java.util.regex.*;

class Test {

    public static void main(String[] argv){
        // given
        test(
            new int[][]{
                {0,1,-1},
                {1,0,-1},
                {1,1, 1}
            }
            ,5
        );
        // my case
        test(
            new int[][]{
                {0,0,1},
                {0,0,0},
                {1,0,0}
            }
            ,2
        );
        test(
            new int[][]{
                {0, 0,1},
                {0,-1,0},
                {1, 0,0}
            }
            ,2
        );
        test(
            new int[][]{
                {0, 0,-1},
                {1, -1,0},
                {-1, 0,0}
            }
            ,0
        );
        // judge
        test(
            new int[][]{
                {1,1,-1},
                {1,-1,1},
                {-1,1,1}
            }
            ,0
        );
    }
    
    public static void test(int[][] grid,int expected){
        System.out.println(String.format("grid=%s, expected=%d",join(grid),expected));
        Solution solution = new Solution();
        int result = solution.cherryPickup(grid);
        System.out.println(String.format("result=%d",result));
        aassert(result == expected);
    }
    
    public static String join(int[][] ary){
        StringBuffer sb=new StringBuffer();
        sb.append("[");
        boolean isFirst=true;
        for(int[] v:ary){
            if(!isFirst){sb.append(",");}
            isFirst=false;
            sb.append(join(v));
        }
        sb.append("]");
        return sb.toString();
    }

    public static String join(int[] ary){
        StringBuffer sb=new StringBuffer();
        sb.append("[");
        boolean isFirst=true;
        for(int v:ary){
            if(!isFirst){sb.append(",");}
            isFirst=false;
            sb.append(Integer.toString(v));
        }
        sb.append("]");
        return sb.toString();
    }

    public static String join(Object[] ary){
        StringBuffer sb=new StringBuffer();
        sb.append("[");
        boolean isFirst=true;
        for(Object v:ary){
            if(!isFirst){sb.append(",");}
            isFirst=false;
            sb.append(v.toString());
        }
        sb.append("]");
        return sb.toString();
    }
    
    public static void aassert(boolean cond){
        if(!cond)throw new AssertionError();
    }
}
