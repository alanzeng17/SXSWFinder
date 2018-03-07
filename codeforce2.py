import copy
class Node():
    node = 0
    value = 0
    #visited = []
    path = []

class adjObj():
    nodeNum = 0
    pathWeight = 0

inp = input().split()
numNodes = int(inp[0])
numEdges = int(inp[1])

def foundPath(z, n):
    for x in n.path:
        if (str(z+1) == x):
            return False
    return True

def foundAdj(i, l):
    for x in l:
        if (i == x.nodeNum):
            return x.pathWeight
    return -1

def adjVal (i, l):
    for x in l:
        if (i == x.nodeNum):
            x.pathWeight = i

a = adjObj()
mat = [[0 for x in range(numNodes)]for y in range(numNodes)]
alist = [[a for x in range(numNodes)]]

print (alist)

#build adjacency list
for i1 in range(numEdges):
    inp = input().split()
    n1 = int(inp[0]) - 1
    n2 = int(inp[1]) - 1
    weight = int(inp[2])
    
    #if not in linked list or the weight is smaller
    val = foundAdj(n2, alist[n1])
    if (val == -1):
        newNo = adjObj()
        newNo.nodeNum = n2
        newNo.pathWeight = weight
        alist.append(newNo)
    elif(val > weight):
        adjVal(weight, alist[n1])

    # if (mat[n1-1][n2-1] == 0 or mat[n1-1][n2-1] > weight):   
    #     mat[n1-1][n2-1] = weight
    #     mat[n2-1][n1-1] = weight


# #build adjacency matrix
# for i1 in range(numEdges):
#     inp = input().split()
#     n1 = int(inp[0])
#     n2 = int(inp[1])
#     weight = int(inp[2])
#     if (mat[n1-1][n2-1] == 0 or mat[n1-1][n2-1] > weight):   
#         mat[n1-1][n2-1] = weight
#         mat[n2-1][n1-1] = weight
    

n = Node()
n.node = 0
n.value = 0
n.path.append("1")
#buildNode(n)

end = numNodes - 1 

queue = []
queue.append(n)
found = 0

check = pow(10,5)
pathsave = ""

while(len(queue) != 0):
    curr = queue.pop(0)
    if (curr.node == end and curr.value < check):
        check = curr.value
        found = 1
        str1 = " ".join(curr.path)
        pathsave = str1
    elif (curr.value > check):
        continue
    else:
        #curr.visited[curr.node] = 1

        for i in range(numNodes):
            jk = i
            f = foundPath(jk, curr)
            val = foundAdj (i, alist[curr.node])
            if (val != -1 and f):
                new = Node()
                new.node = i
                new.value = curr.value + mat[curr.node][i]
                #buildNode(new)
                #new.visited = copy.deepcopy(curr.visited)
                new.path = copy.deepcopy(curr.path)
                new.path.append(str(i+1))
                index = 0
                f = 0
                for q in queue:
                    if (new.value < q.value):
                        queue.insert (index, new)
                        f = 1
                        break
                    index += 1
                if (f == 0):
                    queue.append(new)

if (found == 0):
    print (-1)
else:
    print (pathsave)
