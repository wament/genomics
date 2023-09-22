# Mainframe
# Author: William(Willow) Ament
# Date 9/21/2023



from Basic import *
import random

#str = "AAGGACCCTTGACTTTGCCAAATAgG"
rndDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(20)])

seq = validateSeq(rndDNAStr)

print(seq)
print(countNuc(seq))