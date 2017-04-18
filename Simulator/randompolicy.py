################################################################################
# BOTAI
################################################################################
# https://github.com/RafaelCartenet/BOTAI
# This simulator predicts the efficiency of a given strategy. According to a
# period of time, it will use the strategy policy in order to simulate bets,
# compute the results, and gives statistics, in order to have an idea about the
# efficiency of the model.

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
