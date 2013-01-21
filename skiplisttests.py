"""
SkipListTests:
contains skip lists tests
"""
from skipset import *


class SkipListTests:
    def __init__(self, testalgo=False):
        self.testalgorithms = testalgo

        self.ss = SkipSet()

    def run(self):
        if self.testalgorithms:
            print self.ss # should be empty
            for num in [5,10,7,6, 7, 8]:
                self.ss.insert(num)

            print self.ss # should now have [5,6,7,8,10]
            

            # should print "7 is in the list"
            if self.ss.contains(7):
                print "7 is in the list"
            else:
                print "7 is not in the list"
                
            # should print "-10 not in the list"
            if self.ss.contains(-10):
                print "-10 is in the list"
            else:
                print "-10 not in the list"
                
            # should print [5,6,7,8,10]                    
            print self.ss

            # should delete 7. 
            self.ss.delete(7)

            # should print "7 has been successfully deleted"
            if not self.ss.contains(7):
                print "7 has been successfully deleted"
        
            # should print [5,6,8,10]
            print self.ss

            # should delete 5
            self.ss.delete(5)
            self.ss.delete(20)

            # should print [6,8,10]
            print self.ss

            # should delete 8
            self.ss.delete(100)
            self.ss.delete(5)
            self.ss.delete(8)

            # should print [6,10]
            print self.ss

            # should delete [6, 10]
            self.ss.delete(6)
            self.ss.delete(8)
            self.ss.delete(10)
            self.ss.delete(-1)

            # should print [] (empty)
            print self.ss

            # should print False
            print self.ss.contains(8)

if __name__ == "__main__":
    SkipListTests(True).run()
