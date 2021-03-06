# Author  :  Yagao0o
# Date    :  2015-02-15
# Source  :  https://oj.leetcode.com/problems/simplify-path/

# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        result = []
        paths = path.split('/')
        for i in paths:
            if i == '.' or not i:
                continue
            elif i == "..":
                if result:
                    result.pop(len(result) - 1)
            else:
                result.append('/' + i)
        return "".join(result) if result else "/"