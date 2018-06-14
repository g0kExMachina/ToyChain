import time
import random
from hashlib import sha256
from block import *
from transcation import *
import json

class blockchain:
  def __init__(self):
    self.chain = []
    self.create_genesis()
    self.unpro_txn = []

  def create_genesis(self):
    genesis = block(0,[],0,0)
    self.mine_block(genesis)

  def create_blocks(self):
    prev_hash = self.latest().hashed
    timestamp  = time.time()
    # Change incoming: merkle - get_merkle
    mt = [self.unpro_txn]
    mt,transactions = self.get_merkle(self.unpro_txn,mt)
    mt.append(transactions)
    #Debug Step. Delete.
    print("Merkle Tree:{}".format(mt))
    index = self.latest().index + 1
    new_block = block(index,transactions,prev_hash,timestamp)
    new_block.tree = mt
    self.mine_block(new_block)
    self.unpro_txn = []

  def mine_block(self,block):
  	block.nonce = 0
  	hashed = block.create_hash()
  	while not hashed.startswith('0' * 2):
  		block.nonce += 1
  		hashed = block.create_hash()
  	block.hashed = hashed
  	self.chain.append(block)
  	self.print_OnMine(block)

  def print_OnMine(self, block):
  	print("Mined Block with Index: {}".format(block.index))
  	print("Block Hash: {}".format(block.hashed))
  	print("Nonce: {}".format(block.nonce))
  	print("Prev Hash: {}".format(block.prev_hash))
  	print("*****"*14)
  	print("Transcations: {}".format(block.transactions))
  	print("*****"*14)
  	print("-----" * 14 )

  def get_merkle(self,txn_list,merkle_tree):
  	merkle_list = []
  	for i in range(0,len(txn_list),2):
  		hash_left = sha256(txn_list[i].encode())
  		if i+1 < len(txn_list):
  			hash_right = sha256(txn_list[i+1].encode())
  		else:
  			hash_right = hash_left
  		both = hash_left.hexdigest() + hash_right.hexdigest()
  		merkle_list.append(both)
  	merkle_tree.append(merkle_list)
 
  	if len(merkle_list) > 1 :
  		return self.get_merkle(merkle_list,merkle_tree)
  	elif len(merkle_list) == 1:
  		return merkle_tree,(sha256(json.dumps(merkle_list,sort_keys=True).encode()).hexdigest())


  def make_transactions(self,sender,receiver,value):
    new_trans = transactions(sender,receiver,value)
    self.unpro_txn.append(new_trans.create_hash())

  def verify_transaction(self,txn_hash,block):
  	""" 
	Simple Method: take the hash. find it's position in the block.tree list. Remove it 
	and recompute merkle tree. Check with the the transaction

	Sophisticated Method: Take only the necessary hashes to compute.

  	"""
  	txn_list = block.tree
  	for i in txn_tree[0]:
  		if txn_hash == txn_tree[i]:
  			txn_tree[i] == txn_hash

  	_,recomputedHash = get_merkle(txn_list,txn_list)
  	if recomputedHash == block.tree[-1]:
  		print("The Transaction Veified: {}".format(recomputedHash))


  def latest(self):
    return self.chain[-1]