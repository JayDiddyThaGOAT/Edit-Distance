#Jalen Jackson
#CPSC 485 - Computer Bioinformatics
#CWID: 7403

from enum import Enum

class Operation(Enum):
    MATCH = 0
    REPLACE = 1
    INSERT = 2
    DELETE = 3
    NULL = 4
    
if __name__ == "__main__":
    while True:
        print("\nPlease input two words to find its edit distance\n")
        w = "-" + input("First Word: ")
        v = "-" + input("Second Word: ")

        #Initalize matrix
        s = []
        for i in range(0, len(v)):
            s.append([])
            for j in range(0, len(w)):
                s[i].append(-1)
        b = []
        for i in range(0, len(v)):
            b.append([])
            for j in range(0, len(w)):
                b[i].append(Operation.NULL)


        #Initalize first column & first row to increase by 1
        for j in range(0, len(w)): 
            s[0][j] = j
            b[0][j] = Operation.INSERT
        
        for i in range(1, len(v)): 
            s[i][0] = i
            b[i][0] = Operation.DELETE

        #Align
        for i in range(1, len(v)):
            for j in range(1, len(w)):
                if v[i] == w[j]:
                    s[i][j] = s[i - 1][j - 1]
                    b[i][j] = Operation.MATCH
                else:
                    s[i][j] = min(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1]) + 1
                    if s[i][j] == s[i][j - 1] + 1:
                        b[i][j] = Operation.INSERT
                    elif s[i][j] == s[i - 1][j] + 1:
                        b[i][j] = Operation.DELETE
                    elif s[i][j] == s[i - 1][j - 1] + 1:
                        b[i][j] = Operation.REPLACE

        #Print matrix
        print("\n\t" + '\t'.join(letter for letter in list(w)))
        for i in range(0, len(v)):
            row = s[i]
            print(v[i] + "\t" + '\t'.join(str(num) for num in row))

        #Print edit distance
        edit_distance = s[len(v) - 1][len(w) - 1]
        print("\nEdit Distance =  %d" % edit_distance)

        align_v = []
        align_w = []
        i = len(v) - 1
        j = len(w) - 1
        while True:
            if i == 0 and j == 0:
                break

            if b[i][j] == Operation.MATCH or b[i][j] == Operation.REPLACE:
                align_v.insert(0, v[i])
                align_w.insert(0, w[j])
                i -= 1
                j -= 1
            elif b[i][j] == Operation.DELETE:
                align_v.insert(0, v[i])
                align_w.insert(0, "_")
                i -= 1
            elif b[i][j] == Operation.INSERT:
                align_w.insert(0, w[j])
                align_v.insert(0, "_")
                j -= 1
        
        print("\nAlignment is: ")
        print("".join(align_w))
        print("".join(align_v))

        k = input("\nContinue? Y/N: ")
        if not k == "Y" and not k == "y":
            break
    
    exit(0)