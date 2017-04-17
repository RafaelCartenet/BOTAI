

class Engine:

    def __init__(self, data, policy, stats):
        self.data = data
        self.policy = policy
        self.SPs = data.SPs
        self.dates = data.dates
        self.nbtimesteps = self.data.getN()
        self.stats = stats

    def result_action(self, action, timestep):
        action.isEqual = False
        if action.type == "Put":
            if self.SPs[timestep + 1] < self.SPs[timestep]:
                result = action.ratio*action.amount
                action.isRight = True
            elif self.SPs[timestep +1] == self.SPs[timestep]:
                result = 0
                action.isRight = True
                action.isEqual = True
            else:
                result = -action.amount
                action.isRight = False
        elif action.type == "Call":
            if self.SPs[timestep + 1] > self.SPs[timestep]:
                result = action.ratio*action.amount
                action.isRight = True
            elif self.SPs[timestep + 1] == self.SPs[timestep]:
                result = 0
                action.isRight = True
                action.isEqual = True
            else:
                result = -action.amount
                action.isRight = False
        else:
            result = 0
        return result

    def run(self):
        for ts in range(self.nbtimesteps-1):
            seenSPs = self.SPs[:ts]
            seendates = self.dates[:ts]

            action = self.policy.ChooseAction(seenSPs, ts)

            result = self.result_action(action, ts)

            self.stats.update(ts, action, result)
