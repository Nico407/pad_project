#loading the input file in p1
with open("data.txt", "rt") as f: # r = read, t = txt file
    #print(f.read()) #solely to check functioning read in
    for line in f:
        if not line.startswith(">"):
            raise Exception("malformed input")

        else: 
            #print("works so far")
            clean_line = line[1:].strip() #index 1 so the ">" is removed and .strip to remove white space at the beginning/end
            #print(clean_line)
            separated_line = clean_line.split(maxsplit = 1) # splits the line in label and sequence
            #defining label and sequence
            label, sequence = separated_line[0:2]
            #sequence = separated_line[1]
            sequence = sequence.upper().replace(" ","") #removes the spaces " " from the sequence part
            print(label, sequence)



