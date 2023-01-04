
Rabbits and Recurrence Relations
================================

Source: Rosalind (https://rosalind.info/problems/fib/)

Problem
-------

Recall the definition of the Fibonacci numbers from "Rabbits and Recurrence Relations", which followed the recurrence relation $F_{n} = F_{n−1} + F_{n−2}$ and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See [Figure 4](https://rosalind.info/media/problems/fibd/mortal_rabbit_tree.png) for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

---
<p align="center">
<a href="https://rosalind.info/media/problems/fibd/mortal_rabbit_tree.png"><img src="https://rosalind.info/media/problems/fibd/mortal_rabbit_tree.png" width=400 alt="Figure 4"> </a>

**Figure 4**
</p>

---



**Given:** Positive integers $n \leq 100$ and $m \leq 20$.

**Return:** The total number of pairs of rabbits that will remain after the $n$-th month if all rabbits live for $m$ months.


Sample Dataset
--------------
```
6 3
```

Sample Output
-------------
```
4
```
