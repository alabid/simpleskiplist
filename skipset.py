"""
skipset.py
Contains skipset algorithms
all encapsulated in SkipSet 
class
"""
import math
import random
from skipnode import *



class SkipSet:
    # constants
    MAX_LEVEL = 6
    p = 0.5

    # initializer
    def __init__(self):
        self.level = 0
        self.header = SkipNode(SkipSet.MAX_LEVEL, None)
        
    # print method
    def __repr__(self):
        curr = self.header.forward[0]
        pstring = "{"
        
        while curr != None:
            pstring += str(curr.value)
            
            curr = curr.forward[0]
            if curr != None:
                pstring += ", "
                
        return pstring + "}"
    
    # contains: returns true if value is contained in the list
    def contains(self, value):
        curr = self.header
        for i in range(self.level, -1, -1):
            while curr.forward[i] != None and \
                    curr.forward[i].value < value:
                curr = curr.forward[i]
        curr = curr.forward[0]
        
        return curr != None and curr.value == value
        
    # find and record traversal update[i]
    # returns update[] and insertion/deletion point
    def findandupdate(self, value):
        update = [None]*(SkipSet.MAX_LEVEL+1)
        curr = self.header
        
        for i in range(SkipSet.MAX_LEVEL, -1, -1):
            while curr.forward[i] != None \
                    and curr.forward[i].value < value:
                curr = curr.forward[i]
            update[i] = curr
                
        return (curr.forward[0], update)
            

    # insert method
    def insert(self, value):
        curr, update = self.findandupdate(value)
        
        if curr == None or curr.value != value:
            newlevel = self.randomlevel()

            if newlevel > self.level:
                for i in range(self.level+1, newlevel+1):
                    update[i] = self.header

                self.level = newlevel
                
            newnode = SkipNode(newlevel, value)

            for i in range(0, newlevel+1):
                newnode.forward[i] = update[i].forward[i]
                update[i].forward[i] = newnode

    # deletemethod
    def delete(self, value):
        curr, update = self.findandupdate(value)

        if curr != None and curr.value == value:
            # found it. Remove from list
            for i in range(0, self.level+1):
                if update[i].forward[i] != curr:
                    break
                update[i].forward[i] = curr.forward[i]

            # decrease list level if the node deleted
            # had the highest level in the skip list
            while self.level > 0 and \
                    self.header.forward[self.level] == None:
                self.level -= 1

    """
    randomlevel:
    random level generator for skip list node
    """
    def randomlevel(self):
        level = 1
        while random.random() < SkipSet.p and level < SkipSet.MAX_LEVEL:
            level = level + 1
        return level

    
    






