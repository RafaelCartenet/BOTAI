# LSTM

This is the first attempt of creating a strategy using LSTMs: Long short-term memory neural networks.  

## Concept
For this first attempt we tried to predict the tendency of the next time step.  
Let's consider **SP** being the array of the **N** strike prices for every time step t.  
Let's define **T** the array of tendencies defined as:  
**T[t] = 1** if **SP[t+1]>SP[t]**  
**T[t] = -1** if **SP[t+1]>SP[t]**  
**T[t] = 0** if **SP[t+1]=SP[t]**  
Note that the length of **T** is **N-1** as we don't know **SP[N+1]**.  
**Thus, the aim of this strategy is, from a sequence of consecutive strike prices, guess the tendency between each value and especially between the last one and the next unknown strike price, that represents the tendency after the sequence!**  

The array of tendencies for training is quite easy to produce.  
**SP** and **T** arrays will be used. As the goal is to predict the tendency of the next time step after a given sequence, we will process with sequences. The whole dataset is cut into sequences of size **num_steps** which is the number of steps that will be used in order to predict the next values. If for example it's 8:30, we want to predict the tendency at 8:35 and **num_steps = 5**, then we will be using values at 8:10, 8:15, 8:20, 8:25 and 8:30.

Thus, each sample of data is composed of **num_steps** consecutive strike prices and the associated tendencies.  

Let's say we wager on m5 time step, **num_steps = 5** and:

|time | 8:00  | 8:05  | 8:10  | 8:15  | 8:20  | 8:25 | 8:30 | 8:35 | 8:40  | 8:45  |
|-----|-------|-------|-------|-------|-------|------|------|------|-------|-------|
|SP   |1.08924|1.08979|1.08964|1.08955|1.08921|1.0891|1.0895|1.0895|1.08851|1.08827|
|T    |   1   |  -1   |  -1   |  -1   |   1   |   1  |  0   |  -1  |   -1  |   ?   |

As mentioned, **T** is one value shorter than **SP** as we don't know the value of 8:50 so we can't deduce the tendency at 8:45.  
One sample of data could be the sequence:  
|1.08924|1.08979|1.08964|1.08955|1.08921|
|   1   |  -1   |  -1   |  -1   |   1   |
representing the values from 8:00 to 8:20.
