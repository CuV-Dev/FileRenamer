import os
import glob


def main():
    """
    The Main function of this program.

    :return: void
    """
    renameFiles()
#    createSandbox()


def renameFiles():
    """
    The Core functionality of this program

    :return: void
    """
    pass


def createSandbox():
    """
    Creates a Sandbox with 1000 txt files.

    :return: void
    """
    print('Started setting up Sandbox...')
    print('Started clearing the Sandbox directory...')
    files = glob.glob('/Sandbox/*')
    for file in files:
        os.remove(file)
    print('Successfully cleared Sandbox directory!')
    for x in range(0, 1000):
        open('./Sandbox/myData' + str(x) + '.txt', 'w')
    print('Sandbox successfully set up!')


if __name__ == "__main__":
    main()
