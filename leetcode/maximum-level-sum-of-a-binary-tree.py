# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math


class Solution:
    def maxLevelSum(self, root: TreeNode):
        bfs_queue = [(1, root)]
        sum_each_level = [-math.inf]
        while len(bfs_queue) > 0:
            (level, cursor) = bfs_queue.pop(0)
            if level >= len(sum_each_level):
                sum_each_level.append(cursor.val)
            else:
                sum_each_level[level] = cursor.val if sum_each_level[level] is None else sum_each_level[level] + (cursor.val or 0)
                    
            for neighbor in [cursor.left, cursor.right]:
                if neighbor is not None:
                    bfs_queue.append((level+1, neighbor))
        
        return sum_each_level.index(max(sum_each_level))


def list2tree(tree_list):
    """
    Inorder traverse.
    Args:
        tree_list ([type]): [description]
    """
    reside = len(tree_list)
    max_level = 1
    while reside > 0:
        max_level += 1
        reside = reside // 2
    
    root = TreeNode(val=tree_list[0])
    layers = [[root]]
    for level in range(1, max_level):
        level_layer = []
        start = 2**(level)-1
        end = start + 2*level
        for i in tree_list[start: end]:
            level_layer.append(TreeNode(val=i))
            
        # 0, 
        # 1,2
        # 3,4,5,6
        # 7,8,9,10,11,12,13,14
        layers.append(level_layer)
        
        for i, node in enumerate(layers[level-1]):
            try:
                node.left = layers[level][2*i]
                node.right = layers[level][2*i+1]
            except IndexError:
                break

    return root


list2tree([989,
           None,10250,
           98693,-89388,None,None,
           None,-32127])
list2tree([1,7,0,7,-8,None,None])

assert Solution().maxLevelSum(
    list2tree([-100,
               -200,-300,
               -20,-5,-10,None])
)==3
assert Solution().maxLevelSum(
    list2tree([989,None,10250,98693,-89388,None,None,None,-32127])
) == 2
assert Solution().maxLevelSum(
    list2tree([1,7,0,7,-8,None,None])
)== 2


