import copy
class Node():
    idd = 0
    cost = 0
    path = [] #instead of saving entire path, save next node, then iterate through
    parent = None

#index in adj array is the corresponding node
#key = node connection, value = weight of path
class Adj():
    def __init__(self):
        self.weights = {}


inp = input().split()
numNodes = int(inp[0])
numEdges = int(inp[1])

#z = Adj()
#adjArr = [z for x in range(numNodes)]
adjArr = []
for a in range(numNodes):
    x = Adj()
    adjArr.append(x)

for i in range(numEdges):
    inp = input().split()
    n1 = int(inp[0])-1
    n2 = int(inp[1])-1
    weight = int(inp[2])
    a = adjArr[n1]
    b = adjArr[n2]

    if (n2 in a.weights):
        if (a.weights[n2] > weight):
            a.weights[n2] = weight
    else:
        a.weights[n2] = weight

    if (n1 in b.weights):
        if (b.weights[n1] > weight):
            b.weights[n1] = weight
    else:
        b.weights[n1] = weight

#for a in adjArr:
 #   print (a.weights.items())

#mat = [[0 for x in range(numNodes)]for y in range(numNodes)]
#build adjacency matrix
# for i1 in range(numEdges):
#     inp = input().split()
#     n1 = int(inp[0])
#     n2 = int(inp[1])
#     weight = int(inp[2])
#     if (mat[n1-1][n2-1] == 0 or mat[n1-1][n2-1] > weight):   
#         mat[n1-1][n2-1] = weight
#         mat[n2-1][n1-1] = weight

visited = [False for x in range(numNodes)]

numLeft = numNodes-1
nodeArr = []
for j in range(numNodes):
    n = Node()
    n.idd = j
    n.cost = pow(10,10)
    nodeArr.append(n)

nodeArr[0].cost = 0
    

queue = []
queue.append(nodeArr[0])

def findMin():
    minval = pow(10,11)
    mini = 0
    index = 0
    for x in unvisited:
        if (x.cost < minval):
            minval = x.cost
            mini = index
        index += 1
    return mini

#  keyList = []
#  for i in range(numNodes):
#      keyList.append(adjArr[i].weights.keys())
#for i in range(numNodes-1):
while len(queue) != 0:
    curr = queue.pop(0)
    #curr = unvisited[findMin()]
    if (curr.idd != numNodes-1):
        currAdj = adjArr[curr.idd]
        for key in currAdj.weights.keys():
            newNode = nodeArr[key]
            newWeight = currAdj.weights[key] + curr.cost
            if (visited[key] == False and newWeight < newNode.cost):
                newNode.cost = newWeight
                #newPath = copy.deepcopy(curr.path)
                #newPath.append(str(curr.idd+1))
                #newNode.path = newPath
                newNode.parent = curr
                index = 0
                f = 0
                for z in queue:
                    if z.cost > newNode.cost:
                        queue.insert(index, newNode)
                        f = 1
                        break
                    index += 1
                if (f == 0):
                    queue.append(newNode)

        visited[curr.idd] = True
        #numLeft-=1
    else:
        break

if (nodeArr[numNodes-1].cost == pow(10,10)):
    print (-1)
else:
    #nodeArr[numNodes-1].path.append(str(numNodes))
    #str1 = " ".join(nodeArr[numNodes-1].path)
    l = []
    n = nodeArr[numNodes-1]
    while (n.idd != 0):
        l.append(str(n.idd+1))
        n = n.parent
    l.append("1")
    l.reverse()
    str1 = " ".join(l)
    print (str1)
    