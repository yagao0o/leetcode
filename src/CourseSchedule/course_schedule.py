# Author  :  Yagao0o
# Date    :  2015-02-19
# Source  :  https://leetcode.com/problems/course-schedule/

# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0,
# and to take course 0 you should also have finished course 1. So it is impossible.
#
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices.

# Hints:
# This problem is equivalent to finding if a cycle exists in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
#
# Topological Sort via DFS( https://class.coursera.org/algo-003/lecture/52 )
#  - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
#
# Topological sort could also be done via BFS( http://en.wikipedia.org/wiki/Topological_sorting#Algorithms ).


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        # {node:[[nodes point to],[nodes point from]]}
        graph = {}
        for i in range(numCourses):
            graph[i] = [[], []]
        for pre_re in prerequisites:
            graph[pre_re[0]][0].append(pre_re[1])
            graph[pre_re[1]][1].append(pre_re[0])
        S = []
        for i in range(numCourses):
            if not graph[i][1]:
                S.append(i)
        while S:
            new_node = S.pop(0)
            point_nodes = graph.pop(new_node)[0]
            for l_node in point_nodes:
                graph[l_node][1].remove(new_node)
                if not graph[l_node][1]:
                    S.append(l_node)
        if graph:
            return False
        else:
            return True