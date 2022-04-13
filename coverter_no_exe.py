# simple converter to make a text compatible with the
# Lego Starwars: the skywalker sage credits format
# made by: ntekshadow

def reformat_file():
    with open('input.txt', 'r') as file:
        data = file.readlines()

    print("line count is: ", len(data))

    for x in range(len(data)):
        text = data[x].rstrip("\n")
        data[x] = ("Line" + "            " + '"' + text + '"\n')

    with open('CREDITS_PC.txt', 'w') as file:
        file.writelines(data)


if __name__ == '__main__':
    reformat_file()
