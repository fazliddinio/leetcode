import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_accounts_merge_example1(solution):
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]
    result = solution.accountsMerge(accounts)
    result_sorted = sorted([acc[0:1] + sorted(acc[1:]) for acc in result])
    expected = sorted([["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
                       ["John","johnnybravo@mail.com"],
                       ["Mary","mary@mail.com"]])
    assert result_sorted == expected

def test_accounts_merge_example2(solution):
    accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
                ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
                ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
                ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
                ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"],
                ["Gabe","Gabe0@m.co","Gabe5@m.co","Gabe2@m.co"]]
    result = solution.accountsMerge(accounts)
    result_sorted = sorted([acc[0:1] + sorted(acc[1:]) for acc in result])
    expected = sorted([["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
                       ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe2@m.co","Gabe3@m.co","Gabe5@m.co"],
                       ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
                       ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
                       ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]])
    assert result_sorted == expected

def test_accounts_merge_single_account(solution):
    accounts = [["Alex","alex@mail.com"]]
    result = solution.accountsMerge(accounts)
    assert result == [["Alex","alex@mail.com"]]

def test_accounts_merge_dfs_example1(solution):
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]
    result = solution.accountsMerge_dfs(accounts)
    result_sorted = sorted([acc[0:1] + sorted(acc[1:]) for acc in result])
    expected = sorted([["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
                       ["John","johnnybravo@mail.com"],
                       ["Mary","mary@mail.com"]])
    assert result_sorted == expected
