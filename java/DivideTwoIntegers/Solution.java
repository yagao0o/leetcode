package DivideTwoIntegers;

class Solution {
    public static int divide(int dividend, int divisor) {
        if (divisor == 1) {
            return dividend;
        }
        else if(divisor == -1) {
            if (dividend == (-1 << 31)) {
                return ~(-1 << 31);
            }
            return -dividend;
        }
        else if (divisor == (-1 << 31)) {
            if (dividend == divisor) {
                return 1;
            }
            else {
                return 0;
            }
        }
        int result = 0;

        boolean isNegative = divisor < 0;
        if (isNegative) {
            divisor = -divisor;
        }
        if (dividend < 0) {
            isNegative = !isNegative;
            if (dividend == (-1 << 31)) {
                dividend += divisor;
                result += 1;
            }
            dividend = -dividend;
        }
        int leftTimes = 0;
        int counter = 1;

        int currentVal = divisor;
        while (currentVal < dividend) {
            int newCurrentVal = currentVal << 1;
            if (newCurrentVal < 0){
                while (dividend > currentVal){
                    dividend -= currentVal;
                    result += counter;
                }
            }
            else {
                currentVal = newCurrentVal;
                leftTimes += 1;
                counter = counter << 1;
            }
        }
        while (leftTimes >= 0) {
            while (dividend >= currentVal){
                dividend -= currentVal;
                result += counter;
            }
            currentVal = currentVal >> 1;
            counter = counter >> 1;
            leftTimes -= 1;
        }
        return isNegative?-result:result;
    }
}
