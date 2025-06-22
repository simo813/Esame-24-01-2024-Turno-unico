from dataclasses import dataclass


@dataclass

class Product:
    code: int
    annualRevenue: float

    def __eq__(self, other):
        return self.code == other.code
    def __hash__(self):
        return hash(self.code)

    def __str__(self):
        return f'{self.code} ({self.annualRevenue})'