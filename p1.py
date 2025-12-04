#loading the input file in p1
with open("data.txt", "rt") as f: # r = read, t = txt file
    for line in f:
        line = line.strip() #removing empty lines

        if not line:
            continue

        if not line.startswith(">"):
            raise Exception("malformed input, line does not start with ">"")  #???????????????????
        
        else: 
            line = line[1:].strip().split(maxsplit = 1) #index 1 so the ">" is removed and .strip to remove white space at the beginning/end # splits the line in label and sequence
            
            if len(line) != 2:
                raise Exception("malformed input, line misses label or sequence")

            label, sequence = line[0:2] #defining label and sequence
            sequence = sequence.upper().replace(" ","") #all letters are uppercase #removes the spaces " " from the sequence part
            print(label, sequence, sep = "|")



