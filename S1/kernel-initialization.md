## Deterministic Algorithms
Given an unsorted list, the sorting algorithm, say bubble sort or quick sort, will systematically sort the list until you have an ordered result. Deterministic means that each time the algorithm is given the same list, it will execute in exactly the same way. It will make the same moves at each step of the procedure

Some problems are hard for computers. Perhaps because of the number of combinations; perhaps because of the size of data. They are so hard because a deterministic algorithm cannot be used to solve them efficiently. The algorithm may run, but will continue running until the heat death of the universe

## Non-Deterministic Algorithms
These are algorithms that use elements of randomness when making decisions during the execution of the algorithm. This means that a different order of steps will be followed when the same algorithm is rerun on the same data.

They can rapidly speed up the process of getting a solution, but the solution will be approximate, or “good,” but often not the “best.” Nondeterministic algorithms often cannot make strong guarantees about running time or the quality of the solution found

## Stochastic Search Algorithms
The algorithms are not random per se; instead they make careful use of randomness. They are random within a bound. They share common features in their use of randomness, such as:

- Use of randomness during initialization.
- Use of randomness during the progression of the search.

## How kernels are intialized?
Artificial neural networks are trained using a stochastic optimization algorithm called stochastic gradient descent. In this kernels are initialized to small random values (random, but close to zero, such as in [0.9, 0.1]). This gives algorithem some randomness in selecting a starting point for the search and in the progression of the search. 

As the search process unfolds, there is a risk that we are stuck in an unfavorable area of the search space. Using randomness during the search process gives some likelihood of getting unstuck and finding a better final candidate solution

for e.g.

    [[ 0.91940167  0.08143941]
    [ 0.68744134  0.87236687]]
