Link State Routing Algorithm
This repository contains a Python implementation of the Link State Routing algorithm, based on Dijkstra's shortest path algorithm. The program simulates how each router builds a complete map of the network and then uses that map to find the most efficient path to every other router.

How to Compile and Run
This code is written in Python 3. You can run the script directly from your terminal.

Save the file: Save the provided Python code as a file, for example, lsr_algorithm.py.

Run the script: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:

python3 lsr_algorithm.py

Input Format
The program requires interactive user input to define the network's topology. You will be prompted for the following information:

Number of Nodes: "Enter a single integer representing the total number of routers in the network"
Number of Edges: "Enter a single integer representing the total number of direct connections between routers"
Node Names: "Enter the names of all the nodes on a single line, separated by spaces"
Edge Information: "For each edge, enter the two connected nodes and the weight (cost) of the link, separated by spaces."

Example Input

Enter the number of nodes: 5
Enter the number of edges: 5
Enter the node names (separated by spaces): A B C D E
A B 1
A D 1
A E 7
B C 1
C D 1

Assumptions and Design Choices
Two-Way Paths: The implementation assumes that all network links are symmetric, meaning the cost to travel from Node A to Node B is the same as the cost to travel from Node B to Node A.

No Negative Weights: The algorithm is designed to prevent negative-cost cycles. The code includes a check to exit the program if any negative edge weights are entered, as Dijkstra's algorithm does not work with them.

Centralized Topology: Each router is assumed to have a complete and accurate view of the entire network topology. The program simulates this by running the algorithm from the perspective of each router individually.

Interactive Input: The program relies on standard input for network configuration, making it easy to test various topologies without modifying the code.

Detailed Output: The program is designed to provide clear, formatted output for each router's final routing table, including the lowest cost and a clear path string for each destination.
