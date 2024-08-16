import trees.Node as Node


class BinaryTree:
    def __init__(self, root: int) -> None:
        self.root = Node.Node(root)

    def pre_order_traversal(self, root: Node, response: list[int]) -> list[int]:
        if root:
            response.append(root.item)
            self.pre_order_traversal(root.left, response)
            self.pre_order_traversal(root.right, response)
        return response

    def in_order_traversal(self, root: Node, response: list[int]) -> list[int]:
        if root:
            self.in_order_traversal(root.left, response)
            response.append(root.item)
            self.in_order_traversal(root.right, response)
        return response

    def post_order_traversal(self, root: Node, response: list[int]) -> list[int]:
        if root:
            self.post_order_traversal(root.left, response)
            self.post_order_traversal(root.right, response)
            response.append(root.item)
        return response

