from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Enum.typeExpression import typeExpression

class Main(Instruction):
    def __init__(self, ins) -> None:
        self.ins = ins
    def execute(self, environment: Environment):
       newEnv = Environment(environment)
       for ins in self.ins:
            ins.execute(newEnv)