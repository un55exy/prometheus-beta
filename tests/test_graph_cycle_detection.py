import pytest
from src.graph_cycle_detection import detect_cycle_undirected

def test_graph_with_cycle():
    """Test a graph that contains a cycle."""
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    assert detect_cycle_undirected(graph) == True

def test_graph_without_cycle():
    """Test a graph without a cycle (tree-like structure)."""
    graph = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [],
        4: [],
        5: []
    }
    assert detect_cycle_undirected(graph) == False

def test_empty_graph():
    """Test that an empty graph raises a ValueError."""
    with pytest.raises(ValueError):
        detect_cycle_undirected({})

def test_single_node_graph():
    """Test a graph with a single node."""
    graph = {0: []}
    assert detect_cycle_undirected(graph) == False

def test_disconnected_graph_with_no_cycle():
    """Test a disconnected graph without a cycle."""
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    assert detect_cycle_undirected(graph) == False

def test_disconnected_graph_with_cycle_one_component():
    """Test a disconnected graph with a cycle in the first component."""
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [4],
        4: [] 
    }
    assert detect_cycle_undirected(graph) == True

def test_complex_graph_cycle():
    """Test a more complex graph with a cycle."""
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1, 6],
        4: [1, 5],
        5: [2, 4, 6],
        6: [3, 5]
    }
    assert detect_cycle_undirected(graph) == True

def test_none_input():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError):
        detect_cycle_undirected(None)