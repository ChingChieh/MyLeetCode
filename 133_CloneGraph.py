class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node == None:
            return None
        if len(node.neighbors) == 0:
            n = Node()
            n.val = node.val
            return n
        
        resultDict = dict() 
        nodeSet = set() 
        todoList = list() 
        neighborValList = []
        resultList = list()
        todoList.append(node)

        while todoList != []:
            nd = todoList.pop(0)
            nodeSet.add(nd)
            for i in range(len(nd.neighbors)):
                neighbor = nd.neighbors[i]
                neighborValList.append(neighbor.val)
                if neighbor not in nodeSet:
                    nodeSet.add(neighbor)
                    todoList.append(neighbor)
            resultDict[nd.val] = neighborValList
            neighborValList = []
        
        for i in range(1, len(nodeSet) + 1):
            resultList.append(resultDict.get(i))
            n = Node()
            n.val = i
            neighborValList.append(n)
        # print(resultList)
        # print(neighborValList)
        for index, n in enumerate(neighborValList):
            for idx in resultList[index]:
                n.neighbors.append(neighborValList[idx - 1])
        
        return neighborValList[0]