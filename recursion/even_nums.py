
def even_nums(num):
    print(num)
    if num % 2 != 0:
        print( "Enter even number")
    elif num == 2:
        return num
    elif num <= 1:
        return num
    return even_nums(num-2)

num =int(input("Enter even number: "))
even_nums(num)