from random import randint
from config import L_CONN,H_CONN
def random_peers(source,n):
    num_conn=randint(L_CONN,H_CONN)
    conn_set=set()
    while len(conn_set)<num_conn:
        peer=randint(0,n-1);
        if peer != source:
            conn_set.add(peer)
    lst=list(conn_set)
    lst.sort()
    return lst

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

def create_connected_network(n):
    connected=False
    lst=[]
    while not connected:
        e_lst=[]
        lst= [e_lst for i in range(n)]
        lst = [random_peers(i,n) for i in range(n)]
        connected=check_connected(lst,n)
        if not connected:
            lst=[]
    return lst

print(create_connected_network(10))