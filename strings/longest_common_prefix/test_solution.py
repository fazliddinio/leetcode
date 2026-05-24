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

def test_longestCommonPrefix_optimal(solution):
    assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == ""

def test_longestCommonPrefix_brute(solution):
    assert solution.longestCommonPrefix_brute(["flower","flow","flight"]) == "fl"
    assert solution.longestCommonPrefix_brute(["dog","racecar","car"]) == ""
