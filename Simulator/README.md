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

The datamanager is used for the simulation as well as for simple statistics. Indeed it is important to study the dataset itself in order to find characteristics and interesting properties, such as the number of consecutive ups and downs or the proportion of equal strike prices from a time step to another.

## Action.py

The action class is the parent class for possible actions in binary options trading: Call and Put, which are inherited classes of Action. We also implement a Pass class, which is the "no action" action. These 3 inherited classes are used by the policy when deciding what to do at each given time step and are stored in a list for final statistics. Each time policy choses an action, it creates a new instance of this classes and stores it in a list. The result of the taken action is directly updated on these Action instances, with booleans ```isRight```and ```ìsEqual``` in case the action was right and in case the strike price is equal to the previous time step.


## Engine.py

The engine is the orchestra leader, it runs the simulation itself, it takes as input the loaded data, the policy, and the statistics module and deals with the communications between all of them. For every time step, it sends the new data to policy and gets an action back, it computes the result of this action and sends the results to the statistics module.

## Policy.py

Policy.py is the parent class of every policy. It contains few functions for simple strategy, such as
* getPreviousAction(self) that returns the previous action taken in the simulation, which is an Action instance.
* def call(self, amount) creates the Call Action with the associated amount.
* def put(self, amount) creates the Put Action with the associated amount.
* def pass_(self) creates the Pass Action.
This class is used as model for policy creation, in order to make a functional policy it is necessary to create a child class of Policy and to rewrite the predefined function in the Policy function :

```python
def ChooseAction(self, seendata, timestep):
    # to Redefine
    return
```

The ChooseAction functions is expecting as output an instance of the class Action. The initial inputs are the timestep and the seendata that corresponds to the previous values that have been seen during the past.

For example, in the martingale policy, the function as been rewritten this way:

```python
def ChooseAction(self, seendata, ts):
    if ts == 0:
        return self.put(self.init)
    else:
        prev = self.getPreviousAction()
        if prev.isRight:
            if prev.isEqual:
                return self.put(prev.amount)
            return self.put(self.init)
        return self.put(prev.amount * self.reinvestratio)
```

Note that ```self.init``` and ```self.reinvestratio``` are two variables that have been created within the martingalepolicy child class.


## BOTSimulator.py

This is the main function of the simulator. After loading load thanks to the Data Manager and initializes the Statistics module and the chosen policy, runs the simulation thanks to the engine. Once the simulation is done, calls the statistics to be printed/displayed via the Statistics module.
It looks like :

```python
# DATA MANAGER
datamanager = DataManager("../data/EURUSD.csv",
                "M1",
                "03/04/17 00:00",
                "03/04/17 23:59")
datamanager.ImportData()

# STATS MODULE
modulestats = ModulStat(datamanager, initial_balance=1000)

# POLICY DEFINITION
policy = martingalepolicy(ratio=2.13636364, init=1)

# ENGINE
engine = Engine(datamanager, policy, modulestats)
engine.run()

# STATISTICS
modulestats.compute_stats()
modulestats.display_stats()
modulestats.plot_stats()
```

Example of results displayed:
```
Datas information
--------------------------------------
  Period Start		: 03/04/17 00:00
  Period End		: 03/04/17 23:58
  Timestep used		: M1
  Ups			: 664 | 46.18%
  Downs			: 653 | 45.41%
  Equals		: 121 | 8.41%

Results
--------------------------------------
  Initial Balance	: 1000.00$
  Final Balance		: 1574.64$
  Profit		: 574.64$
  Relative profit	: 57.46%
  Nb actions taken	: 1438
  Max Balance		: 1574.64$
  Min Balance		: 583.77$

Consecutive actions results
--------------------------------------
  MaxConsRight		: 13
  MaxConsWrong		: 9
  Details :
  consecutive right actions
   	|uni	|cumul
   	-------------
    2:	|100	|196
    3:	|46	|96
    4:	|23	|50
    5:	|16	|27
    6:	|4	|11
    7:	|6	|7
    13:	|1	|1
  consecutive wrong actions
   	|uni	|cumul
   	-------------
    2:	|96	|166
    3:	|42	|70
    4:	|17	|28
    5:	|6	|11
    6:	|3	|5
    7:	|1	|2
    9:	|1	|1
```

Another output is the list of every action taken at each time step as well as the result of this action and the evolution of the balance. Here is an example of a Martingale policy simulation with time step M5:
```
...
|239	|2017-03-04 19:50:00+00:00	|1.06636 |Put	|20.83		|False	|1083.75
|240	|2017-03-04 19:55:00+00:00	|1.06638 |Put	|44.50		|True	|1062.92
|241	|2017-03-04 20:00:00+00:00	|1.06603 |Put	|1.00		|False	|1102.08
|242	|2017-03-04 20:05:00+00:00	|1.06609 |Put	|2.14		|True	|1101.08
|243	|2017-03-04 20:10:00+00:00	|1.06601 |Put	|1.00		|False	|1102.96
|244	|2017-03-04 20:15:00+00:00	|1.06606 |Put	|2.14		|False	|1101.96
...
```
Note that the most right ammount is the balance after that the bet has been done, before the result of next time step.
