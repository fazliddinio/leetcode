import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_minmaxGasDist_example1(solution):
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 9
    assert abs(solution.minmaxGasDist(stations, k) - 0.5) < 1e-5
    assert abs(solution.minmaxGasDist_heap(stations, k) - 0.5) < 1e-5

def test_minmaxGasDist_example2(solution):
    stations = [23, 24, 36, 39, 46, 56, 57, 65, 84, 98]
    k = 1
    assert abs(solution.minmaxGasDist(stations, k) - 14.0) < 1e-5
    assert abs(solution.minmaxGasDist_heap(stations, k) - 14.0) < 1e-5

def test_minmaxGasDist_few_stations(solution):
    stations = [10, 20]
    k = 4
    # 5 segments total, dist = 10 / 5 = 2.0
    assert abs(solution.minmaxGasDist(stations, k) - 2.0) < 1e-5
    assert abs(solution.minmaxGasDist_heap(stations, k) - 2.0) < 1e-5
