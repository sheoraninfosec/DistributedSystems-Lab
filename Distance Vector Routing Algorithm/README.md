# Distance Vector Routing Algorithm
## This repository contains a Python implementation of the Distance Vector Routing algorithm, based on the Bellman-Ford equation. 
The program simulates how routers in a network dynamically find the shortest path to every other router through an iterative process of information exchange with their neighbors.

### How to Compile and Run
This code is written in Python 3. You can run the script directly from your terminal.
Save the file: Save the provided Python code as a file, for example, dvr_algorithm.py.

Run the script: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:
```py
python3 dvr-algorithm.py
```

## Input Format

The program requires interactive user input to define the network's topology. You will be prompted for the following information:
```
Number of Nodes: "Enter a single integer representing the total number of routers in the network"
Number of Edges: "Enter a single integer representing the total number of direct connections between routers"
Node Names: "Enter the names of all the nodes on a single line, separated by spaces"
Edge Information: "For each edge, enter the two connected nodes and the weight (cost) of the link, separated by spaces."
```
Example Input
```
Enter the number of nodes: 5
Enter the number of edges: 5
Enter the node names (separated by spaces): A B C D E
A B 1
A D 1
A E 7
B C 1
C D 1
```

### Assumptions and Design Choices
Two-Way Paths: The implementation assumes that all network links are symmetric, meaning the cost to travel from Node A to Node B is the same as the cost to travel from Node B to Node A.

No Negative Weights: The algorithm is designed to prevent negative-cost cycles. 
The code includes a check to exit the program if any negative edge weights are entered.

Direct Path Representation: An infinite cost (float('inf')) is used to represent paths that are not directly connected, which is a standard approach for the Bellman-Ford algorithm.

Interactive Input: The program relies on standard input for network configuration, making it easy to test various topologies without modifying the code.
Detailed Output: The program is designed to provide clear, formatted output at each stage of the process, including:

1. The initial state of the routing tables.
2. A trace of which tables are updated in each iteration.
3. The final, converged routing tables with the lowest cost and a clear path string for each destination.


