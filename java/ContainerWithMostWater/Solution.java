package ContainerWithMostWater;

/**
 * Created by Luyz on 16/8/20.
 * https://leetcode.com/problems/container-with-most-water/
 */
public class Solution {
    public int maxArea(int[] height){
        int result = 0;
        int i = 0, j = height.length - 1;
        while (i < j){
            int heightI = height[i];
            int heightJ = height[j];
            int newSquare = (heightI<heightJ ? heightI: heightJ) * (j - i);
            result = result > newSquare?result:newSquare;
            if (heightI < heightJ){
                while (height[i] <= heightI && i < j){
                    i ++;
                }
            }
            else {
                while (height[j] <= heightJ && i < j){
                    j --;
                }
            }
        }
        return result;
    }

    public int maxArea2(int[] height) {
        // Take the wrong question.
        // I thought the container won't split the water inside.

        int leftmaxIndex = 0, rightmaxIndex = height.length - 1;
        int mostLeft = 0, mostRight = 0;
        for (int i = 0; i < height.length; i++) {
            //left to right
            if (height[i] >= height[leftmaxIndex]){
                int newSize = height[leftmaxIndex] * (i - leftmaxIndex);
                mostLeft = newSize > mostLeft?newSize:mostLeft;
                leftmaxIndex = i;
            }
            if (height[height.length - i - 1] >= height[rightmaxIndex]) {
                int newSize = height[rightmaxIndex] * (rightmaxIndex - height.length + i + 1);
                mostRight = newSize > mostRight ? newSize : mostRight;
                rightmaxIndex = height.length - i - 1;
            }
        }
        return mostLeft>=mostRight?mostLeft:mostRight;
    }
}