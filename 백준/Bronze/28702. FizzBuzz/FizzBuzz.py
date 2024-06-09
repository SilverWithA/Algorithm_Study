next = 0
for i in range(1,4):
    a = input()
    if a == "Fizz" or a == "Buzz" or a == "FizzBuzz":
        pass
    else:
        a= int(a)
        next = a + (3 - i + 1)

if next % 3 == 0:
    if next % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if next % 5 == 0:
        print("Buzz")
    else:
        print(next)