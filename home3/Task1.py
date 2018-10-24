def inverse(filename):
    with open(filename, 'r+') as file:
        buf = list(file.read(2))
        print(buf)
        temp = buf[0]
        print(temp)
        buf[0]=buf[1]
        buf[1]=temp
        # file.write()
    # for j in range(len(filename) - 1):
    #     for i in range(len(filename)-1-j):
    #         temp = filename[i]
    #         filename[i] = filename[i+1]
    #         filename[i+1] = temp
    #         print(filename)
    #     print('run {} finished'.format(j))
    # return filename

print(inverse('input.txt'))