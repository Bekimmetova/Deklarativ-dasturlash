class LogicalOperations:
    @staticmethod
    def and_operation(a, b):
        return a and b

    @staticmethod
    def or_operation(a, b):
        return a or b

    @staticmethod
    def not_operation(a):
        return not a

# Misol
a = True
b = False

print("A va B ning AND amali:", LogicalOperations.and_operation(a, b))
print("A yoki B ning OR amali:", LogicalOperations.or_operation(a, b))
print("A ning NOT amali:", LogicalOperations.not_operation(a))
