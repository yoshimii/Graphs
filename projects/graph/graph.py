"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue
        q = Queue()
        # enque starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty:
        while q.size() > 0:
            # Dequeue the first index
            v = q.dequeue()
            # Check if it's been visited
            if v not in visited:
            # If it has not been visited
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
                # create an empty queue
        q = Stack()
        # enque starting vertex_id to the queue
        q.push(starting_vertex)
        # create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty:
        while q.size() > 0:
            # Dequeue the first index
            v = q.pop()
            # Check if it's been visited
            # If it has been visited
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                print(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)

    def dft_recursive(self, vertex, visited=None, path=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        s = Stack() # neighbors to pop off and check if in visited
        s.push(vertex)
        # Check if the node is visited
        # Hint: https://docs.python-guide.org/writing/gotchas/
        # If not...
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Print
                print(v)
                # Call DFT_Recursive on each child
                for neighbor in self.get_neighbors(v):
                        s.push(neighbor)
            

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        path = [starting_vertex]
        q.enqueue(path)
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            p1 = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            d = p1[-1]            
            # CHECK IF IT'S THE TARGET
                # IF SO, RETURN THE PATH
            if d == destination_vertex:
                return p1
            # Check if it's been visited
            # If it has not been visited...
            if d not in visited:
                # Mark it as visited
                visited.add(d)
                # Then add A PATH TO all neighbors to the back of the queue
                for neighbor in self.get_neighbors(d):
                    # (Make a copy of the path before adding)
                    path_copy = p1.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
                    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        path = [starting_vertex]
        s.push(path)
        visited = set()
        while s.size() > 0:
            p1 = s.pop()
            p = p1[-1]
            if p == destination_vertex:
                return p1
            if p not in visited:
                visited.add(p)
                for neighbor in self.get_neighbors(p):
                    path_copy = p1.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        s = Stack()
        path = [starting_vertex]
        s.push(path)
        while s.size() > 0:
            p1 = s.pop()
            p = p1[-1]
            if p == destination_vertex:
                return p1
            if p not in visited:
                visited.add(p)
                print(p)
                for neighbor in self.get_neighbors(p):
                    path_copy = p1.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
