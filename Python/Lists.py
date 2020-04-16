#Lists
#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(raw_input())

    inputs = []
    for i in range(N):
        inputs.append(raw_input())

    output = []
    for i in inputs:
        command_list = i.split()
        command = command_list[0]

        if command == 'insert':
            output.insert(int(command_list[1]), int(command_list[2]))

        elif command == 'print':
            print(output)

        elif command == 'remove':
            output.remove(int(command_list[1]))

        elif command == 'append':
            output.append(int(command_list[1]))

        elif command == 'sort':
            output.sort()

        elif command ==  'pop':
            output.pop()

        elif command == 'reverse':
            output.reverse()
