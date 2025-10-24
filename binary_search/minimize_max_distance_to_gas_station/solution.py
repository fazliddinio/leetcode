# LeetCode 774: Minimize Max Distance to Gas Station
# Time: O(n * log(max_gap / precision)), Space: O(1)

class Solution:
    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        def count_stations(d):
            count = 0
            for i in range(len(stations) - 1):
                count += int((stations[i + 1] - stations[i]) / d)
            return count
        
        l, r = 0, stations[-1] - stations[0]
        while r - l > 1e-6:
            mid = (l + r) / 2
            if count_stations(mid) <= k:
                r = mid
            else:
                l = mid
        return r
