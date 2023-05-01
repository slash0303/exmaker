text = '''#include <stdio.h>

int main(){
    
}'''

def make_file(file_name:str, index:str):
    with open(file_name+index+".c", "w", encoding="utf-8") as file:
        file.write(text)

index = input("index: ")

index = index.split()
index = list(map(int, index))

file_name = input("file name (default: ex): ")

if file_name == "":
    file_name = "ex"
else:
    pass

if len(index) == 1:
    make_file(file_name, str(index[0]))
else:
    for x in range(index[0], index[1]+1):
        make_file(file_name, str(x))


