import sys

def pythag(a , b):
    return a*a + b*b

if __name__ == "__main__":
    print(pythag(int(sys.argv[1]),int(sys.argv[2])))
    