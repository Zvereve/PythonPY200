from typing import Any, Iterable, Optional

from node import Node, DoubleLinkedNode


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def count(self, value: Any) -> int:
        y = 0
        for x in range(self.len):
            if str(value) == str(self.step_by_step_on_nodes(x)):
                y += 1
        return y

    def extend(self, value: list) -> None:
        if not isinstance(value, list):
            raise TypeError
        for x in value:
            self.insert(self.len + 1, x)

    def pop(self, index=None) -> Any:
        if index == None:
            index = self.len - 1
        x = self.step_by_step_on_nodes(index)
        self.__delitem__(index)
        return x

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __add__(self, other: "LinkedList") -> "LinkedList":
        if not isinstance(other, LinkedList):
            raise TypeError

        for item in other:
            self.append(item)

        return self

    def __radd__(self, other: list) -> "LinkedList":
        if not isinstance(other, list):
            raise TypeError

        return LinkedList(other + self.to_list())

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index < self.len:
            raise IndexError

    def __len__(self):
        return self.len

    def insert(self, index: int, value: Any) -> None:
        """ Метод вставки в связаный узел по индексу """

        if not isinstance(index, int):
            raise TypeError

        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.len += 1
        elif index >= self.len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self.linked_nodes(prev_node, new_node)
            self.linked_nodes(new_node, next_node)
            self.len += 1

    def clear(self):
        self.len = 0
        self.head = None
        self.tail = None


class DoubleLinkedList(LinkedList):
    node_class = DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1



if __name__ == "__main__":
    ll = LinkedList([1, 2, 3])
    l2 = LinkedList([1, 2, 3])
    print(ll + l2)
    print(ll.__len__())

    lll = DoubleLinkedList([1, 2, 3])
    ll3 = DoubleLinkedList([4, 5, 6])
    print(lll + ll3)
    print(ll3)
    ll3 .clear()
    print(ll3)

