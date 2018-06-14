import json
from hashlib import sha256
import uuid
import string

class transactions:
  def __init__(self,sender,receiver,value):
  	# self.id = str(uuid.uuid4()).replace('-','')
  	self.sender = sender
  	self.receiver = receiver
  	self.value = value

  def to_dict(self):
    return self.__dict__


  def create_hash(self):
    string = json.dumps(self.__dict__,sort_keys=True)
    return sha256(string.encode()).hexdigest()