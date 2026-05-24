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

def test_canConstruct_optimal(solution):
    assert solution.canConstruct("a", "b") == False
    assert solution.canConstruct("aa", "ab") == False
    assert solution.canConstruct("aa", "aab") == True

def test_canConstruct_brute(solution):
    assert solution.canConstruct_brute("a", "b") == False
    assert solution.canConstruct_brute("aa", "ab") == False
    assert solution.canConstruct_brute("aa", "aab") == True
