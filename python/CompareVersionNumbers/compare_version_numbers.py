# Author  :  Yagao0o
# Date    :  2015-01-24
# Source  :  https://oj.leetcode.com/problems/compare-version-numbers/

# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three",
# it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        version1_vers = version1.split('.')
        version2_vers = version2.split('.')
        level = 0
        while level < len(version1_vers) or level < len(version2_vers):
            if level >= len(version1_vers):
                current_level_version1 = 0
            else:
                current_level_version1 = int(version1_vers[level])
            if level >= len(version2_vers):
                current_level_version2 = 0
            else:
                current_level_version2 = int(version2_vers[level])
            if current_level_version1 > current_level_version2:
                return 1
            elif current_level_version1 < current_level_version2:
                return -1
            else:
                level += 1
        return 0