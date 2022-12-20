from utils import aoc_part
import re


def get_numbers(line):
    return [int(x) for x in re.findall(r"-?\d+", line)]


def manhattan_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def intersection(p1, p2, m, b):
    # Convert line segment to slope-intercept form
    m1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b1 = p1[1] - m1 * p1[0]

    # Solve for intersection point
    x = (b1 - b) / (m - m1)
    y = m * x + b

    # Check if intersection point is within the line segment
    if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]):
        return x, y
    return None


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, item):
        return self.x if item == 0 else self.y


class Sensor:
    def __init__(self, center, beacon):
        self.center = center
        self.closest_beacon = beacon
        self.distance_to_beacon = manhattan_dist(center, beacon)
        self.vertices = self.calculate_vertices()
        self.edges = self.calculate_edges()

    def calculate_vertices(self):
        return [
            Point(self.center.x - self.distance_to_beacon, self.center.y),
            Point(self.center.x + self.distance_to_beacon, self.center.y),
            Point(self.center.x, self.center.y - self.distance_to_beacon),
            Point(self.center.x, self.center.y + self.distance_to_beacon)
        ]

    def calculate_edges(self):
        return [
            (self.vertices[0], self.vertices[3]),
            (self.vertices[0], self.vertices[2]),
            (self.vertices[1], self.vertices[2]),
            (self.vertices[1], self.vertices[3])
        ]

    def get_intersection_interval(self, line1_id, line2_id):
        line1 = (self.edges[line1_id][0], self.edges[line1_id][1])
        line2 = (self.edges[line2_id][0], self.edges[line2_id][1])

        intersection_1 = intersection(*line1, 0, Y)
        if intersection_1 is None:
            return None

        intersection_2 = intersection(*line2, 0, Y)
        if intersection_2 is None:
            return None
        return intersection_1, intersection_2


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            numbers = get_numbers(line)
            res.append(Sensor(Point(numbers[0], numbers[1]), Point(numbers[2], numbers[3])))
    return res


# interval is ((x1, y1), (x2, y2)), merge if they overlap
def merge_intervals(intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the merged intervals list
    merged = []

    # Initialize the current interval with the first interval in the list
    current_interval = intervals[0]

    # Iterate through the rest of the intervals
    for interval in intervals[1:]:
        # If the current interval overlaps with the next interval, merge them
        if current_interval[1] >= interval[0]:
            current_interval = (current_interval[0], max(current_interval[1], interval[1]))
        # Otherwise, append the current interval to the merged intervals list and update the current interval
        else:
            merged.append(current_interval)
            current_interval = interval

    # After the loop, append the current interval to the merged intervals list
    merged.append(current_interval)
    return merged


@aoc_part(1)
def solve_pt1():
    global Y
    Y = 2000000
    sensors = load_input()
    intervals = []
    for sensor in sensors:
        sensor_intervals = None
        interval1 = sensor.get_intersection_interval(0, 3)
        if interval1:
            sensor_intervals = interval1
        else:
            interval2 = sensor.get_intersection_interval(1, 2)
            if interval2:
                sensor_intervals = interval2
        intervals.append(sensor_intervals)
    intervals_cleaned = [x for x in intervals if x]
    intervals_merged = merge_intervals(intervals_cleaned)
    interval = intervals_merged[0]
    return int(manhattan_dist(interval[0], interval[1]))


@aoc_part(2)
def solve_pt2():
    global Y
    Y = 0
    sensors = load_input()
    while Y < 4000000:
        intervals = []
        for sensor in sensors:
            sensor_intervals = None
            interval1 = sensor.get_intersection_interval(0, 3)
            if interval1:
                sensor_intervals = interval1
            else:
                interval2 = sensor.get_intersection_interval(1, 2)
                if interval2:
                    sensor_intervals = interval2
            intervals.append(sensor_intervals)
        intervals_cleaned = [x for x in intervals if x]
        intervals_merged = merge_intervals(intervals_cleaned)
        if len(intervals_merged) > 1:
            return int((intervals_merged[0][1][0] + 1) * 4000000 + intervals_merged[0][1][1])
        Y += 1


solve_pt1()
solve_pt2()
