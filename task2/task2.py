#! python3.7
import argparse
from math import sqrt


def count_distance(center, point):
    a, b = point[0] - center[0], point[1] - center[1]
    return sqrt(a * a + b * b)


# 2 - точка снаружи
# 1 - точка внутри
# 0 - точка лежит на окружности
def get_location(distance, radius) -> int:
    if distance > radius:
        return 2
    if distance < radius:
        return 1
    return 0


def define_point_location(center, radius, point):
    distance = count_distance(center, point)
    return get_location(distance, radius)


def run(file1: str, file2: str):
    with open(file1, 'r') as f:
        center = list(map(float, f.readline().split()))
        radius = float(f.readline())

    with open(file2, 'r') as f:
        for line in f:
            point = list(map(float, line.split()))
            res = define_point_location(center, radius, point)
            print(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='task2')
    parser.add_argument('file1', type=str, help='center coordinates and radius of the circle file')
    parser.add_argument('file2', type=str, help='coordinates of the points file')
    args = parser.parse_args()

    run(file1=args.file1, file2=args.file2)
