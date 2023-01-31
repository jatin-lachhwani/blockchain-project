from random import randint
from peer import Peer
from config import NUM_TXN
from functions import generate_set,get_list_peers,create_network
from create_link import links
READ_CONFIG=True
if READ_CONFIG :
    from config import n,z0,z1,t_tx
else :
    from cli_arg import n,z0,z1,t_tx # take args from command line
    pass

if __name__=="__main__":
    set_slow,set_lowcpu=generate_set(n,z0),generate_set(n,z1)
    list_peers = get_list_peers(n,set_slow,set_lowcpu,t_tx,NUM_TXN)
    peer_network = create_network(n)
    # for i in range(n):
    #     list_peers[i].info()
    print(peer_network)
    all_links = links(list_peers,peer_network)
    while True:
        i=input("i:")
        j=input("j:")
        pkt_size=input("pkt:")
        """all_links.latency(int(i),int(j),float(pkt_size)) """
        ### ^ use this function to get latency between i and j