from numpy import random
from config import MIN_AMT,MAX_AMT
class Transaction:
    # size="1 KB"
    size=1#KB
    def __init__(self,id,from_peer,to_peer,start_time) -> None:
        self._id=id
        self.id = 'P'+str(from_peer)+'T' + str(id)
        self.from_peer=from_peer
        self.to_peer=to_peer
        self.amt=random.uniform(MIN_AMT,MAX_AMT)
        self.start_time=start_time

    def info(self):
        print(self.id,":",self.from_peer,"pays",self.to_peer,self.amt,"coins")