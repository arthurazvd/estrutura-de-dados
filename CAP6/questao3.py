from abc import ABC, abstractmethod


class AbstractCollection(ABC):
    def __init__(self, source=None):
        self.size = 0
        if source is not None:
            for item in source:
                self.add(item)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def __contains__(self, target):
        return any(item == target for item in self)

    def __str__(self):
        return "{" + ", ".join(repr(item) for item in self) + "}"

    @abstractmethod
    def add(self, item):
        """Adiciona um item à coleção."""


class AbstractBag(AbstractCollection):
    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, AbstractBag) or len(self) != len(other):
            return False
        unmatched = list(other)
        for item in self:
            try:
                unmatched.remove(item)
            except ValueError:
                return False
        return not unmatched


class ArrayBag(AbstractBag):
    def __init__(self, source=None):
        self.items = []
        super().__init__(source)

    def add(self, item):
        self.items.append(item)
        self.size += 1

    def __iter__(self):
        return iter(self.items)


if __name__ == "__main__":
    bag = ArrayBag([1, 2, 2])
    assert len(bag) == 3 and 2 in bag and 9 not in bag
    assert str(bag) == "{1, 2, 2}"
    assert bag == ArrayBag([2, 1, 2])
    print("Questão 3: testes OK")
