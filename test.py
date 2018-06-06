from blockchain import block,blockchain

def check_hash():
  transaction = [{"sender":"alice","receiver":"s"}]
  a = block(1,transaction,"rhfgrelgjp",15246)
  print(a.create_hash())
  a.print_block()
  print("--------------------------------------")

def check_mining_genesis():
  a = block(0,[],0,0)
  chain = []
  a.nonce = 0
  hashed = a.create_hash()

  while not hashed.startswith('0'*4):
    a.nonce += 1
    hashed = a.create_hash()
  a.hashed = hashed
  chain.append(a)
  print(a.hashed)
  print(a.nonce)

def print_genesis():
  a = blockchain()
  print(a.latest().index)
  print("--------------------------------------")

def create_10blocks():
  transcations = [{"sender":"alice","receiver":"sink"}]
  new_blockchain = blockchain()
  for i in range(10):
    new_blockchain.create_blocks(transactions=transcations)
  new_blockchain.iterate_blocks()

  # Running Things

#check_mining_genesis()
create_10blocks()