import os
import hashlib
import random
import string
import sys

def writeFile(numGB):
    desired_size = 1024*1024*1024 * int(numGB)
    filename = f'output_file_{randomString()}.dat'
    print('filename: {0}'.format(filename))
    with open(filename, 'wb') as fout:
        fout.write(os.urandom(desired_size))

    return filename

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

    print('\nWriting file...\n')

    fileName = writeFile(int(desiredSize))
    fileHash = sha256sum(fileName)
    print('sha256sum: ' + fileHash)
    writeSumToFile(fileName, fileHash)


elif action == 'b':
    fileName = input('Enter file name: ')
    fileHash = sha256sum(fileName)
    print('sha256sum: ' + fileHash)
    writeSumToFile(fileName, fileHash)

else:
    print('invalid input. exiting.')
    sys.exit()

print('Done!')
