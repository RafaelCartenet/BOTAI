# BOTAI
Binary Options Trading is as simple as wagering on the tendency of an action, such as currency pairs (EUR/USD etc.).  
At each time step, you can bet a certain amount X that  what they called the "strike price" is gonna increase (in this case that's a "Call") or that it is gonna decrease (in that case it's a "Put").  
If you were right, you will earn a ratio of your bet, this ratio is most of the time either 0.88 or 0.80.  
If you were wrong, you will lose 100% of your bet.  

Simple example:  
Let's say at 16:23 the EUR/USD ratio is 1.20675. You bet 100$ on a Call, and you were right. Ratio is 0.88. You will end up with 188$. Let's say now that you were wrong, you'll have 0$ left.  

Simple calculus leads to notice that in order to be cost effective, your right/wrong ratio needs to be higher than 1/(1+r).  
Which is 53% when the ratio is 0.88, 56% when the ratio is 0.80.  

The goal of the project is to realize an automatized cost effective strategy with a ratio higher than these reference ratios.  
## Simulator
