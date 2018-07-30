package CountAndSay;

class Solution {
    public String countAndSay(int n) {
        String s = "1";
        for (int i = 0; i < n - 1; i++) {
            StringBuffer sb = new StringBuffer();
            char[] chars = s.toCharArray();
            char c = ' ';
            int idx = 0;
            int count = 0;
            while (idx < chars.length) {
                if (chars[idx] == c) {
                    count += 1;
                } else {
                    if (count > 0) {
                        sb.append(count).append(c);
                    }
                    c = chars[idx];
                    count = 1;
                }
                idx += 1;
            }
            if (count > 0) {
                sb.append(count).append(c);
            }
            s = sb.toString();
        }
        return s;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
//        for (int i = 0; i < 20; i++) {
//            System.out.println(s.countAndSay(i + 1));
//        }
//        System.out.println();
        System.out.println(s.countAndSay(70));
    }
}
