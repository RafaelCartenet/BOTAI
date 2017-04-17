from Policy import *

from numpy.random import choice

class randompolicy(Policy):
    def __init__(self):
        Policy.__init__(self)

    def ChooseAction(self, seendata, ts):
        a = ["Call", "Put", "Pass"]
        c = choice(a)
        if c == "Call":
            a = self.call(50)
        elif c == "Put":
            a = self.put(50)
        else:
            a = self.pass_()
        return a
