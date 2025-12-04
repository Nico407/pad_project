#loading the input file in p1
filename = r"C:\Users\nicob\Desktop\MSc ACLS\2. Sem\PAD\project\data.txt"
def ParseSeqFile(filename):
    clean_list = [] #creating empty list to append in later stages
    nucleotides = set("ACGT") #setting valid characters for sequence

    with open(filename, "rt") as f: # r = read, t = txt file
        for line in f:
            line = line.strip() #removing empty lines

            if not line:
                continue

            if not line.startswith(">"):
                raise Exception("malformed input, line does not start with ">"")  #???????????????????

            else: 
                line = line[1:].strip().split(maxsplit = 1) #index 1 so the ">" is removed and .strip to remove white space at the beginning/end # splits the line in label and sequence
            
                if len(line) != 2: #checking whether the line contains exactly two elements (will be defined in the following command)
                    raise Exception("malformed input, line misses label or sequence")#???????????????????

                label, sequence = line[0:2] #defining label and sequence
                sequence = sequence.upper().replace(" ","") #all letters are uppercase #removes the spaces " " from the sequence part
                print(label, sequence, sep = "|")

                if set(label).issubset(nucleotides):        #Checking whether there is a label/sequence part handled as label
                    raise Exception("malformed input, Label might be part of Sequence")#???????????????????

                if not set(sequence).issubset(nucleotides):     #Checking whether the sequence contains only valid characters
                    raise Exception("malformed input, Sequence contains illegal Characters")#???????????????????
            
                clean_list.append((label, sequence))
                print(clean_list)
    return clean_list

ParseSeqFile(filename)