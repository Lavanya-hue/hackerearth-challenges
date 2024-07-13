#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    n = len(p)
    m = len(y)
    cloud_population = [0] * m
    town_covered_by_clouds = [0] * n
    single_cloud_coverage = [0] * m
    sunny_population = 0
    for i in range(m):
        for j in range(n):
            if y[i] - r[i] <= x[j] <= y[i] + r[i]:
                cloud_population[i] += p[j]
                town_covered_by_clouds[j] += 1
    for i in range(n):
        if town_covered_by_clouds[i] == 0:
            sunny_population += p[i]
    
    max_sunny_population = sunny_population
    for i in range(m):
        for j in range(n):
            if y[i] - r[i] <= x[j] <= y[i] + r[i] and town_covered_by_clouds[j] == 1:
                single_cloud_coverage[i] += p[j]
    for i in range(m):
        current_sunny_population = sunny_population + single_cloud_coverage[i]
        max_sunny_population = max(max_sunny_population, current_sunny_population)

    return max_sunny_population

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
