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
    def __init__(self, start=0):
        """Make a new generator, starting at start."""

        self.start = start
        self.next = start
        
    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """This will generate numbers beginning at the start and incrementing by 1 each time generate is called"""

        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Resets the number to the start number"""

        self.next = self.start
        