import os
import hashlib
import random
import string
import sys

incrementalHash = hashlib.sha256()

def writeFile(numGB, path):
    singleGB = 1024*1024*1024

    filename = f'output_file_{randomString()}.dat'
    if path:
        outputPath = path
    else:
        outputPath = filename

    with open(outputPath, 'wb') as fout:
        # write 1 GB at a time so we don't run out of memory
        for i in range(numGB):
            print('generating data')
            randomData = os.urandom(singleGB)
            print('starting write')
            fout.write(randomData)
            print(f'{i + 1} GB written to disk')
            print('incrementing hash')
            incrementalHash.update(randomData)

    return outputPath

def sha256sum(filename):
    h = hashlib.sha256()
    b = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def writeSumToFile(nameOfHashedFile, fileHash):
    print('Writing sha256sum to file')
    with open(nameOfHashedFile + '_hash.txt', 'w') as f:
        f.write(fileHash)

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

actions = '''Enter a or b: 
a.) Write file with random data and generate hash of file
b.) Get file hash

'''

action = input(actions)


if action == 'a':
    desiredSize = input('Enter desired file size in GB: ')

    outputPath = input('Enter the path for the file, or just press enter to use the current directory of the script: \n');

    print('\nWriting file...\n')

    fileName = writeFile(int(desiredSize), outputPath)
    # fileHash = sha256sum(fileName)
    print('sha256sum: ' + incrementalHash.hexdigest())
    writeSumToFile(fileName, incrementalHash.hexdigest())


elif action == 'b':
    fileName = input('Enter file name: ')
    fileHash = sha256sum(fileName)
    print('sha256sum: ' + fileHash)
    writeSumToFile(fileName, fileHash)

else:
    print('invalid input. exiting.')
    sys.exit()

print('Done!')
