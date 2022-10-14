from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Enum.typeExpression import typeExpression

class Main(Instruction):
    def __init__(self, ins) -> None:
        self.ins = ins
    def execute(self, environment: Environment):
        newEnv = Environment(environment)
        Environment.saveExpression("\n")
        Environment.saveExpression("int main(){")
        Environment.saveExpression("H = 0;\n")
        Environment.restartPointer()
        for ins in self.ins:
            ins.execute(newEnv)
        Environment.saveExpression("\n")
        Environment.saveExpression("return 0;")
        Environment.saveExpression("}")