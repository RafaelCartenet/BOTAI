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
This simulator predicts the efficiency of a given strategy. According to a period of time, it will use the chosen strategy in order to simulate bets, compute the results, and gives statistics, in order to have an idea about the efficiency of the model.
The simulation outputs several statistics such as Datas information, Results of the strategy as well as informations relative to the consecutive results.
More details on the code [here](../../tree/master/Simulator)

## Strategies

### LSTM
This is the first attempt of creating a strategy using Recurrent Neural Networks, and more precisely LSTMs: Long short-term memory neural networks.
More information can be found on internet about this subject, including [here](http://colah.github.io/posts/2015-08-Understanding-LSTMs/).
For recurrent neural networks, data is processed as sequences. Each sequence in our case is a sequence of strike prices for example, and we try to predict the next value of this sequence, or maybe the tendency, whether the strike price is gonna be higher or lower at the next time step, there are many different possible options.
More details [here](../../tree/master/LSTM)
