import random

def estimate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_points

# Change this variable to set how many points to use
points = 10

print(f"Estimated Pi with {points} points: {estimate_pi(points)}")