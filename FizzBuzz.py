amount = 1#sets a variable too 1
maxium = int(input("max number:"))
while amount <= maxium:# checks that the amount is equal too or less than 100
    if amount % 3 == 0 and amount %  5 == 0:# checks if the reminder from the amount divided by three is 0 and then five
        print("FizzBuzz")#if both conditions true they will print fizz buzz
        amount = amount + 1#adds 1 to amount
    elif amount % 5 == 0:#divides the amount by 5 and if 0 continues
        print("Buzz")#prints buzz
        amount = amount + 1#adds 1 to amount
    elif amount % 3 == 0:#divides the amount by 3 and if 0 continues
        print("Fizz")#prints fizz
        amount = amount + 1#adds 1 to amount
    else:#anythin else then specified above
        print(amount)#prints the amount
        amount = amount + 1#adds 1 to amount
              
