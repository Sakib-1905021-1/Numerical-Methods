with open("Readme.txt","r") as inp:
    i = 0
    for line in inp:
        print("Printing line:", i, line)
        i += 1
    inp.close()
