from random import randint
from config import L_CONN,H_CONN

def check_connected(lst,n):
    visited=[0]*n
    queue=[]
    queue.append(0)
    visited[0]=1
    while len(queue)>0:
        curr=queue.pop(0)
        for node in lst[curr]:
            if(visited[node]==0):
                queue.append(node)
                visited[node]=1
    for i in visited:
        if i==0:
            return False
    return True

def check_least_conn(var):
    for i in var:
        if i<L_CONN:
            return True
    return False

def create_network(n):
    lst = [[] for i in range(n)]
    var = [0]*n
    connected=False
    while not connected:
        while check_least_conn(var):
            x,y=randint(0,n-1),randint(0,n-1)
            if x==y : 
                continue
            if x not in lst[y]:
                if len(lst[x]) < H_CONN and len(lst[y]) < H_CONN:
                    lst[x].append(y)
                    var[x]+=1
                    lst[y].append(x)
                    var[y]+=1
            print("loop1")
        print("loop2")
        connected=check_connected(lst,n)
        if connected==False:
            lst = [[] for i in range(n)]
            var = [0]*n
    return lst
