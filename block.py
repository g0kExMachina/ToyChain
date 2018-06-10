from hashlib import sha256
import json
import random


class block:
  def __init__(self,index,transactions,prev_hash,timestamp):
    self.index = index
    self.transactions = transactions
    self.prev_hash = prev_hash
    self.timestamp = timestamp
    self.nonce = random.randint(0,50000)
  
  def create_hash(self):
    string = json.dumps(self.__dict__,sort_keys=True)
    return sha256(string.encode()).hexdigest()

# Debug Function. Delete
  def print_block(self):
    print(self.__dict__)