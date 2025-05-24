# Data Structures & Algorithms: Key Concepts

This note reviews the most essential data structures and algorithms for Python interviews. Mastery of these topics is crucial for technical interviews and real-world problem solving.

---

## 1. Arrays (Lists in Python)

- **What:** Ordered, mutable collections of elements.
- **Python:** `list`
- **Common operations:** Indexing, appending, slicing, iterating.
- **Example:**
  ```python
  arr = [1, 2, 3]
  arr.append(4)
  print(arr[1])  # 2
  ```

---

## 2. Linked Lists

- **What:** Linear collection of nodes, each pointing to the next.
- **Types:** Singly, doubly, circular.
- **Python:** Not built-in; implemented via classes.
- **Example:**
  ```python
  class Node:
      def __init__(self, val):
          self.val = val
          self.next = None

  head = Node(1)
  head.next = Node(2)
  ```

---

## 3. Stacks

- **What:** LIFO (Last-In, First-Out) structure.
- **Python:** Use `list` (`append`/`pop`) or `collections.deque`.
- **Example:**
  ```python
  stack = []
  stack.append(1)
  stack.append(2)
  print(stack.pop())  # 2
  ```

---

## 4. Queues

- **What:** FIFO (First-In, First-Out) structure.
- **Python:** Use `collections.deque` or `queue.Queue`.
- **Example:**
  ```python
  from collections import deque
  queue = deque()
  queue.append(1)
  queue.append(2)
  print(queue.popleft())  # 1
  ```

---

## 5. Hash Tables (Dictionaries)

- **What:** Key-value mapping, fast lookup.
- **Python:** `dict`
- **Example:**
  ```python
  d = {'a': 1, 'b': 2}
  print(d['a'])  # 1
  ```

---

## 6. Trees

- **What:** Hierarchical structure with nodes and children.
- **Types:** Binary tree, BST, AVL, Trie, etc.
- **Python:** Implemented via classes.
- **Example:**
  ```python
  class TreeNode:
      def __init__(self, val):
          self.val = val
          self.left = None
          self.right = None
  root = TreeNode(10)
  root.left = TreeNode(5)
  root.right = TreeNode(15)
  ```

---

## 7. Graphs

- **What:** Nodes (vertices) connected by edges.
- **Representations:** Adjacency list (dict of lists), adjacency matrix.
- **Example:**
  ```python
  graph = {
      'A': ['B', 'C'],
      'B': ['A', 'D'],
      'C': ['A'],
      'D': ['B']
  }
  ```

---

## 8. Sorting Algorithms

- **Common types:** Bubble, Selection, Insertion, Merge, Quick, Heap sort.
- **Python:** Built-in `sorted()` uses Timsort (hybrid, stable, O(n log n)).
- **Example:**
  ```python
  arr = [3, 1, 4, 2]
  print(sorted(arr))  # [1, 2, 3, 4]
  ```

---

## 9. Searching Algorithms

- **Linear search:** O(n), scan each element.
- **Binary search:** O(log n), requires sorted array.
- **Example:**
  ```python
  # Linear search
  def linear_search(arr, target):
      for i, v in enumerate(arr):
          if v == target:
              return i
      return -1

  # Binary search
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
  ```

---

## 10. Dynamic Programming (DP)

- **What:** Solving problems by breaking them into overlapping subproblems and storing results (memoization/tabulation).
- **Examples:** Fibonacci, coin change, knapsack.
- **Example:**
  ```python
  # Memoized Fibonacci
  def fib(n, memo={}):
      if n in memo:
          return memo[n]
      if n <= 1:
          return n
      memo[n] = fib(n-1, memo) + fib(n-2, memo)
      return memo[n]
  ```

---

## 11. Recursion

- **What:** A function calling itself to solve subproblems.
- **Key:** Always have a base case!
- **Example:**
  ```python
  def factorial(n):
      if n == 0:
          return 1
      return n * factorial(n-1)
  ```

---

## **Key Interview Tips**

- Know time and space complexity (Big O) for each structure/algorithm.
- Practice coding each from scratch.
- Understand when to use each structure for optimal performance.
- Be able to explain your reasoning and trade-offs.

---

**Recommended Practice:**  
Implement each structure and algorithm in Python. Practice common interview problems (e.g., reverse a linked list, traverse a tree, BFS/DFS on graphs, dynamic programming patterns). 