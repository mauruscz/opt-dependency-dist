from sys import argv
import lal
import os
import sys



auth = sys.argv[1]
print(auth)


os.makedirs('outLAL', exist_ok=True)
os.makedirs('outLAL/' +auth, exist_ok=True)


def gimme_approx_k2(n, store_at):
	n = rT.num_nodes()
	if n in store_at:
		return store_at[n]
	
	N = 10000
	avg = 0
	Gen = lal.generate.rand_ulab_free_trees(n) #free
	
	
	for i in range(0, N):
		random_free_tree = Gen.get_tree()
		avg += lal.properties.mmt_degree(random_free_tree, 2)
	
	store_at[n] = avg/N

	return store_at[n]


storage = dict()


tbdsreader = lal.io.treebank_dataset_reader()
error = tbdsreader.init("index_" +auth + ".txt") 


while tbdsreader.has_treebank():
	tbdsreader.next_treebank()
	
	tbreader = tbdsreader.get_treebank_reader()
	print("Book:", tbreader.get_identifier())
	
	f = open("outLAL/" +auth +"/"+tbreader.get_identifier() + ".df", 'w')
	f.write("n\tapprox_k2\tD\tDmin_unconstrained\tk2\tD_var\tD_exp_1\thead\tdel\tcaterp \n")
	
	k = 1
	while tbreader.has_tree():

		tbreader.next_tree()
		rT = tbreader.get_tree()


		#n
		f.write(str(rT.num_nodes()))
		f.write("\t")


			
		#k2-RUT
		value = gimme_approx_k2(rT, storage)
		f.write(str(round(value,3)))
		f.write("\t")

		
		#D
		f.write(str(round(lal.linarr.sum_length_edges(rT),3)))
		f.write("\t")

		
		#Dmin
		f.write(str(round(lal.linarr.Dmin(rT.to_undirected(), lal.linarr.algorithms_Dmin.Unconstrained_YS)[0],3)))
		f.write("\t")

		
		#k2
		f.write(str(round(lal.properties.mmt_degree(rT,2),3)))
		f.write("\t")

		
		#Var_D
		f.write(str(round(lal.properties.variance_D(rT.to_undirected()),3)))
		f.write("\t")

		
		#Exp_D
		f.write(str(round(lal.properties.expectation_D(rT.to_undirected()),3)))
		f.write("\t")

		
		#Beta
		f.write(str(round(lal.linarr.headedness(rT),3)))
		f.write("\t")

		
		#delta
		f.write(str(round(lal.properties.mean_hierarchical_distance(rT),3)))
		f.write("\t")

	
		#caterpillar
		a = int(rT.is_of_type(lal.graphs.tree_type.caterpillar))
		f.write(str(a))
		f.write("\n")
		

		k+=1
			
	f.close()
