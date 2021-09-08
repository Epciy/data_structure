from collections import deque
class Queue:
  def __init__(self):
    self.queue=deque()
  def enqueue(self,data):
    return self.queue.append(data)
  def peek(self):
    return self.queue[-1]
  def dequeue(self):
    return self.queue.pop()
  def is_empty(self):
    return self.queue==0
  def size(self):
    return len(self.queue)
  def print_f(self):
    return self.queue
if __name__=='__main__':
  pq=Queue()
  pq.enqueue({'company':'welamrt',
             'timestamp':'01.01.2021',
              'price':'855'})
  pq.enqueue({'company':'welamrt',
             'timestamp':'01.01.2021',
              'price':'855'})
  print(pq.queue)
  print(pq.peek())
  print(pq.print_f())