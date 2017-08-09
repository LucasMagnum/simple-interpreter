import operator

from .tokens import PLUS, MINUS, MUL, DIV


class NodeVisitor(object):
    """Node visitor pattern implementation."""

    def visit(self, node):
        """Visit each node based on node type."""
        method_name = 'visit_' + type(node).__name__.lower()
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Generic visit method."""
        raise Exception(
            'No visit_{} method'.format(type(node).__name__.lower())
        )


class Interpreter(NodeVisitor):
    """Interpreter using node visitor pattern."""

    def __init__(self, parser):
        self.parser = parser

    def interpret(self):
        """Interpret parser tree and visit all nodes."""
        tree = self.parser.parse()
        return self.visit(tree)

    def visit_binop(self, node):
        """Visit BinOp nodes."""
        operations = {
            PLUS: operator.add,
            MINUS: operator.sub,
            MUL: operator.mul,
            DIV: operator.truediv
        }

        operation = operations[node.op.type]
        return operation(self.visit(node.left), self.visit(node.right))

    def visit_unaryop(self, node):
        op = node.op.type
        if op == PLUS:
            return + self.visit(node.expr)
        elif op == MINUS:
            return - self.visit(node.expr)

    def visit_num(self, node):
        """Visitor num just return the value."""
        return node.value
