from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque


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


class TreeNode:
    def __init__(self, artifact, left=None, right=None):
        self.artifact = artifact
        self.left = left
        self.right = right


class ArtifactBST:
    def __init__(self):
        self.root = None

    def insert(self, artifact):
        if self.root is None:
            self.root = TreeNode(artifact)
            return True

        current = self.root
        while True:
            if artifact.artifact_id == current.artifact.artifact_id:
                return False

            elif artifact.artifact_id < current.artifact.artifact_id:
                if current.left is None:
                    current.left = TreeNode(artifact)
                    return True
                current = current.left

            else:
                if current.right is None:
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


class ExhibitNode:
    def __init__(self, stop_name, next_node=None):
        self.stop_name = stop_name
        self.next = next_node


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
        stops = []
        current = self.head

        while current:
            stops.append(current.stop_name)
            current = current.next

        return stops

    def count_stops(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


def count_artifacts_by_category(artifacts):
    result = {}

    for art in artifacts:
        result[art.category] = result.get(art.category, 0) + 1

    return result


def unique_rooms(artifacts):
    return {art.room for art in artifacts}


def sort_artifacts_by_age(artifacts, descending=False):
    return sorted(artifacts, key=lambda x: x.age, reverse=descending)


def linear_search_by_name(artifacts, name):
    for art in artifacts:
        if art.name == name:
            return art
    return None


def demo_museum_night():
    print("Demo running...")

    a1 = Artifact(1, "Vase", "Ancient", 200, "Room A")
    a2 = Artifact(2, "Statue", "Medieval", 500, "Room B")

    bst = ArtifactBST()
    bst.insert(a1)
    bst.insert(a2)

    print("Inorder:", bst.inorder_ids())

    queue = RestorationQueue()
    queue.add_request(RestorationRequest(1, "Clean"))

    print("Next request:", queue.peek_next_request())

    stack = ArchiveUndoStack()
    stack.push_action("Added artifact")

    print("Undo:", stack.undo_last_action())

    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("Gallery")

    print("Route:", route.list_stops())