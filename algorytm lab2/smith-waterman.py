import sys
import numpy

file_path = sys.argv[1]
try:
    seq1 = ""
    seq2 = ""
    
    with open(file_path, 'r') as file:
        i = 0
        for line in file:
            if line.startswith(">"):
              i += 1
            else:
              if i == 1:
                   seq1 += str(line)
              elif i == 2:
                   seq2 += str(line)

    seq1 = seq1.replace("\n", "")
    seq2 = seq2.replace("\n", "")
    
except FileNotFoundError:
    print(f"File not found: {file_path}")



