class SingleNumber{
    public int[] singleNumber(int[] nums){
        int result[] = new int[2];
        int oxResult = 0;
        for(int num : nums){
          oxResult ^= num;
        }
        int signal = oxResult & (~oxResult+1);
        
        for(int num : nums){
          if((num & signal) == 0){
            result[0] ^= num;
          }else{
            result[1] ^= num;
          }
        }
        return result;
    }

    public static void main(String[] args){
        SingleNumber sn = new SingleNumber();
        int[] arr = {1,2,3,2,3,5}; 
        int[] result = sn.singleNumber(arr);
        for(int num : result){
          System.out.print(num + " ");
        }
        System.out.println();
    }
}
