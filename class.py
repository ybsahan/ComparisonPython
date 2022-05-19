class Number:
    def __init__(self,value):
        self.value = value

    def __eq__(self, other):
        print("__eq__ called")
        if isinstance(other,Number):
            return self.value == other.value
        return self.value == other

    def __str__(self):
        return str(self.value)

numbers = [Number(i*10) for i in range(1,11)]
print("[", end=" ")
for number in numbers:
    print(f"{number}", end=" ")
print("]")



num1 = Number(20) #True
num2 = 30  # True
num3 = "30" # False

if num3 in numbers:
    print("True")
else:
    print("False")