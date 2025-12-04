def ParseSeqFile():
    load_and_strip(),
    check_begining(),
    clean_and_divide(),
    check_content(),
    add_to_list
    return




def load_and_strip():
    line = line.stip()
    if not line:
        return

def check_begining():
    if not line.startswith(">"):
        raise Exception("malformed input, line does not start with ">"")
    return

def clean_and_divide():
    line = line[1:].strip().split(maxsplit = 1) #index 1 so the ">" is removed and .strip to remove white space at the beginning/end # splits the line in label and sequence    
    if len(line) != 2:
        raise Exception("malformed input, line misses label or sequence")

    label, sequence = line[0:2] #defining label and sequence
    sequence = sequence.upper().replace(" ","") #all letters are uppercase #removes the spaces " " from the sequence part
    print(label, sequence, sep = "|")
    return

def check_content():
    nucleotides = set("ACGT")
    if set(label).issubset(nucleotides):
        raise Exception("malformed input, Label might be part of Sequence")

    if not set(sequence).issubset(nucleotides):
        raise Exception("malformed input, Sequence contains illegal Characters")
    return

def add_to_list():
    clean_list = []
    clean_list.append((label, sequence))
    print(clean_list)    
    return
############################################################################

def ParseSeqFile(filename):
    clean_list = []
    with open("data.txt", "rt") as f:
        for line in f:
            line = line.stip()
        
            if not line:
                continue 
            try: 
                lable, sequence = check_content(line)
            except:
                print()