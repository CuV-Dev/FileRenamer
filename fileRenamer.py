import os
import sys


def main():
    """
    The Main function of this program.

    :return: void
    """
    if sys.argv[1] == '-r':
        if len(sys.argv) == 2:
            renameFiles()
        elif len(sys.argv) == 4:
            renameFiles(sys.argv[3], sys.argv[2])
        else:
            print('This Command doesn\'t exist! Try -h for help.')
    elif sys.argv[1] == '-s':
        if len(sys.argv) == 2:
            createSandbox()
        elif len(sys.argv) == 3:
            createSandbox(sys.argv[2])
        else:
            print('This Command doesn\'t exist! Try -h for help.')
    elif sys.argv[1] == '-h':
        showHelp()
    else:
        print('This Command doesn\'t exist! Try -h for help.')


def renameFiles(path='./Sandbox/', new_name='renamedFile'):
    """
    The Core functionality of this program

    :param: path - The Path where the files are (Default: './Sandbox/')
    :param: new_name - The new name of the files. It will be followed by an incrementing number (Default: 'renamedFile')
    :return: void
    """
    try:
        files = os.listdir(path)
    except OSError as e:
        print('Der Pfad: ' + path + ' konnte nicht gefunden werden. Überprüfe den Pfad und prüfe die Zugriffsrechte.')
        return
    print('Started renaming files...')
    error_files = []
    i = 0
    for file in files:
        try:
            os.rename(path + file, path + new_name + '_' + str(i) + os.path.splitext(file)[1])
            print('Renamed File: ' + file + ' to ' + new_name + '_' + str(i) + os.path.splitext(file)[1])
        except OSError as e:
            error_files.append(file)
            print('File: ' + os.path.basename(file) + ' already exists and couldn\'t be renamed!')
        i += 1
    print('Finished renaming files!')
    print('Total renamed files: ' + str(i - len(error_files)))
    print('Total errors: ' + str(len(error_files)))


def createSandbox(filecount=1000):
    """
    Creates a Sandbox with txt files.

    :param: filecount - The filecount (Default: 1000)
    :return: void
    """
    print('Started setting up Sandbox...')
    path = './Sandbox/'
    if os.path.exists(path[:-1]):
        print('Started clearing the Sandbox directory...')
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))
        print('Successfully cleared Sandbox directory!')
    else:
        print('Creating Sandbox directory...')
        try:
            os.mkdir('./Sandbox')
        except OSError as e:
            print('Error while creating the Sandbox directory: ' + e)
            exit(1)
        print('Successfully created Sandbox directory!')
    print('Started creating dummy files...')
    for x in range(0, int(filecount)):
        open('./Sandbox/myData' + '_' + str(x) + '.txt', 'a')
    print('Finished creating dummy files!')
    print('Sandbox successfully set up!')


def showHelp():
    """
    This function shows a Help menu in the console.

    :return: void
    """
    infoHelp = ''' 
    This Program renames all files in a directory to a desired name.
    It adds numbers starting from 0 with an underscore to the name to distinguish between them later.
    
    Syntax: -[r/s/h] [<new_name>/<filecount>] [<directory>]
    
    Commands:
    - Rename: -r (opt) <new_name> <directory>
    - Setup Sandbox: -s (opt) <filecount>
    - Help: -h
    
    The default values for the optional parameters:
    - <new_name>: 'renamedFile'
    - <directory>: './Sandbox/'
    - <filecount>: '1000'
    
    Example Commands:
    - Rename: -r myNewName ./My/Own/Folder/Path/
    - Sandbox: -s 10000
    '''
    print(infoHelp)


if __name__ == "__main__":
    main()
