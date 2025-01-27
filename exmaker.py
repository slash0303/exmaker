import os

# default input text
text = '''#include <stdio.h>

int main(){
    
}'''

# annotation variable
anno_enable = True
annotation = '''// This file was generated by slash's exmaker
'''

# file generate function
def make_file(file_name:str, index:str):
    with open(file_name+index+".c", "w", encoding="utf-8") as file:
        file.write(text)

# command execute function
def exc_cmd(index):
    if index == "path":
        cd()
    elif index == "rm_anno":
        rm_anno()
    elif index == "version":
        ver()
    else:
        print(f"'{index}' is incorrect request.")

# cd function
def cd():
    while True:
            path = input("path: ")
            try:
                if path == "":
                    path = "C:/Users/Admin/Desktop/_"
                os.chdir(path)
                break
            except:
                print(f"'{path}'is incorrect. please re-write the path.")
                
# annotation option control function
def rm_anno():
    while True:
            tf = input("annotation remove option: ")
            if tf == "0" or tf == "off" or tf.find("lase") != -1:
                print("annotation: off")
                return False
            else:
                print("annotation: on")
                return True

# version print function
def ver(log=False, log_all=False):
    version ="1.1.0"
    ver_log = {"1.1.0" : '''
add path change feature
add annotation and remove option'''}
    print("v",version)
    if log:
        if log_all:
            for x in ver_log.values():
                print(x)
        else:
            print(ver_log[version])

# index/cmd input
while True:
    index = input("index: ")
    index_split = index.split()

    if index[0] == "/":
        cmd_in = index[1:]
        exc_cmd(cmd_in)
    elif index_split[0].isnumeric():
        break
    else:
        pass

if anno_enable:
    text = annotation + text
else:
    pass

# index mapping
index = index.split()
index = list(map(int, index))

# file generate
file_name = input("file name (default: ex): ")

#file
if file_name == "":
    file_name = "ex"
else:
    pass

if len(index) == 1:
    make_file(file_name, str(index[0]))
else:
    for x in range(index[0], index[1]+1):
        make_file(file_name, str(x))
