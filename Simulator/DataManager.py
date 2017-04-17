# Libraries
import pandas as pd
import numpy as np


class DataManager:
    def __init__(self, filename, timestep, time_start=None, time_end=None):
        # np array containing the strikeprice at each time step
        self.SPs = None
        self.dates = None
        self.N = 0
        self.file = filename
        self.tsype = timestep
        self.time_s = time_start
        self.time_e = time_end

    def ImportData(self):
        # loads the data
        df = pd.read_csv(self.file, sep=";")
        self.dates = np.array(df['date'])
        self.SPs = np.array(df['strike price'])
        N = df.shape[0]

        # define starting and ending indexes according to
        ind_start = np.argwhere(self.dates == self.time_s) or np.array([[0]])
        ind_end   = np.argwhere(self.dates == self.time_e) or np.array([[N]])
        ind_start, ind_end = ind_start[0][0], ind_end[0][0]

        # loads the data inside a pandas dataframe
        self.time_s = df['date'][ind_start]
        self.time_e = df['date'][ind_end - 1]
        self.dates = np.array(df['date'][ind_start:ind_end])
        self.SPs = np.array(df['strike price'][ind_start:ind_end])
        self.N = len(self.dates)

        # defines indexes for time steps
        if self.tsype == 'M1':
            coeff = 1
        elif self.tsype == 'M5':
            coeff = 5
        elif self.tsype == 'M15':
            coeff = 15
        indexes = [coeff*i for i in range(1+ self.N//coeff)]
        indexes = [i for i in indexes if i < self.N]

        # updates the data
        self.SPs = self.SPs[indexes]
        self.dates = self.dates[indexes]
        self.N = len(indexes)

    def getN(self):
        return self.N

    def getSPs(self):
        return self.SPs

    def getDates(self):
        return self.dates
