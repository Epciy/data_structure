#  implementation stack:
from collections import deque
class Stack :
  def __init__(self):
    self.container=deque()
  def push(self,data):
    return self.container.append(data)
  def pop(self):
    return self.container.pop()
  def peek(self):
    return self.container[-1]
  def is_empty(self):
    return len(self.container)==0
  def size(self):
    return len(self.container)