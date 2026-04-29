from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Artifact:
    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    artifact_id: int
    description: str


# ---------------- BST ----------------

class TreeNode:
    def __init__(self, artifact):
        self.artifact = artifact
        self.left = None
        self.right = None


class ArtifactBST:
    def __init__(self):
        self.root = None

    def insert(self, artifact):
        if not self.root:
            self.root = TreeNode(artifact)
            return True

        current = self.root
        while True:
            if artifact.artifact_id == current.artifact.artifact_id:
                return False
            elif artifact.artifact_id < current.artifact.artifact_id:
                if not current.left:
                    current.left = TreeNode(artifact)
                    return True
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(artifact)
                    return True
                current = current.right

    def search_by_id(self, artifact_id):
        current = self.root
        while current:
            if artifact_id == current.artifact.artifact_id:
                return current.artifact
            elif artifact_id < current.artifact.artifact_id:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_ids(self):
        result = []

        def dfs(node):
            if node:
                dfs(node.left)
                result.append(node.artifact.artifact_id)
                dfs(node.right)

        dfs(self.root)
        return result

    def preorder_ids(self):
        result = []

        def dfs(node):
            if node:
                result.append(node.artifact.artifact_id)
                dfs(node.left)
                dfs(node.right)

        dfs(self.root)
        return result

    def postorder_ids(self):
        result = []

        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                result.append(node.artifact.artifact_id)

        dfs(self.root)
        return result


# ---------------- QUEUE ----------------

class RestorationQueue:
    def __init__(self):
        self._items = deque()

    def add_request(self, request):
        self._items.append(request)

    def process_next_request(self):
        if self._items:
            return self._items.popleft()
        return None

    def peek_next_request(self):
        if self._items:
            return self._items[0]
        return None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


# ---------------- STACK ----------------

class ArchiveUndoStack:
    def __init__(self):
        self._items = []

    def push_action(self, action):
        self._items.append(action)

    def undo_last_action(self):
        if self._items:
            return self._items.pop()
        return None

    def peek_last_action(self):
        if self._items:
            return self._items[-1]
        return None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


# ---------------- LINKED LIST ----------------

class ExhibitNode:
    def __init__(self, stop_name):
        self.stop_name = stop_name
        self.next = None


class ExhibitRoute:
    def __init__(self):
        self.head = None

    def add_stop(self, stop_name):
        new_node = ExhibitNode(stop_name)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def remove_stop(self, stop_name):
        current = self.head
        prev = None

        while current:
            if current.stop_name == stop_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True

            prev = current
            current = current.next

        return False

    def list_stops(self):
        result = []
        current = self.head

        while current:
            result.append(current.stop_name)
            current = current.next

        return result

    def count_stops(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


# ---------------- UTILITIES ----------------

def count_artifacts_by_category(artifacts):
    result = {}
    for art in artifacts:
        result[art.category] = result.get(art.category, 0) + 1
    return result


def unique_rooms(artifacts):
    rooms = set()
    for art in artifacts:
        rooms.add(art.room)
    return rooms


def sort_artifacts_by_age(artifacts, descending=False):
    return sorted(artifacts, key=lambda x: x.age, reverse=descending)


def linear_search_by_name(artifacts, name):
    for art in artifacts:
        if art.name == name:
            return art
    return None


# ---------------- DEMO (FIXED FOR TEST) ----------------

def demo_museum_night():
    print("Moonlight Museum After Dark")

    artifacts = [
        Artifact(40, "Cursed Mirror", "mirror", 220, "North Hall"),
        Artifact(20, "Clockwork Bird", "machine", 80, "Workshop"),
        Artifact(60, "Whispering Map", "paper", 140, "Archive"),
        Artifact(10, "Glowing Key", "metal", 35, "Vault"),
        Artifact(30, "Moon Dial", "device", 120, "North Hall"),
        Artifact(50, "Silver Mask", "costume", 160, "Gallery"),
        Artifact(70, "Lantern Jar", "glass", 60, "Gallery"),
        Artifact(25, "Ink Compass", "device", 120, "Archive"),
    ]

    bst = ArtifactBST()
    for art in artifacts:
        bst.insert(art)

    print("Inorder IDs:", bst.inorder_ids())

    queue = RestorationQueue()
    queue.add_request(RestorationRequest(40, "Polish mirror"))
    print("Next restoration request:", queue.peek_next_request())

    stack = ArchiveUndoStack()
    stack.push_action("Added artifact")
    print("Undo action:", stack.undo_last_action())

    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("Gallery")
    print("Exhibit route:", route.list_stops())

    print("Category counts:", count_artifacts_by_category(artifacts))