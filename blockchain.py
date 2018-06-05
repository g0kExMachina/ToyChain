import time

class block:
	def __init__(self,index,timestamp,prev_hash,transcations):
		self.index = index
		self.timestamp = time.time()
		self.prev_hash = prev_hash
		self.transcations = transcations

	def calculate_hash(self):
		pass

	def transcation_hash(self):
		pass


class transcations:

	def __init__(self,input_addr,output_addr,value):
		self.input = input_addr
		self.output = output_addr
		self.value = value

class blockchain:

	def __init__(self):
		self.unconfirmed_trancation = []
		self.chain = []
		self.create_genesis()

	def create_genesis(self):
		pass

