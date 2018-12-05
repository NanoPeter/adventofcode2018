def solution1():
    operations = []
    with open('input', 'r') as fil:
        operations = [int(x) for x in fil.readlines()]

    cummulative_sum = [0]
    for operation in operations:
        next_element = operation + cummulative_sum[-1]
        cummulative_sum.append(next_element)    
    print(cummulative_sum[-1])

def solution2():
    def wrap_around(some_list):
        while True:
            for elem in some_list:
                yield elem 
    
    operations = []
    with open('input', 'r') as fil:
        operations = [int(x) for x in fil.readlines()]

    cummulative_sum = [0]
    for operation in wrap_around(operations):
        next_element = operation + cummulative_sum[-1]
        if next_element in cummulative_sum:
            print(next_element)
            break

        cummulative_sum.append(next_element)


if __name__ == '__main__':
    solution1()
    solution2()

