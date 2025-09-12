# Author: Jigesh Sheoran
# Last Updated : 12 Sept, 2025
# Practice code for Distance Vector Routing algorithm using Bellman-Ford

import copy 

def negative_weight(w):      #error handeling / weight cannot be -ve
            if w < 0:
                raise ValueError("Error: Negative weights are not allowed.")
                
# cost = infinty / when path is unknown
INFINITY = float('inf')

def read_input():      # reading & handeling user input
    try:
        num_nodes = int(input("Enter the number of nodes: "))
        num_edges = int(input("Enter the number of edges: "))
    
        nodes = input("Enter the node names (separated by spaces): ").split()

        graph = {node: {} for node in nodes}

        for _ in range(num_edges):
            u, v, w_str = input().split()
            w = int(w_str)
            negative_weight(w)
            graph[u][v] = graph[v][u] = w      #two way path       
        return nodes, graph
        
    except (ValueError, IndexError) as e:      # error handeling
        print(f"Error reading input: {e}. Please check the input format.")
        exit()

def start_routing_table(nodes, graph):  # ITERATION 0
    tables = {}
    for node in nodes:
        tables[node] = {}
        for dest in nodes:
            if node == dest:
                # Cost -> self = 0, next hop = node itself
                tables[node][dest] = (0, node)
            elif dest in graph[node]:
                # Cost -> direct neighbor
                tables[node][dest] = (graph[node][dest], dest)
            else:
                # Cost -> non-neighbor = infinity
                tables[node][dest] = (INFINITY, None)
    return tables

def dvr_algorithm(nodes, graph, tables):
    # ENGINE OF OUR DISTANCE-VECTOR ALGORITHM 
    iterations = 0
    while True:
        iterations += 1
        updated_in_iteration = False
        
        #create a deep copy to compare tables at start & end of iteration
        old_tables = copy.deepcopy(tables)

        for u in nodes:
            for v in graph[u]:
                # get routing table of neighbor `v`
                neighbor_table = tables[v]
                for dest in neighbor_table:
                    cost_from_v_to_dest = neighbor_table[dest][0]
                    
                    # total cost from u to destination via neighbour v / cost = (u -> v) + (v -> dest)
                    new_cost = graph[u][v] + cost_from_v_to_dest
                    
                    # If the new path is shorter then update table & set next hop = v
                    if new_cost < tables[u][dest][0]:
                        tables[u][dest] = (new_cost, v)
                        updated_in_iteration = True
        
        # --- TRACING CHANGES FOR EVERY ITERATION ---
        print(f"--- Iteration {iterations} ---")
        for node in sorted(nodes):
            if old_tables[node] != tables[node]:
                print(f"  Table for Router {node} updated.")
        print("-" * 25)
        
        if not updated_in_iteration:
            break
            
    return tables, iterations

def recreate_path(start_node, dest_node, tables):
    
    # trace full path from start node to destination node
    if tables[start_node][dest_node][0] == INFINITY:
        return "No Path"
    if start_node == dest_node:
        return start_node

    path = [start_node]
    current_node = start_node
    
    # loop until reached to destination
    while current_node != dest_node:
        next_hop = tables[current_node][dest_node][1]   # find the next hop 
        if next_hop is None:
            return "Path error"  # safeguard
        path.append(next_hop)
        current_node = next_hop
        
    return "->".join(path)

def print_routing_table(nodes, tables):
    # PRINTING FINAL ROUTING TABLE
    
    for node in sorted(nodes):
        print(f"*** Distance-Vector: Router {node} ***")
        print(f"{'Dest':<6} {'Cost':<6} {'NextHop':<8} {'Path'}")
        print("-" * 33) 
        
        for dest in sorted(tables[node]):
            cost, next_hop = tables[node][dest]
            
            cost_str = str(cost) if cost != INFINITY else "INF"
            next_hop_str = next_hop if next_hop is not None else "-"
            
            path_str = recreate_path(node, dest, tables)  # recreate & get path for current route
            print(f"{dest:<6} {cost_str:<6} {next_hop_str:<8} {path_str}")
        print()

if __name__ == "__main__":
    nodes, graph = read_input()
    
    initial_tables = start_routing_table(nodes, graph)
    
    print("-- Initial State of Routing Tables --")
    print_routing_table(nodes, initial_tables)
    
    print("\nStarting Distance-Vector Algorithm.........\n")
    
    final_tables, num_iterations = dvr_algorithm(nodes, graph, initial_tables)
    
    # -1 because last loop only confirms no more updates needed
    print(f"\nConvergence achieved after {num_iterations - 1} update iterations.\n") 
    print_routing_table(nodes, final_tables)

