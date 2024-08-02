import os.path
from pprint import pprint

def custom_write(file_name, strings):
    if os.path.isfile(file_name):
        for i in strings:
            file = open(file_name, 'r', encoding="utf-8")
            line = file.read().splitlines()
            if i in line:
                file.close()
                continue
            else:
                file = open(file_name, 'a', encoding="utf-8")
                file.write(i + '\n')
                file.close()
        file = open(file_name, 'r', encoding="utf-8")
        j = 1
        strings_positions = {}
        len_ = len(file.readlines())
        file.seek(0)
        #file.close()
        #file = open(file_name, 'r')
        while j != len_ + 1 :
            line = file.readline()
            strings_positions[(j, file.tell())] = line.rstrip('\n')
            j += 1
        file.close()
        return strings_positions
        # for i in range(len(file.readlines())):
        #     file = open(file_name, 'r')
        #     line = file.readline()
        #     strings_positions[(i, file.tell())] = line.rstrip('\n')
        #     file.close()
        # return strings_positions
    else:
            file = open(file_name, 'w')
            file.close()
            custom_write(file_name, strings)

a = custom_write( "Module_7_2.txt",  [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ])
print(a)

