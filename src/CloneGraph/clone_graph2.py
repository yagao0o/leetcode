# Author  :  Yagao0o
# Date    :  2015-05-26
# Source  :  https://leetcode.com/problems/clone-graph/

# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
#
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        traveled = []
        node_dic = {node.label: UndirectedGraphNode(node.label)}
        current = set([node])
        while current:
            new_travel = current.pop()
            traveled.append(new_travel.label)
            for neigh in new_travel.neighbors:
                neigh_label = neigh.label
                if neigh_label  not in node_dic:
                    node_dic[neigh_label] = UndirectedGraphNode(neigh_label)
                node_dic[new_travel.label].neighbors.append(node_dic[neigh_label])
                if neigh_label not in traveled:
                    current.add(neigh)
        return node_dic[node.label]