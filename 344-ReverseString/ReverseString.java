public class ReverseString{

  // time limit exceed
  public String reverseString(String s){
    String rs = "";
    for(int i=s.length()-1; i>=0; i--){
      rs += s.substring(i, i+1);
    }
    return rs;
  }

  // passed test cases
  public String reverseStringByStringBuilder(String s){
    // can also use StringBuffer -- thread safe
    // return new StringBuffer(s).reverse().toString();
    
    // use reverse function provided by StringBuilder -- not thread safe
    return new StringBuilder(s).reverse().toString();
  }

  public static void main(String[] args){
    ReverseString sol = new ReverseString();
    System.out.println(sol.reverseString("happy"));
  }
}
