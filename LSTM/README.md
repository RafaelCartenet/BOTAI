# LSTM

This is the first attempt of creating a strategy using LSTMs: Long short-term memory neural networks.  

## Concept

We are using recurrent neural networks as we believe the tendency of the last time step can be determined by the use of the previous strike prices, and thus, by the previous tendencies. We can't think about any rule and design a proper function in order to determine the tendency. That's why we are using neural networks that, with the use of training data, will try to model the sequences and will guess values for unseen data. LSTMs network are interesting because they have the ability to remember information from previous time steps and to decide when to forget information and when to keep it, according to seen samples. It also has the ability to use the information that has been seen many time steps ago, which might be useful for our case.

### Representation

For this first attempt we tried to predict the tendency of the next time step.  

Let's consider **SP** being the array of the **N** strike prices for every time step t.  
Let's define **T** the array of tendencies defined as:  
**T[t] = 1** if **SP[t+1]>SP[t]**  
**T[t] = -1** if **SP[t+1]>SP[t]**  
**T[t] = 0** if **SP[t+1]=SP[t]**  

Note that the length of **T** is **N-1** as we don't know **SP[N+1]**.  
**Thus, the aim of this strategy is, from a sequence of consecutive strike prices, guess the tendency between each value and especially between the last one and the next unknown strike price, that represents the tendency after the sequence!**  

The array of tendencies for training is quite easy to produce.  
**SP** and **T** arrays will be used. As the goal is to predict the tendency of the next time step after a given sequence of a finite size, the whole dataset is cut into sequences of size **num_steps** which is the number of steps that will be used in order to predict the tendency for next time step.

If for example it's 8:30, we want to predict the tendency at 8:35 and **num_steps = 5**, then we will be using values from 8:10, 8:15, 8:20, 8:25 and 8:30.

Thus, each sample of data is composed of **num_steps** consecutive strike prices and the associated tendencies.  

Let's say we wager on m5 time step, **num_steps = 5** and the dataset looks like:

|time | 8:00  | 8:05  | 8:10  | 8:15  | 8:20  | 8:25 | 8:30 | 8:35 | 8:40  | 8:45  |
|-----|-------|-------|-------|-------|-------|------|------|------|-------|-------|
|SP   |1.08924|1.08979|1.08964|1.08955|1.08921|1.0891|1.0895|1.0895|1.08851|1.08827|
|T    |   1   |  -1   |  -1   |  -1   |   1   |   1  |  0   |  -1  |   -1  |   ?   |

As mentioned, **T** is one value shorter than **SP** as we don't know the value of 8:50 so we can't deduce the tendency at 8:45.  
One sample of data could be the sequences:  

|time  | 8:00 | 8:05  | 8:10  | 8:15  | 8:20  |
|------|------|-------|-------|-------|-------|
|SP   |1.08924|1.08979|1.08964|1.08955|1.08921|
|T    |   1   |  -1   |  -1   |  -1   |   1   |

representing the values from 8:00 to 8:20.  

Values **1  -1  -1  -1  1** represents the ground truth of the tendencies during this period of time. First 4 values can be determined just by looking at the data. Indeed,  
**T[8:00]=1** because **SP[8:05]>SP[8:00]**   
**T[8:05]=-1** because **SP[8:10]<SP[8:05]** etc.

However, **T[8:20] = 1** can't be explained by the data as in this sample, **SP[8:25]** is unknown!  
That's where we want to use our neural network to help us.  

Note that values for **num_steps** and **timestep** are just for examples.  

### Normalization

One important thing to do before the training is to normalize the data. Indeed the value itself of the strike price, the mos important thing is the variation between the different time steps. Instead of using the values of the strike price we will rather use the relative variation according to the first value of the sequence. If we take the previous example, it will be normalized as:

|time  | 8:00 | 8:05  | 8:10  | 8:15  | 8:20  |
|------|------|-------|-------|-------|-------|
|SP   |0.0    |5.05e-4|3.67e-4|2.85e-4|-2.75e-5|
|T    |   1   |  -1   |  -1   |  -1   |   1   |

Logically, **SP[0] = 0**. The others values represent the relative variation to the strike price at 8:00. That's actually a good practice while using recurrent networks, as the value itself doesn't matter.

### Output

For the output of our LSTM, we decided to use **tanh** activation function, which means that each sequence will produce through the LSTM a list of **num_steps** real values between **-1** and **1**. The reason for this is quite simple, we want our LSTM to predict for each time step whether the tendency will be positive or negative, if the output is close to -1 that means the network predicts a decrease, and if close to 1, that means that the network predicts an increase. The problem is, what does "close to 1" mean. We defined a threshold (in **[0, 1]**) for decision, that can be actually used for safety purpose as well.

If the output value belongs to **[-1, -threshold]** then we will admit that the output of the network is interpreted as **-1**, which means our network predicts a decrease, if the output value belongs **[threshold, 1]** then it will be interpreted as **+1**, which means that our network predicts an increase, if it's between **[-threshold, thresold]** then it will be interpreted as **0** which means that our network either predicts that the strike price will be equal or that it is not confident enough to decide whether the strike price is gonna increase or decrease. This can be seen as a **"risk control"** parameter. If we set the threshold really low (0.1 for example) then our network will rarely produce **0** values which mean that our predictor will take a decision nearly each time.
However, if we set a high threshold, like **0.5** or **0.6**, that means that our predictor will take decisions only when the output of the network is higher in absolute value than **threshold**. In that case it might take decision less often, only when it is confident enough, which can be seen as safer strategy.

### Loss function


### Accuracy estimation
