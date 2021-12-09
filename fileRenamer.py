import os
import glob


def main():
    """
    The Main function of this program.

    :return: void
    """
    renameFiles()
    createSandbox()


def renameFiles():
    """
    The Core functionality of this program

    :return: void
    """
    print('Started renaming files...')
    path = './Sandbox/'
    files = os.listdir(path)
    i = 0
    for file in files:
        os.rename(path + file, path + 'renamedFile' + str(i) + '.txt')
        print('Renamed File: ' + os.path.basename(file) + ' to renamedFile' + str(i) + '.txt')
        i += 1
    print('Finished renaming files!')
    print('Total renamed files: ' + str(i))


def createSandbox():
    """
    Creates a Sandbox with 1000 txt files.

    :return: void
    """
    print('Started setting up Sandbox...')
    path = './Sandbox/'
    print('Started clearing the Sandbox directory...')
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))
    print('Successfully cleared Sandbox directory!')
    print('Started creating dummy files...')
    for x in range(0, 1000):
        open('./Sandbox/myData' + str(x) + '.txt', 'w')
    print('Sandbox successfully set up!')


if __name__ == "__main__":
    main()
