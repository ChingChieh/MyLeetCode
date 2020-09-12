class Solution:
    def __init__(self):
        self.Map = []
        self.grid = []
        self.width = 0
        self.length = 0
        self.counter = 0
        self.I = 0
        self.J = 0
    def goUp(self, I, J):
        print("UP")
        if I == 0 or self.Map[I - 1][J] or self.grid[I - 1][J] == "0":
            return False
        else:
            self.I = I - 1
            self.Map[self.I][J] = True
            print(self.I, J)
            return True
    def goRight(self, I, J):
        print("RIGHT")
        if J == (self.width - 1) or self.Map[I][J + 1] or self.grid[I][J + 1] == "0":
            return False
        else:
            self.J = J + 1
            self.Map[I][self.J] = True
            print(I, self.J)
            return True
    def goDown(self, I, J):
        print("DOWN")
        if I == (self.length - 1) or self.Map[I + 1][J] or self.grid[I + 1][J] == "0":
            return False
        else:
            self.I = I + 1
            self.Map[self.I][J] = True
            print(self.I, J)
            return True
    def goLeft(self, I, J):
        print("LEFT")
        if J == 0 or self.Map[I][J - 1] or self.grid[I][J - 1] == "0":
            return False
        else:
            self.J = J - 1
            self.Map[I][self.J] = True
            print(I, self.J)
            return True

    def markIsland(self, I, J):
        search = True
        c = 0
        self.I = I
        self.J = J
        while(search):
            if not self.goUp(self.I, self.J) and not self.goRight(self.I, self.J) and not self.goDown(self.I, self.J) and not self.goLeft(self.I, self.J):
                search = False
            c += 1
            # if not self.goUp(I, J):
            #     pass 
            # elif not self.goRight(I, J):
            #     pass 
            # elif not self.goDown(I, J):
            #     pass 
            # elif not self.goLeft(I, J):
            #     pass
            # else:
            #     search = False
        
    def numIslands(self, grid) -> int:
        self.grid = grid
        self.width = len(self.grid[0])
        self.length = len(self.grid)

        for i in range(len(grid)):
            tmpList = []
            for j in range(len(grid[i])):
                tmpList.append(False)
            self.Map.append(tmpList)

        for i in range(len(grid)):
            for idx, value in enumerate(grid[i]):
                if self.Map[i][idx]:
                    pass
                else:
                    if value == "1":
                        self.counter += 1
                        self.Map[i][idx] = True
                        self.markIsland(i, idx)
                print("-----------")
        return self.counter


if __name__ == "__main__":
    grid = [
        ["1","1","0","1","0"],
        ["1","1","1","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","1"]
    ]

    sol = Solution()
    print(sol.numIslands(grid))