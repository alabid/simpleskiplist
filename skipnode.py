"""
skipnode.py
contains definition of node structure used in skip list
"""

class SkipNode:
    def __init__(self, level, val):
        self.value = val
        self.forward = [None]*(level+1) # array of pointers


