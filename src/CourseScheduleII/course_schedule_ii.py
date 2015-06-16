# Author  :  Yagao0o
# Date    :  2015-02-19
# Source  :  https://leetcode.com/problems/course-schedule-ii/

# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs,
# return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them.
# If it is impossible to finish all courses, return an empty array.
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0.
#  So the correct course order is [0,1]
#
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
# Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
# Another correct ordering is[0,2,1,3].


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        # {node:[[nodes point to],[nodes point from]]}
        graph = {}
        for i in range(numCourses):
            graph[i] = [[], []]
        for pre_re in prerequisites:
            graph[pre_re[0]][1].append(pre_re[1])
            graph[pre_re[1]][0].append(pre_re[0])
        S = []
        L = []
        for i in range(numCourses):
            if not graph[i][1]:
                S.append(i)
        while S:
            new_node = S.pop(0)
            L.append(new_node)
            point_nodes = graph.pop(new_node)[0]
            for l_node in point_nodes:
                graph[l_node][1].remove(new_node)
                if not graph[l_node][1]:
                    S.append(l_node)
        if graph:
            return []
        else:
            return L