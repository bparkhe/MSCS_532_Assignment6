# MSCS_532_Assignment6
# Data Structures Implementation in Python

This repository provides Python implementations for fundamental data structures, including arrays, stacks, queues, linked lists, and optional rooted trees. The code demonstrates basic operations and allows for experimentation with these structures to understand their behavior and performance.

---

## Features

### Implemented Data Structures

1. **Array**:
   - Basic operations: insertion, deletion, and access.
   - Example use case: Random access storage.

2. **Matrix**:
   - Supports element updates and access.
   - Example use case: Mathematical computations or tabular data storage.

3. **Stack**:
   - Operations: `push`, `pop`, and `peek`.
   - Example use case: Expression evaluation, function call stack.

4. **Queue**:
   - Operations: `enqueue` and `dequeue`.
   - Example use case: Task scheduling, breadth-first search.

5. **Singly Linked List**:
   - Operations: insertion, deletion, and traversal.
   - Example use case: Dynamic data storage, adjacency lists for graphs.

6. **Rooted Tree** (Optional):
   - Node-based structure to represent hierarchical data.
   - Example use case: File systems, organizational charts.

---

## Prerequisites

To run the code, you need:

- Python 3.6 or higher installed on your system.
- A basic understanding of Python programming.

---

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo/data-structures-python.git
    cd data-structures-python
    ```

2. Open the Python script in your favorite IDE or text editor.

3. Run the script:
    ```bash
    python main.py
    ```

---

## Example Usage

### Arrays
```python
arr = Array()
arr.insert(0, 10)
arr.insert(1, 20)
print(arr.access(1))  # Output: 20
arr.delete(0)
