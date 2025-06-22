from dataclasses import dataclass


@dataclass

class Method:
    code: int
    name: str


    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return self.code