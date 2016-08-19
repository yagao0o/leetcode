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
        graph_dic = self.travel(node)
        graph_node_dic = {}
        min_key = None
        for key in graph_dic:
            if min_key is None or min_key > key:
                min_key = key
            graph_node_dic[key] = UndirectedGraphNode(key)
        for key in graph_dic:
            for neighbor in graph_dic[key]:
                graph_node_dic[key].neighbors.append(graph_node_dic[neighbor])
        return graph_node_dic[min_key]

    def travel(self, node):
        if node is None:
            return None
        traveled = []
        result_dic = {}
        current = [node]
        while current:
            new = current.pop(0)
            traveled.append(new.label)
            neighbors_label = []
            for neighbor in new.neighbors:
                if neighbor.label not in traveled:
                    current.append(neighbor)
                neighbors_label.append(neighbor.label)
            result_dic[new.label] = neighbors_label
        return result_dic