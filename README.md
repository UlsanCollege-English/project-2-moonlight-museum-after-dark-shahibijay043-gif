# Project 2: Moonlight Museum After Dark

## Team information
- Team name: 
- Members: 
- Repository name:

---

## Project summary
Our project builds a system to manage museum artifacts after dark.  
It uses different data structures like a BST, queue, stack, and linked list to organize artifacts, restoration requests, exhibit routes, and reports in a simple and efficient way.

---

## Feature checklist

### Core structures
- [x] `Artifact` class/record
- [x] `ArtifactBST`
- [x] `RestorationQueue`
- [x] `ArchiveUndoStack`
- [x] `ExhibitRoute` singly linked list

### BST features
- [x] insert artifact
- [x] search by ID
- [x] preorder traversal
- [x] inorder traversal
- [x] postorder traversal
- [x] duplicate IDs ignored

### Queue features
- [x] add request
- [x] process next request
- [x] peek next request
- [x] empty check
- [x] size

### Stack features
- [x] push action
- [x] undo last action
- [x] peek last action
- [x] empty check
- [x] size

### Linked list features
- [x] add stop to end
- [x] remove first matching stop
- [x] list stops in order
- [x] count stops

### Utility/report features
- [x] category counts
- [x] unique rooms
- [x] sort by age
- [x] linear search by name

### Integration
- [x] `demo_museum_night()`
- [x] at least 8 artifacts in demo
- [x] demo shows system parts working together

---

## Design note (150-250 words)

A Binary Search Tree (BST) is used to store artifacts because each artifact has a unique ID, and BST allows fast searching, insertion, and ordered traversal. This makes it efficient to manage and retrieve artifacts based on their ID.

A queue is used for restoration requests because requests should be handled in the order they arrive (FIFO). This ensures fairness and realistic processing of museum tasks.

A stack is used for undo actions because it follows Last-In-First-Out (LIFO). The most recent action is undone first, which matches real-world undo behavior.

A linked list is used for the exhibit route because it allows easy insertion and removal of stops without shifting elements like in arrays. It is flexible for managing routes.

The system is organized into separate classes for each data structure, making the code clean and modular. Utility functions handle reporting tasks like sorting, searching, and counting, which keeps logic simple and reusable.

---

## Complexity reasoning

- `ArtifactBST.insert`: `O(h)` where h is tree height, because it follows one path down the tree.
- `ArtifactBST.search_by_id`: `O(h)` for the same reason as insert.
- `ArtifactBST.inorder_ids`: `O(n)` because it visits every node once.
- `RestorationQueue.process_next_request`: `O(1)` because deque pop from front is constant time.
- `ArchiveUndoStack.undo_last_action`: `O(1)` because list pop is constant time.
- `ExhibitRoute.remove_stop`: `O(n)` because it may traverse the whole list.
- `sort_artifacts_by_age`: `O(n log n)` due to Python sorting.
- `linear_search_by_name`: `O(n)` because it checks each item.

---

## Edge-case checklist

### BST
- [x] insert into empty tree → creates root
- [x] search for missing ID → returns None
- [x] empty traversals → returns empty list
- [x] duplicate ID → ignored

### Queue
- [x] process empty queue → returns None
- [x] peek empty queue → returns None

### Stack
- [x] undo empty stack → returns None
- [x] peek empty stack → returns None

### Exhibit route linked list
- [x] empty route → handled correctly
- [x] remove missing stop → returns False
- [x] remove first stop → updates head
- [x] remove middle stop → links correctly
- [x] remove last stop → removes properly
- [x] one-stop route → works correctly

### Reports
- [x] empty artifact list → returns empty results
- [x] repeated categories → counted correctly
- [x] repeated rooms → stored once in set
- [x] missing artifact name → returns None
- [x] same-age artifacts → sorted correctly

---

## Demo plan / how to run

Run tests:
```bash
pytest -q