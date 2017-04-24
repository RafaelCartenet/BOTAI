# LSTM

This is the first attempt of creating a strategy using LSTMs: Long short-term memory neural networks.

## Concept
For this first attempt we tried to predict the tendency of the next time step.
Let's consider **SP** being the array of the **N** strike prices for every time step t.
Let's define **T** the array of tendencies defined as:
**T[t] = 1** if **SP[t+1]>SP[t]**
**T[t] = -1** if **SP[t+1]>SP[t]**
**T[t] = 0** if **SP[t+1]=SP[t]**
Note that the length of **T** is **N-1** as we don't know **SP[N+1]**
