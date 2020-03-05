from math import sqrt


def distance_between_points(start, destination):
    """
    This function finds the distance between the two points, start and
    destination using Pythagoras' Theorem.
    """
    startX = start[0]
    startY = start[1]
    destinationX = destination[0]
    destinationY = destination[1]
    diffX = destinationX - startX
    diffY = destinationY - startY
    distance_sq = diffX ** 2 + diffY ** 2
    return sqrt(distance_sq)
