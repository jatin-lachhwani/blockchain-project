from config import pij,fast_cij,slow_cij,dij_numerator,NODE_LIMIT
from config import LOW,HIGH
from peer import Peer
import random
class links:
    def __init__(self,list_peers,peer_network) -> None:
        """
        Node limit is NODE_LIMIT it can not exceed that
        """
        n = len(peer_network)
        self.links_info={}
        for i in range(n):
            for j in peer_network[i]:
                if i<j:
                    self.links_info[get_key(i,j)]= list_peers[i].link_speed and list_peers[j].link_speed
        print(self.links_info)
    def latency(self,i,j,pkt_size):
        print(self.get_link_info(i,j))
        cij = fast_cij if self.get_link_info(i,j) else slow_cij
        dij = random.expovariate(cij/dij_numerator) 
        delay = pij + pkt_size/cij +dij# note pkg_size must be in kb
        return delay
    def get_link_info(self,i,j):
        val=-1
        try:
            val=self.links_info[get_key(i,j)]
        except KeyError:
            print(f"direct link between {i} and {j} does not exist.")
            exit(1)
        return val



def get_key(i,j):
    if i==j:
        raise Exception("a node can not link to itself")
    if i>j:
        i,j=j,i
    return (NODE_LIMIT+1)*i+j


# peer_network=[[5, 9, 3, 1], [9, 4, 8, 5, 3, 6, 0], [3, 6, 7, 4, 9], [6, 9, 2, 7, 1, 0], [9, 1, 5, 6, 2], [8, 0, 4, 1], [3, 2, 4, 1, 9], [3, 9, 8, 2], [5, 1, 7, 9], [1, 4, 3, 0, 7, 6, 8, 2]]
# list_peers='list'
# all_links = links(list_peers,peer_network)