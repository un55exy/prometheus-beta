from typing import Dict, List, Set

def detect_cycle_undirected(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if an undirected graph contains a cycle using Depth-First Search (DFS).
    
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
    
    # Set to keep track of visited nodes
    visited: Set[int] = set()
    
    def dfs(node: int, parent: int) -> bool:
        """
        Depth-First Search to detect cycle.
        
        Args:
            node (int): Current node being explored
            parent (int): Parent node of the current node
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        # Mark the current node as visited
        visited.add(node)
        
        # Explore all adjacent nodes
        for neighbor in graph.get(node, []):
            # Skip the parent node to avoid false cycle detection
            if neighbor == parent:
                continue
            
            # If the neighbor is already visited, we found a cycle
            if neighbor in visited:
                return True
            
            # Recursively explore the neighbor
            if dfs(neighbor, node):
                return True
        
        return False
    
    # Check for cycles in every connected component
    for node in graph:
        # If this node is not visited, explore its entire component
        if node not in visited:
            # If a cycle is found in this component, return True
            if dfs(node, -1):
                return True
    
    return False