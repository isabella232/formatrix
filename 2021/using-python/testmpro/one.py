import time

class One():

  def __init__(self):
    pass

  def run(self, n, linkedlist:list):
    for i in range(2 * n):
      linkedlist.extend([i])
      print("Tick and testarg",n)
      time.sleep(1)