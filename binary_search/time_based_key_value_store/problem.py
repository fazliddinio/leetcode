"""
==========================================
  Time Based Key-Value Store (LeetCode 981)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Design a time-based key-value data structure that can store multiple
values for the same key at different time stamps and retrieve the key's
value at a certain timestamp.

Implement the TimeMap class:
    - TimeMap() Initializes the object.
    - void set(String key, String value, int timestamp) Stores the key
      with the value at the given timestamp.
    - String get(String key, int timestamp) Returns a value such that set
      was called previously, with timestamp_prev <= timestamp. If there
      are multiple such values, it returns the value associated with the
      largest timestamp_prev. If there are no values, it returns "".

Example 1:
    Input: ["TimeMap", "set", "get", "get", "set", "get"]
           [[], ["foo","bar",1], ["foo",1], ["foo",3], ["foo","bar2",4], ["foo",4]]
    Output: [null, null, "bar", "bar", null, "bar2"]

Constraints:
    - 1 <= key.length, value.length <= 100
    - key and value consist of lowercase English letters and digits.
    - 1 <= timestamp <= 10^7
    - All timestamps are strictly increasing for set calls.
    - At most 2 * 10^5 calls will be made to set and get.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

A dictionary that remembers WHEN each value was stored. When you ask for
a value at time T, you get the most recent value that was stored at or
before time T.

    set("foo", "bar", time=1)     → foo's history: [(1, "bar")]
    get("foo", time=1) → "bar"    (exact match at time 1)
    get("foo", time=3) → "bar"    (no new value, use latest: time 1)
    set("foo", "bar2", time=4)    → foo's history: [(1,"bar"), (4,"bar2")]
    get("foo", time=4) → "bar2"   (exact match at time 4)
    get("foo", time=3) → "bar"    (time 3 < 4, so use time 1's value)

How it works:
  - Store: dictionary → key: list of (timestamp, value) pairs
  - Get: binary search the timestamps for the largest one ≤ query time

    foo's timestamps: [1, 4]
    get(foo, 3): binary search for 3 → closest ≤ 3 is 1 → "bar"
    get(foo, 5): binary search for 5 → closest ≤ 5 is 4 → "bar2"
"""
