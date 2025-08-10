class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: performs addition without needing class/instance context."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: can access class attributes and methods via 'cls'."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
