# simple converter to make a text compatible with the
# lego star wars: the skywalker sage credits format
# made by: ntekshadow

import sys

def reformat_file(droppedFile):
    with open(fr'{droppedFile}', 'r')as file:
        data = file.readlines()

    print("line count is: ", len(data))

    for x in range(len(data)):
        text = data[x].rstrip("\n")
        data[x] = ("Line" + "            " + '"' + text + '"\n')

    with open('CREDITS_PC.txt', 'w') as file:
        file.writelines(data)


if __name__ == '__main__':
    try:
        droppedFile = sys.argv[1]
        reformat_file(droppedFile)
    except IndexError:
        print("Plead drag a txt file on the executable")
        input("press enter to exit")

