#!/bin/python3

import math
import os
import random
import re
import sys


# Exercise: Birthday Cake Candles
def birthdayCakeCandles(candles):
    tallestCandle = max(candles)
    return candles.count(tallestCandle)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# Exercise: Number Line Jumps
def kangaroo(x1, v1, x2, v2):
    try:
        rest = (x1 - x2) % (v2 - v1)
    except ZeroDivisionError as e:
        print("NO")

    result = ""

    if (v1 > v2):
        if rest == 0:
            result = "YES"
        else:
            result = "NO"
    else:
        result = "NO"
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# Exercise: Viral Advertising
# CONSULTED ONLINE SOLUTIONS AND COMBINED WITH OWN
def viralAdvertising(n):
    cum = 0
    days = n + 1
    shared = 5

    for i in range(1, days):
        liked = shared // 2  # floor division
        cum = cum + liked
        shared = liked + liked + liked

    return cum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

    fptr.write(str(result) + '\n')

    fptr.close()


# Exercise: Recursive Digit Sum
def superDigit(n, k):
    if len(n) > 1:
        resSum = 0
        for i in range(len(n)):
            resSum += int(n[i])
        return superDigit(str(resSum*k), 1)
    else:
        return int(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# Exercise: Insertion Sort - Part 1
def insertionSort1(n, arr):
    elemToSort = arr[n - 1]
    did_break = False

    for i in reversed(range(n - 1)):
        if arr[i] >= elemToSort:
            arr[i + 1] = arr[i]
            res = " ".join(str(n) for n in arr)
            print(res)

        else:
            arr[i + 1] = elemToSort
            res = " ".join(str(n) for n in arr)
            print(res)
            did_break = True
            break

    if not did_break:
        arr[0] = elemToSort
        res = " ".join(str(n) for n in arr)
        print(res)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# Exercise: Insertion Sort - Part 2
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        print(" ".join(str(n) for n in arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
