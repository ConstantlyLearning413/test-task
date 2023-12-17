#! python3.7
import argparse


def count_steps(nums: list) -> int:
    if len(nums) < 2:
        return 0

    nums.sort()
    median_index = (len(nums) - 1) // 2
    median = nums[median_index]

    res = 0
    for elem in nums:
        res += abs(elem - median)

    return res


def run(file: str):
    with open(file, 'r') as f:
        nums = list(map(int, f))

    res = count_steps(nums=nums)

    print(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='task4')
    parser.add_argument('file', type=str, help='file with integer nums')
    args = parser.parse_args()

    run(file=args.file)
