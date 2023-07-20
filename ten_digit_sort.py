def get_tens_place(num):
    return (num // 10) % 10


def comparator(x, y):
    tens_x = get_tens_place(x)
    tens_y = get_tens_place(y)
    if tens_x == tens_y:
        return y - x
    return tens_x - tens_y


def get_sorted_array(num_array: list):
    num_array.sort(key=lambda x: (get_tens_place(x), -x))
    return num_array


try:
    nums_array = list(map(int, input("Please enter the integers separated by space : ").split()))
    print("The sorted array is : ", get_sorted_array(nums_array))
except ValueError:
    print("Invalid Input. Enter only integers")


