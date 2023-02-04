import numpy as np
import random
from transactions import Transaction
class Peer:
    def __init__(self,id,link_speed,compute,t_tx,num_tx,num_peers) -> None:
        self._id=id
        self.id='P'+str(id) # string or int
        self.link_speed=link_speed # slow or fast
        self.compute=compute # low_cpu or high_cpu
        self.t_tx_time_list = self.get_tx_time_list(t_tx,num_tx)# time of transaction event generation for this peer
        self.tx_list=self.generate_tx_list(num_peers)
        pass
    def get_tx_time_list(self,t_tx,num_tx) :
        expo_values = np.random.exponential(t_tx,num_tx)
        time=0
        time_lst=[]
        for i in expo_values:
            time+=i
            time_lst.append(time)
        return time_lst

    def generate_tx_list(self,n) :
        tx_list=[]
        count=1
        for time in self.t_tx_time_list:
            peer=-1
            while peer ==-1 or peer==self._id:
                peer=random.randint(0,n-1)
            tx_list.append(Transaction(count,self._id,peer,time))
            count+=1
        return tx_list
        
        pass
    def info(self):
        print("id:",self.id)
        print("link_speed:","fast" if self.link_speed else "slow")
        print("compute:","high_cpu" if self.compute else "low_cpu")
        print("txn_time_list:",self.t_tx_time_list)
        print("txn_list:")
        for tx in self.tx_list:
            tx.info()
        print("---------------------------------------------------------")