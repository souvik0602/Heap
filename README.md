# 🔢 Heap Operations in Python

This project demonstrates how to use Python's built-in `heapq` module to:

1. Find the **n-th smallest element** in a list
2. **Sort a list** in ascending order using a min-heap (without using `sort()` or `sorted()`)

---

## 📌 Features

- Uses a **min-heap** to retrieve the n-th smallest element efficiently.
- Demonstrates sorting using a **heap-based approach**.
- Cleanly separates logic into two functions:
  - `nelement(nums, n)`: finds the n-th smallest element
  - `sort_list(nums)`: sorts the list using a heap

---

## 🚀 How It Works

### `nelement(nums, n)`

- Uses `heapq.nsmallest()` to get the `n` smallest elements and returns the last one (`[-1]`), which is the n-th smallest.

### `sort_list(nums)`

- First converts the list into a heap using `heapq.heapify()`.
- Then repeatedly uses `heapq.heappop()` to extract the smallest element until the list is empty, effectively sorting the list.

---

## 🧪 Example Output

```python
Original list: [34, 7, 98, 53, 100, 87, 9, 2, 49, 71]
The nth element of the list is: 9
Heap: [2, 7, 9, 34, 49, 87, 98, 53, 100, 71]
The Sorted list is: [2, 7, 9, 34, 49, 53, 71, 87, 98, 100]


📚 Requirements
Python 3.x (no external libraries required)

📄 License
This project is licensed under the MIT License.
