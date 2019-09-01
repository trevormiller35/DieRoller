from random import randint

def running(n):
    value = randint(1,n)
    print("The value of your roll is ", value)

def main():
    case = 1
    while case:
        print("What size dice do you want?")
        m = int(input())
        #m = int(input(print("What size dice do you want?")))
        if m > 1:
            running(m)
            print("Do you wish to continue? (1 = Yes, 0 = No)")
            check = int(input())
            if check != 1:
                case = 0
        else:
            case = 1
main()
