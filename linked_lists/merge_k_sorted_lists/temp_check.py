import unittest
from solution import Solution, ListNode

# Helper to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to convert a linked list to a list of values
def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# We need to ensure ListNode is available. 
# Since solution.py imports ListNode but doesn't define it if it's not in the same file or standard lib (it's not standard),
# we might need to mock it or define it if solution.py fails to import. 
# However, solution.py usually assumes it exists in the environment (LeetCode).
# For local testing, we must define it and patch solution.py or inject it.
# Actually, looking at solution.py, it imports List, Optional but uses ListNode without importing it from anywhere specific?
# Wait, let's re-read solution.py for merge_k_sorted_lists.

# Re-reading:
# 10: from typing import List, Optional
# 11: import heapq
# 13: class Solution:
# 16:     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

# It uses ListNode but doesn't define it. This will fail locally unless we define it.
# I will define ListNode here and also monkeypatch it into the solution module if necessary, 
# OR I can just define it in tests.py and assume solution.py will use the one available in its scope? 
# No, solution.py is a separate module. It will fail with NameError: name 'ListNode' is not defined when loaded.
# I need to insert ListNode into solution.py's namespace or modify solution.py to include it.
# OR simpler: I write the definition in tests.py and adds it to solution's globals before importing Solution?
# No, I have to import Solution from solution.
# If I import solution, it will fail at class definition time if ListNode is in type hints? 
# Actually type hints `List[Optional[ListNode]]` will fail if ListNode is not defined.
# I might need to append the definition to solution.py or define it in a way that solution.py can see it.

# Best approach for these LeetCode files which are incomplete standalone:
# I will prepend the ListNode class definition to the solution.py file using `sed` or just rewrite it?
# Or I can just define it in tests.py and assume the user has it? No, the user wants me to write tests that run.
# I will modify solution.py to include the definition if it's missing, OR I will create a `list_node.py` and import it.
# But `solution.py` doesn't import it.

# Let's try to define it in tests.py and use `unittest.mock` to patch? 
# No, the file syntax itself is invalid if `ListNode` is not defined and used as a type hint.
# Wait, `from typing import ...` handles the types, but `ListNode` is a forward reference or a class.
# If it's used as `ListNode` it must be defined.

# I will define `ListNode` in `solution.py` for all these files if it's missing.
# That's the most robust way.

# But wait, checking `merge_k_sorted_lists/solution.py` again.
# It uses `ListNode(0)` in line 21. It definitely needs the class.
# I will Add ListNode definition to `solution.py`.

pass
