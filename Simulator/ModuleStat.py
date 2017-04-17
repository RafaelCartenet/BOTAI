
# Libraries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class ModulStat():

    def __init__(self, data, initial_balance):
        self.init_bal = initial_balance
        self.profit = 0
        self.values = np.array([])
        self.balance = self.init_bal
        self.balance_ot = np.array([self.balance])
        self.balance_max = 0
        self.balance_min = 0
        self.data = data
        self.SPs = data.SPs
        self.dates = np.array(data.dates, dtype='S20')
        self.dates = mdates.num2date(mdates.datestr2num(self.dates))
        self.N = data.N
        self.takenactions = np.array([])
        self.nbactions = 0
        self.consRight = dict()
        self.consWrong = dict()
        self.ups = 0
        self.downs = 0
        self.equals = 0


################################################################################
# PLOT / RESULTS
################################################################################

    def plotdata(self):
        x = [i+1 for i in range(self.N)]
        plt.plot(x, self.SPs)
        #plt.xticks(x, self.dates, rotation='vertical')
        plt.margins(0.2)
        plt.subplots_adjust(bottom=0.15)
        plt.grid(True)
        plt.show()

    def plotbalance(self):
        x = [i+1 for i in range(self.N)]
        plt.plot(x, self.balance_ot)
        plt.title('Balance over time')
        #plt.xticks(x, self.dates, rotation='vertical')
        plt.subplots_adjust(bottom=0.15)
        plt.margins(0.2)
        plt.grid(True)
        plt.show()

    def normprice(self, price):
        r = "%.2f" % price
        r += "$"
        return r

    def actions_toStr(self):
        r = "-------------------------------------------------------------------------\n"
        r += "|#\t|Date\t\t|StackP\t|action\t|amount\t\t|result\t|balance\n"
        r += "-------------------------------------------------------------------------\n"
        for i in range(self.N-1):
            r += "|" + str(i+1) + "\t|"
            r += str(self.dates[i]) + "\t|"
            r += "%.5f" % self.SPs[i] + " |"
            r += self.takenactions[i].toStr() + "\t|"
            r += "%.2f" % self.balance_ot[i] + "\t"
            if self.takenactions[i].isEqual:
                r += "IS EQUAL\n"
            else:
                r += "\n"
        r += "|" + str(self.N) + "\t|"
        r += str(self.dates[self.N-1]) + "\t|"
        r += "%.5f" % self.SPs[self.N-1] + " |"
        r += "  X  \t|"
        r += "  X  \t\t|"
        r += "  X  \t|"
        r += "%.2f" % self.balance_ot[self.N-1] + "\n"
        return r

    def dataset_toStr(self):
        r = "Datas information\n"
        r += "--------------------------------------\n"
        r += "  Period Start\t\t: " + self.data.time_s + "\n"
        r += "  Period End\t\t: " + self.data.time_e + "\n"
        r += "  Timestep used\t\t: " + self.data.tsype + "\n"
        r += "  Ups\t\t\t: " + str(self.ups) + "\n"
        r += "  Downs\t\t\t: " + str(self.downs) + "\n"
        r += "  Equals\t\t: " + str(self.equals) + "\n"
        return r

    def results_toStr(self):
        r = "Results\n"
        r += "--------------------------------------\n"
        relativeprofit = 100*((self.balance-self.init_bal)/self.init_bal)
        r += "  Initial Balance\t: " + self.normprice(self.init_bal) + "\n"
        r += "  Final Balance\t\t: " + self.normprice(self.balance) + "\n"
        r += "  Profit\t\t: " + self.normprice(self.balance-self.init_bal) + "\n"
        r += "  Relative profit\t: " + "%.2f" % relativeprofit + "%\n"
        r += "  Nb actions taken\t: " + str(self.nbactions) + "\n"
        r += "  Max Balance\t\t: " + self.normprice(self.balance_max) + "\n"
        r += "  Min Balance\t\t: " + self.normprice(self.balance_min) + "\n"
        return r

    def cons_toStr(self):
        r = "Consecutive actions results\n"
        r += "--------------------------------------\n"
        r += "  MaxConsRight\t\t: " + str(max(self.consRight)) + "\n"
        r += "  MaxConsWrong\t\t: " + str(max(self.consWrong)) + "\n"
        r += "  Details :\n"
        r += "  consecutive right actions\n"
        r += "   \t|uni\t|cumul\n"
        r += "   \t-------------\n"
        for ri in self.consRight:
            r += "    " + str(ri) + ":\t|" + str(self.consRight[ri]) + "\t"
            r += "|" + str(sum([self.consRight[i] for i in self.consRight if i >= ri])) + "\n"
        r += "  consecutive wrong actions\n"
        r += "   \t|uni\t|cumul\n"
        r += "   \t-------------\n"
        for ri in self.consWrong:
            r += "    " + str(ri) + ":\t|" + str(self.consWrong[ri]) + "\t"
            r += "|" + str(sum([self.consWrong[i] for i in self.consWrong if i >= ri])) + "\n"
        return r

    def display_stats(self):
        print(self.actions_toStr())
        print(self.dataset_toStr())
        print(self.results_toStr())
        print(self.cons_toStr())

    def plot_stats(self):
        self.plotbalance()
        self.plotdata()

################################################################################
# COMPUTATIONS
################################################################################

    def computeConsRight(self):
        act_ind = 0
        while act_ind < self.nbactions:
            count = 0
            while (act_ind < self.nbactions) and (self.takenactions[act_ind].isRight):
                count += 1
                act_ind += 1
            if count > 1:
                if count not in self.consRight:
                    self.consRight[count] = 1
                else:
                    self.consRight[count] += 1
            act_ind += 1
        return self.consRight

    def computeConsWrong(self):
        act_ind = 0
        while act_ind < self.nbactions:
            count = 0
            while (act_ind < self.nbactions) and (not self.takenactions[act_ind].isRight):
                count += 1
                act_ind += 1
            if count > 1:
                if count not in self.consWrong:
                    self.consWrong[count] = 1
                else:
                    self.consWrong[count] += 1
            act_ind += 1
        return self.consWrong

    def compute_ups_downs(self):
        for i in range(1, self.N):
            if self.SPs[i] > self.SPs[i-1]:
                self.ups += 1
            elif self.SPs[i] < self.SPs[i-1]:
                self.downs += 1
            else:
                self.equals += 1


################################################################################
# UPDATES
################################################################################

    def update_profit(self):
        self.profit = self.balance - self.init_bal

    def updatebalance(self, newbalance):
        self.balance = newbalance
        self.balance_ot = np.append(self.balance_ot, self.balance)

    def update(self, timestep, action, result):
        self.takenactions = np.append(self.takenactions, action)
        self.nbactions += 1
        action.profit = result
        self.updatebalance(self.balance + result)

    def compute_stats(self):
        self.balance_min = min(self.balance_ot)
        self.balance_max = max(self.balance_ot)
        self.computeConsRight()
        self.computeConsWrong()
        self.compute_ups_downs()
