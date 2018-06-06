from hashlib import sha256
import json
import time


class block:
  def __init__(self,index,transactions,prev_hash,timestamp):
    self.index = index
    self.transactions = transactions
    self.prev_hash = prev_hash
    self.timestamp = timestamp
    self.nonce = 0
  
  def create_hash(self):
    string = json.dumps(self.__dict__,sort_keys=True)
    return sha256(string.encode()).hexdigest()

# Debug Function. Delete
  def print_block(self):
    print(self.__dict__)



class blockchain:
  def __init__(self):
    self.chain = []
    self.create_genesis()

  def create_genesis(self):
    genesis = block(0,[],0,0)
    self.mine_block(genesis)

  def create_blocks(self,transactions):
    prev_hash = self.latest().hashed
    timestamp  = time.time()
    index = self.latest().index + 1
    new_block = block(index,transactions,prev_hash,timestamp)
    self.mine_block(new_block)

  def iterate_blocks(self):
    for b in self.chain:
      print(b.hashed)
      print(b.prev_hash)
      print(b.nonce)

  def mine_block(self,block):
    block.nonce = 0
    hashed = block.create_hash()
    while not hashed.startswith('0' * 4):
      block.nonce += 1
      hashed = block.create_hash()
    block.hashed = hashed
    self.chain.append(block)

  def latest(self):
    return self.chain[-1]