
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

class Put(Action):
    def __init__(self, amount):
        Action.__init__(self, amount)
        self.type = "Put"

    def toStr(self):
        return self.type + "\t|" + "%.2f" % self.amount + "\t\t|" + str(self.isRight)

class Call(Action):
    def __init__(self, amount):
        Action.__init__(self, amount)
        self.type = "Call"

    def toStr(self):
        return self.type + "\t|" + "%.2f" % self.amount + "\t\t|" + str(self.isRight)

class Pass(Action):
    def __init__(self):
        Action.__init__(self,None)
        self.type = "Pass"

    def toStr(self):
        return self.type + "\t|" + "\t|"
