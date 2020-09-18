from typing import List

class Solution:
    inStack = 1
    notVisited = 2
    Visited = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        table = dict()
        is_AbleToFind = True
        result = list()
        for course in prerequisites:
            if course[1] in table:
                table[course[1]].append(course[0])
            else:
                table[course[1]] = [course[0]]
        
        nodeStatus = {k: Solution.notVisited for k in range(numCourses)}

        print(table)

        def dfs(course):
            nonlocal is_AbleToFind

            if not is_AbleToFind:
                return
            
            if course in table:
                for c in table[course]:
                    print(c)
                    if nodeStatus[c] == Solution.notVisited:
                        nodeStatus[c] = Solution.Visited
                        dfs(c)
                    elif nodeStatus[c] == Solution.Visited:
                        is_AbleToFind = False
            
            nodeStatus[course] = Solution.inStack
            result.append(course)
        
        for course in range(numCourses):
            if nodeStatus[course] == Solution.notVisited:
                dfs(course)

        print(is_AbleToFind)
        if is_AbleToFind:
            return result[::-1]
        else:
            return []

if __name__ == "__main__":
    sol = Solution()
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(sol.findOrder(numCourses, prerequisites))
                    
                
        
        