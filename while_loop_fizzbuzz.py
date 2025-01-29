counter = 1

while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print(f"{counter}Fizzbuzz")
    elif counter % 3 == 0:
        print(f"{counter}Fizz")
    elif counter % 5 == 0:
        print(f"{counter}Buzz")
    else:
        print(counter)
    counter += 1 
   