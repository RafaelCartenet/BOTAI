# BOTAI (Binary Optins Trading Artificial Intelligence)
Binary Options Trading is as simple as wagering on the tendency of an asset, such as currency pairs (EUR/USD etc.). It is considered sometimes more like gambling than real trading.  
At each time step, you can bet a certain amount X that the value of the asset, also called strike price, is gonna increase (in this case it's a "Call") or that it is gonna decrease (in that case it's a "Put").  
If you were right, you will earn a ratio of your bet, this ratio is most of the time either 0.88 or 0.80.  
If you were wrong, you will lose 100% of your bet.  

**Simple example:**  
Let's say at 16:23 the EUR/USD ratio is 1.20675. Your initial balance is 1000$. You bet 100$ on a Call for the next minute. At 16:24 the EUR/USD ratio is 1.20679. It's slightly better, you were right. Ratio is 0.88. You will end up with 1088$. Let's say now that the EUR/USD ratio at 16:24 was actually 1.2059, you would have been wrong and would have ended up with 900$.  

Simple calculus leads to notice that in order to be cost effective, your right/wrong ratio needs to be higher than 1/(1+r).  
Which is 53% when the ratio is 0.88, 56% when the ratio is 0.80.  

The goal of the project is to realize an automatized cost effective strategy with a ratio higher than these reference ratios, with as few as possible risks and a balance and reinvestment management strategy.

Files belows are independant for now.  

## Simulator
More details on the code [here](../../tree/master/Simulator)  
This simulator predicts the efficiency of a given strategy. According to a period of time, it will use the chosen strategy in order to simulate bets, compute the results, and gives statistics, in order to have an idea about the efficiency of the model.

The simulation outputs several statistics such as Datas information, Results of the strategy as well as informations relative to the consecutive results. Example of results displayed:
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

## LSTM
This is the first try of predictive model, using LSTM neural networks.  
**in construction**
