import copy
class Node():
    idd = 0
    cost = 0
    path = None

inp = input().split()
numNodes = int(inp[0])
numEdges = int(inp[1])

mat = [[0 for x in range(numNodes)]for y in range(numNodes)]
#build adjacency matrix
for i1 in range(numEdges):
    inp = input().split()
    n1 = int(inp[0])
    n2 = int(inp[1])
    weight = int(inp[2])
    if (mat[n1-1][n2-1] == 0 or mat[n1-1][n2-1] > weight):   
        mat[n1-1][n2-1] = weight
        mat[n2-1][n1-1] = weight

visited = [False for x in range(numNodes)]
visited[0] = True
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
    for x in queue:
        if (x.cost < minval):
            minval = x.cost
            mini = index
        index += 1
    return mini

while len(queue) != 0:
    curr = queue.pop(findMin())
    if (curr.idd != numNodes-1):
        for j in range(numNodes):
            if (mat[curr.idd][j] != 0):
                #print("mod:")
                #print (curr.idd, j)
                newNode = nodeArr[j]
                newWeight = mat[curr.idd][j] + curr.cost
                #print (newWeight, newNode.cost)
                #print ("")
                if (visited[j] == False and newWeight < newNode.cost):
                    newNode.cost = newWeight
                    #newPath = copy.deepcopy(curr.path)
                    #newPath.append(str(curr.idd+1))
                    #newNode.path = newPath
                    newNode.parent = curr
                    queue.append(newNode)
        visited[curr.idd] = True
        #numLeft-=1
    else:
        break

if (nodeArr[numNodes-1].cost == pow(10,10)):
    print (-1)
else:
    # nodeArr[numNodes-1].path.append(str(numNodes))
    # str1 = " ".join(nodeArr[numNodes-1].path)
    # print (str1)

    l = []
    n = nodeArr[numNodes-1]
    while (n.idd != 0):
        l.append(str(n.idd+1))
        n = n.parent
    l.append("1")
    l.reverse()
    str1 = " ".join(l)
    print (str1)
    
    