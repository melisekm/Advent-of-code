from dataclasses import dataclass

from utils import aoc_part


@dataclass
class Point:
    x: int
    y: int
    z: int = 0


@dataclass
class Ray:
    origin: Point
    direction: Point


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            split = line.strip().split("@")
            pos = split[0].split(",")
            velocity = split[1].split(",")
            origin = Point(int(pos[0]), int(pos[1]), int(pos[2]))
            direction = Point(origin.x + int(velocity[0]), origin.y + int(velocity[1]), origin.z + int(velocity[2]))
            ray = Ray(origin, direction)
            res.append(ray)
    return res


def line_line_intersection(A, B, C, D):
    # Line AB represented as a1x + b1y = c1
    a1 = B.y - A.y
    b1 = A.x - B.x
    c1 = a1 * A.x + b1 * A.y

    # Line CD represented as a2x + b2y = c2
    a2 = D.y - C.y
    b2 = C.x - D.x
    c2 = a2 * C.x + b2 * C.y

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return None
    x = (b2 * c1 - b1 * c2) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return Point(x, y)


def is_in_past(intersection, ray):
    if ray.origin.x < ray.direction.x:
        if ray.origin.x > intersection.x:
            return True
    else:
        if ray.origin.x < intersection.x:
            return True

    if ray.origin.y < ray.direction.y:
        if ray.origin.y > intersection.y:
            return True
    else:
        if ray.origin.y < intersection.y:
            return True

    return False


@aoc_part(1)
def solve_pt1():
    data = load_input()
    res = 0
    area = (200000000000000, 400000000000000)
    for idx, ray in enumerate(data):
        for jdx, other_ray in enumerate(data[idx + 1:]):
            intersection = line_line_intersection(ray.origin, ray.direction, other_ray.origin, other_ray.direction)
            if not intersection:
                continue

            if area[0] < intersection.x < area[1] and area[0] < intersection.y < area[1]:
                if not (is_in_past(intersection, ray) or is_in_past(intersection, other_ray)):
                    res += 1
    return res


# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass


solve_pt1()
# solve_pt2()
