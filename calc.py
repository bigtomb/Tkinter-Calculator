class Calc:
    def __init__(self, entry):
        print("Calculating...")
        self.entry = entry
        self.expression = ""

    def click(self, num):
        self.expression += num
        self.entry.insert("end", num)

    def add(self):
        self.expression += "+"
        self.entry.delete(0, "end")

    def subtract(self):
        self.expression += "-"
        self.entry.delete(0, "end")

    def multiply(self):
        self.expression += "*"
        self.entry.delete(0, "end")

    def divide(self):
        self.expression += "/"
        self.entry.delete(0, "end")

    def clear(self):
        self.expression = ""
        self.entry.delete(0, "end")

    def equals(self):
        self.entry.delete(0, "end")
        result = str(eval(self.expression))
        self.entry.insert(0, result)
        self.expression = ""
