from Policy import *

from numpy.random import choice

class martingalepolicy(Policy):
    def __init__(self, ratio=2.5, init=1):
        Policy.__init__(self, "MartinGale " + str(ratio))
        self.rr = ratio
        self.init = init
        self.amount = self.init

    def ChooseAction(self, seendata, ts):
        if ts == 0:
            return self.put(self.init)
        else:
            prev = self.getPreviousAction()
            if prev.isRight:
                if prev.isEqual:
                    return self.put(prev.amount)
                return self.put(self.init)
            return self.put(prev.amount * self.rr)
