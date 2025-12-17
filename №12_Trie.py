class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_count = 0
        self.prefix_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1
        node.is_word = True
        node.word_count += 1

    def _find_node(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def count_words_equal_to(self, word: str) -> int:
        node = self._find_node(word)
        return node.word_count if node else 0

    def count_words_starting_with(self, prefix: str) -> int:
        node = self._find_node(prefix)
        return node.prefix_count if node else 0

    def erase(self, word: str) -> None:
        if self.count_words_equal_to(word) == 0:
            return

        node = self.root
        stack = []

        for ch in word:
            stack.append((node, ch))
            node = node.children[ch]
            node.prefix_count -= 1

        node.word_count -= 1
        if node.word_count == 0:
            node.is_word = False

        for parent, ch in reversed(stack):
            child = parent.children[ch]
            if child.prefix_count == 0 and not child.is_word and not child.children:
                del parent.children[ch]
            else:
                break


def test_trie():
    trie = Trie()
    words = ["apple", "app", "apply", "app", "bat", "batch"]
    for w in words:
        trie.insert(w)

    assert trie.count_words_equal_to("app") == 2
    assert trie.count_words_equal_to("apple") == 1
    assert trie.count_words_equal_to("apply") == 1
    assert trie.count_words_equal_to("bat") == 1
    assert trie.count_words_equal_to("batch") == 1
    assert trie.count_words_equal_to("bad") == 0

    assert trie.count_words_starting_with("app") == 4
    assert trie.count_words_starting_with("ap") == 4
    assert trie.count_words_starting_with("b") == 2
    assert trie.count_words_starting_with("ba") == 2
    assert trie.count_words_starting_with("bat") == 2
    assert trie.count_words_starting_with("c") == 0

    trie.erase("app")
    assert trie.count_words_equal_to("app") == 1
    assert trie.count_words_starting_with("app") == 3

    trie.erase("apple")
    assert trie.count_words_equal_to("apple") == 0
    assert trie.count_words_starting_with("app") == 2

    trie.erase("app")
    assert trie.count_words_equal_to("app") == 0
    assert trie.count_words_starting_with("app") == 1

    trie.erase("apply")
    assert trie.count_words_equal_to("apply") == 0
    assert trie.count_words_starting_with("app") == 0

    trie.erase("bat")
    assert trie.count_words_equal_to("bat") == 0
    assert trie.count_words_starting_with("bat") == 1

    trie.erase("batch")
    assert trie.count_words_equal_to("batch") == 0
    assert trie.count_words_starting_with("bat") == 0

    trie.erase("not_in_trie")
    assert trie.count_words_equal_to("not_in_trie") == 0

    print("Все тесты Trie пройдены успешно!")


if __name__ == "__main__":
    test_trie()
