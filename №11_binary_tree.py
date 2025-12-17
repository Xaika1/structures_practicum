class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node



    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)


    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            succ = self._min_value_node(node.right)
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)

        return node


    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, node, res):
        if node is None:
            return
        self._inorder(node.left, res)
        res.append(node.key)
        self._inorder(node.right, res)

    def preorder(self):
        res = []
        self._preorder(self.root, res)
        return res

    def _preorder(self, node, res):
        if node is None:
            return
        res.append(node.key)
        self._preorder(node.left, res)
        self._preorder(node.right, res)

    def postorder(self):
        res = []
        self._postorder(self.root, res)
        return res

    def _postorder(self, node, res):
        if node is None:
            return
        self._postorder(node.left, res)
        self._postorder(node.right, res)
        res.append(node.key)


    def is_balanced(self):
        balanced, _ = self._check_balanced(self.root)
        return balanced

    def _check_balanced(self, node):
        if node is None:
            return True, 0  

        left_bal, left_h = self._check_balanced(node.left)
        right_bal, right_h = self._check_balanced(node.right)

        current_bal = left_bal and right_bal and abs(left_h - right_h) <= 1
        current_h = 1 + max(left_h, right_h)

        return current_bal, current_h




def test_bst():
    bst = BST()


    values = [10, 5, 15, 3, 7, 12, 18]
    for v in values:
        bst.insert(v)

    inorder_res = bst.inorder()
    assert inorder_res == sorted(values), f"In-order неверен: {inorder_res}"


    for v in values:
        assert bst.search(v) is not None, f"Поиск не нашёл {v}"
    assert bst.search(100) is None, "Поиск нашёл несуществующий элемент"

    balanced1 = bst.is_balanced()
    print("Сбалансировано после первой вставки:", balanced1)

    bst.delete(3)
    assert bst.search(3) is None, "3 не удалён"
    inorder_res = bst.inorder()
    assert inorder_res == sorted([v for v in values if v != 3]), \
        f"In-order после удаления 3 неверен: {inorder_res}"
    bst.delete(5)
    assert bst.search(5) is None, "5 не удалён"
    inorder_res = bst.inorder()
    expected = sorted([v for v in values if v not in (3, 5)])
    assert inorder_res == expected, f"In-order после удаления 5 неверен: {inorder_res}"

    bst.delete(10)
    assert bst.search(10) is None, "10 не удалён"
    inorder_res = bst.inorder()
    expected = sorted([v for v in values if v not in (3, 5, 10)])
    assert inorder_res == expected, f"In-order после удаления 10 неверен: {inorder_res}"

    bst2 = BST()
    for v in [1, 2, 3, 4, 5]:
        bst2.insert(v)
    assert not bst2.is_balanced(), "Дерево из отсортированной последовательности не должно быть сбалансированным"

    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    test_bst()
    bst = BST()
    for x in [10, 5, 15, 3, 7, 12, 18]:
        bst.insert(x)
    print("In-order:", bst.inorder())
    print("Pre-order:", bst.preorder())
    print("Post-order:", bst.postorder())
    print("Сбалансировано:", bst.is_balanced())
