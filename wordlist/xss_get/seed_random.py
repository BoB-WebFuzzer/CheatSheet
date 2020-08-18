import random
import re
def ReadFile(fd,ls):
    line = None
    while line != "":
        line = fd.readline()
        if line != "" and line[-1] == '\n':
            #line.strip('\n')
            line = re.sub('[\n]', '', line)
        ls.append(line)

def RandomSeed(ls1,ls2,ls3,ou3tput, n):
    for i in range(n):
        seed = ls1[random.randint(0, len(ls1) -1)] + ls2[random.randint(0, len(ls2) -1)] +  ls3[random.randint(0, len(ls3) -1)]
        print("*New SEED: ", seed)
        seed = seed + '\n'
        output.writelines(seed)

first = open("first_gadget.txt", "r")
second = open("second_gadget.txt", "r")
third = open("third_gadget.txt", "r")
output = open("output.txt","w")
ls1,ls2,ls3 = [],[],[]

ReadFile(first,ls1)
ReadFile(second,ls2)
ReadFile(third,ls3)

n = int(input("How many SEED do you need?: "))
RandomSeed(ls1,ls2,ls3,output, n)





