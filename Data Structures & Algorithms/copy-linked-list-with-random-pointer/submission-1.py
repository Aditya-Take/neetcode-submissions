"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        old_to_new = {}
        cur = head

        while cur:
            node = Node(cur.val)
            old_to_new[cur] = node
            cur = cur.next
        
        cur = head
        while cur:
            new_node = old_to_new[cur]
            new_node.next = old_to_new.get(cur.next) 
            new_node.random = old_to_new.get(cur.random) 
            cur = cur.next
        
        return old_to_new[head]