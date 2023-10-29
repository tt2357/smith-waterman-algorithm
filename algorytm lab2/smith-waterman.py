import sys
import numpy as np

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
                   seq2 += str(line)
              elif i == 2:
                   seq1 += str(line)

    seq1 = seq1.replace("\n", "")
    seq2 = seq2.replace("\n", "")
    
except FileNotFoundError:
    print(f"File not found: {file_path}")

def createMatrix(seq1, seq2):
  matrix = np.zeros((len(seq1)+1, len(seq2)+1), dtype=int)
  return matrix

def backtrackMatrix(seq1, seq2):
  matrix = [["" for j in range(len(seq1)+1)] for i in range(len(seq2)+1)]
  return matrix

def fillMatrix(matrix,bMatrix, seq1, seq2,match,indel,mismatch):
  mList = ["0", "UP", "LEFT","LEFTUP"]
  oList = []
  for i in range(1,len(seq1)+1):
    for j in range(1,len(seq2)+1):
      oList.append(0)
      oList.append(matrix[i-1][j] + indel)
      oList.append(matrix[i][j-1] + indel)
      if(seq1[i-1] == seq2[j-1]):
        oList.append(matrix[i-1][j-1] + match)
      else:
        oList.append(matrix[i-1][j-1] + mismatch)
      matrix[i][j] = max(oList)
      print(oList)
      bMatrix[i][j] = mList[oList.index(max(oList))]
      oList.clear()

  for row in matrix:
    for element in row:
      print(element, end="\t")
    print()

  for row in bMatrix:
    for element in row:
      print(element, end="\t")
    print()

match = 1
indel = -1
mismatch = -1

matrix = createMatrix(seq1, seq2)
bMatrix = backtrackMatrix(seq1, seq2)
fillMatrix(matrix,bMatrix, seq1, seq2,match,indel,mismatch)