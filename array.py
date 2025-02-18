N_MAX = 15

def read_array():
    arr = []
    n = int(input("Введите количество элементов (макс. 15): "))
    if n > N_MAX:
        print("Максимальное количество элементов равно 15")
        return arr
    print("Введите элементы:")
    for i in range(n):
        arr.append(int(input()))
    return arr

def print_array(arr):
    print("Массив:")
    for elem in arr:
        print(elem, end=" ")
    print()

def main():
    arr = read_array()
    print_array(arr)

if __name__ == "__main__":
    main()
