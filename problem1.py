#!/bin/python3
import os
import textwrap
from collections import OrderedDict
from collections import defaultdict
import calendar
from datetime import timedelta
from datetime import datetime
import datetime
import re
from html.parser import HTMLParser
import sys
import xml.etree.ElementTree as etree
import operator
import numpy


# Introduction (all – total: 7 - max points: 75)
# https://www.hackerrank.com/domains/python/py-introduction

# [Introduction] Exercise 1: Say "Hello, World!" With Python
print("Hello, World!")

# [Introduction] Exercise 2: Python If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        if n >= 2 and n <= 5:
            print("Not Weird")
        if n >= 6 and n <= 20:
            print("Weird")
        if n > 20:
            print("Not Weird")
    else:
        print("Weird")

# [Introduction] Exercise 3: Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

res_sum = a + b
res_diff = a - b
res_prod = a * b

print(res_sum)
print(res_diff)
print(res_prod)

# [Introduction] Exercise 4: Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a // b)
print(a / b)

# [Introduction] Exercise 5: Loops
if __name__ == '__main__':
    n = int(input())

for val in range(n):
    print(pow(val, 2))

# [Introduction] Exercise 6: Print Function
if __name__ == '__main__':
    n = int(input())

for val in range(n + 1):
    if val != 0:
        print(val, end='')

# [Introduction] Exercise 7: Input()
str_variabili = input()
polynom = input()

x = int(str_variabili.split()[0])
k = int(str_variabili.split()[1])

poly_sum = eval(
    polynom)  # Treat the second input (the polynomial expression) as an algebrical expression so Python can calculate it directly
print(poly_sum == k)


# [Introduction] Exercise 8: Write a function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))

# Data types (all – total: 6 - max points: 60)
# https://www.hackerrank.com/domains/python/py-basic-data-types

# [Data types] Exercise 1: List Comprehensions
# The code may be from HackerRank; Found the solution on Github
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

list_of_lists = [[i, j, k]
                 for i in range(0, x + 1)
                 for j in range(0, y + 1)
                 for k in range(0, z + 1)
                 if i + j + k != n]
print(list_of_lists)

# [Data types] Exercise 2: Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

set_of_int = sorted(set(arr))
set_of_int.reverse()

if len(set_of_int) == 0:
    print(0)
else:
    if len(set_of_int) == 1:
        print(max(set_of_int))
    else:
        set_of_int.remove(max(set_of_int))
        print(max(set_of_int))

# [Data types] Exercise 3: Nested Lists
if __name__ == '__main__':
    complex_lst = []
    list_of_scores = []
    for _ in range(int(input())):
        lst = []
        name = input()
        score = float(input())
        lst.append(name)
        lst.append(score)
        list_of_scores.append(score)
        complex_lst.append(lst)

set_of_scores = set(list_of_scores)
set_of_scores.remove(min(set_of_scores))
second_lowest_score = min(set_of_scores)

list_of_names = []

for m in range(len(complex_lst)):
    if complex_lst[m][1] == second_lowest_score:
        list_of_names.append(complex_lst[m][0])

list_of_names.sort()

for _ in list_of_names:
    print(_)

# [Data types] Exercise 4: Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

for key in student_marks:
    if key == query_name:
        sum_of_scores = sum(student_marks[key])
        res = sum_of_scores / len(student_marks[key])
        formatted_res = "{:.2f}".format(res)
        print(formatted_res)

# [Data types] Exercise 5: Lists
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):

        # Differentiate command and list of strings
        command, *values = input().split()

        # Convert the list of strins into a list of integers
        for i in range(0, len(values)):
            values[i] = int(values[i])

        # Filtrate operations per command
        if command == "append":
            for num in values:
                lst.append(int(num))
        if command == "insert":
            lst.insert(values[0], values[1])
        if command == "remove":
            lst.remove(values[0])
        if command == "pop":
            lst.pop()
        if command == "sort":
            lst.sort()
        if command == "reverse":
            lst.reverse()
        if command == "print":
            print(lst)

# [Data types] Exercise 6: Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
print(hash(integer_list))


# Strings (all – total: 14 - max points: 220)
# https://www.hackerrank.com/domains/python/py-strings
# https://www.hackerrank.com/domains/python/py-strings/2

# [Strings] Exercise 1: sWAP cASE
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# [Strings] Exercise 2: String Split and Join
def split_and_join(line):
    # Convert string to list of strings
    line = line.split(" ")
    # Join strings by symbol "-"
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# [Strings] Exercise 3: What's Your Name?
def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# [Strings] Exercise 4: Find a string
def count_substring(string, sub_string):
    occurrences = 0
    for const in range(len(string)):
        if string[const:].startswith(sub_string):
            occurrences += 1
    return occurrences


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


# [Strings] Exercise 5: String Formatting
# CONSULTED ONLINE SOLUTIONS
def print_formatted(number):
    # Removing "0b" prefix
    form = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexa = (hex(i)[2:]).upper()
        binary = bin(i)[2:]

        print(decimal.rjust(form), octal.rjust(form), hexa.rjust(form), binary.rjust(form))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# [Strings] Exercise 6: Mutations
def mutate_string(string, position, character):
    string = string[: position] + character + string[position + 1:]
    # s = s[:index] + newstring + s[index + 1:]
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# [Strings] Exercise 7: String Validators
def stringValidator(string):
    # Verifying if at least on character of the string satisfies the conditions
    print(any(ch.isalnum() for ch in string))
    print(any(ch.isalpha() for ch in string))
    print(any(ch.isdigit() for ch in string))
    print(any(ch.islower() for ch in string))
    print(any(ch.isupper() for ch in string))

if __name__ == '__main__':
    s = input()
    stringValidator(s)


# [Strings] Exercise 8: Text Alignment
# Replace all ______ with rjust, ljust or center.
thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
        thickness * 6))


# [Strings] Exercise 9: Text Wrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# [Strings] Exercise 10: Designer Door Mat
def designDoorMat(n, m):
# CONSULTED ONLINE SOLUTIONS
    # The pattern that repeats
    pattern_singolo = ".|."

    # Design by diving in three parts: upper, central and lower

    # Upper part
    for i in range(1, n, 2):
        pattern_replicato = pattern_singolo * i
        print(pattern_replicato.center(m, "-"))

    # Central part
    print("WELCOME".center(m, "-"))

    # Lower part
    for i in range(n - 2, -1, -2):
        pattern_replicato = pattern_singolo * i
        print(pattern_replicato.center(m, "-"))

if __name__ == '__main__':
    n, m = input().split()
    n = int(n)
    m = int(m)
    string = designDoorMat(n, m)


# [Strings] Exercise 11: Alphabet Rangoli
# # CONSULTED ONLINE SOLUTIONS, I thought that the exercise was complex and time consuming
def print_rangoli(n):
    s = "abcdefghijklmnopqrstuvwxyz"

    for i in range(n - 1, 0, -1):
        row = ["-"] * (n * 2 - 1)
        for j in range(0, n - i):
            row[n - 1 - j] = s[j + i]
            row[n - 1 + j] = s[j + i]
        print("-".join(row))

    for i in range(0, n):
        row = ["-"] * (n * 2 - 1)
        for j in range(0, n - i):
            row[n - 1 - j] = s[j + i]
            row[n - 1 + j] = s[j + i]
        print("-".join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# [Strings] Exercise 12: Capitalize!
def solve(s):
    # List of strings
    lst = s.split()
    # Replace each element of the list with the capitalized element
    for elem in lst:
        s = s.replace(elem, elem.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()


# [Strings] Exercise 13: The Minion Game
def minion_game(string):
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    Kevin = 0
    Stuart = 0
    for ch in range(len(string)):
        if string[ch] in consonants:
            Stuart += len(string) - ch
        else:
            Kevin += len(string) - ch
    if Kevin > Stuart:
        print("Kevin", Kevin)
    else:
        if Kevin < Stuart:
            print("Stuart", Stuart)
        else:
            print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)


# [Strings] Exercise 14: Merge the Tools!
def merge_the_tools(string, k):
    n = len(string)  # n, lenght of the string
    if k == 1:
        for ch in string:
            print(ch)
    else:
        numSubstrings = int(n / k)  # ogni sottostringa è di lunghezza k
        for c in range(0, n, k):
            res = "".join(dict.fromkeys(string[c:k]))
            print(res)
            k += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# [Sets] Exercise 1: Introduction to Sets
def average(array):
    set_of_int = set(array)
    return sum(set_of_int) / len(set_of_int)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# [Sets] Exercise 2: Set .add()
if __name__ == '__main__':
    N = int(input())
    lst = []
    for c in range(N):
        lst.append(input())
    lst = set(lst)
    print(len(lst))

# [Sets] Exercise 3: Set .discard(), .remove() & .pop()
if __name__ == '__main__':

    # The first line contains integer , the number of elements in the set
    n = int(input())

    # The second line contains  space separated elements of set
    s = set(map(int, input().split()))

    # The third line contains integer N, the number of commands
    N = int(input())

    for c in range(N):
        command = input().split()

        if command[0] == "discard":
            # print("DISCARD " + command[1])
            s.discard(int(command[1]))
            # print(s)

        else:
            if command[0] == "remove":
                # print("REMOVE " + command[1])
                if int(command[1]) in s:
                    s.remove(int(command[1]))
                # print(s)

            else:
                if len(s) > 0:
                    # print("POP ")
                    s.pop()
                    # print(s)
    # print(s)
    s = list(s)
    print(sum(s))


# [Sets] Exercise 4: Set .union() Operation
def studentUnion(ENstudents, FRstudents):
    res = ENstudents.union(FRstudents)
    return len(res)


if __name__ == '__main__':
    # The number of students who have subscribed to the English newspaper
    n = int(input())

    # Contains n space separated roll numbers of those students
    ENstudents = set(map(int, input().split()))

    # The number of students who have subscribed to the French newspaper
    b = int(input())

    # Contains b space separated roll numbers of those students
    FRstudents = set(map(int, input().split()))
    res = studentUnion(ENstudents, FRstudents)
    print(res)


# [Sets] Exercise 5: Set .intersection() Operation
def studentIntersection(ENstudents, FRstudents):
    res = ENstudents.intersection(FRstudents)
    return len(res)

if __name__ == '__main__':
    # The number of students who have subscribed to the English newspaper
    n = int(input())

    # Contains n space separated roll numbers of those students
    ENstudents = set(map(int, input().split()))

    # The number of students who have subscribed to the French newspaper
    b = int(input())

    # Contains b space separated roll numbers of those students
    FRstudents = set(map(int, input().split()))
    res = studentIntersection(ENstudents, FRstudents)
    print(res)


# [Sets] Exercise 6: Set .difference() Operation
def studentDifference(ENstudents, FRstudents):
    res = ENstudents.difference(FRstudents)
    return len(res)

if __name__ == '__main__':
    # The number of students who have subscribed to the English newspaper
    n = int(input())

    # Contains n space separated roll numbers of those students
    ENstudents = set(map(int, input().split()))

    # The number of students who have subscribed to the French newspaper
    b = int(input())

    # Contains b space separated roll numbers of those students
    FRstudents = set(map(int, input().split()))
    res = studentDifference(ENstudents, FRstudents)
    print(res)


# [Sets] Exercise 7: Set .symmetric_difference() Operation
def studentSymDifference(ENstudents, FRstudents):
    res = ENstudents.symmetric_difference(FRstudents)
    return len(res)

if __name__ == '__main__':
    # The number of students who have subscribed to the English newspaper
    n = int(input())

    # Contains n space separated roll numbers of those students
    ENstudents = set(map(int, input().split()))

    # The number of students who have subscribed to the French newspaper
    b = int(input())

    # Contains b space separated roll numbers of those students
    FRstudents = set(map(int, input().split()))
    res = studentSymDifference(ENstudents, FRstudents)
    print(res)


# [Sets] Exercise 8: Symmetric Difference
def studentSymDifference(elements_of_M, elements_of_N):
    res = elements_of_M.symmetric_difference(elements_of_N)
    res = sorted(res)
    for elem in res:
        print(elem)

if __name__ == '__main__':
    # The number of elements in M
    M = int(input())

    # Contains M space-separated integers
    elements_of_M = set(map(int, input().split()))

    # The number of elements in N
    N = int(input())

    # Contains N space-separated integers
    elements_of_N = set(map(int, input().split()))
    res = studentSymDifference(elements_of_M, elements_of_N)


# [Sets] Exercise 9: Check Subset
def checkSubset(A, B):
    res = False
    if A.intersection(B) == A:
        res = True
    print(res)

if __name__ == '__main__':

    # The first line will contain the number of test cases, T
    T = int(input())

    for tc in range(0, T):
        # Contains the number of elements in set A
        lenSetA = int(input())

        # Contains the space separated elements of set A
        A = set(map(int, input().split()))

        # Contains the number of elements in set B
        lenSetB = int(input())

        # Contains the space separated elements of set A
        B = set(map(int, input().split()))

        checkSubset(A, B)


# [Sets] Exercise 10: Set Mutations
if __name__ == '__main__':

    # Contains the number of elements in set A
    lengthA = int(input())

    # Contains the space separated list of elements in set A
    A = set(map(int, input().split()))

    # Contains integer N, the number of other sets
    N = int(input())

    for x in range(0, N):

        # Reading first input line: operation and length of B set
        operation, lengthB = input().split()
        lengthB = int(lengthB)

        # Reading second input line: elements of set B
        B = set(map(int, input().split()))

        # Identifying the operation to apply on set A
        if operation == "intersection_update":
            A.intersection_update(B)

        elif operation == "update":
            A.update(B)
        elif operation == "symmetric_difference_update":
            A.symmetric_difference_update(B)
        else:
            A.difference_update(B)

    print(sum(A))


# [Sets] Exercise 11: The Captain's Room
def findCaptainsRoom(rooms, K):
    roomsWithAtLeastOneGuest, roomsWithMoreThanOneGuest = set(), set()

    for room in rooms:
        if room in roomsWithAtLeastOneGuest:
            roomsWithMoreThanOneGuest.add(room)
        roomsWithAtLeastOneGuest.add(room)
    for room in roomsWithAtLeastOneGuest - roomsWithMoreThanOneGuest:
        print(room)

if __name__ == '__main__':
    # K the size of each group
    K = int(input())

    # Contains the unordered elements of the room number list
    rooms = list(map(int, input().split()))
    findCaptainsRoom(rooms, K)

# [Sets] Exercise 12: Check Strict Superset
if __name__ == '__main__':

    # Contains the space separated elements of set A
    A = set(map(int, input().split()))

    # n, the number of other sets
    n = int(input())

    # The next n lines contains the space separated elements of the other sets
    for c in range(n):
        N = set(map(int, input().split()))
        if len(N.difference(N.intersection(A))) == 0:
            res = True
        else:
            res = False
            break
    print(res)


# [Sets] Exercise 13: No Idea!
def amIHappy(lst, A, B):
    happiness = 0

    for elem in lst:
        if elem in A:
            happiness += 1
        if elem in B:
            happiness -= 1

    print(happiness)

if __name__ == '__main__':
    # Contains integers n and m separated by a space
    n, m = input().split()
    n = int(n)
    m = int(m)

    # Contains n integers, the elements of the array
    lst = list(map(int, input().split()))

    # The third and fourth lines contain m integers, A and B, respectively
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    amIHappy(lst, A, B)  # Answer: Yes, because the code compiles at the first try!


# Collections (all – total: 8 - max points: 220)
# https://www.hackerrank.com/domains/python/py-collections

# [Collections] Exercise 1: collections.Counter()
if __name__ == '__main__':

    # X, the number of shoes
    X = int(input())

    # List of all the shoe sizes in the shop
    shoes = list(map(int, input().split()))

    # Contains N, the number of customers
    N = int(input())

    profit = 0

    # Contains the shoe size desired by the customer and the price of the shoe
    for i in range(N):
        size, price = input().split()
        size = int(size)
        price = int(price)
        if size in shoes:
            shoes.remove(size)
            profit += price

    print(profit)

# [Collections] Exercise 2: DefaultDict Tutorial
if __name__ == '__main__':

    # The first line contains integers n and m
    n, m = input().split()
    n = int(n)
    m = int(m)

    # The next n lines contain the words belonging to group A
    A = defaultdict(list)
    for i in range(n):
        A[str(input())].append(i + 1)

    # The next m lines contain the words belonging to group B
    B = []
    for i in range(m):
        B.append(str(input()))

    # For each m words, check whether the word has appeared in group A or not
    for w in B:
        if w in A:
            lst = A[w]
            res = ""
            for y in lst:
                res += str(y) + " "
            print(res)
        else:
            print(-1)

# [Collections] Exercise 3: Collections.namedtuple()
if __name__ == '__main__':

    # The first line contains N, the total number of students
    N = int(input())

    # The second line contains the names of the columns in any order
    A, B, C, D = input().split()

    # Identify the index of the MARKS column
    if A == "MARKS":
        index = 0
    elif B == "MARKS":
        index = 1
    elif C == "MARKS":
        index = 2
    else:
        index = 3

    sigma = 0

    # The next N lines contains the marks, IDs, name and class, under their respective column names
    for student in range(N):
        # List of attributes for a student
        lst = list(input().split())

        # Mark of a student
        mark = lst[index]
        sigma += int(mark)

    # Calculate average of all marks
    res = sigma / N
    formatted_res = "{:.2f}".format(res)
    print(formatted_res)

# [Collections] Exercise 4: Collections.OrderedDict()
if __name__ == '__main__':

    # The first line contains the number of items, N
    N = int(input())

    # Create an ordered dictionary of selled items
    selledItems = OrderedDict()

    #  The next N lines contain the item's name and price, separated by a space
    for product in range(N):
        item, price = input().rsplit(" ", 1)
        price = int(price)

        if item in selledItems:
            selledItems[item] += price
        else:
            selledItems[item] = price

    for key in selledItems.keys():
        print(key + " " + str(selledItems[key]))

# [Collections] Exercise 5: Collections.deque()
from collections import deque

if __name__ == '__main__':

    # The first line contains an integer N, the number of operations
    N = int(input())

    # Create an empty deque
    d = deque()

    # The next N lines contains the space separated names of methods and their values
    for i in range(N):
        method, *value = input().split()
        value = list(map(int, value))

        if method == "append":
            d.append(value[0])
        elif method == "appendleft":
            d.appendleft(value[0])
        elif method == "popleft":
            d.popleft()
        else:
            d.pop()

    res = ""
    for elem in d:
        res += str(elem) + " "
    print(res)

# [Collections] Exercise 6: Word Order
from collections import OrderedDict

if __name__ == '__main__':

    # The first line contains the integer, N
    N = int(input().strip())

    # Create an empty ordered dictionary
    dictionary_of_words = OrderedDict()

    # The next N lines each contain a word
    for i in range(N):
        word = input().strip()
        if word in dictionary_of_words.keys():
            dictionary_of_words[word] += 1
        else:
            dictionary_of_words[word] = 1

    res = ""
    for val in dictionary_of_words.values():
        res += str(val) + " "
    print(len(dictionary_of_words))
    print(res)

# [Collections] Exercise 7: Company Logo
if __name__ == '__main__':

    # The inoput contains the string s
    string = input()

    # Create an empty ordered dictionary
    d, d_final = OrderedDict(), OrderedDict()

    # Create an ordered dictionary of characters (keys) and their occurences (values)
    for character in string:
        if character in d.keys():
            d[character] += 1
        else:
            d[character] = 1

    # Identify the 3 most used characters
    while len(d_final) < 3:
        max1 = max(d.values())
        keys_with_max = [key for key in d.keys() if d[key] == max1]  # adding elements that satisfy the if condition
        """ List comprehension
        result = []
        for key in d.keys():
            if d[key] == max1:
                result.append(key)
        """
        key = sorted(keys_with_max)[0]

        d_final[key] = max1
        del d[key]

    for key, value in d_final.items():
        print(str(key) + " " + str(value))

# [Collections] Exercise 8: Piling Up!
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        base = 99999999999999
        n = input()

        # Create deque of cubes
        cubes = deque(map(int, input().split()))

        ok = True

        while ok and len(cubes) > 0:
            if cubes[0] >= cubes[-1]:
                if cubes[0] <= base:
                    base = cubes[0]
                    cubes.popleft()
                else:
                    ok = False
            else:
                if cubes[-1] <= base:
                    base = cubes[-1]
                    cubes.reverse()
                    cubes.popleft()
                else:
                    ok = False
        print("Yes" if ok else "No")

# Date and Time (all – total: 2 - max points: 40)
# https://www.hackerrank.com/domains/python/py-date-time

# [Date and Time] Exercise 1: Calendar Module
if __name__ == '__main__':
    # Month, day, year
    date_string = input()
    date = datetime.strptime(date_string, '%m %d %Y').date()

    # Get day name
    dayName = date.strftime("%A")
    dayName = str(dayName)
    print(dayName.upper())


# [Date and Time] Exercise 2: Time Delta
# Complete the time_delta function below.
def time_delta(t1, t2):
    # Convert the strings t1 and t2 to datetime objects

    # Data format example: Sun 10 May 2015 13:54:36 -0700
    t1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    diff = abs(t1 - t2)
    res = int(diff.total_seconds())
    return str(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# Exceptions (only 1 - max points: 10)
# https://www.hackerrank.com/challenges/exceptions

# [Exceptions] Exercise 1: Exceptions
if __name__ == '__main__':

    # Number of test cases
    T = int(input())

    # The next T lines contain the test cases
    for tc in range(T):
        a, b = input().split()
        try:
            print(round(int(a) / int(b)))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)

# • Built-ins (only 3 - max points: 80)
# https://www.hackerrank.com/challenges/zipped
# https://www.hackerrank.com/challenges/python-sort-sort
# https://www.hackerrank.com/challenges/ginorts

# [Built-ins] Exercise 1: Zipped!
if __name__ == '__main__':

    # The first line contains N, the number of students, and X, the number of subjects
    N, X = input().split()
    N = int(N)
    X = int(X)

    list_of_total_marks = []

    for subject in range(X):
        # Read the marks of the N students for subject Xi
        list_of_marks = list(map(float, input().split()))
        list_of_total_marks += [list_of_marks]

    list_of_total_marks = zip(*list_of_total_marks)
    for tuple_of_marks in list_of_total_marks:
        print(sum(tuple_of_marks) / len(tuple_of_marks))


# [Built-ins] Exercise 2: Athlete Sort
if __name__ == '__main__':
    nm = input().split()

    # n, number of athletes
    n = int(nm[0])

    # m, the number of attributes
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # k, the index of the attribute for whom we will sort the original array
    k = int(input())

    # Return a sorted array, using x[k] as the key for sorting
    # [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]
    sorted_arr = sorted(arr, key=lambda x: x[k])

    for i in range(n):
        res = ""
        for c in sorted_arr[i]:
            res += str(c) + " "
        print(res)

# [Built-ins] Exercise 3: ginortS
if __name__ == '__main__':

    # S, the string to be sorted
    S = list(map(str, input()))

    even_digits_list, odd_digits_list = [], []
    lowercase_letters_list, uppercase_letters_list = [], []

    for i in range(len(S)):

        # Check if character is an even digit and add it to the list of even digits
        if S[i].isdigit() and int(S[i]) % 2 == 0:
            even_digits_list.append(str(S[i]))

        # Check if character is an odd digit and add it to the list of odd digits
        elif S[i].isdigit() and int(S[i]) % 2 != 0:
            odd_digits_list.append(str(S[i]))

        # Check if character is an uppercase letter
        elif S[i].isalpha() and S[i].isupper():
            uppercase_letters_list.append(str(S[i]))

        # The character is a lowercase letter
        else:
            lowercase_letters_list.append(str(S[i]))

    # Sort all the lists
    even_digits_list = sorted(even_digits_list)
    odd_digits_list = sorted(odd_digits_list)
    uppercase_letters_list = sorted(uppercase_letters_list)
    lowercase_letters_list = sorted(lowercase_letters_list)

    # Concatenate all the string elements into one string, each
    string_of_even_digits = "".join(even_digits_list)
    string_of_odd_digits = "".join(odd_digits_list)
    string_of_uppercase_letters = "".join(uppercase_letters_list)
    string_of_lowercase_letters = "".join(lowercase_letters_list)

    # Concatenate all string to have one single string
    res = string_of_lowercase_letters + string_of_uppercase_letters + string_of_odd_digits + string_of_even_digits

    print(res)

# Python Functionals (only 1 - max points: 20)
# https://www.hackerrank.com/challenges/map-and-lambda-expression

# [Python Functionals] Exercise 1: Map and Lambda Function
cube = lambda x: pow(x, 3)


def fibonacci(n):
    # return a list of fibonacci numbers
    list_of_fibonacci = []

    for num in range(n):
        if num == 0 or num == 1:
            list_of_fibonacci.append(num)
        else:
            res = int(list_of_fibonacci[num - 2]) + int(list_of_fibonacci[num - 1])
            list_of_fibonacci.append(res)
    return list_of_fibonacci


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# Regex and Parsing challenges (all – total: 17 - max points: 560)
# https://www.hackerrank.com/domains/python/py-regex
# https://www.hackerrank.com/domains/python/py-regex/2

# [Regex and Parsing challenges] Exercise 1: Detect Floating Point Number

# The first line contains an integer N, the number of test cases
T = int(input())

# The next T line(s) contains a string N
for i in range(T):
    string = input()

    # The input string has to:
    # - begin with (^) the characters + or - that appears 0 or 1 time
    # - it continues with a digit \d that appears 0 or more times (*)
    # - it continues with the character \. that apears exatly one time ({1})
    # - it ends with ($) a digit \d that appers one or more times (+)
    print(bool(re.match(r"^[+-]{0,1}\d*\.{1}\d+$",string)))


# [Regex and Parsing challenges] Exercise 2: Re.split()
regex_pattern = r"[,.]+" # Do not delete 'r'.
print("\n".join(re.split(regex_pattern, input())))

# [Regex and Parsing challenges] Exercise 3: Re.start() & Re.end()
string = input()
substring = input()

found = False
i = 0
while True:
    m = re.search(substring, string[i:])

    # If the substring is contained in the original string
    if m is not None:

        # Print the indexes of the starting and ending points in the original substring
        print("(" + str( i + m.start()) + ", " + str( i + m.end() - 1) + ")")
        found = True
        i += m.start() + 1

    # If the result of the search function is "None" exit the loop and print (-1,-1)
    else:
        break
if not found:
    print("(-1, -1)")


# [Regex and Parsing challenges] Exercise 4: Re.findall() & Re.finditer()
list_of_vowels = re.findall(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])", input())

for string in list_of_vowels:
    print(string)

if len(list_of_vowels) == 0:
    print(-1)


# [Regex and Parsing challenges] Exercise 5: Group(), Groups() & Groupdict()
# \1 matches the string that was matched by the content of group 1
match = re.search(r'([abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789])\1+', input())

if match:
    print(match.group(1))
else:
    print(-1)

# [Regex and Parsing challenges] Exercise 6: Validating and Parsing Email Addresses
number_of_test_cases = int(input())

for i in range(number_of_test_cases):

    username, mail_address = input().split()

    if bool(re.match(r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>", mail_address)):
        print(username, mail_address)


# [Regex and Parsing challenges] Exercise 7: Validating phone numbers
number_phone_numbers = int(input())

for i in range(number_phone_numbers):
    phone_number = input()
    if bool(re.search(r"^(7|8|9){1}\d{9}$", phone_number)):
        print("YES")
    else:
        print("NO")

# [Regex and Parsing challenges] Exercise 8: Validating UID
# I CHECKED THE HACKERRANK SOLUTION BECAUSE I DID'T KNOW HOW TO APPLY ALL THE FILTERS TOGETHER

# Filters to apply on the single UID
no_repeats = r"(?!.*(.).*\1)"
two_or_more_upper = r"(.*[A-Z]){2,}"
three_or_more_digits = r"(.*\d){3,}"
ten_alphanumerics = r"[a-zA-Z0-9]{10}"
filters = no_repeats, two_or_more_upper, three_or_more_digits, ten_alphanumerics

number_of_UIDs = int(input())

for i in range(number_of_UIDs):
    UID = input()

    res = "Invalid"

    for f in filters:
        if re.match(f, UID):
            res = "Valid"
        else:
            res = "Invalid"
            break

    print(res)


# [Regex and Parsing challenges] Exercise 9: Validating Roman Numerals
# CHECKED ONLINE SOLUTIONS ON HACKERRANK
# ?: non capturing group (used to match but not i'm not interested in that group)
thousands = "(?:M{0,3}){0,1}"
hundreds = "(?:D{0,1}C{0,3}|CM|CD){0,1}"
tens = "(?:L{0,1}X{0,3}|XC|XL){0,1}"
digits = "(?:V{0,1}I{0,3}|IV|IX){0,1}"
regex_pattern = r"^" + thousands + hundreds + tens + digits + "$"
print(str(bool(re.match(regex_pattern, input()))))


# [Regex and Parsing challenges] Exercise 10: Hex Color Code
N = int(input())

for i in range(N):
    list_of_matches = re.findall(r"[\s:](#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})", input())
    for match in list_of_matches:
        print(match)

# [Regex and Parsing challenges] Exercise 11: HTML Parser - Part 1
N = int(input())

html_data = ""

for i in range(N):
    html_data += input()

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for a in attrs:
            print('-> ' + str(a[0]) + " > " + str(a[1]))

    def handle_endtag(self, tag):
        print('End   :',tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for a in attrs:
            print('-> ' + str(a[0]) + " > " + str(a[1]))

parser = MyHTMLParser()
parser.feed(html_data)


# [Regex and Parsing challenges] Exercise 12: HTML Parser - Part 2
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if len(data) > 1:
            print(">>> Data", "\n" + data)

    def handle_comment(self, data):
        list_of_strings = data.split("\n")
        if len(list_of_strings) == 1:
            print(">>> Single-line Comment" + "\n" + data)
        else:
            print(">>> Multi-line Comment" + "\n" + data)

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()


# [Regex and Parsing challenges] Exercise 13: Detect HTML Tags, Attributes and Attribute Values
class MyHTMLParser(HTMLParser):

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if len(attrs) > 0:
            for a in attrs:
                print("-> " + a[0] + " > " + a[1])

    def handle_starttag(self, tag, attrs):
        print(tag)
        if len(attrs) > 0:
            for a in attrs:
                print("-> " + a[0] + " > " + a[1])

html = ""

for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()


# [Regex and Parsing challenges] Exercise 14: Regex Substitution
number_of_lines = int(input())

def substituteSymbols(match):
    stringToBeSubstituted = match.string[match.start():match.end()]
    if stringToBeSubstituted == "&&":
        return "and"
    if stringToBeSubstituted == "||":
        return "or"

for i in range(number_of_lines):
    print(re.sub("(?<=\s{1})(&&|\|\|)(?=\s{1})", substituteSymbols, input()))

# [Regex and Parsing challenges] Exercise 15: Validating Credit Card Numbers
n = int(input())

for i in range(n):
    line = input()
    valid = True
    is_digits_and_dashes_ok = re.search("^([0-9]{4}(-?)){3}[0-9]{4}$", line)
    if is_digits_and_dashes_ok:
        line = line.replace("-", "")
    else:
        valid = False

    is_start_ok = re.search("^[456]", line)
    if not is_start_ok:
        valid = False

    has_repeating_four = re.search(r"(.)\1{3,}", line)
    if has_repeating_four:
        valid = False

    print("Valid" if valid else "Invalid")


# [Regex and Parsing challenges] Exercise 16: Validating Postal Codes
regex_integer_in_range = r"[100000-999999]{6}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# [Regex and Parsing challenges] Exercise 17: Matrix Script
# !/bin/python3
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix = zip(*matrix)

finalString = ""

for elem in matrix:
    elem = "".join(elem)
    finalString += elem

finalString = re.sub(r'(?<=[a-zA-Z0-9])([^a-zA-Z0-9]{1,})(?=[a-zA-Z0-9])', " ", finalString)

print(finalString)

# XML (all – total: 2 - max points: 40)
# https://www.hackerrank.com/domains/python/xml

# [XML] Exercise 1: XML 1 - Find the Score
def get_attr_number(node):
    # print(node)
    # all_links = tree.findall('.//{http://www.w3.org/2005/Atom}link')
    # print(all_links)
    # print(len(node))
    # >>> root[4].attrib
    # all_links = tree.findall('')
    '''sumOfElements = 0
    for i in range(len(node)):
        #print(node[i].attrib)
        sumOfElements += len(node[i].attrib)
    return sumOfElements + len(node.attrib)'''
    sumOfAttributes = 0
    for e in tree.iter():
        sumOfAttributes += len(e.attrib)
    return sumOfAttributes


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# [XML] Exercise 2: XML2 - Find the Maximum Depth
# APPROACH FOUND ON STACKOVERFLOW
maxdepth = 0

def depth(elem, level):
    global maxdepth

    if (level == maxdepth):
        maxdepth += 1
    # recursive call to function to get the depth
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# Closures and Decorations (all – total: 2 - max points: 60)
# https://www.hackerrank.com/domains/python/closures-and-decorators

# [Closures and Decorations] Exercise 1: Standardize Mobile Number Using Decorators
import re

def wrapper(f):
    def fun(l):
        lstOfSortedNumbers = []
        for cell in l:
            last_10_characters = "+91 " + cell[-10:-5] + " " + cell[-5:]
            lstOfSortedNumbers.append(last_10_characters)
        f(lstOfSortedNumbers)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

# [Closures and Decorations] Exercise 2: Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key = lambda x: int(x[2]) )
        listOfSortedPeople = []
        for person in people:
            listOfSortedPeople.append(f(person))
        return listOfSortedPeople
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# Numpy (all – total: 15 - max points: 300)
# https://www.hackerrank.com/domains/python/numpy
# https://www.hackerrank.com/domains/python/numpy/2

# [Numpy] Exercise 1: Arrays
def arrays(arr):
    # Convert array of strings into numpy array of float
    arr = numpy.array(arr,float)

    # Reverse/flip the order of the numpy array
    arr =  numpy.flip(arr)

    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# [Numpy] Exercise 2: Concatenate
N, M, P = input().split()
N, M, P = int(N), int(M), int(P)

lst = []

for i in range(N+M):
    arr = list(map(int, input().split()))
    lst.append(arr)
print(numpy.array(lst,int))

# [Numpy] Exercise 3: Min and Max
# nxm dimension array
n, m = map(int, input().split())

lst = []

for row in range(n):
    listOfIntegers = list(map(int, input().split()))
    lst.append(listOfIntegers)

lst = numpy.array(lst)
minimun = numpy.min(lst, axis = 1)
print(max(minimun))


# [Numpy] Exercise 4: Sum and Prod
n, m = map(int, input().split())

lst = []

for row in range(n):
    listOfIntegers = list(map(int, input().split()))
    lst.append(listOfIntegers)

lst = numpy.array(lst)
resSum = numpy.sum(lst, axis = 0)
print(numpy.prod(resSum))

# [Numpy] Exercise 5: Mean, Var, and Std
n, m = map(int, input().split())

lst = []

for row in range(n):
    listOfIntegers = list(map(int, input().split()))
    lst.append(listOfIntegers)

# Setting numpy version, if not the format won't be accepted on HackerRank
numpy.set_printoptions(legacy='1.13')

lst = numpy.array(lst)
print(numpy.mean(lst, axis = 1))
print(numpy.var(lst, axis = 0))
print(numpy.std(lst))


# [Numpy] Exercise 6: Floor, Ceil and Rint
listOfFloat = list(map(float, input().split()))

# Setting numpy version, if not the format won't be accepted on HackerRank
numpy.set_printoptions(legacy='1.13')

print(numpy.floor(listOfFloat))
print(numpy.ceil(listOfFloat))
print(numpy.rint(listOfFloat))


# [Numpy] Exercise 7: Transpose and Flatten
n, m = map(int, input().split())

lst = []

for row in range(n):
    listOfIntegers = list(map(int, input().split()))
    lst.append(listOfIntegers)

# Setting numpy version, if not the format won't be accepted on HackerRank
#numpy.set_printoptions(legacy='1.13')

lst = numpy.array(lst)

print(numpy.transpose(lst))
print(lst.flatten())


# [Numpy] Exercise 8: Zeros and Ones

# Create tuple with n dimension
shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, dtype = numpy.int))
print(numpy.ones(shape, dtype = numpy.int))


# [Numpy] Exercise 9: Eye and Identity
n, m = map(int, input().split())

# Setting numpy version, if not the format won't be accepted on HackerRank
numpy.set_printoptions(legacy='1.13')

print(numpy.eye(n,m))


# [Numpy] Exercise 10: Dot and Cross
matrixA, matrixB = [], []

N = int(input())

for i in range(N):
    listOfIntegers = list(map(int,input().split()))
    matrixA.append(listOfIntegers)

matrixA = numpy.array(matrixA)

for i in range(N):
    listOfIntegers = list(map(int,input().split()))
    matrixB.append(listOfIntegers)

matrixB = numpy.array(matrixB)

# Perform matrix multiplication (dot)
print(numpy.dot(matrixA,matrixB))


# [Numpy] Exercise 11: Array Mathematics
arrayA, arrayB = [], []

N, M = map(int, input().split())

for i in range(N):
    listOfIntegers = list(map(int,input().split()))
    arrayA.append(listOfIntegers)

arrayA = numpy.array(arrayA)

for i in range(N):
    listOfIntegers = list(map(int,input().split()))
    arrayB.append(listOfIntegers)

arrayB = numpy.array(arrayB)

print(numpy.add(arrayA,arrayB))
print(numpy.subtract(arrayA,arrayB))
print(numpy.multiply(arrayA,arrayB))
print(arrayA//arrayB)
print(numpy.mod(arrayA,arrayB))
print(numpy.power(arrayA,arrayB))


# [Numpy] Exercise 12: Inner and Outer
arrayA = list(map(int,input().split()))
arrayA = numpy.array(arrayA)

arrayB = list(map(int,input().split()))
arrayB = numpy.array(arrayB)

print(numpy.inner(arrayA,arrayB))
print(numpy.outer(arrayA,arrayB))


# [Numpy] Exercise 13: Polynomials
lst = list(map(float,input().split()))
lst = numpy.array(lst)

x = float(input())

# Evaluate the polynomial at value x
print(numpy.polyval(lst, x))


# [Numpy] Exercise 14: Shape and Reshape
arr = list(map(int,input().split()))
arr = numpy.array(arr)

print(numpy.reshape(arr,(3,3)))


# [Numpy] Exercise 15: Linear Algebra
n = int(input())

arr = []

for i in range(n):
    listOfFloat = list(map(float,input().split()))
    arr.append(listOfFloat)

arr = numpy.array(arr)
det = numpy.linalg.det(arr)
print(round(det,2))




