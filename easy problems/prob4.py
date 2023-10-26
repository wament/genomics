import sys

def loops(a , b):
    out = 0
    for i in range(a, b+1):
        if i % 2 == 1:
            out = out + i
    return out

if __name__ == "__main__":
    print(loops(int(sys.argv[1]),int(sys.argv[2])))
    