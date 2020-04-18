from time import time
from data.values import make_random_values

def dt(f):
    def inner(array):
        tc = time()
        print(f'<- START ->\ncomputing...')
        array = f(array)
        print(f'<- STOP ->\ncomputation time:{time() - tc}s')
        return array
    return inner

@dt
def bubble_sort(array):
    steps = 0
    while True:
        swapped = False
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
            steps += 1
        if not swapped:
            print(f'bubble sorted {len(array)} values in {steps} steps.')
            break
    return array

if __name__ == '__main__':
    array = make_random_values(5000)
    array = bubble_sort(array)
