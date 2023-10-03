def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    n = int(input("кол-во чисел: "))
    arr = []
    for i in range(n):
        num = int(input("элемент {}: ".format(i + 1)))
        arr.append(num)

    direction = input("как сортировать (восх/низх) ")

    if direction.lower() == "восх":
        bubble_sort(arr)
    elif direction.lower() == "низх":
        bubble_sort(arr)
        arr.reverse()
    else:
        print("что-то не так  !")

    print("Sorted list:", arr)

if __name__ == "__main__":
    main()