class Stack:

    def __init__(self, base_stack=[]):
        self.__items = base_stack

    def isEmpty(self):
        return self.__items == []

    def push(self, item):
        self.__items.insert(0, item)

    def stack_pop(self):
        return self.__items.pop(0)

    def peek(self):
        return self.__items[0]

    def size(self):
        return len(self.__items)

    def remove(self):
        return self.__items.remove(0)

    def stack_shuffle(self):
        from random import shuffle as rand_shuffle
        rand_shuffle(self.__items)
        return self

    def reveal(self):
        return self.__items


class Queue:

    def __init__(self, start=[]):
        self.__items = start

    def isEmpty(self):
        return len(self.__items) == 0

    def pop_item(self):
        return self.__items.pop(-1)

    def push(self, item):
        self.__items.insert(0, item)

    def remove_item(self):
        self.__items.remove(self.__items[-1])

    def get_length(self):
        return len(self.__items)

    def reveal(self):
        return self.__items
