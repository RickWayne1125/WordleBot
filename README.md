# WordleBot

A tool for solving wordle puzzles.

## About Algorithm

The algorithm of this project basically refers to the method of [3B1B](https://www.youtube.com/watch?v=v68zYyaEmEA).
The first step is mostly picking a best open word by sorting the different words based on the calculation result of information entropy.

$$
Entropy(w)=\sum_{x \in X}p(x)\cdot log_2(1/p(x))

$$
