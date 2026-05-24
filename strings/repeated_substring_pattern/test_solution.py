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

def test_repeatedSubstringPattern_optimal(solution):
    assert solution.repeatedSubstringPattern("abab") == True
    assert solution.repeatedSubstringPattern("aba") == False
    assert solution.repeatedSubstringPattern("abcabcabcabc") == True

def test_repeatedSubstringPattern_brute(solution):
    assert solution.repeatedSubstringPattern_brute("abab") == True
    assert solution.repeatedSubstringPattern_brute("aba") == False
    assert solution.repeatedSubstringPattern_brute("abcabcabcabc") == True
