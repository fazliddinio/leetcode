import pytest
from solution import TimeMap, TimeMapLinear

@pytest.fixture
def time_map():
    return TimeMap()

@pytest.fixture
def time_map_linear():
    return TimeMapLinear()

def test_timeMap_example1(time_map, time_map_linear):
    for tm in [time_map, time_map_linear]:
        tm.set("foo", "bar", 1)
        assert tm.get("foo", 1) == "bar"
        assert tm.get("foo", 3) == "bar"
        tm.set("foo", "bar2", 4)
        assert tm.get("foo", 4) == "bar2"
        assert tm.get("foo", 5) == "bar2"

def test_timeMap_missing_key(time_map, time_map_linear):
    for tm in [time_map, time_map_linear]:
        assert tm.get("missing", 1) == ""

def test_timeMap_timestamp_too_early(time_map, time_map_linear):
    for tm in [time_map, time_map_linear]:
        tm.set("foo", "bar", 5)
        assert tm.get("foo", 2) == ""
