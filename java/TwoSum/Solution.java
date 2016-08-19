package TwoSum;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Luyz on 16/8/19.
 * https://leetcode.com/problems/two-sum/
 */
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i]) && nums[i] * 2 == target){
                result[0] = map.get(nums[i]);
                result[1] = i;
                return  result;
            }
            map.put(nums[i], i);
        }
        for(Integer key:map.keySet()){
            if (map.containsKey(target - key)) {
                result[0] = map.get(key);
                result[1] = map.get(target - key);
                break;
            }
        }
        return result;
    }
}
