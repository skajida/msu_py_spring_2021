# 9 test RTE
# cause of RecursionError -> заменить на цикл

# чтобы не иметь дело с уродством ниже можно хранить отсортированные символы
# в листе, затем проходить по ним и проверять, есть ли они dict-е ноды

from collections import deque
from bisect import insort


class Node:

    def __init__(self, key=None):
        if key is not None and (not str.isprintable(key) or len(key) > 1):
            raise TypeError
        self.key = key
        self.is_leaf = False
        self.offspring = list()

    def append(self, key):
        if not self.offspring or key not in tuple(zip(*self.offspring))[0]:
            insort(self.offspring, (key, Node(key)))
        idx = tuple(zip(*self.offspring))[0].index(key)
        return self.offspring[idx][1]

    def pop(self, key):
        if self.offspring and key in tuple(zip(*self.offspring))[0]:
            idx = tuple(zip(*self.offspring))[0].index(key)
            self.offspring.pop(idx)

    def get(self, key):
        idx = tuple(zip(*self.offspring))[0].index(key)
        return self.offspring[idx][1]

    def __contains__(self, key):
        if self.offspring and key in tuple(zip(*self.offspring))[0]:
            return True
        return False


class Trie:

    def __init__(self):
        self.root = Node()
        self.size = 0

    def add(self, word):
        if not isinstance(word, str):
            raise TypeError
        cur_node = self.root
        for char in word:
            cur_node = cur_node.append(char)
        self.size += not cur_node.is_leaf
        cur_node.is_leaf = True

    def pop(self, word):
        if not isinstance(word, str):
            raise TypeError
        path = [self.root]
        for char in word:
            if char not in path[-1]:
                raise KeyError(word)
            path.append(path[-1].get(char))
        if not path[-1].is_leaf:
            raise KeyError(word)
        self.size -= 1
        path[-1].is_leaf = False
        if path[-1].offspring:
            return
        i = len(word)
        while i and len(path[-1].offspring) < 1 and not path[-2].is_leaf:
            i -= 1
            path[-2].pop(word[i])
            path.pop()

    def __len__(self):
        return self.size

    def __dfs(self, node, word):
        if not word:
            return node.is_leaf
        if word[:1] not in node:
            return False
        return self.__dfs(node.get(word[:1]), word[1:])

    def __contains__(self, word):
        if not isinstance(word, str):
            raise TypeError
        return self.__dfs(self.root, word)

    def __iter__(self):
        return TrieIterator(self.root)

    def starts_with(self, prefix):
        cur_node = self.root
        for char in prefix:
            if char not in cur_node:
                return TrieIterator()
            cur_node = cur_node.get(char)
        return TrieIterator(cur_node, prefix)


class TrieIterator:

    def __init__(self, root=None, prefix=''):
        if root is not None:
            self.queue = deque()
            self.queue.append((root, prefix))

    def __iter__(self):
        return self

    def __next__(self):
        if not hasattr(self, 'queue'):
            raise StopIteration
        while self.queue:
            item, string = self.queue.popleft()
            for key, node in item.offspring:
                self.queue.append((node, string + key))
            if item.is_leaf:
                return string
        raise StopIteration
