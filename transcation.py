class transactions:
  def __init__(self,sender,receiver,value):
    self.sender = sender
    self.receiver = receiver
    self.value = value

  def to_dict(self):
    return self.__dict__