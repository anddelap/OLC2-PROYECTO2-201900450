from Environment.Symbol import Symbol
from abc import ABC, abstractmethod
from Environment.Environment import Environment

class Expression(ABC):
    @abstractmethod
    def execute(self, environment: Environment) -> Symbol:
        pass