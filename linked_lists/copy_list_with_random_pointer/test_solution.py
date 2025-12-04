import pytest
from .solution import Solution, SolutionMap, Node

def create_random_list(data):
    # data: list of [val, random_index]
    if not data: return None
    nodes = [Node(x[0]) for x in data]
    for i, node in enumerate(nodes):
        if i < len(nodes) - 1:
            node.next = nodes[i+1]
        random_idx = data[i][1]
        if random_idx is not None:
            node.random = nodes[random_idx]
    return nodes[0]

def list_to_data(head):
    if not head: return []
    nodes = []
    curr = head
    idx_map = {}
    i = 0
    while curr:
        nodes.append(curr)
        idx_map[curr] = i
        curr = curr.next
        i += 1
        
    res = []
    for node in nodes:
        rand_idx = idx_map[node.random] if node.random else None
        res.append([node.val, rand_idx])
    return res

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionMap])
@pytest.mark.parametrize(
    "data",
    [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]],
        [],
    ],
)
def test_copy_random_list(SolutionClass, data):
    solution = SolutionClass()
    head = create_random_list(data)
    copy = solution.copyRandomList(head)
    assert list_to_data(copy) == data
    # Ensure deep copy
    if head:
        assert head is not copy
        assert head.next is not copy.next
