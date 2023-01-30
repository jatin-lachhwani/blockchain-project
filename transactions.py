class Transaction:
    # size="1 KB"
    size=1#KB
    def __init__(self,id,from_peer,to_peer,amt,start_time) -> None:
        self._id=id
        self.id = 'T' + str(id)
        self.from_peer=from_peer
        self.to_peer=to_peer
        self.amt=amt
        self.start_time=start_time

    def info(self):
        print(self.id,":",self.from_peer,"pays",self.to_peer,self.amt,"coins")