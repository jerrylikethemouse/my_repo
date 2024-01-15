class Calculator:

    def validate_inputs(self,x,y):
        def is_numeric(value):
            return isinstance(value, (int, float)) or str(value).replace('.', '', 1).replace('-', '', 1).isnumeric()
        
        if not is_numeric(x):
            raise TypeError("Invalid type for x. Must be int or float.")
        
        if not is_numeric(y):
            raise TypeError("Invalid type for y. Must be int or float.")
    
    def add(self, x, y):
        self.validate_inputs(x,y)
        return float(x) + float(y)
    
    def subtract(self, x, y):
        self.validate_inputs(x,y)
        return float(x) - float(y)

    def multiply(self, x, y):
        self.validate_inputs(x,y)
        return float(x) * float(y)

    def divide(self, x, y):
        self.validate_inputs(x,y)

        if float(y) == 0:
            raise ZeroDivisionError("y cannot be zero")

        return float(x) / float(y)