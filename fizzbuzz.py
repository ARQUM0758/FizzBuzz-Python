for result in range(1, 101):
    if result % 3 == 0 and result % 5 == 0:
        print("FizzBuzz")
    elif result % 3 == 0:
        print("Fizz")
    elif result % 5 == 0:
        print("Buzz")
    else:
        print(result)
