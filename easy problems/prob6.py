import sys

if __name__ == "__main__":
    f = open('rosalind_ini6.txt', 'r')
    string = f.read()
    #print(string)
    
    dict = {}
    dict['When'] = 1
    
    for i in string.split(' '):

        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    
    for key, value in dict.items():
        print(key, value)

    f.close()