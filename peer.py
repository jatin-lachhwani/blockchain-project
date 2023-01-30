import numpy as np
class Peer:
    def __init__(self,id,link_speed,compute,t_tx,num_tx) -> None:
        self._id=id
        self.id='P'+str(id) # string or int
        self.link_speed=link_speed # slow or fast
        self.compute=compute # low_cpu or high_cpu
        self.t_tx_time_list = self.get_tx_time_list(t_tx,num_tx)# time of transaction event generation for this peer
        pass
    def get_tx_time_list(self,t_tx,num_tx) :
        expo_values = np.random.exponential(t_tx,num_tx)
        time=0
        time_lst=[]
        for i in expo_values:
            time+=i
            time_lst.append(time)
        return time_lst
    def info(self):
        print("id:",self.id)
        print("link_speed:","fast" if self.link_speed else "slow")
        print("compute:","high_cpu" if self.compute else "low_cpu")
        print("txn_time_list:",self.t_tx_time_list)
        print("---------------------------------------------------------")