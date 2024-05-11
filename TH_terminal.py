#importing the networkx library
# from pickle import SHORT_BINSTRING
from random import *
from settings import *
import networkx as nx

qustions = {

    "what is the degree of any node of compelete graph with 5 vertices?" : '4',
    "what is the no. of edges of a compelete graph with 5 vertices?" : '10',
    "what is the no. of spanning tree we get from K5?" : '125',
    "Can a regular graph with degree 4 be Euler graph? YES or NO" :'yes',
    "Consider a simple undirected graph of 10 vertices. If the graph is disconnected, then the maximum number of edges it can have is __" : "36",
    "In network topology, the property between two graphs so that both have got same Incidence matrix is known as" : "isomorphism"
}

# shortest path algorithm using breadth first 
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []
#importing the lotlib library for plotting the graph
# import matplotlib.pyplot as plt


GRAPH_EDGES = [
    (5372,9697),
    (5372,4391),
    (9697,6921),
    (7397,5933),
    (9397,6315),
    (7697,6315),
    (6921,2320),
    (6921,7013),
    (6921,5805),
    (2320,4391),
    (2320,2265),
    (2320,7464),
    (2320,6315),
    (4391,4687),
    (4391,5767),
    (4391,5372),
    (2265,5705),
    (2265,5402),
    (2265,5403),
    (7464,5933),
    (7464,6315),
    (7464,5372),
    (6315,7397),
    (6315,6921),
    (6315,9697),
    (5933,7464),
    (4687,6672),
    (6672,5767),
    (6672,7052),
    (6672,3896),
    (7052,3896),
    (5767,7052),
    (5767,3896),
    (3896,6330),
    (3896,2663),
    (2663,2888),
    (2663,1054),
    (2888,6330),
    (2888,4053),
    (2888,5403),
    (6330,5403),
    (6330,5705),
    (4053,5403),
    (4053,3454),
    (3454,5403),
    (3454,1054),
    (3454,1999),
    (1999,5403),
    (1999,5402),
    (1999,1436),
    (1436,1054),
    (1436,5805),
    (5402,2265),
    (5402,5403),
    (2265,5403),
    (2265,5705),
    (2265,2320),
    (5705,6330),
    (5705,5403),
    (7013,8821),
    (8821,9243),
    (8821,7110),
    (1054,8549),
    (8549,6709),
    (8549,5000),
    (6709,5000)
]
print(len(GRAPH_EDGES))
GRAPH_EDGES = set(GRAPH_EDGES)
GRAPH_EDGES = list(GRAPH_EDGES)
print(len(GRAPH_EDGES))

H=nx.Graph()
for i in GRAPH_EDGES:
    H.add_edge(*i)

# G= nx.erdos_renyi_graph(50,0.1)#important.. draws random graph with 35 vertices, and probablity of edge connecting between two vertices is 0.4
# while (not nx.is_connected(G)):
#     G= nx.erdos_renyi_graph(50,0.1)#important.. draws random graph with 35 vertices, and probablity of edge connecting between two vertices is 0.4

# nx.write_adjlist(G, "test.adjlist")
# fh = open("test.adjlist", "rb")
# H = nx.read_adjlist(fh)
# print(f'___{H}__');
# nx.write_adjlist(H, "test2.adjlist")
# nx.draw(H, with_labels=True)
# plt.plot(G)
# plt.show()
# sub_graph = G.subgraph([0,1,2])
# nx.draw(sub_graph,with_labels = True);
# plt.show()


'''
adjacency_dict={}
for node in G:
    adjacency_dict[node] = list(G.neighbors(node))
print(adjacency_dict)


    #BFS

    visited = [] # List for visited nodes.
    queue = []     #Initialize a queue

    def bfs(visited, graph, node): #function for BFS
        visited.append(node)
        queue.append(node)

        while queue:          # Creating loop to visit each node
            m = queue.pop(0) 
            print (m, end = " ") 

            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        # Driver Code
        print("Following is the Breadth-First Search")
        bfs(visited, G, 0) 
'''

max=0
# print(G.nodes())

# choosing the longest shortest path.. looping through all vertices and checking the shortest path... saving the longest
#shortest path in max. The traversal path is stored in node_traversal_longest_shortest_path.
node_traversal_longest_shortest_path=[]
start_node = choice(KEYS)

while(start_node == 5805):
    start_node = choice(KEYS)
print(start_node)
for j in range(0,len(H.nodes())):
    x = len(shortest_path(H,start_node,list(H.nodes())[j]))
    if x > max:
        max = x
        node_traversal_longest_shortest_path = shortest_path(H,start_node,list(H.nodes())[j])

print(max)
print(node_traversal_longest_shortest_path)

orig_shortest_path_length = len(node_traversal_longest_shortest_path)


# starting_point = node_traversal_longest_shortest_path[0]
# ending_point = node_traversal_longest_shortest_path[-1]

# current_node = starting_point

# o=0
# iterations=0
# '''
# while (current_node!=ending_point and iterations!=7):

#     x = randint(0,len(qustions)-1)

#     print(list(qustions.keys())[x])
#     ans = input("enter your ans here: ")
#     print(list(qustions.keys())[x])
#     if ans == qustions[list(qustions.keys())[x]]:
#         print(f'{node_traversal_longest_shortest_path[o+1]} is the right way')
#         current_node = node_traversal_longest_shortest_path[o+1]
#         o+=1
#     else:
#         print('wrong ans please guess the path')

#         print(list(G.neighbors(current_node)))
#         choice = int(input('choose 1 of the above options: '))
#         current_node = choice
#         node_traversal_longest_shortest_path = shortest_path(G,int(choice), int(ending_point))
#         print(f"\n\n{list(node_traversal_longest_shortest_path)} \n\n        ")
#     iterations+=1
# '''
# x=prev_x=0
# while (current_node!=ending_point ):# loop runs until the current node is not equal to the final node , meaning until the user is not reached to the treasure point.

#     while(x==prev_x):# for getting different questions( to avoid repeated questions consecutively )
#         x = randint(0,len(qustions)-1)
#     prev_x = x

#     print(list(qustions.keys())[x])# asking a question from above question set
#     ans = input("enter your ans here: ")
#     ans = ans.lower()#making the answer from the user case insensitive
#     # print(f' v {list(qustions.keys())[x]}')
#     if ans == qustions[list(qustions.keys())[x]]:# if answer is correct
#         print(f'{node_traversal_longest_shortest_path[o+1]} is the right way')#showing the right way to the user
#         current_node = node_traversal_longest_shortest_path[o+1]# setting the new right paths node as the current node.
#         o+=1
#     else:#if answer is not correct
#         print('wrong ans please guess the path')
#         print(list(G.neighbors(current_node)))# showing path options to user from the current node 
#         choice = int(input('choose 1 of the above options: '))
#         current_node = choice # setting the path that user chose as the current path
#         node_traversal_longest_shortest_path = shortest_path(G,int(choice), int(ending_point))# running the shortest path algo again between the new current node and the final point.
#         o=0
#         print(f"\n\n{list(node_traversal_longest_shortest_path)} \n\n  ")
#     iterations+=1

#     if(iterations == 15):# breaking the loop if the user takes 15 or more steps... as time is a factor in any game .. this conditiin plays that role
#         print('you have exhausted your chances. GAME OVER.')

# if(iterations+1 == orig_shortest_path_length):# most optimized solution possible to the treasure hunt game
#     print("CONGRATULATIONS YOU HAVE REACHED TO TREASURE IN MINIMUM NO. OF STEPS POSSIBLE.")
# else: # more time  or steps taken than necessary
#     print(f'THE SHORTEST PATH COULD BE ACHIEVED IN {orig_shortest_path_length}. AND YOU TOOK {iterations+1} STEPS')