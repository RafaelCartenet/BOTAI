################################################################################
# BOTAI
################################################################################
# https://github.com/RafaelCartenet/BOTAI
# This simulator predicts the efficiency of a given strategy. According to a
# period of time, it will use the strategy policy in order to simulate bets,
# compute the results, and gives statistics, in order to have an idea about the
# efficiency of the model.

# Martingale Policy.
# Strategy:
# - Always bet either on calls either on puts, stick to one action.
# - Bet an initial bet. (init)
# - if you were right, bet the initial bet. (init)
# - if you were wrong, bet ratio times the previous bet
# - if the strike price is equal, bet the same amount than previous time step
# - and so on.


# Policy Parent class.
from Policy import *

# Libraries
from numpy.random import choice

class martingalepolicyUD(Policy):
    def __init__(self, ratio=2.5, init=1):
        Policy.__init__(self, "MartinGale " + str(ratio))
        self.reinvestratio = ratio
        self.init = init
        self.amount = self.init

    def ChooseAction(self, seendata, ts):
        if ts == 0:
            return self.call(self.init)
        else:
            prev = self.getPreviousAction()
            if prev.isRight:
                if prev.isEqual:
                    return self.call(prev.amount)
                return self.call(self.init)
            else:
                if prev.type == "Call":
                    return self.put(prev.amount * self.reinvestratio)
                else:
                    return self.call(prev.amount * self.reinvestratio)
