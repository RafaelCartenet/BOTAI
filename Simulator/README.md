# Simulator
The goal of this simulator is to predict the efficiency of a strategy. It takes as input a strategy defined according to a simple API and the values of a given currency pair on a period of time in order to simulate the behavior of the strategy.  
Many statistics have been implemented in order to visualize the results and the efficiency of the strategy. The goal is to be able to test our future strategies in the future using this fast simulator rather than trying our strategy on real time.

## DataManager.py
The DataManager handles the data. It loads the whole given data csv file, and keeps only the lines of the values according to parameters. It is possible to select the period of time, by giving the starting time and the ending time with dd/mm/yy hh:mm format as well as the time steps chosen. Common time steps in Binary Options Trading are:
* M1: every minute
* M5: every 5 minutes
* M15: every 15 minutes
* M30: every 30 minutes
* H1: every hour

For example to use the EUR/USD data every minutes from 00:00 23h59 3rd of April:
```python
datamanager = DataManager("../data/EURUSD.csv", "M1", "03/04/17 00:00", "03/04/17 23:59")
```

The datamanager is used for the simulation as well as for simple statistics. Indeed it is important to study the dataset itself in order to find characteristics. 

## Action.py



## BOTSimulator.py





## Engine.py


## Policy.py
