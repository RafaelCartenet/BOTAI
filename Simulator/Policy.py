################################################################################
# BOTAI
################################################################################
# https://github.com/RafaelCartenet/BOTAI
# This simulator predicts the efficiency of a given strategy. According to a
# period of time, it will use the strategy policy in order to simulate bets,
# compute the results, and gives statistics, in order to have an idea about the
# efficiency of the model.

from Action import *
import numpy as np

class Policy:
    def __init__(self, name="PolicyName"):
        self.takenactions = np.array([])
        self.name = name
        return

    def getPreviousAction(self):
        return self.takenactions[-1]

    def call(self, amount):
        action = Call(amount)
        self.takenactions = np.append(self.takenactions, action)
        return action

    def put(self, amount):
        action = Put(amount)
        self.takenactions = np.append(self.takenactions, action)
        return action

    def pass_(self):
        action = Pass()
        self.takenactions = np.append(self.takenactions, action)
        return action

    def ChooseAction(self, seendata, timestep):
        # to Redefine
        return
