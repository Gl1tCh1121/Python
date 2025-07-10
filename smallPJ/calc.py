print("""
_____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")


start_num = float(input("What's the first number?:  "))

def starter(num):
    print("+\n-\n*\n/\n")
    op = input("Pick an operation: ")
    next_num = float(input("What's the next number?: "))
    if op == "+":
        def plus(num, next_num):
            final_num = num + next_num
            return final_num
        print(f"{num} + {next_num} = {plus(num, next_num)}")

        if input(f"Type 'y' to continue calculating with {plus(num, next_num)}, or type 'n' to start a new calculation:").lower() == "y":
            starter(plus(num, next_num))
        else:
            start_num = float(input("What's the first number?:  "))
            starter(start_num)
    elif op == "-":
        def minus(num, next_num):
            final_num = num - next_num
            return final_num
        print(f"{num} - {next_num} = {minus(num, next_num)}")

        if input(f"Type 'y' to continue calculating with {minus(num, next_num)}, or type 'n' to start a new calculation:").lower() == "y":
            starter(minus(num, next_num))
        else:
            start_num = float(input("What's the first number?:  "))
            starter(start_num)
    elif op == "*":
        def mult(num, next_num):
            final_num = num * next_num
            return final_num
        print(f"{num} * {next_num} = {mult(num, next_num)}")

        if input(f"Type 'y' to continue calculating with {mult(num, next_num)}, or type 'n' to start a new calculation:").lower() == "y":
            starter(mult(num, next_num))
        else:
            start_num = float(input("What's the first number?:  "))
            starter(start_num)
    elif op == "/":
        def divide(num, next_num):
            final_num = num / next_num
            return final_num
        print(f"{num} / {next_num} = {divide(num, next_num)}")

        if input(f"Type 'y' to continue calculating with {divide(num, next_num)}, or type 'n' to start a new calculation:").lower() == "y":
            starter(divide(num, next_num))
        else:
            start_num = float(input("What's the first number?:  "))
            starter(start_num)
    
    
starter(start_num)





