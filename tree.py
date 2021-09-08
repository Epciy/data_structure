#@ simple tree
class TreeNode:
  def __init__(self, data):
    self.data=data
    self.children=[]
    self.parent=None


  def add_child(self, child):
        child.parent=self
        self.children.append(child)
  def get_level(self):
    level=0
    p=self.parent 
    while p:
      level +=1
      p=p.parent
    return level

  def print_tree(self):
    spaces= ' ' * self.get_level()*3
    prfx= spaces + "|__"  if self.parent else ''
    
    print(prfx+self.data)
    for child in self.children :
      if self.children:
        child.print_tree()
     

def build_product_tree():
  root=TreeNode('electornics')
  laptop=TreeNode('laptop')
  laptop.add_child(TreeNode('Macbook'))
  laptop.add_child(TreeNode('hp'))
  laptop.add_child(TreeNode('lenovo'))

  cellphone=TreeNode('cellphone')
  cellphone.add_child(TreeNode('iphone'))
  cellphone.add_child(TreeNode('huwaei'))
  cellphone.add_child(TreeNode('nokia'))
    

  tv=TreeNode('tv')
  tv.add_child(TreeNode('samsung'))
  tv.add_child(TreeNode('LG'))
     

  root.add_child(laptop)
  root.add_child(cellphone)
  root.add_child(tv)



  #print(tv.get_level())
  return root


if __name__=='__main__':
  root=build_product_tree()
  root.print_tree()
  #print(tv.get_level())#@ simple tree
class TreeNode:
  def __init__(self, data):
    self.data=data
    self.children=[]
    self.parent=None


  def add_child(self, child):
        child.parent=self
        self.children.append(child)
  def get_level(self):
    level=0
    p=self.parent 
    while p:
      level +=1
      p=p.parent
    return level

  def print_tree(self):
    spaces= ' ' * self.get_level()*3
    prfx= spaces + "|__"  if self.parent else ''
    
    print(prfx+self.data)
    for child in self.children :
      if self.children:
        child.print_tree()
     

def build_product_tree():
  root=TreeNode('electornics')
  laptop=TreeNode('laptop')
  laptop.add_child(TreeNode('Macbook'))
  laptop.add_child(TreeNode('hp'))
  laptop.add_child(TreeNode('lenovo'))

  cellphone=TreeNode('cellphone')
  cellphone.add_child(TreeNode('iphone'))
  cellphone.add_child(TreeNode('huwaei'))
  cellphone.add_child(TreeNode('nokia'))
    

  tv=TreeNode('tv')
  tv.add_child(TreeNode('samsung'))
  tv.add_child(TreeNode('LG'))
     

  root.add_child(laptop)
  root.add_child(cellphone)
  root.add_child(tv)



  #print(tv.get_level())
  return root


if __name__=='__main__':
  root=build_product_tree()
  root.print_tree()
  #print(tv.get_level())#@ simple tree



 