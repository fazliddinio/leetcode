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

def test_isPalindrome_optimal(solution):
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
    assert solution.isPalindrome("race a car") == False
    assert solution.isPalindrome(" ") == True

def test_isPalindrome_brute(solution):
    assert solution.isPalindrome_brute("A man, a plan, a canal: Panama") == True
    assert solution.isPalindrome_brute("race a car") == False
    assert solution.isPalindrome_brute(" ") == True
