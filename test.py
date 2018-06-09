from blockchain import block,blockchain,transactions
import uuid
import string
import random

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
  transcations = make_10transactions()
  new_blockchain = blockchain()
  for i in range(10):
    new_blockchain.create_blocks(transactions=transcations)
  new_blockchain.iterate_blocks()

def check_transactions():
  new_trans = transactions("Gokul","Alice",100)
  print(new_trans.to_dict())

def make_10transactions():
  transactions_list  =[]
  for i in range(10):
    sender = str(uuid.uuid4()).replace('-','')
    receiver = str(uuid.uuid4()).replace('-','')
    new_trans = transactions(sender,receiver,random.randint(50,5000))
    transactions_list.append(new_trans.to_dict())
  return transactions_list

  # Running Things

#check_mining_genesis()
#check_transactions()
create_10blocks()
#make_10transcations()

