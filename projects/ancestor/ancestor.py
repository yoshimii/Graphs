from util import Stack, Queue
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
            
class Graph:
    
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_ancestors(self, vertex_id):
        """
        Get all ancestors (parents) of a vertex.
        """
        return self.vertices[vertex_id]

    def earliest_ancestor(self, ancestors, starting_node):
        """
        1. Translate the problem into graph terminology:
         
            Return the furthest node from the starting node
        """
        # 2. Build your graph
        v0 = [i[1] for i in ancestors]
        v1 = [i[0] for i in ancestors]
        v0.extend(v1)
        vertexes = set(v0)
        # Add vertices
        for i in vertexes:
            self.add_vertex(i)
        # Add edges   
        for i in ancestors:
            self.add_edge(i[1], i[0])
        # Create an empty stack
        s = Stack()
        longest_path = [starting_node]
        visited = set()
        s.push(longest_path)
        while s.size() > 0:
            lp1 = s.pop()
            n = lp1[-1]            
            if len(lp1) > len(longest_path):
                longest_path = lp1
            if n not in visited:
                visited.add(n)
                for neighbor in self.get_ancestors(n):
                    path_copy = lp1.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)
        if len(longest_path) == 1:
            return -1
        else:
            return longest_path[-1]