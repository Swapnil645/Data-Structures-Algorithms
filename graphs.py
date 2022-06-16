'''
Adjacency List 
0 --> [1,4]
1 --> [0,2,3,4]
2 --> [1,3]
3 --> [1,2,4]
4 --> [0,1,3]

Adjacency list can tell which node is connecteted to what all nodes
like directly we can say node 0 is connected to 1 and 4
'''



import queue


class Graph:
    ''''Constructor creates adjancency list'''
    def __init__(self,num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            '''insert into right list according to the index'''
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return '\n'.join(["{}: {}".format(ind,value) for ind,value in enumerate(self.data)])
    
            
    # def __str__(self):
    #     return self.__repr__()


    def remove_edge(self,u,v):
        self.data[u].remove(v)
        self.data[v].remove(u)

    def add_edge(self,u,v):
        self.data[u].append(v)
        self.data[v].append(u)


def BFS(graph,root):
    queue=[]
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)


    discovered[root] = True
    queue.append(root)
    distance[root] = 0
    idx = 0 
    while idx < len(queue):
        current = queue[idx]
        #check the edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                discovered[node] = True
                parent[node] = current
                queue.append(node)
        idx += 1
    return queue,distance,parent




def DFS(graph,root):
    stack = []
    discovered = [False]* len(graph.data)
    result = []
    stack.append(root)
    while len(stack)>0:
        current = stack.pop()
        if not discovered[node]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)



''''DFS is not good for shortest path'''

'''
Directed -  if 0--->1    then in adjacency list there is a edge between 0 to 1 
not 1 to 0

Weighted - along with the edge, the weight of the edge is also given (x,y,z)
here x--->y is edge and z is weight of edge
'''



class AllGraphs:
    def __init__(self,num_nodes, edges,directed = False,weighted = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            '''insert into right list according to the index'''
            if self.weighted:
                node1,node2,weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1,node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)


    def __repr__(self):
        result = ''

        if self.weighted:
            for i,(nodes,weights) in enumerate(zip(self.data,self.weight)):
                result += '{}:{}\n'.format(i,list(zip(nodes,weights)))
        else:
            for i,nodes in enumerate(self.data):
                result += '{}:{}\n'.format(i,nodes)

        return result




            
    def __str__(self):
        return self.__repr__()




num_nodes = 5
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
num_nodes2 = 9
edges2 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]

num_nodes3 = 9
edges3 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]


obj1 = AllGraphs(num_nodes,edges)

obj2 = AllGraphs(num_nodes2,edges2)

obj3 = AllGraphs(num_nodes3,edges3,False,True)

obj4 = AllGraphs(num_nodes6,edges6,True,False)
print(obj1,'\n\n',obj2,'\n\n',obj3,'\n\n',obj4)


# q = BFS(obj,3)
# print(q)