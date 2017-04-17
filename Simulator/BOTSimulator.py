# Classes
from DataManager import *
from ModuleStat import *
from Engine import *

# Libraries
import warnings
warnings.filterwarnings('ignore')

# Policies
from randompolicy import *
from martingalepolicy import *

class BOTSimulator:
    def __init__(self, policy=randompolicy):
        self.DataExtractor = DataExtraction()
        self.StatModule = ModuleStat()
        self.policy = policy

    def getData(self):
        self.data = DataExtractor.getData()

    def loadPolicy(self):
        self.policy = self.policy()

    def run(self):
        self.getData()
        self.loadPolicy()


c = DataManager("EURUSD.csv",
                "M1",
                "03/04/17 00:00",
                "03/04/17 23:59")
c.ImportData()

m = ModulStat(c, 1000)


p = martingalepolicy(ratio=2.13636364, init=1)

engine = Engine(c, p, m)
engine.run()

m.compute_stats()
m.display_stats()
m.plot_stats()
