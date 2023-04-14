# get two integer parameters
# return sum
def ca1(x, y):
    return x+y

def ca2(x, y):
    return x-y

def ca3(x,y):
    return x*y

def ca4(x,y):
    try:
        result = x/y
        return result
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus 2: minus 3: multiplication 4: division")
        check = int(input("입력:"))
        if check == 1:
            print("First Number")
            x = int(input("입력:"))
            print("Second Number")
            y = int(input("입력:"))
            print("answer : ", ca1(x,y))
        elif check == 2:
            print("First Number")
            x = int(input("입력:"))
            print("Second Number")
            y = int(input("입력:"))
            print("answer : ", ca2(x,y))
        elif check == 3:
            print("First Number")
            x = int(input("입력:"))
            print("Second Number")
            y = int(input("입력:"))
            print("answer : ", ca3(x,y))
        elif check == 4:
            print("First Number")
            x = int(input("입력:"))
            print("Second Number")
            y = int(input("입력:"))
            print("answer : ", ca4(x,y))
        elif check > 4 or check < 0:
            print("Unsupported")
        else:
            print("Thank you")
            
                

if __name__ == "__main__":
    main()
