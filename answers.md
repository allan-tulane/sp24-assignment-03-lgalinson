# CMPS 2200 Assignment 3
## Answers

**Name:** Lakeland Galinson


Place all written answers from `assignment-03.md` here for easier grading.


**1a.** To make N dollars with the fewest number of coins in the powers of 2(2^0 to 2^k), one starts with the larget denomination coin that does not exceed $N$. One then subtracts the value of that coin from N to get a new value of N. We then repeat this process until N is == 0.

**1b.** For any number $N$, selecting $2^k$, where $k$ is the highest integer for which $2^k \leq N$, is the optimal initial step as it maximizes the reduction of $N$ in one step. Once the first denomination is selected, the problem reduces to finding change for $N - 2^k$, a smaller yet similar challenge. This new problem is independent of earlier decisions and can be tackled with the same approach. The total solution for $N$ combines the selected $2^k$ with the solution for $N - 2^k$. Due to the binary structure of the coin denominations, using smaller coins would result in a suboptimal solution requiring more coins overall.

**1c.** Work = $O(log N)$ and Span = $O(log N)$



**2a.** Instead of starting with the largest denomination:

Pick the $10$ dollar denomination three times.
This totals exactly $30$ dollars using three coins of $10$ dollars each.
This example clearly illustrates that the greedy algorithm can fail to find a solution even when one exists, and it can also fail to minimize the number of coins when it does find a solution. In Fortuito, the greedy algorithm is not just suboptimal, but it could potentially miss viable solutions entirely, depending on the available denominations.

**2b.** The optimal method to create change for an amount $N$ is derived from the optimal solutions for smaller amounts. Assuming that the minimal number of coins required for all amounts less than $N$ is known, then the optimal number of coins for $N$ can be determined by adding one coin to the minimum of the optimal solutions for $N - D_i$ for each denomination $D_i$ that is available.

**2c.** Top-Down Dynamic Programming Approach (Memoization) uses recursion to solve the problem, caching the results of subproblems to avoid redundant computations:

```{python}
def min_coins(N, denominations):
    # table initalization
    memo = [0] + [float('inf')] * N

    def solve(n):
        if memo[n] != float('inf'):
            return memo[n]
        for coin in denominations:
            if coin <= n:
                memo[n] = min(memo[n], solve(n - coin) + 1)
        return memo[n]

    result = solve(N)
    return result if result != float('inf') else -1

# example usage:
denominations = [1, 5, 10, 25]
N = 63
print(min_coins(N, denominations))

```
The work is $W = O(Nk)$, and the span is $S = O(N)$









