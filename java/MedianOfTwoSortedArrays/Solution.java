package MedianOfTwoSortedArrays;

/**
 * Created by Luyz on 16/8/19.
 */
public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2){
        int[] mergedList = merge(nums1, nums2);
        return findMedianFromList(mergedList, 0, mergedList.length - 1);
    }

    public double findMedianSortedArrays2(int[] nums1, int[] nums2) {
        int headA = 0,headB =0;
        int tailA = nums1.length - 1, tailB = nums2.length - 1;
        while (headA <= tailA && headB <= tailB && leftNumbers(headA, tailA, headB, tailB) > 2){
            if (nums1[headA] <= nums2[headB]){
                headA += 1;
            }
            else {
                headB += 1;
            }
            if (nums1[tailA] <= nums2[tailB]){
                tailB -= 1;
            }
            else {
                tailA -= 1;
            }
        }
        if (headA > tailA){
            return findMedianFromList(nums2, headB, tailB);
        }
        if (headB > tailB){
            return  findMedianFromList(nums1, headA, tailA);
        }
        return (0.0 + nums1[headA] + nums2[headB])/2.0;
    }

    private int leftNumbers(int headA, int tailA, int headB, int tailB){
        return tailA - headA + 1 + tailB - headB + 1;
    }

    private double findMedianFromList(int[] nums, int start, int end){
        while (start < end - 1){
            start += 1;
            end -= 1;
        }
        if(start == end){
            return nums[start];
        }
        else{
            return (0.0 + nums[start] + nums[end]) / 2.0;
        }
    }




    public int[] merge(int[] nums1, int[] nums2){
        int[] result = new int[nums1.length + nums2.length];
        int flag1 = 0;
        int flag2 = 0;
        while (flag1 < nums1.length && flag2 < nums2.length){
            if (nums1[flag1] < nums2[flag2]){
                result[flag1 + flag2] = nums1[flag1];
                flag1 += 1;
            }
            else {
                result[flag1 + flag2] = nums2[flag2];
                flag2 += 1;
            }
        }
        while (flag1 < nums1.length){
            result[flag1 + flag2] = nums1[flag1];
            flag1 += 1;
        }
        while (flag2 < nums2.length){
            result[flag1 + flag2] = nums2[flag2];
            flag2 += 1;
        }
        return result;
    }
}
