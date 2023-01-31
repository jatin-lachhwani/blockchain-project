from random import randint
from peer import Peer
##########################################################
# function to create slow links and low cpu
def generate_set(n,percent):
    nlow=int(n*(percent/100))
    ans_set=set()
    while len(ans_set) < nlow:
        ans_set.add(randint(0,n-1))
    return ans_set

# create the list of peers satisfying the number of slow,fast links and low,high cpu.
def get_list_peers(n,set_slow,set_lowcpu,t_tx,NUM_TXN):
    from config import LOW,HIGH
    peer_lst=[]
    for i in range(n):
        link_speed = LOW if i in set_slow else HIGH
        compute = LOW if i in set_lowcpu else HIGH
        peer = Peer(i,link_speed,compute,t_tx,NUM_TXN)
        peer_lst.append(peer)
    return peer_lst

##########################################################
# Create network of peers
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
        connected=check_connected(lst,n)
        if connected==False:
            lst = [[] for i in range(n)]
            var = [0]*n
    return lst
##########################################################