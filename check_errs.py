import lal


import os
import sys



auth = sys.argv[1]
print(auth)


errlist = lal.io.check_correctness_treebank_dataset("./index_" +auth + ".txt") 

print("Loading...")
for err in errlist:
	print(err)
