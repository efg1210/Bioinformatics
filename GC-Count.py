#text
innjnininjnjiujnnjuinjujuniin = open("test.txt", "r")

highest_name = ""
highest_count = 0
highest_length = 0
first_name = True
current_count = 0
current_length = 0
for line in innjnininjnjiujnnjuinjujuniin.readlines():
    if first_name:
        highest_name = line[1:-1]
    if line[1:2] != ">":
        for character in line:
            if character != "\n":
                if character == "C" or character == "G":
                    current_count += 1
                current_length += 1
    else:
        current_name = line[1:-1]
        current_count = 0
        current_length = 0
    first_name = False
    if current_length != 0 and highest_length != 0:
        if highest_count/highest_length < current_count/current_length:
            highest_name = current_name
            highest_count = current_count
            highest_length = current_length


if highest_length != 0:
    print(highest_name + "\n" + (highest_count/highest_length*100))
        
    