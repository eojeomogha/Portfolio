import heapq
import math

# Define grid dimensions
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Define grid cells as blocked (1) or unblocked (0)
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
grid[1][3] = 1
grid[2][3] = 1
grid[3][3] = 1
grid[4][3] = 1

# Define grid cell size
CELL_SIZE = 50

# Define heuristic function (Euclidean distance)
def heuristic(node, goal):
    dx = abs(node[0] - goal[0])
    dy = abs(node[1] - goal[1])
    return math.sqrt(dx**2 + dy**2)

# A* pathfinding algorithm
def a_star(start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if (0 <= neighbor[0] < GRID_WIDTH and
                0 <= neighbor[1] < GRID_HEIGHT and
                grid[neighbor[1]][neighbor[0]] == 0):

                tentative_g_score = g_score[current] + CELL_SIZE
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

start_node = (0, 0)
goal_node = (GRID_WIDTH - 1, GRID_HEIGHT - 1)

path = a_star(start_node, goal_node)
print("Path:", path)
