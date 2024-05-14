class RecursiveDescentParser:
    def __init__(self, expression):
        self.expression = expression
        self.index = 0

    def parse(self):
        return self.expr()

    def expr(self):
        result = self.term()
        while self.index < len(self.expression) and self.expression[self.index] in ('+', '-'):
            op = self.expression[self.index]
            self.index += 1
            if op == '+':
                result += self.term()
            else:
                result -= self.term()
        return result

    def term(self):
        result = self.factor()
        while self.index < len(self.expression) and self.expression[self.index] in ('*', '/'):
            op = self.expression[self.index]
            self.index += 1
            if op == '*':
                result *= self.factor()
            else:
                result /= self.factor()
        return result

    def factor(self):
        if self.expression[self.index] == '(':
            self.index += 1
            result = self.expr()
            if self.expression[self.index] != ')':
                raise SyntaxError("Expected ')' at index {}".format(self.index))
            self.index += 1
            return result
        elif self.expression[self.index].isdigit():
            start = self.index
            while self.index < len(self.expression) and self.expression[self.index].isdigit():
                self.index += 1
            return int(self.expression[start:self.index])
        else:
            raise SyntaxError("Invalid character '{}' at index {}".format(self.expression[self.index], self.index))


# Example usage:
expression = "3 + (4 * 5) - 6 / 2"
parser = RecursiveDescentParser(expression)
result = parser.parse()
print("Result:", result)
