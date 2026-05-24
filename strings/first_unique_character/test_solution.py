import pytest
import importlib.util
import os

@pytest.fixture
def solution():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "solution.py")
    spec = importlib.util.spec_from_file_location("local_solution", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()

def test_firstUniqChar_optimal(solution):
    assert solution.firstUniqChar("leetcode") == 0
    assert solution.firstUniqChar("loveleetcode") == 2
    assert solution.firstUniqChar("aabb") == -1

def test_firstUniqChar_brute(solution):
    assert solution.firstUniqChar_brute("leetcode") == 0
    assert solution.firstUniqChar_brute("loveleetcode") == 2
    assert solution.firstUniqChar_brute("aabb") == -1
