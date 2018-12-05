def first():
    with open('input.txt') as fil:
        data = fil.readlines()

    twos = 0
    threes = 0

    for text in data:
        unique = {}
        for char in text:
            if char not in unique:
                unique[char] = 1
            else:
                unique[char] +=1

        has_two = False 
        has_three = False

        for key, value in unique.items():
            if value == 2:
                has_two = True 
            if value == 3:
                has_three = True 

        if has_three:
            threes +=1
        if has_two:
            twos += 1

    print(threes * twos)

def second():
    with open('input.txt') as fil:
        data = fil.readlines()


    l = 0

    for n in range(len(data)):
        string1 = data[n]
        for m in range(n + 1, len(data)):
            string2 = data[m]
            same = ''.join([char for index, char in enumerate(string1) if string2[index] == char])
            if len(same) +1 ==  len(string2):
                print(same)

if __name__ == '__main__':
    first()
    second()