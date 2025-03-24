from typing import Dict, List, Set, Tuple

def detect_cycle_undirected(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if an undirected graph contains a cycle using Union-Find algorithm.
    
    Args:
        graph (Dict[int, List[int]]): An adjacency list representation of the graph
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if the graph contains a cycle, False otherwise.
    
    Raises:
        ValueError: If the input graph is empty or None.
    """
    # Validate input
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Initialize parent and rank for Union-Find
    parent: Dict[int, int] = {}
    rank: Dict[int, int] = {}
    
    # Initialize parent and rank for each node
    for node in graph:
        parent[node] = node
        rank[node] = 0
    
    def find(x: int) -> int:
        """
        Find the root of a node with path compression.
        
        Args:
            x (int): Node to find the root for
        
        Returns:
            int: Root of the node
        """
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x: int, y: int) -> bool:
        """
        Union two sets. 
        
        Args:
            x (int): First node
            y (int): Second node
        
        Returns:
            bool: True if a cycle is formed, False otherwise
        """
        root_x = find(x)
        root_y = find(y)
        
        # If roots are the same, a cycle is found
        if root_x == root_y:
            return True
        
        # Union by rank
        if rank[root_x] < rank[root_y]:
            root_x, root_y = root_y, root_x
        
        parent[root_y] = root_x
        
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1
        
        return False
    
    # Check for cycles by checking all unique edges
    processed_edges: Set[Tuple[int, int]] = set()
    
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            # Avoid processing the same edge twice
            if (neighbor, node) in processed_edges:
                continue
            
            # If union finds an existing connection, a cycle exists
            if union(node, neighbor):
                return True
            
            processed_edges.add((node, neighbor))
    
    return False