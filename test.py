from block import *
from transcation import *
from blockchain import *
import uuid
import string
import random


def check_hash():
  transaction = [{"sender":"alice","receiver":"s"}]
  a = block(1,transaction,"rhfgrelgjp",15246)
  print(a.create_hash())
  a.print_block()
  print("--------------------------------------")

def print_genesis():
  a = blockchain()
  print(a.latest().index)
  print("--------------------------------------")

def create_10blocks():
  new_blockchain = blockchain()
  for i in range(10):
    make_10transactions(new_blockchain)
    new_blockchain.create_blocks()
  # new_blockchain.iterate_blocks()

def create_1blocks():
  new_blockchain = blockchain()
  check_transactions(new_blockchain)
  new_blockchain.create_blocks()

def check_transactions(new_blockchain):
  new_trans = new_blockchain.make_transactions("Gokul","Alice",5)

def make_10transactions(new_blockchain):
  for i in range(10):
    sender = str(uuid.uuid4()).replace('-','')
    receiver = str(uuid.uuid4()).replace('-','')
    new_trans = new_blockchain.make_transactions(sender,receiver,random.randint(50,5000))

  # Running Things

#check_mining_genesis()
#check_transactions()
create_10blocks()
# create_1blocks()
#make_10transcations()
