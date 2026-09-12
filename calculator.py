calc1 = int(input("please select first number"))
calc2 = int(input("please select next number")) 
choice = input("select + - x / ** for it to work")
if choice == "x":
    answer = calc1 * calc2
    print(answer)
elif choice == "+":
    answer = calc1 + calc2
    print(answer)
elif choice == "-":
    answer = calc1 - calc2
    print(answer)
elif choice == "/":
        answer = calc1 / calc2
        print(answer)
elif choice == "**":
    answer = calc1 ** calc2 
    print(answer)
