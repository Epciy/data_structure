class BinarySearchTreeNode:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
  def add_child(self,data):
    if data == self.data :
      return 
    if data < self.data :
      # add to  left subtree
      if self.left :
        self.left.add_child(data)
      else :
        self.left=BinarySearchTreeNode(data)
    else :
      # add to right subtree
      if self.right :
        self.right.add_child(data)
      else :
        self.right=BinarySearchTreeNode(data)


  def in_order_traversal(self):
    elements =[]

    # visit left tree 
    if self.left :
      elements +=self.left.in_order_traversal()

    # visit  base node 
    elements.append(self.data)

    # visit right tree 
    if self.right :
      elements += self.right.in_order_traversal()
    return elements

  def find_max(self):
    if self.right is None :
      return self.data 
    
    return self.right.find_max()
  def find_min(self) :
    if self.left is None :
      return self.data
    return self.left.find_min()


  def delete(self, val):
    if val< self.data :
      if self.left :
        self.left=self.left.delete(val)
    elif val> self.data :
      if self.right:
        self.right=self.right.delete(val)
    else :
      if self.right is None and self.left is None :
        return None 

      if self.left is None :
        return self.right 
      if self.right is None :
        return self.left
      
      min_val=self.right.find_min()
      
      self.data=min_val
      self.right=self.right.delete(min_val)
    return self

  def search_tree(self,val):
    if self.data == val :
      return True 
    if val < self.data :
      # val might be in left subtree 
      if self.left :
        return self.left.search_tree(val)
      else :
        return False
    if val> self.data :
      # val might be in right subtree
      if self.right :
        return self.right.search_tree(val)
      else :
        return False


def build_binary_tree(elements):
  root=BinarySearchTreeNode(elements[0])

  for i in range(1,len(elements)):
    root.add_child(elements[i])
  return root

if __name__=='__main__':
  numbers=[17,2,24,15,8,45,2,12]
  numb_tree= build_binary_tree(numbers)
  print(numb_tree.search_tree(21))
  numb_tree.delete(2)
  print(numb_tree.in_order_traversal())