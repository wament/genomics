import sys

def strings_lists(s, a , b, c, d):
    return s[a:(b+1)],s[c:(d+1)] 

if __name__ == "__main__":
    print(strings_lists(sys.argv[1],int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
    