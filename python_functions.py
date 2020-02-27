def double(x):
    """
    This function multiplies its input by 2.
    """
    return x * 2


class CountingClicker:
    """This is a docstring. This is CountingClicker."""
    def __init__(self, count = 0):
        self.count = count
    
    def __repr__(self):
        return f"CountingClicker(count = {self.count})"
    
    def click(self, num_times =1):
        """Click the clicker some number of times"""""
        self.count += num_times
    
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0

clicker = CountingClicker()
print(clicker.read())