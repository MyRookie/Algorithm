#!/usr/bin/python3
import math

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.father = None
		self.height = 0

class AVL_Tree:
	def __init__(self):
		self.root = None

	def find(self,key):
		if self.root is None:
			return False
		else:
			return self._find(key,self.root)

	def _find(self,key,node):
		if node is None:
			return None
		elif key < node.data:
			_find(key,node.left)
		elif key > node.data:
			_find(key,node.right)
		else:
			return node

	def height(self,node):
		if node is None:
			return -1
		return node.height

	def singleLeftRotate(self,node):
		k1 = node.left
		node.left = k1.right
		k1.right = node

		node.height = max(self.height(node.right),self.height(node.left))+1
		k1.height = max(self.height(k1.left),node.height)+1
		return k1

	def singleRightRotate(self,node):
    	k1 = node.right
    	node.right = k1.left
    	k1.left = node
    	node.height = max(self.height(node.right),self.height(node.left))+1
    	k1.height = max(self.height(k1.right),node.height)+1
    	return k1

    def doubleRightRotate(self,node):
    	node.right = self.singleLeftRotate(node.right)
    	return self.singleRightRotate(node)

    def doubleLeftRotate(self,node):
    	node.left = self.singleRightRotate(node.left)
    	return self.singleLeftRotate(node)
    	
    def put(self,key):
    if not self.root:
        self.root=Node(key)
    else:
        self.root=self._put(key,self.root)
	def _put(self,key,node):
    	if node is None:
  	      node=Node(key)
  	  elif key<node.data:
    	    node.left=self._put(key,node.left)
        	if (self.height(node.left)-self.height(node.right))==2:
            	if key<node.left.data:
            	    node=self.singleLeftRotate(node)
            	else:
            	    node=self.doubleLeftRotate(node)
         
    	elif key>node.data:
    	    node.right=self._put(key,node.right)
        	if (self.height(node.right)-self.height(node.left))==2:
            	if key<node.right.data:
                	node=self.doubleRightRotate(node)
            	else:
                	node=self.singleRightRotate(node)
     
     
   		node.height=max(self.height(node.right),self.height(node.left))+1
    	return node


def Reverse(ptr):
	if ptr == None:
		return
	print ptr.data
	Reverse(ptr.left)
	Reverse(ptr.right)

def insert(n,ptr):
	print ptr.data
	if n > ptr.data and ptr.right == None:
		print "added right"
		ptr.right = Node(n)
		return True
	elif n < ptr.data and ptr.left == None:
		print "added left"
		ptr.left = Node(n)
		return True
	elif n < ptr.data:
		insert(n,ptr.left)
	else:
		insert(n,ptr.right)

	return False


def search(n,ptr):
	if ptr == None:
		return False
	print "checked :" + str(ptr.data)
	if n == ptr.data:
		return True
	elif n > ptr.data:
		search(n,ptr.right)
	else:
		search(n,ptr.left)

	return True

def remove(n,ptr):
	pass

if __name__ == "__main__":
	root = Node(input("Input thr root node:"))
	while(True):
		cmd = input("Input command:\n(1) insert\n(2) search\n(3) remove\n(4) reverse :")
		if cmd is 1:
			n = input("Input the node:\n")
			insert(n,root)
		elif cmd is 2:
			n = input("Input the node:\n")
			print search(n,root)
		elif cmd is 3:
			n = input("Input the node:\n")
			remove(n,root)
		elif cmd is 4:
			Reverse(root)
		else:
			print "wrong command"