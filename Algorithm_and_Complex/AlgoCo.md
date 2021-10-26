---
title: "Algorithms and Complexity"

marp: true

size: 16:9
footer: "Algorithms and Complexity by Fabián Vega"
paginate: true

backgroundImage: url('https://visme.co/blog/wp-content/uploads/2017/07/50-Beautiful-and-Minimalist-Presentation-Backgrounds-029.jpg')
style: |
  section {
      backgroundColor: white;
      alpha: 0.5;
  }
---

<!-- footer: "" -->

<style>
h1,h2,h3{
  transition: 1s;
}
h1:hover, h2:hover, h3:hover{
  color:#55a1f3;
}
img[src*="notation.jpg"] {
  width: 45%;
  float: right;
  float: inline-end;
  margin: 0; 
  padding:0;
  transition: 1s;
 }
 img[src*="notation.jpg"]:hover{
   width: 50%;
 }
 
</style>

# <!-- fit --> **Algorithms and Complexity**

### by Fabián Vega

---

<!-- footer: "Algorithms and Complexity by Fabián Vega" -->

# Table of Contents

1. [What is an Algorithm?]()
2. [What is the Complxity of Algorithm?]()
3. [The different asymptotic notations]()
4. [How does program performance?]()
5. [Use the recursion as your ally]()

---

<style>
  img {
    margin-left: 25%;
    width: 40%;
    transition: 2s;
  }
  img:hover{
    margin-left:22%;
    width: 45%;
  }
</style>

# What is an Algorithm?

![](img/algoritthm_definition.png)

> An algorithm is a set of instructions designed to perform a specific task.

---

# What is the Complxity of Algorithm?

It is defined as the amount of time and space required to solve a problem with size $n$.

- Time Complexity
- Space Complexity

---

# The different asymptotic notations

- **The Big Oh**
  ![](https://www.tutorialspoint.com/assets/questions/media/9995/big_oh_notation.jpg)

  It's said that a is $f(x) = O(g(x))$ if exists a $c > 0$ then $|f(x)| \leq c|g(x)|$ $(x\geq x_0)$

---

- **The Big Omega**
  ![](https://www.tutorialspoint.com/assets/questions/media/9995/big_omega_notation.jpg)

  It's said that a is $f(x) = \Omega(g(x))$ if exists a $c > 0$ then $|f(x)| \geq c|g(x)|$ $(x\geq x_0)$

---

- **The Big Theta**
  ![](https://www.tutorialspoint.com/assets/questions/media/9995/big_theta_notation.jpg)

  It's said that a is $f(x) = \Theta(g(x))$ if exists a $f(x) = O(g(x))$ and $f(x) = \Omega(g(x))$

---

## Other Notations

- **Little Oh**
  It's said that a is $f(x) = o(g(x))$ if $\lim_{x->\infty}{\frac{f(x)}{g(x)}} = 0$
- **Little Omega**
  It's said that a is $f(x) = \omega(g(x))$ if $\lim_{x->\infty}{\frac{f(x)}{g(x)}} \not= 0$
- **Landau Notation**
  It's said that a is $f(x) \sim g(x)$ if $\lim_{x->\infty}{\frac{f(x)}{g(x)}} = 1$

---
# <!-- fit --> **Break**

# <!-- fit --> This is the moment for doing all your questions :wink:

---

# A very brief introduction to algorithm design

---

# How does program performance?

## The basic principles

- **Sequence of actions**: The sum of costs of each action.
- **Alternation**: The number of times that do one alternative.
- **Cycles**: The evaluations of the cost of each iteration.
- **Procedure calls**: The cost of each call to a procedure.
---

# Use the recursion as your ally

The recursion is a very important tool in the design of algorithms. This allows us to split the problem into smaller problems that are easier to solve.

> "If the self-reference is confusing, it may be helpful to imagine that someone else is going to solve the simpler problems, just as you would assume for other types of reductions. I like to call that someone else the Recursion Fairy." Jeff Erickson

---

<style scoped>
  p:nth-child(4) {
    margin-left: 30%;
  }

</style>

## A basic example: Calculation of the factorial of a number

``` Haskell
let factorial = fn n::int -> int {
  if n <= 1 then {
    return 1;
  } 
  
  return n * factorial(n-1);
}
```

We can estimate the time complexity.
Let $T(1)=1$ and $T(n+1) = T(n) + 1$, if we expand it, obtained:

$T(1)=1$
$T(2)=T(1)+1=2$
$T(3)=T(2)+1=3$
...
$T(n) \Rightarrow O(n)$

---

## **The Metaheuristics "Divide And Conquer"**

### 1. Tower of Hanoi

> We has the goal to move all the disks from A to C with the help of B, but only one disk at a time without put a big disk on top o a small disk.

## ![](/Algorithm_and_Complex/img/external-content.duckduckgo.com.jpeg)
---
<style scoped>
  p:nth-child(3) {
    margin-left: 30%;
  }

</style>
``` Haskell
let hanoi = fn n::int, src::str, tmp::str, dst::str -> int {
    if n > 0 then {
        hanoi(n-1, src, tmp, dst);
        printLn("Move disk " + to_string(n) + " from " + src + " to " + dst);
        hanoi(n-1, tmp, dst, src);
    }
}
```
We can estimate the time complexity.
Let $T(0)=0$ and $T(n+1) = 2T(n) + 1$, if we expand it, obtained:

$T(0)=0$
$T(1)=2T(0)+1=1$
$T(2)=2T(1)+1=3$
$T(3)=2T(2)+1=7$
...
$T(n)=2^n-1 \Rightarrow O(2^n)$


---
### 2. Mergesort
> We has the goal to sort an array of numbers. 

``` Haskell
let mergesort = fn arr::list -> list{
  let n = length(arr);
  if n > 1 then {
    let mid1 = mergesort(arr[0,floor(n/2)]);
    let mid2 = mergesort(arr[ceil(n/2),n]);
    => merge(mid1, mid2);
  }
  => arr;
}
```

Then the amount of work units are when $T(0) = T(1) = 1$ and $T(n) = T(\lfloor \frac{n}{2} \rfloor) +T(\lceil \frac{n}{2} \rceil) + m(\lfloor \frac{n}{2}\rfloor,  \lceil \frac{n}{2} \rceil)$. The complexity of Merge Sort is $O(n\log{n})$.
> This is not demonstrable with the that we have, for this we must use the Master Theorem.

---

### 3. Backtracking
One idea for solving complex problems is to build the solution incrementally, exploring different branches and backtracking if a path turns out to be a dead end. The natural way to describe these algorithms is by recursion.

---
#### The 8 Queens Problem

<style scoped>

  img {
  width: 30%;
  float: right;
  }
  p:nth-child(3) {
    display: inline-block;
    margin-top: -350px;
    width: 60%;
  }
  img:hover {
  width: 35%;
  }

</style>
![The 8 Queens Problem Gif](https://upload.wikimedia.org/wikipedia/commons/b/b0/8queensminconflict.gif)

This problem is a classic example of the backtracking algorithm. In this problem, we are given a board of size 8×8, and we are asked to place 8 queens on the board so that no two queens attack each other. 
The idea is to place a queen on every possible position on the board, and if a path turns out to be a dead-end, we can backtrack and try another path, until we find a valid solution.


---
``` Python
def solve(c):
    global solutions

    if c == 8:
        solutions += 1
        print(solutions, end=": ")
        for r in range(8):
            print(queen[r] + 1, end=" " if r < 7 else "\n")
    else:
        for r in range(8):
            if rfree[r] and dd[c+r] and du[c+7-r]:
                queen[c] = r
                rfree[r] = dd[c+r] = du[c+7-r] = False
                solve(c+1)
                rfree[r] = dd[c+r] = du[c+7-r] = True


queen = [0 for _ in range(8)]
rfree = [True for _ in range(8)]
du = [True for _ in range(15)]
dd = [True for _ in range(15)]
solutions = 0

solve(0)

print(f"\nThere are {solutions} solutions")
```

---
<style scoped> 
  img{
    width: 20%;
    position: absolute;
    left: 50%;
    top: 5%;
    transition: 1s;
  }
  img:hover{
    width: 21.5%;
    top: 1%;
  }
  h3{
    display: inline-block;
    width: 60%;
  }
  p:nth-child(3) {
    display: inline-block;
    width: 70%;
  }
</style>

![](/Algorithm_and_Complex/img/BB.png)
### 4. Branch and Bound

This is a set of techniques for searching an optimal node in the graph, based on the idea of generating new branches that are evaluated to prune the branches that do not lead to the goal, where the evaluation gives the bound.

> This is also a **Greedy algorithm**.
---
#### Traveling Salesman Problem 
<style scoped> 
  img{
    width: 30%;
    position: absolute;
    left: 37%;
    top: 30%;
    transition: 1s;
  }
  img:hover{
    width: 35%;
    
  }
  h4{
    display: inline-block;
    width: 60%;
  }
  p:nth-child(3) {
    display: inline-block;
    width: 60%;
  }
</style>

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/TSP.png)

This problem is a classic example of the branch and bound algorithm. In this problem, we are given a set of N cities and we are asked to find the shortest route between the cities such that the distance between any two cities is less than or equal to the distance between the two cities in the shortest route.

---

<style scoped> 
  img{
    width: 30%;
    position: absolute;
    left: 37%;
    top: 30%;
    transition: 1s;
  }
  img:hover{
    width: 35%;
    
  }
  h3{
    display: inline-block;
    width: 60%;
  }
  p:nth-child(2) {
    display: inline-block;
    width: 60%;
  }
</style>

### 5. A Star

Suppose you want to find a way from a point to another into a graph. This is an algorithm that allows giving a solution to this problem, prioritizing some paths.

Some aplications of A* are:
- Robotics
- Games

![](https://dl.dropboxusercontent.com/s/selx3h5jmy5bc9j/3DPathfinding2.gif)

---
<style scoped> 

img {
    width: 50%;
    position: absolute;
    top: 30%;
    right: 25%;
    transition: 1s;
}
img:hover {
    width: 55%; 
    right: 24%;   
}
p:nth-child(2) {
  position: absolute;
  left: 65%;
  top: 80%;
  font-size: 50px;
}
</style>

![](https://media.giphy.com/media/rjNuJMkbr8yuA/source.gif)

to be continue...


---
<style scoped>
  p:nth-child(3) {
    opacity: 0;
    color: purple;
    transition: 1s;
  }
  p:nth-child(3):hover {
    opacity: 1;
  }
</style>
References:

1. [Algorithms and Complexities](https://www.tutorialspoint.com/Algorithms-and-Complexities)
2. [Analysis of algorithems little o and little omega notations](https://www.geeksforgeeks.org/analysis-of-algorithems-little-o-and-little-omega-notations/)
3. [Recursion](https://jeffe.cs.illinois.edu/teaching/algorithms/book/01-recursion.pdf)
4. [A star](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
5. [PathFinding]( https://qiao.github.io/PathFinding.js/visual/ ) :star:
6. [Merge sort animation](https://www.youtube.com/watch?v=JSceec-wEyw)
7. [Traveling Salesman Problem using Branch And Bound](https://www.geeksforgeeks.org/traveling-salesman-problem-using-branch-and-bound-2/)

Enchulado por la novia, Camilú.