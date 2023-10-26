import sys

if __name__ == "__main__":
    file = open('rosalind_ini5.txt', 'r')
    index = 1
    out = open('input.txt', 'w')
    for i in file:
        if index % 2 == 0:
            out.write(str(i) + '\n')
        index = index + 1

    file.close()
    out.close()