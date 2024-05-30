"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
class SerialGenerator:
    """Class to generate a series of sequential numbers starting from a given number."""
    
    def __init__(self, start=0):
        """
        Initialize the serial number generator with a start number.
        
        :param start: The starting number for the serial number generator.
        """
        self.start = start
        self.current = start
    
    def generate(self):
        """
        Generate the next number in the sequence.
        
        return: The next sequential number.
        """
        current_number = self.current
        self.current += 1
        return current_number
    
    def reset(self):
        """
        Reset the serial number generator back to the original start number.
        """
        self.current = self.start
