# BOTAI
Binary Options Trading is as simple as wagering on the tendency of an action, such as currency pairs (EUR/USD etc.).  
At each time step, you can bet a certain amount X that  what they called the "strike price" is gonna increase (in this case that's a "Call") or that it is gonna decrease (in that case it's a "Put").  
If you were right, you will earn a ratio of your bet, this ratio is most of the time either 0.88 or 0.80.  
If you were wrong, you will lose 100% of your bet.  

Simple example:  
Let's say at 16:23 the EUR/USD ratio is 1.20675. You bet 100$ on a Call, and you were right. Ratio is 0.88. You will end up with 188$. Let's say now that you were wrong, you'll have 0$ left.  

Simple calculus leads to notice that in order to be cost effective, your right/wrong ratio needs to be higher than 1/(1+r).  
Which is 53% when the ratio is 0.88, 56% when the ratio is 0.80.  

The goal of the project is to realize an automatized cost effective strategy with a ratio higher than these reference ratios, with as few as possible risks and a good balance and reinvestment management.

Files belows are independant for now.  


## Simulator
This simulator predicts the efficiency of a given strategy. According to a period of time, it will use the strategy actions in order to simulate bets, compute the results, and gives statistics, in order to have an idea about the efficiency of the model.

example of simulation output:
```
Datas information
--------------------------------------
  Period Start		: 03/04/17 00:00
  Period End		: 03/04/17 23:58
  Timestep used		: M1
  Ups			: 664
  Downs			: 653
  Equals		: 121

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
## LSTM
This is the first try of predictive model, using LSTM neural networks.
