# Examples and Practice for Data Structures & Algorithms

# --- 1. Arrays (Lists) ---
arr = [1, 2, 3]
arr.append(4)
print('Array:', arr)
print('Second element:', arr[1])  # 2

# --- 2. Linked List ---
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create linked list: 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Traverse linked list
current = head
while current:
    print('Linked list node:', current.val)
    current = current.next

# --- 3. Stack ---
stack = []
stack.append(10)
stack.append(20)
print('Stack pop:', stack.pop())  # 20

# --- 4. Queue ---
from collections import deque
queue = deque()
queue.append('a')
queue.append('b')
print('Queue popleft:', queue.popleft())  # 'a'

# --- 5. Hash Table (Dictionary) ---
d = {'x': 1, 'y': 2}
d['z'] = 3
print('Dictionary:', d)
print('Value for y:', d['y'])

# --- 6. Tree (Binary Tree) ---
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print('Tree node:', node.val)
        inorder(node.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
inorder(root)  # 3, 5, 7

# --- 7. Graph (Adjacency List) ---
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
# DFS traversal
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print('Visited:', node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
dfs(graph, 'A')

# --- 8. Sorting (Bubble Sort Example) ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print('Bubble sorted:', bubble_sort([5, 2, 9, 1]))

# --- 9. Searching (Binary Search) ---
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print('Binary search for 9:', binary_search([1, 2, 5, 9], 9))

# --- 10. Dynamic Programming (Fibonacci with Memoization) ---
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
print('Fibonacci(6):', fib(6))

# --- 11. Recursion (Factorial) ---
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print('Factorial(5):', factorial(5))

# --- Questions ---
# 1. How would you reverse a singly linked list?
# 2. What is the time complexity of bubble sort?
# 3. How would you traverse a tree in post-order?
# 4. What is the difference between DFS and BFS in a graph?
# 5. Why is memoization useful in dynamic programming? 