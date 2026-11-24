# dsa-grind

Data structures and algorithms practice in Python, grouped by pattern. The file structure and complexity notes follow [WORKFLOW..md](WORKFLOW..md).

As [me.md](me.md) says, LLMs are used to guide learning and practice, and at times to polish comments.

## Topics

| Folder | Python files | Examples |
| :--- | ---: | :--- |
| [arrays and matrices](arrays%20and%20matrices) | 12 | spiral matrix, rotate image, set matrix zeroes |
| [search](search) | 11 | number of islands, BFS, DFS, binary search trees |
| [random](random) | 10 | merged intervals, search a 2D matrix, sort colors |
| [c5](c5) | 10 | short contest-style problems |
| [prefix-sum](prefix-sum) | 7 | subarray sum, product except self, 2D range sum |
| [linked-list](linked-list) | 6 | cycle detection, palindrome, middle node |
| [sliding window mastery](sliding%20window%20mastery) | 5 | minimum window, longest substring |
| [sorts](sorts) | 5 | counting sort, selection sort, relative sort |
| [hashmap](hashmap) | 3 | two sum, valid anagram |
| [stack](stack) | 3 | min stack, valid parentheses |
| [two-pointers](two-pointers) | 1 | two sum II |

Short notes live in [guides](guides), including a [tree complexity reference](guides/tree-complexity-reference.md).

**A good place to start reading:** [search/number-of-islands.py](search/number-of-islands.py).

## Tech stack

Python 3.

## How to run

Files that include their own examples run directly:

```bash
git clone https://github.com/blip-cmd/dsa-grind.git
cd dsa-grind
python search/number-of-islands.py
```

## What I would improve next

- Add automated tests for the solutions and run them in CI.
- Use one file naming style throughout.
- Add dynamic programming and shortest-path sections.
