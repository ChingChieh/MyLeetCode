class Solution:
    def numIslands(self, List) -> int:
        count = 0
        Map = list()
        tmpList = list()
        for i in range(len(List)):
            for j in range(len(List[0])):
                tmpList.append(False)
            Map.append(tmpList)
            tmpList = []

        for i in range(len(List)):
            for j in range(len(List[0])):
                if Map[i][j] == False:  #代表還沒走過
                    Map[i][j] = True #標示成走過了
                    if List[i][j] == "0": #可以直接跳過了
                        continue
                    else:
                        # 我想從這個點開始做 recursive 然後把走過的點標起來
                        count += 1
                        markIsland(Map, List, i, j)

                if Map[i][j] == True:   #代表走過了
                    pass

        print(Map)
        return count
def goUp(Map, List, i, j):
    if i == 0 or Map[i - 1][j] or List[i - 1][j] == "0":
        return False
    else:
        return True

def goRight(Map, List, i, j):
    if j == len(List[0]) - 1 or Map[i][j + 1] or List[i][j + 1] == "0":
        return False
    else:
        return True

def goDown(Map, List, i, j):
    if i == len(List) - 1 or Map[i + 1][j] or List[i + 1][j] == "0":
        return False
    else:
        return True

def goLeft(Map, List, i, j):
    if j == 0 or Map[i][j - 1] or List[i][j - 1] == "0":
        return False
    else:
        return True

def markIsland(Map, List, i, j):
    # 如果怎樣都走不下去就 return False
    up = goUp(Map, List, i, j)
    right = goRight(Map, List, i, j)
    down = goDown(Map, List, i, j)
    left = goLeft(Map, List, i, j)
    if (not up) and (not right) \
        and (not down) and (not left):
        return 
    if up:
        Map[i - 1][j] = True
        markIsland(Map, List, i - 1, j)
    if right:
        Map[i][j + 1] = True
        markIsland(Map, List, i, j + 1)
    if down:
        Map[i + 1][j] = True
        markIsland(Map, List, i + 1, j)
    if left:
        Map[i][j - 1] = True
        markIsland(Map, List, i, j - 1)
    
    return 

if __name__ == "__main__":
    grid = [
        ["1","1","0","1","0"],
        ["1","1","1","1","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","1"]
    ]

    sol = Solution()
    print(sol.numIslands(grid))