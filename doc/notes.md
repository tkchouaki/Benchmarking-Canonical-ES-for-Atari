#Des notes sur l'article


## Introduction
Recently it has been shown [Salimans et al., 2017] that ES
algorithms can be used for tasks which are dominated by deep
reinforcement learning (RL) algorithms

ES advantages compared to deep RL

* Highly parallelizable
* They can offer better exploration in some problems
* They are not sensitive to the distribution of rewards and do not require careful tuning of discount factors
* They can be used for the optimization of nondifferentiable
policy functions


Salimans used a specialized ES algorithms
In this article, they use a simpler very basic canonical ES algorithm from the 70s.


The contributions :

* A very basic ES is enough
* After 5 Hours of training, Canonical ES is able to find novel solution & even exploit the game's design & bugs.
* Comparing RL to Canonical ES

## Background

### RL for playing Atari

I need more knowledge on RL but i think i got the main lines.

### Natural Evolution for playing Atari

It was a brief review of [Salimans et al., 2017], i should read it for a better insight.


### Canonical ES algorithm

I should also read about ES algorithms to understand more.

## Experiments

We going throught neural networks again ...

A big table, a lot of stories about results in games & youtube videos.




## Recent related works

Similarly to our work, Such et al. [2017] studied the performance
of simpler algorithms than OpenAI’s specialized
ES variant. They show that genetic algorithms (another broad
class of black-box optimization algorithms).

==> So ES algorithms are not a subcategory of Genetic Algorithms, they're more like siblings.