from random import randint
from peer import Peer
def generate_set(n,percent):
    nlow=int(n*(percent/100))
    ans_set=set()
    while len(ans_set) < nlow:
        ans_set.add(randint(0,n-1))
    return ans_set

def get_list_peers(n,set_slow,set_lowcpu,t_tx,NUM_TXN):
    from config import LOW,HIGH
    peer_lst=[]
    for i in range(n):
        link_speed = LOW if i in set_slow else HIGH
        compute = LOW if i in set_lowcpu else HIGH
        peer = Peer(i,link_speed,compute,t_tx,NUM_TXN)
        peer_lst.append(peer)
    return peer_lst