from typing import List
import collections

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d = list()
        for point in points:
            val = point[0]**2 + point[1]**2
            d.append((point, val))
        
        #print(d)
        d = [v for v in sorted(d, key=lambda x: x[1])]
        #print(d)
        counter = 0
        result = list()
        for v in d:
            if counter == K:
                break
            result.append(v[0])
            counter += 1
        #print(result)
        return result

if __name__ == "__main__":
    sol = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    sol.kClosest(points, K)