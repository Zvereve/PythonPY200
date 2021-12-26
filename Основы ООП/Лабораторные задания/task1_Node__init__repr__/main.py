from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next_ = next_


    def __repr__(self)->str:
        return f"Node({self.value}, {self.next_})"

    # TODO реализовать метод __repr__ для отображения экземпляра


if __name__ == '__main__':
    first_node = Node(1)

    second_node = Node(2)  # TODO инициализировать второй узел
    first_node.next_ = second_node  # TODO через атрибут экземпляра устанавливаем первому узлу следующий узел

    print(first_node)
    print(second_node)
