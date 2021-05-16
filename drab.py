#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import spacy
from spacy import displacy
from pathlib import Path
import webbrowser
import time
import pandas as pd
import io
import string
import traceback
import os

#from cairosvg import svg2png
#spacy.require_gpu() / spacy.prefer_gpu()  
nlp = spacy.load("en_core_web_trf")
nlp.max_length = 10000000




def printConll(sent,k, file):
        out = ''
        #svg = displacy.render(sent, style="dep", jupyter=False)
        #svg2png(bytestring = svg, write_to="Out/pdf/"+ file +"/dependency_plot"+str(k)+".png")
        
        for i, word in enumerate(sent):
            if word.head == word:
                head_idx = 0
            else:
                 head_idx = word.head.i - sent[0].i + 1
            out +="%d\t%s\t%s\t%s\t%s\t%s\n"%(
                  i+1, # There's a word.i attr that's position in *doc*
                  word,
                  word.lemma_,
                  word.tag_, # Fine-grained tag
                  str(head_idx),
                  word.dep_ # Relation
                 )
        return out



def parse_txt(data, file):
	print(file)
	res = []
	count_short = 0
	count_err = 0
	doc = nlp(data)
	lista = list(doc.sents)
	
	print(len(lista))
	k = 0
	count = 0
	for sent in lista:
		k +=1
		bug = False
		try:
			out = printConll(sent,k, file)
	
			conll = io.StringIO(out)
			df = pd.read_csv(conll, header = None, sep = '\t')
			if len(df) >1:
				
				#remove punctuation marks	  	
				pun = df.index[df[5] == 'punct'].tolist()   
				pun = sorted(pun)     
				el_pun =  [x+1 for x in pun]

				#If the root is a punctuation mark, the sentence is invalid
				for i in range(0, len(pun)):
					  if df[2][pun[i]] == 0:
						  bug = True
			
				#rescale in case punctuation are not leaves
				for j in range(0, len(df[4])): 
					if df[4][j]!= 0:
						if df[4][j] in el_pun:
						    prec = df[4][j]
						    df[4][j] = df[4][prec-1]
				
				for j in range(0, len(df[4])):            
					num_v = sum(df[4][j] >= i+1 for i in pun)
					df[4][j] = df[4][j]-num_v            


					
				df.drop(pun, inplace = True) 
				df = df.reset_index(drop=True)
				df[0] = df.index +1
				
				l = df[4].astype(int).tolist()
				
				l_in = range(1, len(l)+1)
				
				#Sanity checks: Exactly a root, feasible maximum value.
				if len(l) >3:
					root = l.index(0) +1
					if root not in l:
						bug = True	   
					for i in range(len(l)):    
						if l[i]==l_in[i]:
							bug = True
							break	
					if max(l) > max(l_in):
							bug = True
					if l.count(0) >1 :
							bug = True
					if l.count(0) != 1:
							bug = True
									
					if not bug:
						res.append(l)
								
			else:
				count_short +=1
		except:
			count_err +=1

	#Trasform treebank in a string
	res1 = []
	for i in res:
		res1.append(" ".join(str(x) for x in i))
	res = res1
	
	return res


    




########################




files = [i for i in os.listdir("./drab") if i.endswith("txt")]
files_new = []

for file in files:
	file = os.path.splitext(file)[0]
	files_new.append(file)

files = files_new
for file in files:
	filetxt = file+ ".txt" 
	
	fp = open("drab/" +filetxt,encoding="windows-1252")
	#Create monolithic string
	data = fp.read()
	data = data.replace("\n", " ")
	data = data.replace("\t", " ")
	data = ' '.join(data.split())

	chunks = 1
	dati = []
	k = 0
	#avoid spacy overloading by splitting large files
	if(len(data) >500000):
		firstpart, secondpart = data[:len(data)//2], data[len(data)//2:]
		dati.append(firstpart)
		dati.append(secondpart)
		chunks = 2
	else:
		dati.append(data)

	open("treebanks-drab/out-" +filetxt, 'w').close()  

	print("chunks: " + str(chunks))

		
	for i in range (0,chunks):
		start = time.time()
		res = parse_txt(dati[i],file)
		end = time.time()
		
		print("Elapsed time = %s" % (end - start))

		
		for i in range(0, len(res)):
			with open("treebanks-drab/out-" +filetxt, 'a') as f:
				if res[i] != '' and len(res[i]) > 2:  
					f.write("%s " % res[i])
					f.write("\n")    


