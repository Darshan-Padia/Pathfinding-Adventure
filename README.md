# Pathfinding Adventure

## Description
Pathfinding Adventure is an educational game that teaches graph theory concepts through an engaging treasure hunt experience. The game is based on the rules of a treasure hunt but with its own unique twist.

## Features
- Generates a random tree subgraph using the Breadth-First Search (BFS) shortest path algorithm.
- Player spawns at a random checkpoint on the map.
- Progression to the next checkpoint requires correctly answering a question.
- Scoring system: Correct answers award 100 points, incorrect answers deduct 50 points.
- Game ends if the player answers five questions incorrectly.
- Objective is to reach the destination checkpoint by following the shortest path.

## Technologies Used
- Python programming language
- Pygame library for game development
- Tiled Map Editor for creating the game map
- Vector graphics and sprites for visual appeal

## Question Generation
The game generates questions from various domains, including general knowledge, science, math, politics, and graph theory itself. These questions encourage players to learn and apply concepts to progress through the game.

## Implementation
- Developed using Python and the Pygame library.
- Tiled Map Editor used for creating the city map.
- Vector graphics and sprites enhance the visual appeal.
- Pygame library handles the graphical user interface (GUI), including the map and checkpoint pillars.
- Python implements the game logic, including graph theory concepts and algorithms.

## Graph Theory Concepts
The game incorporates various graph theory concepts, such as:
- Unweighted graphs
- Directed graphs
- Trees
- Graph types (e.g., wheel graph, complete graph, bipartite graph)
- Bridge (cut edge)
- Cut vertex

The BFS shortest path algorithm is a key component of the game, determining the optimal path for the player to navigate through the checkpoints.

## How to Play
1. The game starts by spawning the player at a random checkpoint on the map.
2. The player must answer a question correctly at the current checkpoint to receive the key to the next checkpoint.
3. Answering correctly awards 100 points, while answering incorrectly deducts 50 points.
4. The game ends if the player answers five questions incorrectly.
5. The player must navigate through the checkpoints by following the shortest path determined by the BFS algorithm.
6. The objective is to reach the destination checkpoint by answering questions correctly and following the optimal path.

(For more detailed gameplay information, please refer to the provided flowchart image.)
<img src="https://github.com/Darshan-Padia/Pathfinding-Adventure/assets/89976375/a846c408-8602-4300-bea9-2cae644238dc" alt="Flowchart" width="500">

## Note
This game, "Pathfinding Adventure," is my original creation, and the copyright has been secured.
