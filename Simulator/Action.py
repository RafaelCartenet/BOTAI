################################################################################
# BOTAI
################################################################################
# https://github.com/RafaelCartenet/BOTAI
# This simulator predicts the efficiency of a given strategy. According to a
# period of time, it will use the strategy policy in order to simulate bets,
# compute the results, and gives statistics, in order to have an idea about the
# efficiency of the model.

# Different possible actions, put, call, or not doing anything: pass.

# Action parent class
class Action:
    def __init__(self, amount):
        self.amount = amount
        self.ratio = 0.88
        self.isRight = None
        self.isEqual = None
        self.profit = 0
        self.type = "None"

    def toStr(self):
        return "not rewritten function, please rewrite"


# Put class
class Put(Action):
    def __init__(self, amount):
        Action.__init__(self, amount)
        self.type = "Put"

    def toStr(self):
        return self.type + "\t|" + "%.2f" % self.amount + "\t\t|" + str(self.isRight)


# Call class
class Call(Action):
    def __init__(self, amount):
        Action.__init__(self, amount)
        self.type = "Call"

    def toStr(self):
        return self.type + "\t|" + "%.2f" % self.amount + "\t\t|" + str(self.isRight)


# Pass class
class Pass(Action):
    def __init__(self):
        Action.__init__(self,None)
        self.type = "Pass"

    def toStr(self):
        return self.type + "\t|" + "\t|"
