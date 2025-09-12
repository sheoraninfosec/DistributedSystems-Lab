# Author: Jigesh Sheoran
# Last Updated : 12 Sept, 2025
# Practice code for Link State Routing using Dijkstra's algorithm

import copy 

def negative_weight(w):      # Error handling: weight cannot be -ve
    if w < 0:
        raise ValueError("Error: Negative weights are not allowed.")

# cost = infinity when path = unknown
INFINITY = float('inf')

def read_input():      # read & handle user input
    try:
        num_nodes = int(input("Enter the number of nodes: "))
        num_edges = int(input("Enter the number of edges: "))
        nodes = input("Enter the node names (separated by spaces): ").split()

        graph = {node: {} for node in nodes}

        for i in range(num_edges):
            u, v, w_str = input().split()
            w = int(w_str)
            negative_weight(w)
            graph[u][v] = graph[v][u] = w # two-way path 
        
        return nodes, graph
        
    except (ValueError, IndexError) as e:
        print(f"Error reading input: {e}. Please check the input format.")
        exit()

def LSR(start_node, nodes, graph):
    # ENGINE OF LINK STATE ROUTING ALGO
    
    distances = {node: 0 if node == start_node else INFINITY for node in nodes}
    lastnode = {node: None for node in nodes}
    unvisited_node = set(nodes)

    while unvisited_node:
        currentnode = min(unvisited_node, key=lambda node: distances[node])
        
        if distances[currentnode] == INFINITY:
            break
        
        for neighbor, weight in graph.get(currentnode, {}).items():
            if neighbor in unvisited_node:
                new_distance = distances[currentnode] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    lastnode[neighbor] = currentnode
        
        unvisited_node.remove(currentnode)
    
    return distances, lastnode

def print_lsr_table(router, nodes, distances, lastnode):
    # print final routing table for single router
    
    print(f"\n*** Link-State: Router {router} ***")
    print(f"{'Dest':<6} {'Cost':<6} {'NextHop':<8} {'Path'}")
    print("-" * 33)
    
    for dest in sorted(nodes):
        cost = distances.get(dest, INFINITY)
        
        cost_str = str(cost) if cost != INFINITY else "INF"
        
        # logic to trace the path & find next hop
        if cost == INFINITY:
            nexthop = "-"
            path_str = "No Path"
        elif router == dest:
            nexthop = "-"
            path_str = router
        else:
            path = []
            current = dest
            while lastnode[current] is not None:
                path.insert(0, current)
                current = lastnode[current]
            path.insert(0, router)
            nexthop = path[1]
            path_str = "->".join(path)
        
        print(f"{dest:<6} {cost_str:<6} {nexthop:<8} {path_str}")

def main():
    nodes, graph = read_input()
    
    # In LSR, every router calculate its own routing table.
    for startnode in nodes:
        distances, lastnode = LSR(startnode, nodes, graph)
        print_lsr_table(startnode, nodes, distances, lastnode)

if __name__ == "__main__":
    main()