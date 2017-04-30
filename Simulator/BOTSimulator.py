################################################################################
# BOTAI
################################################################################
# https://github.com/RafaelCartenet/BOTAI
# This simulator predicts the efficiency of a given strategy. According to a
# period of time, it will use the strategy policy in order to simulate bets,
# compute the results, and gives statistics, in order to have an idea about the
# efficiency of the model.

#Classes
from DataManager import *
from ModuleStat import *
from Engine import *

# Policies
from randompolicy import *
from martingalepolicy import *
from martingalepolicyUD import *

# Libraries
import warnings
warnings.filterwarnings('ignore')

def main():
    # DATA MANAGER
    datamanager = DataManager("../data/EURUSD.csv",
                    "M5",
                    "m03/04/17 00:00",
                    "m03/04/17 23:59")

    datamanager.ImportData()

    # STATS MODULE
    modulestats = ModulStat(datamanager, initial_balance=1000)

    # POLICY DEFINITION
    policy = martingalepolicyUD(ratio=2.13636364, init=1)

    # ENGINE
    engine = Engine(datamanager, policy, modulestats)
    engine.run()

    # STATISTICS
    modulestats.compute_stats()
    modulestats.display_stats()
    #modulestats.plot_stats()

if __name__ == "__main__":
    main()
