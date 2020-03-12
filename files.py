f = open("rosalind_ini5.txt", "r")

counter = 1
for line in f.readlines():
    if counter % 2 == 0:
        print(line, end="")
    counter+=1