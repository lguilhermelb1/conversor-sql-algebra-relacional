from sqlalchemy import null


class Node:
   def __init__(self, id, label):
      self.id = id
      self.label = label
      self.pai = None

   def setPai(self,node):
      self.pai = node